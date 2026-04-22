#判斷題目一的平均分是否及格。

a=int(input("請輸入國文成績(0-100分):"))
b=int(input("請輸入英文成績(0-100分):"))
c=int(input("請輸入數學成績(0-100分):"))
d=int(input("請輸入理化成績(0-100分):"))
e=int(input("請輸入社會成績(0-100分):"))


grade=a+b+c+d+e
print("總分為:", grade)
print("平均為:", grade/5)

avg=grade/5

if avg>=90:
    print("優")
elif avg>=80:
    print("甲")
elif avg>=70:
    print("乙")
elif avg>=60:
    print("丙")
elif avg>=50:
    print("補考")
else:
    print("明年再來")