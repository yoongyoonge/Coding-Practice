from itertools import cycle

def solution(answers):
    
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5] 
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
    
    student_answer = [
        cycle(a),
        cycle(b),
        cycle(c)
    ]
    
    score_a, score_b, score_c = 0, 0, 0
    
    for sol in answers:
        if sol == next(student_answer[0]):
            score_a += 1
            
        if sol == next(student_answer[1]):
            score_b += 1
            
        if sol == next(student_answer[2]):
            score_c += 1
    
    students = {1: score_a, 2: score_b, 3: score_c}
    ret = [name for name, score in students.items() if score == max(students.values())]

    return ret