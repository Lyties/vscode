# coding=utf-8
from matplotlib import pyplot as plt;
from matplotlib import rcParams

rcParams['font.sans-serif']=['Songti SC','STFangsong']
#rcParams['axes.unicode_minus'] = False  # 用来正常显示负号



x = range(2,26,2)
y1 = [15,13,14.5,17,20,25,26,27,22,18,15,14]
y2 = [16,13,14.7,17,22,25,28,27,23,18,15,12]
fig = plt.figure(figsize=(5,3), dpi=96)

plt.plot(x, y1,label='北京')
plt.plot(x, y2,label='上海')
_x =range(2,25,2)
x_lables = ['{}点'.format(i) for i in _x]
plt.xticks(_x,x_lables,rotation=45)
plt.yticks(range(min(y1),(max(y2) + 1)))

plt.legend()
plt.xlabel('时间')
plt.ylabel('温度 单位(℃)')
plt.title('今天的气温变化')
plt.grid(alpha=.2)
# png svg
plt.savefig("./weather.svg")
plt.show()