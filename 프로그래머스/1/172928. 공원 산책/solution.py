class Dog:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.g = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

    def move(self, park, direction, distance):
        i, j = self.g[direction] # 동서남북 동작 방향
        x, y = self.x + (i * distance), self.y + (j * distance) # 변위

        if x < 0 or y < 0 or x >= len(park) or y >= len(park[0]): # 이동할 위치가 공원 밖의 범위라면 이동하지 않음
            return park
        elif "X" in park[x][min(self.y, y) : max(self.y, y) + 1] or "X" in [row[y] for row in park[min(self.x, x) : max(self.x, x)]]: # 이동할 거리 안에 장애물이 있다면 이동하지 않음
            return park
        
        # 이동할 위치에 이상이 없다면 기존 위치를 O로 지정하고 이동할 위치를 S로 지정
        park[self.x][self.y] = "O"
        park[x][y] = "S"

        self.x = x
        self.y = y

        return park
    
    @classmethod
    def detect_start_dogs_location(self, park):
        """ 시작 위치가 고정되어있지 않기 때문에 시작위치를 추출하는 메소드
        """        
        for i, row in enumerate(park):
            for j, item in enumerate(row):
                if item == "S":
                    return i, j


def solution(park, routes):

    # park = ["OOXOS","OOOOO","OOOOO", "OOOOO", "OOOOO"]
    # park의 모든 요소를 쪼개어 2차원 배열로 만듦
    park = [list(row) for row in park]

    # 시작 위치를 추출
    x, y = Dog.detect_start_dogs_location(park)

    # 클래스 인스턴스 생성
    dog = Dog(x, y)

    # 루트를 방향과 거리로 쪼개어 Dog 클래스의 move실행
    for route in routes:
        direction, distance = route.split()
        park = dog.move(park, direction, int(distance))

    return [dog.x, dog.y]


park = ["OOXOS","OOOOO","OOOOO", "OOOOO", "OOOOO"]
routes =  ["W 3"]
solution(park, routes)