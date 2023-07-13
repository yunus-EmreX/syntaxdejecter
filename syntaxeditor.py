import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import autopep8

class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Yazılım Düzenleyici")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("icon.png"))

        self.text_edit = QTextEdit(self)
        self.text_edit.setFontPointSize(12)
        self.setCentralWidget(self.text_edit)

        self.statusBar().showMessage("Yazılım Düzenleyici Hazır")

        self.createMenuBar()

        self.show()

    def createMenuBar(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("Dosya")

        open_action = file_menu.addAction("Aç")
        open_action.triggered.connect(self.openFile)

        save_action = file_menu.addAction("Kaydet")
        save_action.triggered.connect(self.saveFile)

        edit_menu = menubar.addMenu("Düzenle")

        format_action = edit_menu.addAction("Kodu Düzenle")
        format_action.triggered.connect(self.formatCode)

    def openFile(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Dosya Aç", "", "Python Dosyaları (*.py)")

        if file_path:
            with open(file_path, "r") as file:
                code = file.read()
                self.text_edit.setPlainText(code)

    def saveFile(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Dosya Kaydet", "", "Python Dosyaları (*.py)")

        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_edit.toPlainText())

    def formatCode(self):
        code = self.text_edit.toPlainText()

        try:
            formatted_code = autopep8.fix_code(code)
            self.text_edit.setPlainText(formatted_code)
        except Exception as e:
            QMessageBox.critical(self, "Hata", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = CodeEditor()
    sys.exit(app.exec_())
