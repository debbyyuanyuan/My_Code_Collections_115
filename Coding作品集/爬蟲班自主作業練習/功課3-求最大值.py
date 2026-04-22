#題目3_求最大值


a=int(input("請輸入第一個數:"))
b=int(input("請輸入第二個數:"))
c=int(input("請輸入第三個數:"))

if a==b or b==c or a==c:
    print("輸入錯誤，請輸入三個不同的數字")
else:
    print("最大值為:", a*b*c)