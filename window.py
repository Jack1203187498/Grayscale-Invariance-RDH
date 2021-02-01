from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from start import mainEmbedProcess, mainExtractProcess


class Ui_MainWindow(QtWidgets.QMainWindow):

	def __init__(self):
		super(Ui_MainWindow,self).__init__()
		self.setupUi(self)
		self.retranslateUi(self)
		self.filename = ""
		self.embedMessage = ""
		self.warningMesage = ""

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(690, 790)
		self.widget = QtWidgets.QWidget(MainWindow)
		self.retranslateUi(MainWindow)

		self.pushButton = QtWidgets.QPushButton(self.widget)
		self.pushButton.setGeometry(QtCore.QRect(10, 400, 280, 40))
		self.pushButton.setText("打开")

		self.pushButton2 = QtWidgets.QPushButton(self.widget)
		self.pushButton2.setGeometry(QtCore.QRect(10, 450, 280, 40))
		self.pushButton2.setText("嵌入")

		self.pushButton3 = QtWidgets.QPushButton(self.widget)
		self.pushButton3.setGeometry(QtCore.QRect(10, 500, 280, 40))
		self.pushButton3.setText("提取")

		self.textEdit = QtWidgets.QPlainTextEdit(self.widget)
		self.textEdit.setGeometry(QtCore.QRect(10, 10, 280, 380))
		self.textEdit.setPlaceholderText("在这里输入嵌入信息")
		# self.textEdit.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)

		# self.textEdit.setAcceptRichText(True)


		self.warningLabel = QtWidgets.QPlainTextEdit(self.widget)
		self.warningLabel.setGeometry(QtCore.QRect(10, 550, 280, 230))
		self.warningLabel.setPlainText("在这里显示提示信息\n")
		# self.warningLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		self.warningLabel.setReadOnly(True)


		self.original = QtWidgets.QLabel(self.widget)
		self.original.setGeometry(QtCore.QRect(300, 10, 380, 380))
		self.original.setText("这里显示原来的图片")

		self.changed = QtWidgets.QLabel(self.widget)
		self.changed.setGeometry(QtCore.QRect(300, 400, 380, 380))
		self.changed.setText("这里显示嵌入/提取之后的图片")



		MainWindow.setCentralWidget(self.widget)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.action()

	def action(self):
		self.pushButton.clicked.connect(self.openfile)
		self.pushButton2.clicked.connect(self.processEmbed)
		self.pushButton3.clicked.connect(self.processExtract)


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "保持灰度不变性的可逆图片隐藏"))


	def openfile(self):
		openfile_name = QFileDialog.getOpenFileName(self,'选择图片文件','','图片文件(*.png)')
		print(openfile_name)
		self.filename = openfile_name[0]
		if self.filename:
			self.pix = QtGui.QPixmap(self.filename.encode('utf-8').decode('utf-8'))
			# 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
			self.original.setPixmap(self.pix)
			self.original.setScaledContents(True)

	def processEmbed(self):
		self.embedMessage = self.textEdit.toPlainText()
		if not self.filename:
			self.warningMesage = "请选择图片文件！"
			self.warningLabel.setPlainText(self.warningMesage)
			return
		elif not self.embedMessage:
			self.warningMesage = "请输入嵌入信息"
			self.warningLabel.setPlainText(self.warningMesage)
			return

		self.embedMessage = self.textEdit.toPlainText()
		self.warningMesage = "嵌入信息：" + self.embedMessage + "\n开始嵌入"
		self.warningLabel.setPlainText(self.warningMesage)
		try:
			mainEmbedProcess(Size=None, fig=self.filename, Dt=20, rhoT=0, msg=self.embedMessage)
			self.warningMesage += "\n嵌入成功！"
			self.warningLabel.setPlainText(self.warningMesage)
		except:
			self.warningMesage += "\n嵌入失败！"
			self.warningLabel.setPlainText(self.warningMesage)
			return

		self.resultfilename = '.'.join(self.filename.split('.')[:-1] + ['modified'] + self.filename.split('.')[-1:])
		self.warningMesage += "\n嵌入后文件保存为 " + self.resultfilename
		self.warningLabel.setPlainText(self.warningMesage)
		print(self.resultfilename)

		self.pixEmbed = QtGui.QPixmap(self.resultfilename)
		self.changed.setPixmap(self.pixEmbed)
		self.changed.setScaledContents(True)

	def processExtract(self):
		self.embedMessage = self.textEdit.toPlainText()
		if not self.filename:
			self.warningMesage = "请选择图片文件！"
			self.warningLabel.setPlainText(self.warningMesage)
			return

		self.warningMesage = "开始提取信息"
		self.warningLabel.setPlainText(self.warningMesage)
		try:
			self.extractMessage = mainExtractProcess(fig=self.filename)
			self.warningMesage += "\n提取成功！" + "\n提取信息为：" + self.extractMessage
			self.warningLabel.setPlainText(self.warningMesage)

		except:
			self.warningMesage += "\n提取失败！"
			self.warningLabel.setPlainText(self.warningMesage)
			return

		self.resultfilename = '.'.join(self.filename.split('.')[:-1] + ['extracted'] + self.filename.split('.')[-1:])
		self.warningMesage += "\n提取后文件保存为 " + self.resultfilename
		self.warningLabel.setPlainText(self.warningMesage)
		print(self.resultfilename)
		#
		self.pixEmbed = QtGui.QPixmap(self.resultfilename)
		self.changed.setPixmap(self.pixEmbed)
		self.changed.setScaledContents(True)

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())