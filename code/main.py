from QtTest import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5 import QtGui

class CamShow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):   # 绑定
        super(CamShow, self).__init__(parent)
        self.setupUi(self)
        # 信号与槽
        self.OpenFileBtn.clicked.connect(self.loadImage)    # 当被点击之后就会连接loadImage函数
        self.actionOpen.triggered.connect(self.loadImage)    # triggered是菜单栏的按下
        self.actionexit.triggered.connect(self.exit)    # 退出
        self.actionabout.triggered.connect(self.about)   # 关于

    def loadImage(self):
        # print("按钮被按下了")
        self.infoLabel.setText("打开文件按钮被按下了")
        self.fname, _ = QFileDialog.getOpenFileName(self, '选择图片', '.', '图像文件(*.jpg *.png)')
        print(self.fname)

        pix = QtGui.QPixmap(self.fname).scaled(self.ImageLabel.width(), self.ImageLabel.height())
        self.ImageLabel.setPixmap(pix)

    def exit(self):
        sys.exit(app.exec_())

    def about(self):
        self.infoLabel.setText("帮助按钮被按下了")
        QMessageBox.information(self, '软件说明', '该软件由xxx制作而成，软件版本为1.0')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = CamShow()
    ui.show()
    sys.exit(app.exec_())
