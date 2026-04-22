#題目2_break跳離迴圈
#猜一猜數字，給使用者5次機會，猜對就秀出好棒棒，猜錯必須告知比預設的值大還是小

import random
num=random.randint(1,100)

for i in range (5):
  guess=int(input('從1-100，請猜猜看數字:'))

  if guess>num:
    print("再往小的猜!")
  elif guess<num:
    print("再往大的猜!")
  else:
    print("好棒棒!")
    break

