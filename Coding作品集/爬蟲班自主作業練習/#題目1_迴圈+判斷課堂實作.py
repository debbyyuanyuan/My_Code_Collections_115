#題目1_迴圈+判斷課堂實作
#(1)使用者輸入國、英、數三科成績
#(2)計算國英數三科成績的總分及平均
#(3)利用平均判斷是否及格?
#(4)可讓5個同學輸入三科成績


for i in range(5):
  i=i+1
  for j in range(i):

    print("學生", i)
    
    chinese=int(input("請輸入國文成績:"))
    math=int(input("請輸入數學成績:"))
    english=int(input("請輸入英文成績:"))

    sum=chinese+math+english
    avg=sum/3

    print("總分=",sum)
    print("平均分=",avg)

    if avg>=60:
      print("及格\n")
    else:
      print("不及格\n")
    
    break