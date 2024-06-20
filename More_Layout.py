# -*- coding: utf-8 -*-
from PySide2 import QtWidgets, QtGui
import sys, json
class mlayout(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(mlayout, self).__init__(parent=parent)

        self.male_list = []
        self.female_list = []
        self.user_list = []
        self.user_dict = {}
        self.setWindowTitle(u"用户信息")

        self.label1 = QtWidgets.QLabel(u"用户名：")
        self.label2 = QtWidgets.QLabel(u"姓名：")
        self.label3 = QtWidgets.QLabel(u"性别：")
        self.label4 = QtWidgets.QLabel(u"年龄：")
        self.label5 = QtWidgets.QLabel(u"部门：")
        self.other_label = QtWidgets.QLabel(u"备注：")

        self.sex_cbx = QtWidgets.QComboBox()
        self.sex_cbx.insertItem(0, u"男")
        self.sex_cbx.insertItem(1, u"女")

        self.user_line = QtWidgets.QLineEdit()
        self.name_line = QtWidgets.QLineEdit()
        self.age_line = QtWidgets.QLineEdit()
        self.department_line_text = QtWidgets.QTextEdit()
        self.other_line = QtWidgets.QLineEdit()

        left_layout = QtWidgets.QGridLayout()
        left_layout.addWidget(self.label1, 0, 0)
        left_layout.addWidget(self.user_line, 0, 1)
        left_layout.addWidget(self.label2, 1, 0)
        left_layout.addWidget(self.name_line, 1, 1)
        left_layout.addWidget(self.label3, 2, 0)
        left_layout.addWidget(self.sex_cbx, 2, 1)
        left_layout.addWidget(self.label4, 3, 0)
        left_layout.addWidget(self.age_line, 3, 1)
        left_layout.addWidget(self.label5, 4, 0)
        left_layout.addWidget(self.department_line_text, 4, 1)
        left_layout.addWidget(self.other_label, 5, 0, 1, 2)
        left_layout.addWidget(self.other_line, 5, 1, 1, 2)
        left_layout.setColumnStretch(0, 1)
        left_layout.setColumnStretch(1, 3)

        self.label6 = QtWidgets.QLabel(u"头像")
        icon_label = QtWidgets.QLabel()
        icon = QtGui.QPixmap("image/P1.JPG")
        icon_label.resize(icon.width(), icon.height())
        icon_label.setPixmap(icon)
        self.icon_but = QtWidgets.QPushButton(u"更换头像")

        hb_layout = QtWidgets.QHBoxLayout()
        hb_layout.setMargin(20)
        hb_layout.addWidget(self.label6)
        hb_layout.addWidget(icon_label)
        hb_layout.addWidget(self.icon_but)

        self.label7 = QtWidgets.QLabel(u"个人说明")
        self.desc_text_edit = QtWidgets.QTextEdit()

        right_layout = QtWidgets.QVBoxLayout()
        right_layout.setMargin(10)
        right_layout.addLayout(hb_layout)
        right_layout.addWidget(self.label7)
        right_layout.addWidget(self.desc_text_edit)

        self.ok_btn = QtWidgets.QPushButton(u"确认")

        self.cancel_btn = QtWidgets.QPushButton(u"取消")
        bottom_layout = QtWidgets.QHBoxLayout()
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.ok_btn)
        bottom_layout.addWidget(self.cancel_btn)


        main_layout = QtWidgets.QGridLayout(self)
        main_layout.setMargin(15)
        main_layout.setSpacing(10)
        main_layout.addLayout(left_layout, 0, 0)
        main_layout.addLayout(right_layout, 0, 1)
        main_layout.addLayout(bottom_layout, 1, 0, 1, 2)
        main_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)


        self.Create_connection()
    def Create_connection(self):
        self.icon_but.clicked.connect(self.open_file)
        self.ok_btn.clicked.connect(self.save_data)
        self.cancel_btn.clicked.connect(self.Cancel_btn)


    def open_file(self):
        f = QtWidgets.QFileDialog.getOpenFileName(self, "Open new picture file","/", "Picture(*.JPG)")

    def closeEvent(self,event):
        close = QtWidgets.QMessageBox.question(self, u"信息收集", u"你要退出收集吗？",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            self.sult_save()
            event.accept()
        else:
            event.ignore()




    def add_clear(self):
        self.user_line.clear()
        self.name_line.clear()
        self.age_line.clear()
        self.other_line.clear()
        self.department_line_text.clear()
        self.desc_text_edit.clear()

    def save_data(self):
        user = self.user_line.text()
        name = self.name_line.text()
        age = self.age_line.text()
        other = self.other_line.text()
        department = self.department_line_text.toPlainText()
        desc = self.desc_text_edit.toPlainText()
        sex = self.sex_cbx.currentText()
        self.user_all_data = {u"用户名": user, u"姓名": name, "性别": sex, u"年龄": age, u"部门": department,
                         u"备注": other, u"个人说明": desc}

        sex = self.sex_cbx.currentText()

        user_sex = self.user_all_data.get("性别")
        user = self.user_dict.get(user_sex)
        if self.user_dict.get(user_sex):
            self.user_dict.get(user_sex).append(self.user_all_data)
        else:
            self.user_dict[user_sex] = [self.user_all_data]



        QtWidgets.QMessageBox.information(self, u'提示', u'信息已保存成功')
        self.user_line.clear()
        self.name_line.clear()
        self.age_line.clear()
        self.other_line.clear()
        self.department_line_text.clear()
        self.desc_text_edit.clear()

    def sult_save(self):

        json_u = json.dumps(self.user_dict, ensure_ascii=False, indent=4)
        with open('user_information.json', 'w') as my_f:
            my_f.write(json_u)
    def Cancel_btn(self):
        button = QtWidgets.QMessageBox.warning(self, "Warning", "此选项会清除已填写的所有数据。",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel,
                                                QtWidgets.QMessageBox.Cancel)
        if button == QtWidgets.QMessageBox.Yes:
            self.user_line.clear()
            self.name_line.clear()
            self.age_line.clear()
            self.other_line.clear()
            self.department_line_text.clear()
            self.desc_text_edit.clear()
        else:
            return


app=QtWidgets.QApplication(sys.argv)
get_layout = mlayout()
get_layout.show()
app.exec_()