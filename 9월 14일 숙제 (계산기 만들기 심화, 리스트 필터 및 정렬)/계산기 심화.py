
class claculator():
    def __init__(self):
        while True:
            try:
                num1,oper,num2 = input().split(' ')
                num1 = int(num1)
                num2 = int(num2)
                if num2 == 0 and oper == '/':
                    print('0으로 나눌 수 없습니다')
                    continue 
                elif oper not in ['+','-','*','/']:
                    print('수식을 다시입력해 주세요')
                    continue
                else:
                    break
            except: 
                print('잘못 입력하셨습니다. 다시 입력해 주세요. :숫자 기호 숫자')
        self.num1 = int(num1)
        self.num2 = int(num2)
        self.oper = oper
    def EXPRESSTION(self):
        if self.oper =='+':
            return self.num1 + self.num2
        elif self.oper =='-':
            return self.num1 - self.num2
        elif self.oper =='*':
            return self.num1 * self.num2
        elif self.oper =='/':
            return self.num1 / self.num2
cal1 = claculator()
print(cal1.EXPRESSTION())
