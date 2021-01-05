'''
    factorial 一个正整数的阶乘（factorial）是所有小于及等于该数的正整数的积，并且0的阶乘为1。
    自然数n的阶乘写作n!。
'''
# 普通写法
'''
ret = 1
x = validInputNum()
if(x==0):
    ret = 1
else:
    for i in range(1, x+1):
        ret = ret * i

print(ret)
'''


#迭代的方法

def fact(n):
    if(n==0):
        return 1
    else:
        return n * fact(n-1)

    
#检查输入数字是否正确
def validInputNum():
    while 1==1:
        try:
            x = int(input('请输入正整数：'))
            if(x<0):
                print('输入的数字必须是正整数')
                continue
            break
        except:
            print('请输入正确的正整数')

    return x

if __name__ == '__main__':
    n = validInputNum()
    print(fact(n))
