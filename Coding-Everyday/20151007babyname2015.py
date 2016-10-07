import pandas as pd
path = "F:\Downloads\\names\yob2015.txt"
name2015 = pd.read_csv(path, names=['name', 'sex', 'number'])#读取文件数据，文件分为三列，name,sex,number
sex2015 = name2015['sex']#取出sex这一列
boy2015 = name2015[sex2015 == 'M']#判断这一列哪些是M，哪些是F，若为M则返回True否则返回False，得到一个bool型的索引
print(boy2015[:10])#打印出排名前十的男生名字
print(name2015[:10])#女生名字在最前面，所以可以直接打印前十个元素即为排名前十的女生名字
