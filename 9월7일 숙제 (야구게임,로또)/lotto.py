import random

def lotto():
    while True:
        try:
            get_lotto = int(input('로또 몇장 살겨?: '))
            if get_lotto == 0:
                print('빵장 말고 ㅡㅡ')
            else:break
        except:
            print('숫자를 입력해 주세요')
            continue
    lotto_nums = []
    for _ in range(get_lotto):
        while len(lotto_nums) < 5:
            a = random.randint(1,45)
            if a not in lotto_nums:
                lotto_nums.append(a)
        lotto_nums.sort()
        if len(lotto_nums) !=6:
            while len(lotto_nums) < 6:
                bonus = random.randint(1,45)
                if bonus not in lotto_nums:
                    break
        print(f'로또번호는 : {lotto_nums} 보너스번호는 : {[bonus]}')
        
        
    # lotto_list=[]
# for _ in range(get_lotto):
    #     while len(lotto_nums) < 5:
    #         num = random.randint(1,45)
    #         if num not in lotto_nums:
    #             lotto_nums.append
    #     if len(lotto_nums) == 5:
    #         bonus = random.randint(1,45)
    #         lotto_nums.append(f'+{bonus}')
    #     lotto_list.append([lotto_nums])
    #     lotto_nums = []
    # print(lotto_list)
    
lotto()