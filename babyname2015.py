import pandas as pd
path = "F:\Downloads\\names\yob2015.txt"
name2015 = pd.read_csv(path, names=['name', 'sex', 'number'])
sex2015 = name2015['sex']
boy2015 = name2015[sex2015 == 'M']
print(boy2015[:10])
print(name2015[:10])
