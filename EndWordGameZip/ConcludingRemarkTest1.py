# 한글만 포함되어야 합니다.-영어 및 숫자, 특수문자가 포함된 문자를 받을 수 없습니다.
# 글자수는 10자 이하여야 합니다.
# 공백이 있어선 안됩니다.
# 한번 등장한 단어는 중첩해서 나올 수 없습니다.
# 프로그램은 종료 될 수 없습니다.

# 끝말잇기 게임 렐리가 길어질 수록 점수를 획득하는 방식으로 구현해주세요
# 만약에 가능하다면 점수가 떨어지는 조건도 만들어보세요
# 중첩된 단어가 나온경우 점수를 떨어트리고 다시 시도하게 만든다던지 특수문자나 기타 쓸 수 없는 문자를 쓰면 점수를 떨어트린다던지 등
# 모든 코드는 클래스 단위로 작성하셔야 합니다.
#끝말잇기 과제

#special_characters=[#,$,%,^,&,*,(,),_,+,{,},|,\,:,;,",',,,.,/,<,>,?]
# count=0

used_list=[]
english_text=["a","b","c"]

def ConcludingRemark():
    while True:
        print(f"현재 입력 단어{used_list}")
        user_input = input("단어를 입력해 주세요:")

        if len(used_list) <1:
            used_list.append(user_input)

        else:
            if len(user_input)>= 11:
                print("글자수는 10자 이하")

            elif user_input in english_text or 'abc' in user_input:
                print("영어가 입력됐습니다. 다시 입력해 주세요")


            elif user_input.isspace() or ' ' in user_input:
                print("공백이 있습니다. 다시 입력해 주세요")

            elif user_input[0] != used_list[-1][-1]:
                print("뒷자리가 맞지 않습니다.. 다시 입력하시오.")
                #str[3][0] # 3번째 인덱스의 리스트에서 다시 0번째 인덱스를 확인한다.

            elif user_input in used_list:
                print("앞에서 사용한 단어와 동일한 단어, 입력 다시 입력하시오.")
                continue


            else:
                used_list.append(user_input)


start = ConcludingRemark()
start
        # if first_given_word[-1] != user_input[0]:
        #     print("단어가 옳지 않습니다.")



#user_input(사용자 압력값 제약 조건): 글자수 제한(10자 이하) -------------------------- O
#user_input(사용자 압력값 제약 조건): 영어, 숫자, 특수문자, 공백 불가
#user_input(사용자 압력값 제약 조건): 이전에 나왔던 단어 중첩 X


#사용자가 계속해서 단어를 이어나가는 방식
#프로그램은 종료될 수 없다.


#
# class EndWord:
#     def __init__(self,first_word, user_word):
#         self.first_word=first_word
#         self.user_word=user_word
#
#     def

#다시 생각
"""
유저가 입력하는 조건=> 한글만 가능(영어, 숫자, 특수문자, 공백 안됨)
                => 이전에 유저가 입력했던 단어가 또 나오면 안됨
                => 글자는 10글자 이하
"""

# class Endword:
#     def __init__(self, user_word):
#         self.user_word=""
#
#     def UserRule(self):
#         user_word = input("끝말잇기를 입력하시오:")
#         special_string = ["#", "*", "^"]
#
#         if len(self.user_word) >=11:
#             return "길이가 너무 깁니다. 다시 입력해 주세요"
#         elif self.user_word.isalpha():
#             return "영어 입니다. 다시 입력해 주세요"
#         elif self.user_word in special_string:
#             return "특수 문자 입니다. 다시 입력해 주세요"
#
#     if __name__=="__main__":
