# -*- coding: utf-8 -*-
from PySide2 import QtWidgets, QtGui, QtCore
import sys
class basic_dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(basic_dialog, self).__init__(parent=parent)
        self.setWindowTitle('个人信息收集')

        main_splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal, self)
        main_splitter.setOpaqueResize(True)

        self.list_widget = QtWidgets.QListWidget(main_splitter)
        self.list_widget.insertItem(0, '个人资料')
        self.list_widget.insertItem(1, '联系方式')
        self.list_widget.insertItem(2, '详细信息')

        frame = QtWidgets.QFrame(main_splitter)
        stack = QtWidgets.QStackedWidget()
        stack.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Raised)  #设置堆栈窗的显示风格


        base_info = baseinfo()
        contact = contact_data()
        detail = detail_data()
        stack.addWidget(base_info)
        stack.addWidget(contact)
        stack.addWidget(detail)

        save_btn = QtWidgets.QPushButton('保存')
        self.cancel_btn = QtWidgets.QPushButton('取消')

        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addStretch(1)
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(self.cancel_btn)

        main_layout = QtWidgets.QVBoxLayout(frame)
        main_layout.setMargin(10)
        main_layout.setSpacing(6)
        main_layout.addWidget(stack)
        main_layout.addLayout(btn_layout)

        self.list_widget.currentRowChangeed.connect(stack.setCurrentIndex)#列表框的currentRowChanged()信号与堆栈窗的setCurrentIndex()槽相连接，达到按用户选择的条目显示页面的要求。
        self.cancel_btn.clicked.connect(self.close)

        lout = QtWidgets.QHBoxLayout(self)
        lout.addWidget(main_layout)
        self.setLayout(lout)


class baseinfo(QtWidgets):
    pass
class contact_data(QtWidgets):
    pass
class detail_data(QtWidgets):
    pass

app = QtWidgets.QApplication(sys.argv)
wind = basic_dialog()
wind.show()
app.exec_()