import numpy as np
import pandas as pd

'Working with series in Pandas along with Numpy'
# arr = np.array([10,20,30,40,50])
# s = pd.Series(arr)
# print(s)

# t = np.sqrt(s)
# print(t)

# index = np.array(['a','b','c','d','e'])
# arr = np.array([10,20,30,40,50])
# s = pd.Series(arr,index = index)
# print(s)

'Finding number of elements in a series'
# s1 = np.array([10,20,30,40,50])
# print('Series is: ',s1)
# print('Size of the series is: ',s1.size)

'Mean, Max and MIn in a Series'
# s1 = np.array([10,20,30,40,50])
# print(f"Mean of s1 is {s1.mean()}")
# print(f"Min value in s1 is {s1.min()}")
# print(f"Max value in s1 is {s1.max()}")

'Sorting a Series'
# s1 = pd.Series([40,80,90,70,60,50,10,30,20])
# print(f"Original series is \n{s1}")
# print(f"Sorted series is \n{s1.sort_values()}")

'Displaying unique values in a series'
# s1 = pd.Series([50,40,60,70,80,80,40])
# print(s1.unique())
# print(s1.nunique())

'Summary of series statistics'
# s1 = pd.Series([10,20,30,40,50,60,70])
# print(s1.describe())

'Creating Data frame from a series'
# name = pd.Series(["Rohit","Virat"])
# team = pd.Series(["MI","RCB"])
# dic = {"Name":name, "Team":team}
# df = pd.DataFrame(dic)
# print(df)

'Creating Data frame from list of dictionaries'
# l = [{'Name':'Sachin', 'Surname':'Tendulkar'},
#     {'Name':'Hardik', 'Surname':'Patel'},
#     {'Name':'Virat', 'Surname':'Kohli'}]
# df = pd.DataFrame(l)
# print(df)    

'Accessing row_wise and column-wise data'
# l = [{'Name':'Sachin', 'Surname':'Tendulkar'},
#     {'Name':'Hardik', 'Surname':'Patel'},
#     {'Name':'Virat', 'Surname':'Kohli'}]
# df = pd.DataFrame(l)
# print(df)   

# for (row_index, row_value) in df.iterrows():
#     print("\n Row index is ", row_index)
#     print("Row value is ", row_value)
    
# for (col_index, col_value) in df.items():
#     print("\n Col index is ", col_index)
#     print("Col value is ", col_value)
    
'Add, rename or delete a column'
# s = pd.Series([10,15,20,25,30])
# df = pd.DataFrame(s)
# # print(df)
# df.columns = ['List1']
# df['List2'] = ([10,15,20,25,30])
# print(df)

'Add, rename or delete a column'
# s = pd.Series([10,15,20,25,30])
# df = pd.DataFrame(s)
# df.columns = ['List1']
# df['List2'] = ([15,20,25,30,35])
# df['List3'] = ([20,25,30,35,40])
# df['List4'] = df['List1'] + df['List2'] + df['List3']
# del df['List4']
# df.pop('List3')
# print(df)

s = pd.Series([10,15,20,25,30])
df = pd.DataFrame(s)
df.columns = ['List1']
df['List2'] = ([15,20,25,30,35])
df['List3'] = ([20,25,30,35,40])
print(df)
df1 = df.drop('List2',axis=1)
print(df1)
df2 = df.drop('List3',axis=0)
print(df2)

'Boolean Indexing in Data frames'
# dic = {'Name':['Sachin','Virat','Hardik'],
#             'Age' : [50,34,29]}
            
# df = pd.DataFrame(dic, index =[True,False,True])
# print(df)
# print(df.loc[False])

'Concatenating two dataframes'
dict1 = {'id': [10,18,7], 'Name': ['Sachin','Kohli','Dhoni']}
# df1 = pd.DataFrame(dict1)
# print(df1)

# dict2 = {'id': [45,27], 'Name': ['Rohit','Shikhar']}
# df2 = pd.DataFrame(dict2)
# print(df2)

# df3 =pd.concat([df1,df2])
# print(df3)