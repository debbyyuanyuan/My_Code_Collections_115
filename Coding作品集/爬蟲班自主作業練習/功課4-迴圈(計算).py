#題目1_迴圈(計算)
#sum=1+3+5+...+29

sum=0

for i in range(1,31,2):
    sum=sum+i

print(int(sum))