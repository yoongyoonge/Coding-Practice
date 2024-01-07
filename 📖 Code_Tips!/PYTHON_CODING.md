## @classmethod 와 @staticmethod

1. 정적메소드
- 정적메소드는 클래스에서 직접 접근할 수 있는 메소드 
- **파이썬에서 classmethod 와 staticmethod는 클래스에서 직접 접근할 수 있는 메소드 이지만 인스턴스에서도 접근이 가능하다는 것에 큰 차이가 있음**

```python
class CustomClass:

    # instance method
    def add_instance_method(self, a,b):
        return a + b

    # classmethod
    @classmethod
    def add_class_method(cls, a, b):
        return a + b

    # staticmethod
    @staticmethod
    def add_static_method(a, b):
        return a + b



>>> a = CustomClass()
>>> a.add_class_method(3, 5)
8 # 객체에서도 접근 가능
>>> a.add_static_method(3, 5)
8 # 객체에서도 접근 가능
```

2. @classmethod 와 @staticmethod의 차이
- 상속에서 차이가 남 

```python
class Language:
    default_language = "English"

    def __init__(self):
        self.show = '나의 언어는' + self.default_language

    @classmethod
    def class_my_language(cls):
        return cls()

    @staticmethod
    def static_my_language():
        return Language()

    def print_language(self):
        print(self.show)


class KoreanLanguage(Language):
    default_language = "한국어"



>>> from language import *
>>> a = KoreanLanguage.static_my_language()
>>> b = KoreanLanguage.class_my_language()
>>> a.print_language()
나의 언어는English # 부모클래스의 클래스 속성 값을 가져온다.
>>> b.print_language()
나의 언어는한국어 # cls 인자를 활용하여 cls의 클래스 속성을 가져온다.
```


참고: https://wikidocs.net/16074