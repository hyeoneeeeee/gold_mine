from datetime import datetime
import random, time

def baseball_game():
    while True:
        try:    
            get_number = int(input('1~10자리중 선택하세요: '))
            if get_number == 0:
                print('0은 입력할 수 없습니다. 다시 입력해 주세요')
                continue
            elif get_number >10 :
                print('10자리를 넘게 설정하실수 없습니다.')
                continue
            else:break
        except:
            print('다시 입력해 주세요')
            continue
            
    state = True
    answer_num_list = []
    count = 0  
    Ball = 0
    Strike = 0
    
    while len(answer_num_list) < get_number:
        answer_num = random.randint(0,9)
        if str(answer_num) not in answer_num_list:
            answer_num_list.append(str(answer_num))
    
    start_time = time.time()
    while state:
        while True:
            try:
                print('숫자를 입력해 주세요')
                user_num = list(map(str,input()))
                print(answer_num_list)
                print(user_num)
                if user_num == ['e','x','i','t']:           # 게임 종료(하기 싫을때)
                    state = False
                    break
                elif len(user_num) == len(answer_num_list):
                    break
                # elif user_num == answer_num_list:
                #     end_time = time.time()
                #     elapes_time = end_time - start_time
                #     print(f'Home run!!\n{count}번 만에 맞추었습니다!\n시간은 {elapes_time:.5f}초 걸렸습니댜!')
                #     state = False
                    # break
                elif len(set(user_num)) != len(answer_num_list): # 적게 적는거 방지
                    print(f'올바른 숫자 {get_number}개를  입력해 주새요')
                    continue
                else:                           # 문자입력 방지
                    print(f'올바른 숫자 {get_number}개를  입력해 주새요')
                    continue
            except:                             # 기타 오류 방지
                print(f'올바른 숫자 {get_number}개를  입력해 주새요')
                continue
        
        #  유저 번호와 정답이 같은지 확인
        count += 1
        for ind1,num1 in enumerate(user_num):
            if num1 in user_num:
                for ind2,num2 in enumerate(answer_num_list):
                    if ind1 == ind2 and num1 == num2:
                        Strike += 1
                    elif ind1 != ind2 and num1 == num2:
                        Ball += 1
                    else: pass
                    
        if user_num == answer_num_list:
            end_time = time.time()
            elapes_time = end_time - start_time
            print(f'Home run!!\n{count}번 만에 맞추었습니다!\n시간은 {elapes_time:.0f}초 걸렸습니댜!')
            print(datetime.now()) 
            state = False
        elif Strike == 0 and Ball == 0:
            print('Out!')
        else : 
            print(f'S: {Strike}, B: {Ball}')
        
        
        Strike = 0
        Ball = 0
        user_num.clear()

    print('게임이 종료되었습니다')
    time.sleep(2)

baseball_game()