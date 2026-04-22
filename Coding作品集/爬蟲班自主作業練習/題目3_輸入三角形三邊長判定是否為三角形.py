#題目3_輸入三角形三邊長判定是否為三角形?
#(1)輸入三邊長
#(2)判定是否為三角形
#(3)再判定是等腰、直角、正三角形

a=int(input("輸入邊長a:"))
b=int(input("輸入邊長b:"))
c=int(input("輸入邊長c:"))

if a<=0 or b<=0 or c<=0:
  print("邊長為0無法形成三角形")

elif a+b>c and a+c>b and b+c>a:
  print("這是一個三角形")
  if a==b==c:
    print("且這是一個正三角形")
  elif a==b or b==c or a==c: 
    print("且這是一個等腰三角形")
  elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
    print("且這是一個直角三角形")
  else:
    print("這個三角形沒有特別之處")

else:
  print("這不是一個三角形")

  




