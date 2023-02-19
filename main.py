from PyQt6.QtWidgets import QApplication
import sys
import LoginUI

app = QApplication(sys.argv)
mainWindow = LoginUI.Login_Form()
mainWindow.show()
sys.exit(app.exec())