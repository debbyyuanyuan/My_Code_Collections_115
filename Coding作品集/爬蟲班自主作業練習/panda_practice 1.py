import pandas as pd
s = pd.Series({'小明':90, '小華':80, '小李':70})
s['小強'] = 55
print(s)