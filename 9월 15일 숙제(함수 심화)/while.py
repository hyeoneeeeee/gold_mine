
def 숫자가두배():
    for _ in range(5):
        while True:
            try:
                num = input()
                if num == 'exit':
                    return
                num = int(num)
                if type(num) == int:
                    print(f"입력한 숫자는 {num}입니다")
                    break
            except:
                print(f'{num}말고 숫자를 입력해애애애ㅐㅇ')
        print(num*2)
숫자가두배()