import numpy as np
arr=np.random.randn(10)
np.save('arr',arr)#本操作在当前项目文件夹下生成一个arr.npy的二进制文件
a=np.load('arr.npy')#导入文件必须添加后缀
arr2=np.random.randn(9)
np.savez('some_arr',a=arr,b=arr2)#a,b相当于索引
x=np.load('some_arr.npz')生成的x是一个类似字典的对象
print(x['a'])#打印出a对应的arr数组
