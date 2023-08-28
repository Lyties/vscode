import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('_01-data_analyse/pandas/IMDB-Movie-Data.csv')
print(data.head(1))
print(data.info())

print(len(data['Director'].unique()))

print('导演人数：%s' % len(set(data['Director'].values)))

#print('演员人数： %s' % len(set(data['Actors'].values)))

nums = data['Actors'].str.split(',').tolist()
print(len(set([i for j in nums for i in j])))

# list = np.array(nums).flatten()
#print(len(list))
print('*' * 50)
print(data['Genre'])
nums = data['Genre'].str.split(',').tolist()
columns = set([i for j in nums for i in j])

frame = pd.DataFrame(np.zeros((data.shape[0],len(columns))), columns=list(columns))
print(frame)
# 给每个电影赋值为1
for i in range(data.shape[0]):
    frame.loc[i,nums[i]] = 1
print(frame.head(1))
print('a,',frame.sum(axis=0))
count = frame.sum(axis=0).sort_values()
plt.figure(figsize=(5,3),dpi=96)
plt.bar(range(len(count.index)), count.values)
plt.xticks(range(len(count.index)),count.index,  rotation=45)
plt.show()
print('*' * 50)

t1 = data['Runtime (Minutes)']

print(t1)

times = t1.values
 
max_time = times.max()
min_time = times.min()

group = (max_time - min_time) // 5


plt.figure(figsize=(6,3), dpi=96)
plt.xticks(range(min_time,max_time + 5, 5), rotation=45)
plt.hist(times, group)
#plt.show()

