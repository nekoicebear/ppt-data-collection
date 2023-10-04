used_list=[]
english_text=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# special_text=["~","!","#","$","%","^","&","*","(",")","_","+","\","|",":",";","<",">","?"]
special_text = ["~", "!", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "\\", "|", ":", ";", "<", ">", "?","."]
num_list = ["1","2","3","4","5","6","7","8","9","0"]
#i=0
#리스트명 = [요소1, 요소2, 요소3, ...]

def ConcludingRemark():
    #함수를 호출하령면 이름 뒤에 괄호를 사용한다.
    while True:
        print(f"현재 입력 단어{used_list}")
        #if
        #print(f"당신의 현재 점수는 {i}점 입니다. ")
        user_input = input("단어를 입력해 주세요:")

        if len(used_list) <1: #used_list가 빈칸일때 유저가 입력한 단어를 사용된 단어에 추가해 준다.append는 리스트의 맨 마지막에 x를 추가하는 함수
            used_list.append(user_input)

        else:
            if len(user_input)>= 11:
                print("글자수는 10자 이하")
                #글자수 10자 이하 조건

            elif any(char in user_input for char in english_text):
                #영어 문자를 char에 하나씩 할당하는 데, 이 문자열(char)이 유저가 입력한 단어(user_input)에
                #포함되어 있는지 확인한다.
                #any는 괄호 안의 조건 중 하나라도 참이 면 True를 반환한다.
                #그래서 문자열인 char이 user_input 문자열에 포함되어 있다면 True를 반환한다.
                print("영어 입력. 다시 입력해 주세요.")
                #user_input 문자열에 english_text 리스트의 각 문자열(char) 중 하나라도 포함되어 있는지를 확인.
                #any() 함수는 인자로 받은 반복 가능한(iterable) 객체(여기서는 리스트) 내에서 어떤 조건을 만족하는 요소가 하나라도 있는지 확인하는 함수

            elif any(char in user_input for char in special_text): #for 변수 in 리스트(튜플,문자열)
                print("특수 문자 입력. 다시 입력해 주세요")

            elif any(char in user_input for char in num_list):
                print("숫자가 입력됨. 다시 입력해 주세요")

            elif user_input.isspace() or ' ' in user_input:
                print("공백이 있습니다. 다시 입력해 주세요")

            elif user_input[0] != used_list[-1][-1]:
                print("뒷자리가 맞지 않습니다.. 다시 입력하시오.")
                #str[3][0] # 3번째 인덱스의 리스트에서 다시 0번째 인덱스를 확인한다.

            elif user_input in used_list:
                print("앞에서 사용한 단어와 동일한 단어, 입력 다시 입력하시오.")
                continue #while 문을 빠져나가지 않고 while 문의 맨 처음(조건문)으로 다시 돌아가게 만들고 싶은 경우

            else:
                used_list.append(user_input)


        #점수를 획득하는 방식으로 구현


ConcludingRemark()
