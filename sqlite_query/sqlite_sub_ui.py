# Form implementation generated from reading ui file 'd:\NTPU\110_2_Soft_Design\APP_code\sqlite_query\sqlite_sub.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Form.resize(861, 662)
        Form.setStyleSheet("background-color: rgb(0, 44, 47);\n"
"color: rgb(255, 255, 255);")
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(20, 60, 821, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("background-color: rgb(178, 165, 159);\n"
"color: rgb(255, 255, 255);")
        self.label_title.setText("")
        self.label_title.setObjectName("label_title")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(290, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.textBrowser_Authors = QtWidgets.QTextBrowser(Form)
        self.textBrowser_Authors.setGeometry(QtCore.QRect(290, 170, 161, 121))
        self.textBrowser_Authors.setStyleSheet("background-color: rgb(2, 52, 89);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_Authors.setObjectName("textBrowser_Authors")
        self.textBrowser_Abstract = QtWidgets.QTextBrowser(Form)
        self.textBrowser_Abstract.setGeometry(QtCore.QRect(20, 410, 431, 241))
        self.textBrowser_Abstract.setStyleSheet("background-color: rgb(2, 52, 89);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_Abstract.setObjectName("textBrowser_Abstract")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 370, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(290, 300, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_image = QtWidgets.QLabel(Form)
        self.label_image.setGeometry(QtCore.QRect(20, 150, 241, 201))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.textBrowser_Papertext = QtWidgets.QTextBrowser(Form)
        self.textBrowser_Papertext.setGeometry(QtCore.QRect(470, 170, 371, 481))
        self.textBrowser_Papertext.setStyleSheet("background-color: rgb(2, 52, 89);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_Papertext.setObjectName("textBrowser_Papertext")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(470, 130, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pBut_to_main = QtWidgets.QPushButton(Form)
        self.pBut_to_main.setGeometry(QtCore.QRect(20, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pBut_to_main.setFont(font)
        self.pBut_to_main.setStyleSheet("background-color: rgb(30, 100, 110);\n"
"color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\NTPU\\110_2_Soft_Design\\APP_code\\sqlite_query\\icon/arrow-left-circle.svg"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        self.pBut_to_main.setIcon(icon)
        self.pBut_to_main.setObjectName("pBut_to_main")
        self.pBut_event_info = QtWidgets.QPushButton(Form)
        self.pBut_event_info.setGeometry(QtCore.QRect(330, 300, 21, 21))
        self.pBut_event_info.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\NTPU\\110_2_Soft_Design\\APP_code\\sqlite_query\\icon/info.svg"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap("d:\\NTPU\\110_2_Soft_Design\\APP_code\\sqlite_query\\icon/info.svg"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        self.pBut_event_info.setIcon(icon1)
        self.pBut_event_info.setObjectName("pBut_event_info")
        self.label_Eventtype = QtWidgets.QLabel(Form)
        self.label_Eventtype.setGeometry(QtCore.QRect(290, 330, 161, 31))
        self.label_Eventtype.setStyleSheet("background-color: rgb(2, 52, 89);\n"
"color: rgb(255, 255, 255);")
        self.label_Eventtype.setText("")
        self.label_Eventtype.setObjectName("label_Eventtype")
        self.label_ID = QtWidgets.QLabel(Form)
        self.label_ID.setGeometry(QtCore.QRect(760, 30, 81, 21))
        self.label_ID.setStyleSheet("color: rgb(178, 165, 159);")
        self.label_ID.setText("")
        self.label_ID.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_ID.setObjectName("label_ID")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "作者"))
        self.label_3.setText(_translate("Form", "摘要"))
        self.label_4.setText(_translate("Form", "型態"))
        self.label_5.setText(_translate("Form", "全文"))
        self.pBut_to_main.setText(_translate("Form", "  返回查詢頁面"))
