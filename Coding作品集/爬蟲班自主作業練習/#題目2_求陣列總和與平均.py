#題目2_求陣列總和與平均
scores = [41,23,56,45,90,86,34,52,88,70,86,68,61]
total = 0
for s in scores:
    total += s
avg = total / len(scores)
print(f"總分: {total}, 平均: {avg:.2f}")
