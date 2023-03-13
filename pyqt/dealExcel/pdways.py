# 导入pandas库
import pandas as pd

# 一些简单配置设置
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


def getFile(file_path):
    file_path = file_path.replace('\\', '\\\\')
    # print(file_path)
    return pd.read_excel(file_path)


def getIndex(file, row):
    return file.iloc[row, :]

#
# file_path = 'D:\GKS\_1024\_1024.xlsx'
#
# textExcel = getFile(file_path)
# indexText = getIndex(textExcel, 1)


# print(indexText)


# 将系统模块添加到测试标题用例
def add_module_to_title(file_path, row_module, row_title):
    # print(file.iloc[1:10, row_module])
    # print(file.iloc[1:10, row_title])
    # print(len(file.iloc[:,1]))
    file=pd.read_excel(file_path)
    for i in range(1, len(file.iloc[:, 1])):
        file.iloc[i, row_title] = '【' + file.iloc[i, row_module] + '】'+file.iloc[i, row_title]
    # print(file.iloc[1:10,row_title])
    return file
#
#
# data_test=add_module_to_title(file_path, 0, 3)
#
# outPath = 'C:\\Users\\000000\\Desktop\\_testData.xlsx'
#
# # outpath为输出文件地址及名称类型
# data_test.to_excel(outPath, sheet_name='前置条件与测试步骤')


# getcount函数用于获取当前的步骤值，以换行为计数点
def getcount(strData):
    return str(strData).count('\n') + 1

# addCount函数用来处理字符串，将、前面的数字增加对应的数值，即修改步骤值，使得步骤与前置条件数值顺序统一
def addCount(count, strData):
    # 转换成列表进行编辑
    strList = list(strData)
    for i in range(1, len(strList)):
        # 默认、符号前面的为步骤值
        if strList[i] == '、':
            strList[i - 1] = int(strList[i - 1]) + count
            strList[i - 1] = str(strList[i - 1])
    return ''.join(strList)

#合并前置条件与操作步骤
def add_precondition_and_step(file_path,col_1,col_2):
    file=pd.read_excel(file_path)
    Data=[]
    data1=file.iloc[1:,col_1]
    data2=file.iloc[1:,col_2]
    # print(file.iloc[1:,col_1])
    # print(file.iloc[1:,col_2][1:10])
    for i in range(1, len(data1) + 1):
        count = getcount(data1[i])
        # print(count)
        data1[i] = str(data1[i]) + '\n'
        if data2[i] == data2[i]:
            data2[i] = addCount(count, data2[i])
        Data.append(str(data1[i]) + str(data2[i]))
    return pd.DataFrame(Data)

# a=add_precondition_and_step('D:\GKS\_1024\_1024.xlsx',4,5)
# # print(a[1:10])
# a=pd.DataFrame(a)
# # # 输出文件地址与名称
# outPath = 'C:\\Users\\000000\\Desktop\\_Test.xlsx'
# #
# # outpath为输出文件地址及名称类型
# a.to_excel(outPath)