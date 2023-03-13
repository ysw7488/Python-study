dic = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F"}

A = """Apple"""
B = """Banana"""
C = """Cat"""
D = """Dog"""
E = """Elephant"""
F = """Fox"""

n = True

while n:
    for i in range(1, len(dic) + 1):
        print(i, dic[i],end="\n")
    num=int(input("번호를 입력하세요 : "))
    if num == 1:
        print(A)
    elif num == 2:
        print(B)
    elif num == 3:
        print(C)
    elif num == 4:
        print(D)
    elif num == 5:
        print(E)
    elif num == 6:
        print(F)
    break
