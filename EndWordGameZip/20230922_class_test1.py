#사칙연산 클래스 만들기
#변수 2가지 선언(first, second)
#초기 값으로 2가지 수 받기
#더하기, 곱하기, 나누기, 빼기 메서드 구현
#각 더하기, 곱, 빼기, 나누기 결과 출력

class Calculate:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def plus(self):
        result = self.first+self.second
        return result

    def subtract(self):
        return self.first-self.second

    def divide(self):
        return self.first/self.second

    def multi(self):
        return self.first*self.second

my_first_num=Calculate(1,2)
print(my_first_num.plus())

class PowerCal(Calculate):
    #상속받은 것에서 거듭제곱을 새로 만든 함수
    def power(self):
        return self.first ** self.second

    #매서드 오버라이딩(기존에 있던 나누기를 덮어씌운다.)
    def new_dev(self):
        if self.first==0:
            return "오류 입니다."
        else:
            return self.first/self.second


new_second_data=PowerCal(3,3)
print(new_second_data.power())
print(new_second_data.new_dev())

#생성자란 객체가 생성될때 자동으로 호출되는 메서드이다.
"""
"""
