import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1350, 680)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 90, 1111, 641))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.txtName = QtWidgets.QTextEdit(self.widget)
        self.txtName.setGeometry(QtCore.QRect(190, 70, 291, 30))
        self.txtName.setObjectName("txtName")
        self.txtContact = QtWidgets.QTextEdit(self.widget)
        self.txtContact.setGeometry(QtCore.QRect(190, 350, 291, 30))
        self.txtContact.setObjectName("txtContact")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(90, 120, 91, 30))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(100, 230, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txtRoll = QtWidgets.QTextEdit(self.widget)
        self.txtRoll.setGeometry(QtCore.QRect(190, 120, 291, 30))
        self.txtRoll.setObjectName("txtRoll")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(90, 340, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txtBranch = QtWidgets.QTextEdit(self.widget)
        self.txtBranch.setGeometry(QtCore.QRect(190, 290, 291, 30))
        self.txtBranch.setObjectName("txtBranch")
        self.txtAddress = QtWidgets.QTextEdit(self.widget)
        self.txtAddress.setGeometry(QtCore.QRect(190, 400, 291, 31))
        self.txtAddress.setObjectName("txtAddress")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(90, 400, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 70, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(100, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtFName = QtWidgets.QTextEdit(self.widget)
        self.txtFName.setGeometry(QtCore.QRect(190, 170, 291, 31))
        self.txtFName.setObjectName("txtFName")
        self.rbMale = QtWidgets.QRadioButton(self.widget)
        self.rbMale.setGeometry(QtCore.QRect(200, 240, 95, 20))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        self.rbMale.setFont(font)
        self.rbMale.setObjectName("rbMale")
        self.rbFemale = QtWidgets.QRadioButton(self.widget)
        self.rbFemale.setGeometry(QtCore.QRect(280, 240, 95, 20))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        self.rbFemale.setFont(font)
        self.rbFemale.setObjectName("rbFemale")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(140, 20, 41, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.txtId = QtWidgets.QTextEdit(self.widget)
        self.txtId.setGeometry(QtCore.QRect(190, 20, 291, 41))
        self.txtId.setObjectName("txtId")
        self.btnSave = QtWidgets.QPushButton(self.widget, clicked=lambda: self.save())
        self.btnUpdate = QtWidgets.QPushButton(self.widget, clicked=lambda: self.update())
        self.btnDelete = QtWidgets.QPushButton(self.widget, clicked=lambda: self.delete())
        self.btnRefresh = QtWidgets.QPushButton(self.widget, clicked=lambda: self.refresh())
        self.btnSearch = QtWidgets.QPushButton(self.widget,clicked=lambda: self.search())
        self.btnSave.setGeometry(QtCore.QRect(92 , 490,121, 40))
        self.btnSave.setObjectName("btnSave")

        self.btnUpdate.setGeometry(QtCore.QRect(310, 490, 121, 40))
        self.btnUpdate.setObjectName("btnUpdate")

        self.btnDelete.setGeometry(QtCore.QRect(90, 540,121, 40))
        self.btnDelete.setObjectName("btnDelete")

        self.btnRefresh.setGeometry(QtCore.QRect(310, 540, 121, 40))
        self.btnRefresh.setObjectName("btnRefresh")
        self.tblViewData = QtWidgets.QTableWidget(self.widget)
        self.tblViewData.setGeometry(QtCore.QRect(510, 130, 601, 400))
        self.tblViewData.setObjectName("tblViewData")
        self.tblViewData.setRowCount(0)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(510, 80, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(630, 81, 81, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(720, 80, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.txtSearch = QtWidgets.QTextEdit(self.widget)
        self.txtSearch.setGeometry(QtCore.QRect(740, 80, 231, 31))
        self.txtSearch.setObjectName("txtSearch")

        self.btnSearch.setGeometry(QtCore.QRect(990, 80, 121, 30))
        self.btnSearch.setObjectName("btnSearch")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(360, 20, 431, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:red;")
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.txtId.setDisabled(True)
        self.tblViewData.setColumnCount(8)
        self.tblViewData.setRowCount(0)
        self.tblViewData.setHorizontalHeaderLabels(
            ["Id", "Student Name", "Roll", "Father Name", "Gender", "Branch", "Contact", "Address"])
        self.tblViewData.clicked.connect(self.onRowClick)
        self.comboBoxData = ["Id","Name", "Roll_num", "Fname", "Gender", "Branch", "Contact", "Address"]
        self.comboBox.addItems(self.comboBoxData)
        self.showDataOnTable()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Roll No"))
        self.label_4.setText(_translate("Dialog", "Gender"))
        self.label_7.setText(_translate("Dialog", "Contact"))
        self.label_6.setText(_translate("Dialog", "Address"))
        self.label_3.setText(_translate("Dialog", "Father Name"))
        self.label.setText(_translate("Dialog", "Student Name"))
        self.label_5.setText(_translate("Dialog", "Branch"))
        self.rbMale.setText(_translate("Dialog", "Male"))
        self.rbFemale.setText(_translate("Dialog", "Female"))
        self.label_8.setText(_translate("Dialog", "Id"))
        self.btnSave.setText(_translate("Dialog", "Save"))
        self.btnUpdate.setText(_translate("Dialog", "Update"))
        self.btnDelete.setText(_translate("Dialog", "Delete"))
        self.btnRefresh.setText(_translate("Dialog", "Refresh"))
        self.label_10.setText(_translate("Dialog", "Search By"))
        self.label_11.setText(_translate("Dialog", ":"))
        self.btnSearch.setText(_translate("Dialog", "Search"))
        self.label_9.setText(_translate("Dialog", "Student Management System"))

    def checkEmpty(self):
        name = self.txtName.toPlainText()
        roll = self.txtRoll.toPlainText()
        fname = self.txtFName.toPlainText()
        genderm = self.rbMale.text()
        genderf = self.rbFemale.text()
        branch = self.txtBranch.toPlainText()
        contact = self.txtContact.toPlainText()
        address = self.txtAddress.toPlainText()
        if name == "" or roll == "" or fname == "" or genderf == "" or genderm == "" or branch == "" or contact == "" or address == "":
            return False
        return True

    def errorMessageBox(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def successMessageBox(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Success")
        msg.setInformativeText(message)
        msg.setWindowTitle("Success")
        msg.exec_()

    def clearfield(self):
        self.txtId.setText("")
        self.txtName.setText("")
        self.txtRoll.setText("")
        self.txtSearch.setText("")
        self.txtBranch.setText("")
        self.txtContact.setText("")
        self.txtAddress.setText("")
        self.txtFName.setText("")
        self.comboBox.setCurrentIndex(0)

    def connection(self):
        conn = sqlite3.connect(
            r'C:\Users\Acer\OneDrive\Desktop\sms2\database.db')
        return conn

    def onRowClick(self, item):
        self.row_num = item.row()
        data_on_row = self.getData("select * from student")
        for row, data in enumerate(data_on_row):
            if self.row_num == row:
                self.txtId.setText(str(data[0]))
                self.txtName.setText(data[1])
                self.txtRoll.setText(data[2])
                self.txtFName.setText(data[3])
                self.txtBranch.setText(data[5])
                self.txtContact.setText(data[6])
                self.txtAddress.setText(data[7])

    def delete(self):
        id = self.txtId.toPlainText()
        if id != "":
            query = f"delete from student where id={int(id)}"
            self.IUD(query)
            self.successMessageBox("Student deleted successfully")
            self.refresh()
        else:
            self.errorMessageBox("Please select student from table which needs to be deleted")

    def update(self):
        id = self.txtId.toPlainText()
        if id != "":
            if self.checkEmpty():
                name = self.txtName.toPlainText()
                roll = self.txtRoll.toPlainText()
                fname = self.txtFName.toPlainText()
                genderm = self.rbMale.text()
                gender = self.rbFemale.text()
                branch = self.txtBranch.toPlainText()
                contact = self.txtContact.toPlainText()
                address = self.txtAddress.toPlainText()
                if genderm == "male":
                   gender == "male"
                else:
                    gender = "female"
                query = f"update student set name='{name}',Roll_num='{roll}',Fname='{fname}',Gender='{gender}',Branch='{branch}',Contact='{contact}',Address='{address}' where id={int(id)}"
                self.IUD(query)
                print("aakash")
                self.successMessageBox("Student Updated Successfully")
                self.refresh()
            else:
                self.errorMessageBox("Please enter all fields")
        else:
            self.errorMessageBox("Please select from Table on right")

    def getData(self,query):
        con = self.connection()
        c = con.cursor()
        c.execute(query)
        data = c.fetchall()
        return data

    def refresh(self):
        self.clearfield()
        self.tblViewData.setRowCount(0)
        self.showDataOnTable()


    def search(self):
        field = self.comboBox.currentText()
        value = self.txtSearch.toPlainText()
        if value=="":
            self.errorMessageBox(f"Please put your {field} in the text box")
        else:
            if field=="ID":
                query = f"select * from student where ID={value}"
            else:
                query = f"Select * from student where {field} like '{value}%'"
            data = self.getData(query)
            self.tblViewData.setRowCount(0)
            for row, form in enumerate(data):
                self.tblViewData.insertRow(row)
                for column, item in enumerate(form):
                    self.tblViewData.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))


    def showDataOnTable(self):
        data = self.getData(f"select * from student")
        self.tblViewData.setRowCount(0)
        for row, form in enumerate(data):
            self.tblViewData.insertRow(row)
            for column, item in enumerate(form):
                self.tblViewData.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))




    def save(self):
        if (self.checkEmpty()):
            name = self.txtName.toPlainText()
            roll = self.txtRoll.toPlainText()
            fname = self.txtFName.toPlainText()
            genderm = self.rbMale.text()
            genderf = self.rbFemale.text()
            branch = self.txtBranch.toPlainText()
            contact = self.txtContact.toPlainText()
            address = self.txtAddress.toPlainText()
            if genderm == "male":
                gender = "male"
            else:
                gender = "female"
            query = f"insert into student(Name, Roll_num, Fname, Gender,Branch, Contact,Address) values ('{name}', '{roll}', '{fname}','{gender}','{branch}','{contact}','{address}' )"
            self.IUD(query)
            self.successMessageBox("Student added Successfully")
            self.refresh()
        else:
            self.errorMessageBox("Please enter all fields")

    def IUD(self, query):
        con = self.connection()
        c = con.cursor()
        c.execute(query)
        con.commit()
        con.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
