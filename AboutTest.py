import xlrd
import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
# pd.set_option('max_colwidth',100)
TextExcel=pd.read_excel('C:\\Users\\gks30\\Desktop\\test.xls',sheet_name='测试记录')
# print(TextExcel.iloc[1,[2,3,5,6,7]])
Data1=TextExcel.iloc[1:,3]
Data2=TextExcel.iloc[1:,5]
# print(Data2)
Data3=[]
Data3.append(0)
print(len(Data1),len(Data2))
# print(Data1)
for i in range(1,10):
    if Data1[i]!=Data1[i] :
        Data1[i]=Data1[i-1]
    # Data3[i]=str(Data1[i])+str(Data2[i])
    Data3.append(str(Data1[i]+'\n')+str(Data2[i]))
    print(Data3[i])
    # print(Data1[i])
    print('----')
    # print(Data2[i])
# print(Data3)
Data4=pd.DataFrame(Data3)
print(Data4)
Data4.to_excel('C:\\Users\\gks30\\Desktop\\AboutTest.xls',sheet_name='测试记录')