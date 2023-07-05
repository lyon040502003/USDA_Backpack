# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_backpack_ui_v001_01.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Usd_Backpack(object):
    def setupUi(self, Usd_Backpack):
        if not Usd_Backpack.objectName():
            Usd_Backpack.setObjectName(u"Usd_Backpack")
        Usd_Backpack.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Usd_Backpack.sizePolicy().hasHeightForWidth())
        Usd_Backpack.setSizePolicy(sizePolicy)
        Usd_Backpack.setMinimumSize(QSize(800, 600))
        Usd_Backpack.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(Usd_Backpack)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 761, 571))
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_main_name = QLabel(self.widget)
        self.label_main_name.setObjectName(u"label_main_name")
        font = QFont()
        font.setPointSize(12)
        self.label_main_name.setFont(font)
        self.label_main_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_main_name)

        self.label_version_name = QLabel(self.widget)
        self.label_version_name.setObjectName(u"label_version_name")
        self.label_version_name.setFont(font)
        self.label_version_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_version_name)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_input_usd = QLabel(self.widget)
        self.label_input_usd.setObjectName(u"label_input_usd")
        self.label_input_usd.setFont(font)
        self.label_input_usd.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_input_usd)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_input_usd = QLineEdit(self.widget)
        self.lineEdit_input_usd.setObjectName(u"lineEdit_input_usd")

        self.horizontalLayout.addWidget(self.lineEdit_input_usd)

        self.pushButton_input_usd_browser = QPushButton(self.widget)
        self.pushButton_input_usd_browser.setObjectName(u"pushButton_input_usd_browser")

        self.horizontalLayout.addWidget(self.pushButton_input_usd_browser)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_output_usd = QLabel(self.widget)
        self.label_output_usd.setObjectName(u"label_output_usd")
        self.label_output_usd.setFont(font)
        self.label_output_usd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_output_usd)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_output_usd = QLineEdit(self.widget)
        self.lineEdit_output_usd.setObjectName(u"lineEdit_output_usd")

        self.horizontalLayout_2.addWidget(self.lineEdit_output_usd)

        self.pushButton_output_usd_browser = QPushButton(self.widget)
        self.pushButton_output_usd_browser.setObjectName(u"pushButton_output_usd_browser")

        self.horizontalLayout_2.addWidget(self.pushButton_output_usd_browser)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_pack_to_zip = QCheckBox(self.widget)
        self.checkBox_pack_to_zip.setObjectName(u"checkBox_pack_to_zip")

        self.verticalLayout_3.addWidget(self.checkBox_pack_to_zip)

        self.checkBox_create_command_line_script = QCheckBox(self.widget)
        self.checkBox_create_command_line_script.setObjectName(u"checkBox_create_command_line_script")

        self.verticalLayout_3.addWidget(self.checkBox_create_command_line_script)

        self.checkBox_command_line_script_outside_zip = QCheckBox(self.widget)
        self.checkBox_command_line_script_outside_zip.setObjectName(u"checkBox_command_line_script_outside_zip")

        self.verticalLayout_3.addWidget(self.checkBox_command_line_script_outside_zip)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.pushButton_pack_and_export = QPushButton(self.widget)
        self.pushButton_pack_and_export.setObjectName(u"pushButton_pack_and_export")

        self.verticalLayout_4.addWidget(self.pushButton_pack_and_export)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.scrollArea_debug_info = QScrollArea(self.widget)
        self.scrollArea_debug_info.setObjectName(u"scrollArea_debug_info")
        self.scrollArea_debug_info.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 757, 69))
        self.scrollArea_debug_info.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea_debug_info)

        Usd_Backpack.setCentralWidget(self.centralwidget)

        self.retranslateUi(Usd_Backpack)

        QMetaObject.connectSlotsByName(Usd_Backpack)
    # setupUi

    def retranslateUi(self, Usd_Backpack):
        Usd_Backpack.setWindowTitle(QCoreApplication.translate("Usd_Backpack", u"Usd_Backpack", None))
        self.label_main_name.setText(QCoreApplication.translate("Usd_Backpack", u"Usd Backpack", None))
        self.label_version_name.setText(QCoreApplication.translate("Usd_Backpack", u"V000.01", None))
        self.label_input_usd.setText(QCoreApplication.translate("Usd_Backpack", u"Input Usd", None))
        self.pushButton_input_usd_browser.setText(QCoreApplication.translate("Usd_Backpack", u"Browser", None))
        self.label_output_usd.setText(QCoreApplication.translate("Usd_Backpack", u"Output Usd", None))
        self.pushButton_output_usd_browser.setText(QCoreApplication.translate("Usd_Backpack", u"Browser", None))
        self.checkBox_pack_to_zip.setText(QCoreApplication.translate("Usd_Backpack", u"Zip", None))
        self.checkBox_create_command_line_script.setText(QCoreApplication.translate("Usd_Backpack", u"Create_commandLine_render_pyScript", None))
        self.checkBox_command_line_script_outside_zip.setText(QCoreApplication.translate("Usd_Backpack", u"Command line render script outside of Zip", None))
        self.pushButton_pack_and_export.setText(QCoreApplication.translate("Usd_Backpack", u"Pack_and_export", None))
    # retranslateUi

