from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QMainWindow
from PyQt6 import uic





class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("USDA_Backpack_scripts\\ui_scripts\\main_backpack_ui_v001_01.ui", self)

    #     self.label_result = self.findChild(QLabel, "label_result")

    #     self.combo = self.findChild(QComboBox, "comboBox")

    #     self.combo.currentTextChanged.connect(self.combo_changed)


    # def combo_changed(self):
    #     item = self.combo.currentText()
        # self.label_result.setText("Your Favorite Language : " + item)



app = QApplication([])
window = UI()
window.show()
app.exec()