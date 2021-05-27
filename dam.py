import math
n= int(input())
x=list(map(int,input().split()))
dict={}
for i in x:
    dict[i] = x.count(i)
keys =(list(dict.keys()))
values = (list(dict.values()))
maxcount = max(values)
mincount = min(values)
maxarr=[keys[values.index(maxcount)]]
minarr=[]
for i in range(len(values)):
    if(values[i] == mincount):
        minarr.append(keys[i])
# print(maxarr)
# print(minarr)
answers = []
for i in range(len(minarr)):
    diff= math.fabs(maxarr[0] - minarr[i])
    answers.append(diff)
print(int(max(answers)))
