class WordGame:
    def __init__(self):
        self.used_list = []
        self.english_text = [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        self.special_text = ["~", "@", "!", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "\\", "|", ":", ";", "<", ">", "?", "."]
        self.num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.score = 1

    def ConcludingRemarkGame(self): #함수를 호출하려면 이름 뒤에 괄호를 사용한다.
        while True:
            print(f"입력된 단어 {self.used_list}")
            user_input = input("단어를 입력해 주세요:")

            if len(self.used_list) < 1: #used_list가 빈칸일때 유저가 입력한 단어를 사용된 단어에 추가해 준다.append는 리스트의 맨 마지막에 x를 추가하는 함수
                self.used_list.append(user_input)
            else:
                if len(user_input) >= 11:
                    print("글자수는 10자 이하")

                elif any(char in user_input for char in self.english_text):
                    print("영어 입력. 다시 입력해 주세요.")
                    """
                    영어 문자(english_text)를 char에 하나씩 할당하는 데, 이 문자열(char)이 유저가 입력한 단어(user_input)에
                    포함되어 있는지 확인한다.
                    *** any는 괄호 안의 조건 중 하나라도 참이면 True를 반환한다. ***
                    그래서 문자열인 char이 user_input 문자열에 포함되어 있다면 True를 반환한다.
                    user_input 문자열에 english_text 리스트의 각 문자열(char) 중 하나라도 포함되어 있는지를 확인.
                    any() 함수는 인자로 받은 반복 가능한(iterable) 객체(여기서는 리스트) 내에서 어떤 조건을 만족하는 요소가 하나라도 있는지 확인하는 함수
                    """
                elif any(char in user_input for char in self.special_text): #for 변수 in 리스트(튜플,문자열)
                    print("특수 문자 입력. 다시 입력해 주세요")

                elif any(char in user_input for char in self.num_list):
                    print("숫자가 입력됨. 다시 입력해 주세요")

                elif user_input.isspace() or ' ' in user_input:
                    print("공백이 있습니다. 다시 입력해 주세요")

                elif user_input[0] != self.used_list[-1][-1]: #example_list[3][0] # 3번째 인덱스의 리스트에서 다시 0번째 인덱스를 확인한다.
                    print("뒷자리가 맞지 않습니다.. 다시 입력하시오.")

                elif user_input in self.used_list:
                    print("앞에서 사용한 단어와 동일한 단어, 입력 다시 입력하시오.")

                else:
                    self.used_list.append(user_input)
                    self.score += 1 # 조건 통과시 숫자(score)를 1 증가시킴
                    print(f"현재 점수: {self.score}점")

if __name__ == "__main__":
    print("끝말잇기 게임을 시작합니다!")
    game = WordGame()
    game.ConcludingRemarkGame()