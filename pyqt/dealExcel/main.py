import sys

import pandas as pd
from pdways import add_module_to_title,add_precondition_and_step


from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from FileDeal import Ui_MainWindow


class mywindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.file_button.clicked.connect(self.getFile)
        self.file_show.clicked.connect(self.showFile)
        self.save_file.clicked.connect(self.saveFile)


    def getFile(self):
        filtpath=QFileDialog.getOpenFileName(self,'选择文件','D:\\GKS\\_1024')
        self.file_input.setText(filtpath[0])
        # print(filtpath[0])
    def showFile(self):
        filepath=self.file_input.text()
        file_index=self.index_box.text()
        textExcel=pd.read_excel(filepath)
        indexStr=textExcel.iloc[int(file_index),:].tolist()
        # print(indexStr)
        for i in range(0,len(indexStr)):
            indexStr[i]=str(i)+'.'+str(indexStr[i])
        self.index_text.setText('\n'.join(indexStr))
    def saveFile(self):
        step=self.choose_step.currentText()
        savepath = QFileDialog.getSaveFileName()
        index1=int(self.index1.text())
        index2=int(self.index2.text())
        # print(index1)
        if step=='合并模块与标题':
            file=add_module_to_title(self.file_input.text(),index1,index2)
            file.to_excel(savepath[0])
            print('保存成功')
        elif step=='合并预置条件与操作步骤':
            file=add_precondition_and_step(self.file_input.text(),index1,index2)
            file.to_excel(savepath[0])
            print('保存成功')
        else:
            print('暂无该功能')


        print(savepath[1])
if __name__=='__main__':
    app=QApplication(sys.argv)
    myapp=mywindow()
    myapp.show()
    sys.exit(app.exec())