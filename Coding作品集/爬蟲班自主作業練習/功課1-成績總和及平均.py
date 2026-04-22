#請使用者輸入5科成績（0~100），得出總和及平均分。

a=int(input("請輸入國文成績(0-100分):"))
b=int(input("請輸入英文成績(0-100分):"))
c=int(input("請輸入數學成績(0-100分):"))
d=int(input("請輸入理化成績(0-100分):"))
e=int(input("請輸入社會成績(0-100分):"))


grade=a+b+c+d+e
print("總分為:", grade)
print("平均為:", grade/5)