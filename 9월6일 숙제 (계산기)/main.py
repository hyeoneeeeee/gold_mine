import operation

num_list = list(map(str,input('숫자 기호 숫자 :').split()))
a,b = int(num_list[0]),int(num_list[2])
if num_list[1] == '+':
    operation.sum(a,b)
elif num_list[1] == '-':
    operation.min(a,b)
elif num_list[1] == '/':
    operation.div(a,b)
elif num_list[1] == '*':
    operation.mul(a,b)
        
    