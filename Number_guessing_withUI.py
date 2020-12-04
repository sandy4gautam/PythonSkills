import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    def guess(self):

        try:
            user_input = int(self.lineEdit.text())
            self.lineEdit.setText("")
        except ValueError:
            self.label.setText('Only Enter numbers')
        if n == user_input:
            self.label.setText(f'Bravo!! You guessed it!')
        elif 5 < (abs(n - user_input)) <= 10:
            self.label.setText('Hey! you are close!')
        elif (abs(n - user_input)) < 5:
            self.label.setText('Almost There!! veryy close!')
        elif (abs(n - user_input)) > 10:
            self.label.setText('Common!!! you can do better. Try again!!')

    def setupUi(self, Dialog):
        count = 0
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 351, 41))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 70, 151, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.guess)




        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(39, 146, 341, 20))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Guess a number between 0 to 100 here"))
        self.pushButton.setText(_translate("Dialog", "Check!!"))


if __name__ == "__main__":
    import sys
    n = random.randint(1, 100)

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
