import matplotlib.pyplot as plt   # 导包
import numpy as np 
# 解决图表中不显示文字和负号的问题
plt.rcParams['font.sans-serif'] =['Songti SC','Microsoft YaHei']  
plt.rcParams['axes.unicode_minus'] = False

x = [1.3,2.5,3.7,5.7,8.9,9.5]
y = [2.5,3.5,4.5,6.8,7.9,9.9]
plt.figure(figsize=(10,4))  # 创建画布
# 折线图 简单看看 下面更详细
plt.plot(x, # x轴数据
        y,  # y轴数据 
        color='c',   # 线颜色
        linewidth=5, # 线宽度 
        linestyle='--', # 线样式 虚线
        marker='o',  # 点标记 
        markeredgecolor='red', # 点边缘颜色 点默认与线颜色一致
        markeredgewidth=1,     # 点边缘宽度
        markersize=10,         # 点大小
        label='我是图例'         # 图例 默认不显示 需与plt.legend()一起使用
           )
# plt.plot(x,y,linestyle='--',marker='o') 可简写成 plt.plot(x,y,‘--o’)         
plt.title('我是标题',fontsize=20,color='red',loc='left')  # 设置标题, fontsize字号20, color颜色红色, loc位置左
plt.xlabel('我是x轴',fontsize=15,color='blue',labelpad=-25,position=(1.05,0))            # 设置x轴标签
plt.ylabel('我是y轴',fontsize=15,color='blue',labelpad=10,position=(0,0.9))# 设置y轴标签
plt.xticks(x,[f'x_{i}' for i in range(len(x))],size=12)  # 设置x轴刻度显示值 plt.xticks(原x刻度,新x刻度) 维度需一致
plt.yticks(y,["%.2f" %i for i in y],size=11)             # 设置y轴刻度显示值 保留两位小数
plt.ylim([0,15])                                          # 设置y轴范围 ； x轴范围设置一样 plt.xlim([])     
plt.legend(loc='upper center')                            # 设置图例 显示位置

#设置上边和右边无边框  
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 添加数据标签
for x,y in zip(x,y):
    plt.text(x-0.1,y+0.5,y)   # plt.text(x,y,text)  在(x,y)出显示text 

# 设置带有箭头的任意文本  
plt.annotate('我在学习python画图呢!',xytext = (6,4),xy = (9,10), arrowprops = dict(facecolor = 'blue', shrink = 0.1))    # plt.annotate(text,xytext,xy) 箭头由xytext指向xy 文本在xytext处显示
plt.scatter(9,10,s=100,c='m')  # 为了更清晰上面的效果 散点图画出一个点
plt.show() 
