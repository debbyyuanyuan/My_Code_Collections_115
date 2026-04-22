import numpy as np

s='78,92,,abc,100,67,25,85'
ps=s.split(',') 
print(ps) 

p=[] 

for x in ps: 
  if x=='': 
    continue
  try:
    p.append(int(x)) 
  except: 
    pass
print(p)
print(f'average:{np.mean(p)}')
print(f'ignore blank getting average: {np.nanmean(p)}')
print(f'standard deviation:{np.std(p)}')
print(f'ignore blank getting sd: {np.std(p)}')