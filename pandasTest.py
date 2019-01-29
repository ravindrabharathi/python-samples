import pandas as pd
tmp = [['Jan',52],['Apr',29],['Mar',46],['Feb',3]]
indx=['zero','one', 'two','three']
df = pd.DataFrame(tmp, columns=["Month", "Count"],index=[i for i in indx])
print(df)
print(df.loc['one':'three'])
df1=pd.read_csv('test1.csv')
print(df1)
print(df1.iloc[2:3])
print(df.loc[df['Month']=='Feb'])
print(df1.loc[df1['Month']=='Feb'])
print(df['Count'].sum())
print(df['Count'].count())
print(df['Count'].min())
print(df['Count'].max())
print(df.values)
print(df.info())
