#題目1_一串數列中找出最大值
nums = [3,51,63,23,7,18,85,12,5,34]
max_val = nums[0]
min_val = nums[0]
for n in nums[1:]:
    if n > max_val:
        max_val = n
print(max_val)
