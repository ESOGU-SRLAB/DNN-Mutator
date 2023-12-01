# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QTreeView,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1443, 1000)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1000, 1000))
        MainWindow.setMaximumSize(QSize(1445, 1000))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /"
                        "////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: "
                        "no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////"
                        "////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    b"
                        "ackground-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; "
                        "}\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget "
                        "*/\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertic"
                        "al\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
" "
                        "   height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
""
                        "    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
""
                        "	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////////////////"
                        "//////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;"
                        "\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: r"
                        "gb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hov"
                        "er {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_46 = QLabel(self.topLogoInfo)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(0, 0, 50, 50))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy1)
        self.label_46.setMinimumSize(QSize(50, 50))
        self.label_46.setMaximumSize(QSize(16777215, 50))
        self.label_46.setSizeIncrement(QSize(-1, 0))
        self.label_46.setPixmap(QPixmap(u"../../../../Desktop/Dnn Module/Yedek/Tailored-Mutation-based-Software-Fault-Injection-Tool-IM-FIT/src/images/images/ros-icon.png"))
        self.label_46.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy2)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy2.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy2)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.open_ros_page = QPushButton(self.topMenu)
        self.open_ros_page.setObjectName(u"open_ros_page")
        sizePolicy2.setHeightForWidth(self.open_ros_page.sizePolicy().hasHeightForWidth())
        self.open_ros_page.setSizePolicy(sizePolicy2)
        self.open_ros_page.setMinimumSize(QSize(0, 45))
        self.open_ros_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_ros_page.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-dialpad.png);")

        self.verticalLayout_8.addWidget(self.open_ros_page)

        self.btn_start = QPushButton(self.topMenu)
        self.btn_start.setObjectName(u"btn_start")
        sizePolicy2.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy2)
        self.btn_start.setMinimumSize(QSize(0, 45))
        self.btn_start.setFont(font)
        self.btn_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start.setLayoutDirection(Qt.LeftToRight)
        self.btn_start.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-data-transfer-down.png);")

        self.verticalLayout_8.addWidget(self.btn_start)

        self.btn_scan = QPushButton(self.topMenu)
        self.btn_scan.setObjectName(u"btn_scan")
        sizePolicy2.setHeightForWidth(self.btn_scan.sizePolicy().hasHeightForWidth())
        self.btn_scan.setSizePolicy(sizePolicy2)
        self.btn_scan.setMinimumSize(QSize(0, 45))
        self.btn_scan.setFont(font)
        self.btn_scan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_scan.setLayoutDirection(Qt.LeftToRight)
        self.btn_scan.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-magnifying-glass.png);")

        self.verticalLayout_8.addWidget(self.btn_scan)

        self.btn_fiplan = QPushButton(self.topMenu)
        self.btn_fiplan.setObjectName(u"btn_fiplan")
        sizePolicy2.setHeightForWidth(self.btn_fiplan.sizePolicy().hasHeightForWidth())
        self.btn_fiplan.setSizePolicy(sizePolicy2)
        self.btn_fiplan.setMinimumSize(QSize(0, 45))
        self.btn_fiplan.setFont(font)
        self.btn_fiplan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_fiplan.setLayoutDirection(Qt.LeftToRight)
        self.btn_fiplan.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-clipboard.png);")

        self.verticalLayout_8.addWidget(self.btn_fiplan)

        self.btn_execution = QPushButton(self.topMenu)
        self.btn_execution.setObjectName(u"btn_execution")
        sizePolicy2.setHeightForWidth(self.btn_execution.sizePolicy().hasHeightForWidth())
        self.btn_execution.setSizePolicy(sizePolicy2)
        self.btn_execution.setMinimumSize(QSize(0, 45))
        self.btn_execution.setFont(font)
        self.btn_execution.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_execution.setLayoutDirection(Qt.LeftToRight)
        self.btn_execution.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-terminal.png);")

        self.verticalLayout_8.addWidget(self.btn_execution)

        self.btn_monitoring = QPushButton(self.topMenu)
        self.btn_monitoring.setObjectName(u"btn_monitoring")
        sizePolicy2.setHeightForWidth(self.btn_monitoring.sizePolicy().hasHeightForWidth())
        self.btn_monitoring.setSizePolicy(sizePolicy2)
        self.btn_monitoring.setMinimumSize(QSize(0, 45))
        self.btn_monitoring.setFont(font)
        self.btn_monitoring.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_monitoring.setLayoutDirection(Qt.LeftToRight)
        self.btn_monitoring.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-check.png);")

        self.verticalLayout_8.addWidget(self.btn_monitoring)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.btn_dnn = QPushButton(self.leftMenuFrame)
        self.btn_dnn.setObjectName(u"btn_dnn")

        self.verticalMenuLayout.addWidget(self.btn_dnn)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy3)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy4)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setFamilies([u"URW Gothic"])
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setStyleSheet(u"font: 63 13pt \"URW Gothic\";")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.refresh_page = QPushButton(self.rightButtons)
        self.refresh_page.setObjectName(u"refresh_page")
        self.refresh_page.setMinimumSize(QSize(0, 0))
        self.refresh_page.setMaximumSize(QSize(16777215, 16777215))
        self.refresh_page.setFont(font)
        self.refresh_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.refresh_page.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-loop-circular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refresh_page.setIcon(icon)
        self.refresh_page.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.refresh_page)

        self.reset_for_all = QPushButton(self.rightButtons)
        self.reset_for_all.setObjectName(u"reset_for_all")
        self.reset_for_all.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-ban.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reset_for_all.setIcon(icon1)
        self.reset_for_all.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.reset_for_all)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon4)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_5 = QVBoxLayout(self.home)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setSpacing(20)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setHorizontalSpacing(20)
        self.plainTextEdit_3 = QPlainTextEdit(self.home)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_24.addWidget(self.plainTextEdit_3, 0, 0, 1, 1)

        self.plainTextEdit_7 = QPlainTextEdit(self.home)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        self.plainTextEdit_7.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_24.addWidget(self.plainTextEdit_7, 0, 3, 1, 1)

        self.plainTextEdit_5 = QPlainTextEdit(self.home)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_24.addWidget(self.plainTextEdit_5, 0, 1, 1, 1)

        self.plainTextEdit_6 = QPlainTextEdit(self.home)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_24.addWidget(self.plainTextEdit_6, 0, 2, 1, 1)

        self.plainTextEdit_8 = QPlainTextEdit(self.home)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")
        self.plainTextEdit_8.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_24.addWidget(self.plainTextEdit_8, 0, 4, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_24, 1, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.label_2 = QLabel(self.home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(1280, 400))
        self.label_2.setPixmap(QPixmap(u"../../../../Desktop/Dnn Module/Yedek/Tailored-Mutation-based-Software-Fault-Injection-Tool-IM-FIT/src/images/images/IM-FIT_Mimari.jpg"))
        self.label_2.setScaledContents(True)

        self.gridLayout_15.addWidget(self.label_2, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(13, 397, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_15)

        self.btn_go_start = QPushButton(self.home)
        self.btn_go_start.setObjectName(u"btn_go_start")
        sizePolicy4.setHeightForWidth(self.btn_go_start.sizePolicy().hasHeightForWidth())
        self.btn_go_start.setSizePolicy(sizePolicy4)
        self.btn_go_start.setMinimumSize(QSize(300, 30))
        self.btn_go_start.setMaximumSize(QSize(16777215, 30))
        self.btn_go_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_go_start.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_go_start.setIcon(icon5)

        self.verticalLayout_5.addWidget(self.btn_go_start)

        self.stackedWidget.addWidget(self.home)
        self.start = QWidget()
        self.start.setObjectName(u"start")
        self.start.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.start)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setSpacing(10)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_52 = QGridLayout()
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_52.setHorizontalSpacing(10)
        self.label_42 = QLabel(self.start)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(16777215, 30))
        self.label_42.setStyleSheet(u"")

        self.gridLayout_52.addWidget(self.label_42, 0, 0, 1, 1)

        self.plainTextEdit_13 = QPlainTextEdit(self.start)
        self.plainTextEdit_13.setObjectName(u"plainTextEdit_13")
        self.plainTextEdit_13.setMinimumSize(QSize(0, 30))
        self.plainTextEdit_13.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_13.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.plainTextEdit_13.setReadOnly(True)

        self.gridLayout_52.addWidget(self.plainTextEdit_13, 0, 1, 1, 1)

        self.btn_select_workload = QPushButton(self.start)
        self.btn_select_workload.setObjectName(u"btn_select_workload")
        self.btn_select_workload.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_select_workload.sizePolicy().hasHeightForWidth())
        self.btn_select_workload.setSizePolicy(sizePolicy5)
        self.btn_select_workload.setMinimumSize(QSize(80, 30))
        self.btn_select_workload.setMaximumSize(QSize(80, 30))
        self.btn_select_workload.setFont(font)
        self.btn_select_workload.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_select_workload.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_select_workload.setIcon(icon6)

        self.gridLayout_52.addWidget(self.btn_select_workload, 0, 2, 1, 1)

        self.plainTextEdit_14 = QPlainTextEdit(self.start)
        self.plainTextEdit_14.setObjectName(u"plainTextEdit_14")
        self.plainTextEdit_14.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.plainTextEdit_14.setReadOnly(True)

        self.gridLayout_52.addWidget(self.plainTextEdit_14, 1, 0, 1, 3)


        self.gridLayout_22.addLayout(self.gridLayout_52, 0, 0, 1, 4)

        self.btn_select_snippet = QPushButton(self.start)
        self.btn_select_snippet.setObjectName(u"btn_select_snippet")
        self.btn_select_snippet.setMinimumSize(QSize(0, 30))
        self.btn_select_snippet.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-hand-point-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_select_snippet.setIcon(icon7)

        self.gridLayout_22.addWidget(self.btn_select_snippet, 6, 0, 1, 2)

        self.gridLayout_49 = QGridLayout()
        self.gridLayout_49.setSpacing(10)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.checkBox_5 = QCheckBox(self.start)
        self.checkBox_5.setObjectName(u"checkBox_5")
        sizePolicy5.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy5)
        self.checkBox_5.setMinimumSize(QSize(100, 30))
        self.checkBox_5.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_5.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox_5.setIcon(icon8)

        self.gridLayout_49.addWidget(self.checkBox_5, 0, 1, 1, 1)

        self.btn_create_workload = QPushButton(self.start)
        self.btn_create_workload.setObjectName(u"btn_create_workload")
        sizePolicy5.setHeightForWidth(self.btn_create_workload.sizePolicy().hasHeightForWidth())
        self.btn_create_workload.setSizePolicy(sizePolicy5)
        self.btn_create_workload.setMinimumSize(QSize(100, 30))
        self.btn_create_workload.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_create_workload.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_create_workload.setIcon(icon9)

        self.gridLayout_49.addWidget(self.btn_create_workload, 0, 0, 1, 1)

        self.btn_clear_workload = QPushButton(self.start)
        self.btn_clear_workload.setObjectName(u"btn_clear_workload")
        sizePolicy5.setHeightForWidth(self.btn_clear_workload.sizePolicy().hasHeightForWidth())
        self.btn_clear_workload.setSizePolicy(sizePolicy5)
        self.btn_clear_workload.setMinimumSize(QSize(100, 30))
        self.btn_clear_workload.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear_workload.setIcon(icon10)

        self.gridLayout_49.addWidget(self.btn_clear_workload, 0, 2, 1, 1)


        self.gridLayout_22.addLayout(self.gridLayout_49, 1, 0, 2, 4)

        self.checkBox_3 = QCheckBox(self.start)
        self.checkBox_3.setObjectName(u"checkBox_3")
        font5 = QFont()
        font5.setFamilies([u"Ubuntu"])
        font5.setPointSize(13)
        font5.setBold(False)
        font5.setItalic(False)
        self.checkBox_3.setFont(font5)
        self.checkBox_3.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_22.addWidget(self.checkBox_3, 7, 2, 1, 1)

        self.code_snippet_list = QListWidget(self.start)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        QListWidgetItem(self.code_snippet_list)
        font6 = QFont()
        font6.setPointSize(20)
        __qlistwidgetitem = QListWidgetItem(self.code_snippet_list)
        __qlistwidgetitem.setFont(font6);
        __qlistwidgetitem.setFlags(Qt.NoItemFlags);
        self.code_snippet_list.setObjectName(u"code_snippet_list")
        sizePolicy4.setHeightForWidth(self.code_snippet_list.sizePolicy().hasHeightForWidth())
        self.code_snippet_list.setSizePolicy(sizePolicy4)
        self.code_snippet_list.setMinimumSize(QSize(0, 0))
        self.code_snippet_list.setMaximumSize(QSize(16777215, 16777215))
        self.code_snippet_list.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_22.addWidget(self.code_snippet_list, 4, 0, 2, 2)

        self.label_55 = QLabel(self.start)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"")

        self.gridLayout_22.addWidget(self.label_55, 3, 2, 1, 1)

        self.label_54 = QLabel(self.start)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"")

        self.gridLayout_22.addWidget(self.label_54, 3, 0, 1, 2)

        self.gridLayout_47 = QGridLayout()
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setHorizontalSpacing(10)
        self.btn_create_code = QPushButton(self.start)
        self.btn_create_code.setObjectName(u"btn_create_code")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_create_code.sizePolicy().hasHeightForWidth())
        self.btn_create_code.setSizePolicy(sizePolicy6)
        self.btn_create_code.setMinimumSize(QSize(0, 30))
        self.btn_create_code.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-code.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_create_code.setIcon(icon11)

        self.gridLayout_47.addWidget(self.btn_create_code, 0, 0, 1, 1)

        self.btn_add_custom = QPushButton(self.start)
        self.btn_add_custom.setObjectName(u"btn_add_custom")
        sizePolicy6.setHeightForWidth(self.btn_add_custom.sizePolicy().hasHeightForWidth())
        self.btn_add_custom.setSizePolicy(sizePolicy6)
        self.btn_add_custom.setMinimumSize(QSize(0, 30))
        self.btn_add_custom.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        self.btn_add_custom.setIcon(icon9)

        self.gridLayout_47.addWidget(self.btn_add_custom, 0, 1, 1, 2)


        self.gridLayout_22.addLayout(self.gridLayout_47, 7, 0, 1, 2)

        self.listWidget_8 = QListWidget(self.start)
        self.listWidget_8.setObjectName(u"listWidget_8")
        self.listWidget_8.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")

        self.gridLayout_22.addWidget(self.listWidget_8, 4, 3, 3, 1)

        self.label_56 = QLabel(self.start)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"")

        self.gridLayout_22.addWidget(self.label_56, 3, 3, 1, 1)

        self.btn_remove_snip = QPushButton(self.start)
        self.btn_remove_snip.setObjectName(u"btn_remove_snip")
        sizePolicy6.setHeightForWidth(self.btn_remove_snip.sizePolicy().hasHeightForWidth())
        self.btn_remove_snip.setSizePolicy(sizePolicy6)
        self.btn_remove_snip.setMinimumSize(QSize(0, 30))
        self.btn_remove_snip.setMaximumSize(QSize(16777215, 16777215))
        self.btn_remove_snip.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove_snip.setIcon(icon12)

        self.gridLayout_22.addWidget(self.btn_remove_snip, 7, 3, 1, 1)

        self.plainTextEdit_15 = QPlainTextEdit(self.start)
        self.plainTextEdit_15.setObjectName(u"plainTextEdit_15")
        self.plainTextEdit_15.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_22.addWidget(self.plainTextEdit_15, 4, 2, 3, 1)


        self.gridLayout.addLayout(self.gridLayout_22, 0, 1, 4, 4)

        self.gridLayout_48 = QGridLayout()
        self.gridLayout_48.setSpacing(10)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_36 = QGridLayout()
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.plainTextEdit_11 = QPlainTextEdit(self.start)
        self.plainTextEdit_11.setObjectName(u"plainTextEdit_11")
        self.plainTextEdit_11.setMinimumSize(QSize(0, 30))
        self.plainTextEdit_11.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_11.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.plainTextEdit_11.setReadOnly(True)

        self.gridLayout_36.addWidget(self.plainTextEdit_11, 0, 1, 1, 1)

        self.label_58 = QLabel(self.start)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(30, 0))
        self.label_58.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_36.addWidget(self.label_58, 0, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.start)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 30))
        self.pushButton_10.setMaximumSize(QSize(80, 30))
        self.pushButton_10.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        self.pushButton_10.setIcon(icon6)

        self.gridLayout_36.addWidget(self.pushButton_10, 0, 2, 1, 1)

        self.plainTextEdit_12 = QPlainTextEdit(self.start)
        self.plainTextEdit_12.setObjectName(u"plainTextEdit_12")
        self.plainTextEdit_12.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.plainTextEdit_12.setReadOnly(True)

        self.gridLayout_36.addWidget(self.plainTextEdit_12, 1, 0, 1, 3)


        self.gridLayout_48.addLayout(self.gridLayout_36, 0, 0, 1, 3)

        self.plainTextEdit_9 = QPlainTextEdit(self.start)
        self.plainTextEdit_9.setObjectName(u"plainTextEdit_9")
        self.plainTextEdit_9.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.plainTextEdit_9.setReadOnly(True)

        self.gridLayout_48.addWidget(self.plainTextEdit_9, 2, 0, 1, 3)

        self.label_9 = QLabel(self.start)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setStyleSheet(u"")

        self.gridLayout_48.addWidget(self.label_9, 1, 0, 1, 1)

        self.btn_open_folder = QPushButton(self.start)
        self.btn_open_folder.setObjectName(u"btn_open_folder")
        sizePolicy.setHeightForWidth(self.btn_open_folder.sizePolicy().hasHeightForWidth())
        self.btn_open_folder.setSizePolicy(sizePolicy)
        self.btn_open_folder.setMinimumSize(QSize(0, 30))
        self.btn_open_folder.setMaximumSize(QSize(80, 30))
        self.btn_open_folder.setFont(font)
        self.btn_open_folder.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_folder.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_open_folder.setIcon(icon6)

        self.gridLayout_48.addWidget(self.btn_open_folder, 1, 2, 1, 1)

        self.gridLayout_34 = QGridLayout()
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.checkBox_8 = QCheckBox(self.start)
        self.checkBox_8.setObjectName(u"checkBox_8")
        sizePolicy5.setHeightForWidth(self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy5)
        self.checkBox_8.setMinimumSize(QSize(0, 30))
        self.checkBox_8.setMaximumSize(QSize(16777215, 30))
        self.checkBox_8.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.checkBox_8.setIcon(icon8)

        self.gridLayout_34.addWidget(self.checkBox_8, 0, 0, 1, 1)

        self.btn_clear_codes = QPushButton(self.start)
        self.btn_clear_codes.setObjectName(u"btn_clear_codes")
        sizePolicy5.setHeightForWidth(self.btn_clear_codes.sizePolicy().hasHeightForWidth())
        self.btn_clear_codes.setSizePolicy(sizePolicy5)
        self.btn_clear_codes.setMinimumSize(QSize(0, 30))
        self.btn_clear_codes.setMaximumSize(QSize(16777215, 30))
        self.btn_clear_codes.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_clear_codes.setIcon(icon10)

        self.gridLayout_34.addWidget(self.btn_clear_codes, 0, 1, 1, 1)


        self.gridLayout_48.addLayout(self.gridLayout_34, 3, 0, 1, 3)

        self.plainTextEdit_10 = QPlainTextEdit(self.start)
        self.plainTextEdit_10.setObjectName(u"plainTextEdit_10")
        self.plainTextEdit_10.setMinimumSize(QSize(0, 30))
        self.plainTextEdit_10.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_10.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        self.plainTextEdit_10.setReadOnly(True)

        self.gridLayout_48.addWidget(self.plainTextEdit_10, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_48, 0, 0, 4, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.gridLayout_35 = QGridLayout()
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setHorizontalSpacing(50)
        self.gridLayout_35.setVerticalSpacing(6)
        self.btn_go_scan = QPushButton(self.start)
        self.btn_go_scan.setObjectName(u"btn_go_scan")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_go_scan.sizePolicy().hasHeightForWidth())
        self.btn_go_scan.setSizePolicy(sizePolicy7)
        self.btn_go_scan.setMinimumSize(QSize(200, 30))
        self.btn_go_scan.setMaximumSize(QSize(200, 30))
        self.btn_go_scan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_go_scan.setStyleSheet(u"font: 11pt \"Ubuntu\";\n"
"background-color: rgb(52, 59, 72);")
        self.btn_go_scan.setIcon(icon5)

        self.gridLayout_35.addWidget(self.btn_go_scan, 0, 1, 1, 1, Qt.AlignRight)

        self.pushButton_5 = QPushButton(self.start)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(200, 30))
        self.pushButton_5.setMaximumSize(QSize(200, 30))
        self.pushButton_5.setStyleSheet(u"font: 11pt \"Ubuntu\";\n"
"background-color: rgb(52, 59, 72);")
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon13)

        self.gridLayout_35.addWidget(self.pushButton_5, 0, 0, 1, 1, Qt.AlignLeft)


        self.verticalLayout.addLayout(self.gridLayout_35)

        self.stackedWidget.addWidget(self.start)
        self.ros_page = QWidget()
        self.ros_page.setObjectName(u"ros_page")
        self.verticalLayout_32 = QVBoxLayout(self.ros_page)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setSpacing(10)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setSpacing(10)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.checkBox_11 = QCheckBox(self.ros_page)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.gridLayout_31.addWidget(self.checkBox_11, 2, 2, 1, 2)

        self.label_95 = QLabel(self.ros_page)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_31.addWidget(self.label_95, 4, 0, 1, 1)

        self.label_93 = QLabel(self.ros_page)
        self.label_93.setObjectName(u"label_93")
        sizePolicy3.setHeightForWidth(self.label_93.sizePolicy().hasHeightForWidth())
        self.label_93.setSizePolicy(sizePolicy3)
        self.label_93.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_31.addWidget(self.label_93, 0, 2, 1, 2)

        self.label_97 = QLabel(self.ros_page)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_31.addWidget(self.label_97, 4, 3, 1, 1)

        self.remove_order_btn = QPushButton(self.ros_page)
        self.remove_order_btn.setObjectName(u"remove_order_btn")
        sizePolicy4.setHeightForWidth(self.remove_order_btn.sizePolicy().hasHeightForWidth())
        self.remove_order_btn.setSizePolicy(sizePolicy4)
        self.remove_order_btn.setMaximumSize(QSize(16777215, 30))
        self.remove_order_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.remove_order_btn.setIcon(icon12)

        self.gridLayout_31.addWidget(self.remove_order_btn, 3, 3, 1, 1)

        self.listWidget_27 = QListWidget(self.ros_page)
        self.listWidget_27.setObjectName(u"listWidget_27")
        self.listWidget_27.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_31.addWidget(self.listWidget_27, 5, 0, 1, 1)

        self.label_94 = QLabel(self.ros_page)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_31.addWidget(self.label_94, 4, 1, 1, 1)

        self.label_96 = QLabel(self.ros_page)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_31.addWidget(self.label_96, 4, 2, 1, 1)

        self.treeView = QTreeView(self.ros_page)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setMinimumSize(QSize(0, 0))
        self.treeView.setMaximumSize(QSize(16777215, 16777215))
        self.treeView.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_31.addWidget(self.treeView, 1, 0, 2, 2)

        self.listWidget_29 = QListWidget(self.ros_page)
        self.listWidget_29.setObjectName(u"listWidget_29")
        self.listWidget_29.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_31.addWidget(self.listWidget_29, 5, 2, 1, 1)

        self.add_order_btn = QPushButton(self.ros_page)
        self.add_order_btn.setObjectName(u"add_order_btn")
        sizePolicy4.setHeightForWidth(self.add_order_btn.sizePolicy().hasHeightForWidth())
        self.add_order_btn.setSizePolicy(sizePolicy4)
        self.add_order_btn.setMinimumSize(QSize(0, 30))
        self.add_order_btn.setMaximumSize(QSize(16777215, 30))
        self.add_order_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.add_order_btn.setIcon(icon9)

        self.gridLayout_31.addWidget(self.add_order_btn, 3, 0, 1, 2)

        self.gridLayout_32 = QGridLayout()
        self.gridLayout_32.setSpacing(10)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_100 = QLabel(self.ros_page)
        self.label_100.setObjectName(u"label_100")

        self.gridLayout_32.addWidget(self.label_100, 0, 2, 1, 1)

        self.listWidget_33 = QListWidget(self.ros_page)
        self.listWidget_33.setObjectName(u"listWidget_33")
        self.listWidget_33.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_32.addWidget(self.listWidget_33, 1, 0, 5, 1)

        self.listWidget_35 = QListWidget(self.ros_page)
        self.listWidget_35.setObjectName(u"listWidget_35")
        self.listWidget_35.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_32.addWidget(self.listWidget_35, 1, 2, 3, 1)

        self.listWidget_34 = QListWidget(self.ros_page)
        QListWidgetItem(self.listWidget_34)
        QListWidgetItem(self.listWidget_34)
        QListWidgetItem(self.listWidget_34)
        QListWidgetItem(self.listWidget_34)
        QListWidgetItem(self.listWidget_34)
        QListWidgetItem(self.listWidget_34)
        self.listWidget_34.setObjectName(u"listWidget_34")
        self.listWidget_34.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_32.addWidget(self.listWidget_34, 1, 1, 3, 1)

        self.add_ros_btn = QPushButton(self.ros_page)
        self.add_ros_btn.setObjectName(u"add_ros_btn")
        self.add_ros_btn.setMinimumSize(QSize(0, 30))
        self.add_ros_btn.setMaximumSize(QSize(16777215, 30))
        self.add_ros_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.add_ros_btn.setIcon(icon7)

        self.gridLayout_32.addWidget(self.add_ros_btn, 4, 1, 1, 1)

        self.mutate_ros_btn = QPushButton(self.ros_page)
        self.mutate_ros_btn.setObjectName(u"mutate_ros_btn")
        self.mutate_ros_btn.setMinimumSize(QSize(0, 30))
        self.mutate_ros_btn.setMaximumSize(QSize(16777215, 30))
        self.mutate_ros_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon14 = QIcon()
        icon14.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mutate_ros_btn.setIcon(icon14)

        self.gridLayout_32.addWidget(self.mutate_ros_btn, 5, 2, 1, 1)

        self.label_99 = QLabel(self.ros_page)
        self.label_99.setObjectName(u"label_99")

        self.gridLayout_32.addWidget(self.label_99, 0, 0, 1, 1)

        self.checkBox_9 = QCheckBox(self.ros_page)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setMinimumSize(QSize(0, 30))
        self.checkBox_9.setMaximumSize(QSize(16777215, 30))
        self.checkBox_9.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_32.addWidget(self.checkBox_9, 5, 1, 1, 1)

        self.label_91 = QLabel(self.ros_page)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_32.addWidget(self.label_91, 0, 1, 1, 1)

        self.remove_ros_btn = QPushButton(self.ros_page)
        self.remove_ros_btn.setObjectName(u"remove_ros_btn")
        self.remove_ros_btn.setMinimumSize(QSize(0, 30))
        self.remove_ros_btn.setMaximumSize(QSize(16777215, 30))
        self.remove_ros_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.remove_ros_btn.setIcon(icon12)

        self.gridLayout_32.addWidget(self.remove_ros_btn, 4, 2, 1, 1)


        self.gridLayout_31.addLayout(self.gridLayout_32, 7, 0, 5, 4)

        self.listWidget_28 = QListWidget(self.ros_page)
        self.listWidget_28.setObjectName(u"listWidget_28")
        self.listWidget_28.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_31.addWidget(self.listWidget_28, 5, 1, 1, 1)

        self.rosrun_btn = QPushButton(self.ros_page)
        self.rosrun_btn.setObjectName(u"rosrun_btn")
        sizePolicy4.setHeightForWidth(self.rosrun_btn.sizePolicy().hasHeightForWidth())
        self.rosrun_btn.setSizePolicy(sizePolicy4)
        self.rosrun_btn.setMinimumSize(QSize(0, 30))
        self.rosrun_btn.setMaximumSize(QSize(16777215, 30))
        self.rosrun_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.rosrun_btn.setIcon(icon14)

        self.gridLayout_31.addWidget(self.rosrun_btn, 3, 2, 1, 1)

        self.scan_ros_btn = QPushButton(self.ros_page)
        self.scan_ros_btn.setObjectName(u"scan_ros_btn")
        self.scan_ros_btn.setMinimumSize(QSize(0, 30))
        self.scan_ros_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon15 = QIcon()
        icon15.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.scan_ros_btn.setIcon(icon15)

        self.gridLayout_31.addWidget(self.scan_ros_btn, 6, 0, 1, 4)

        self.listWidget_30 = QListWidget(self.ros_page)
        self.listWidget_30.setObjectName(u"listWidget_30")
        self.listWidget_30.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_31.addWidget(self.listWidget_30, 5, 3, 1, 1)

        self.listWidget_26 = QListWidget(self.ros_page)
        self.listWidget_26.setObjectName(u"listWidget_26")
        self.listWidget_26.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget_26.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_31.addWidget(self.listWidget_26, 1, 2, 1, 2)

        self.label_89 = QLabel(self.ros_page)
        self.label_89.setObjectName(u"label_89")
        sizePolicy4.setHeightForWidth(self.label_89.sizePolicy().hasHeightForWidth())
        self.label_89.setSizePolicy(sizePolicy4)
        self.label_89.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_31.addWidget(self.label_89, 0, 0, 1, 2)


        self.gridLayout_10.addLayout(self.gridLayout_31, 0, 2, 10, 3)

        self.label_81 = QLabel(self.ros_page)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMinimumSize(QSize(0, 30))
        self.label_81.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_10.addWidget(self.label_81, 4, 6, 1, 2)

        self.gridLayout_42 = QGridLayout()
        self.gridLayout_42.setSpacing(10)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.ros_fiplan_save = QPushButton(self.ros_page)
        self.ros_fiplan_save.setObjectName(u"ros_fiplan_save")
        self.ros_fiplan_save.setMinimumSize(QSize(130, 30))
        self.ros_fiplan_save.setMaximumSize(QSize(16777215, 30))
        self.ros_fiplan_save.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon16 = QIcon()
        icon16.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ros_fiplan_save.setIcon(icon16)

        self.gridLayout_42.addWidget(self.ros_fiplan_save, 0, 1, 1, 1)

        self.ros_slct_fiplan = QPushButton(self.ros_page)
        self.ros_slct_fiplan.setObjectName(u"ros_slct_fiplan")
        self.ros_slct_fiplan.setMinimumSize(QSize(130, 30))
        self.ros_slct_fiplan.setMaximumSize(QSize(200, 30))
        self.ros_slct_fiplan.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.ros_slct_fiplan.setIcon(icon6)

        self.gridLayout_42.addWidget(self.ros_slct_fiplan, 0, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_42, 6, 5, 1, 3)

        self.label_90 = QLabel(self.ros_page)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_10.addWidget(self.label_90, 0, 5, 1, 3)

        self.label_102 = QLabel(self.ros_page)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_10.addWidget(self.label_102, 7, 5, 1, 3)

        self.label_101 = QLabel(self.ros_page)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_10.addWidget(self.label_101, 4, 5, 1, 1)

        self.listWidget_36 = QListWidget(self.ros_page)
        self.listWidget_36.setObjectName(u"listWidget_36")
        self.listWidget_36.setMaximumSize(QSize(16777215, 100))
        self.listWidget_36.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_10.addWidget(self.listWidget_36, 8, 5, 1, 3)

        self.remove_ros_mutant = QPushButton(self.ros_page)
        self.remove_ros_mutant.setObjectName(u"remove_ros_mutant")
        self.remove_ros_mutant.setMinimumSize(QSize(0, 30))
        self.remove_ros_mutant.setMaximumSize(QSize(16777215, 30))
        self.remove_ros_mutant.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.remove_ros_mutant.setIcon(icon12)

        self.gridLayout_10.addWidget(self.remove_ros_mutant, 3, 5, 1, 3)

        self.ros_fiplan_remove = QPushButton(self.ros_page)
        self.ros_fiplan_remove.setObjectName(u"ros_fiplan_remove")
        self.ros_fiplan_remove.setMinimumSize(QSize(130, 30))
        self.ros_fiplan_remove.setMaximumSize(QSize(16777215, 30))
        self.ros_fiplan_remove.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.ros_fiplan_remove.setIcon(icon4)

        self.gridLayout_10.addWidget(self.ros_fiplan_remove, 9, 5, 1, 3)

        self.listWidget_31 = QListWidget(self.ros_page)
        self.listWidget_31.setObjectName(u"listWidget_31")
        self.listWidget_31.setMinimumSize(QSize(410, 150))
        self.listWidget_31.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_10.addWidget(self.listWidget_31, 1, 5, 2, 3)

        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.listWidget_32 = QListWidget(self.ros_page)
        self.listWidget_32.setObjectName(u"listWidget_32")
        self.listWidget_32.setMinimumSize(QSize(0, 0))
        self.listWidget_32.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget_32.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_28.addWidget(self.listWidget_32, 3, 0, 1, 3)

        self.select_trgt_btn = QPushButton(self.ros_page)
        self.select_trgt_btn.setObjectName(u"select_trgt_btn")
        sizePolicy4.setHeightForWidth(self.select_trgt_btn.sizePolicy().hasHeightForWidth())
        self.select_trgt_btn.setSizePolicy(sizePolicy4)
        self.select_trgt_btn.setMinimumSize(QSize(80, 30))
        self.select_trgt_btn.setMaximumSize(QSize(80, 30))
        self.select_trgt_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.select_trgt_btn.setIcon(icon6)

        self.gridLayout_28.addWidget(self.select_trgt_btn, 1, 2, 1, 1)

        self.label_98 = QLabel(self.ros_page)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_28.addWidget(self.label_98, 1, 0, 1, 1)

        self.label_51 = QLabel(self.ros_page)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_28.addWidget(self.label_51, 0, 0, 1, 3)

        self.label_85 = QLabel(self.ros_page)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMinimumSize(QSize(0, 30))
        self.label_85.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_28.addWidget(self.label_85, 2, 0, 1, 1)

        self.label_86 = QLabel(self.ros_page)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMinimumSize(QSize(0, 30))
        self.label_86.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_28.addWidget(self.label_86, 2, 1, 1, 2)

        self.plainTextEdit_32 = QPlainTextEdit(self.ros_page)
        self.plainTextEdit_32.setObjectName(u"plainTextEdit_32")
        self.plainTextEdit_32.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_32.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.plainTextEdit_32.setReadOnly(True)

        self.gridLayout_28.addWidget(self.plainTextEdit_32, 1, 1, 1, 1)


        self.gridLayout_33.addLayout(self.gridLayout_28, 0, 0, 1, 1)

        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.open_target_ros = QPushButton(self.ros_page)
        self.open_target_ros.setObjectName(u"open_target_ros")
        self.open_target_ros.setMinimumSize(QSize(80, 30))
        self.open_target_ros.setMaximumSize(QSize(80, 30))
        self.open_target_ros.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.open_target_ros.setIcon(icon6)

        self.gridLayout_29.addWidget(self.open_target_ros, 1, 2, 1, 1)

        self.listWidget_10 = QListWidget(self.ros_page)
        self.listWidget_10.setObjectName(u"listWidget_10")
        self.listWidget_10.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_29.addWidget(self.listWidget_10, 2, 0, 1, 3)

        self.label_27 = QLabel(self.ros_page)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 30))
        self.label_27.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_29.addWidget(self.label_27, 1, 0, 1, 1)

        self.label_50 = QLabel(self.ros_page)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_29.addWidget(self.label_50, 0, 0, 1, 3)

        self.plainTextEdit_33 = QPlainTextEdit(self.ros_page)
        self.plainTextEdit_33.setObjectName(u"plainTextEdit_33")
        self.plainTextEdit_33.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_33.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.plainTextEdit_33.setReadOnly(True)

        self.gridLayout_29.addWidget(self.plainTextEdit_33, 1, 1, 1, 1)


        self.gridLayout_33.addLayout(self.gridLayout_29, 1, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_33, 0, 1, 10, 1)

        self.label_103 = QLabel(self.ros_page)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_10.addWidget(self.label_103, 5, 5, 1, 1)

        self.plainTextEdit_34 = QPlainTextEdit(self.ros_page)
        self.plainTextEdit_34.setObjectName(u"plainTextEdit_34")
        self.plainTextEdit_34.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_34.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_34.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_10.addWidget(self.plainTextEdit_34, 5, 6, 1, 2)


        self.verticalLayout_32.addLayout(self.gridLayout_10)

        self.gridLayout_41 = QGridLayout()
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.back_start_page = QPushButton(self.ros_page)
        self.back_start_page.setObjectName(u"back_start_page")
        self.back_start_page.setMinimumSize(QSize(200, 30))
        self.back_start_page.setMaximumSize(QSize(200, 30))
        self.back_start_page.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.back_start_page.setIcon(icon13)

        self.gridLayout_41.addWidget(self.back_start_page, 0, 0, 1, 1, Qt.AlignLeft)

        self.go_execution = QPushButton(self.ros_page)
        self.go_execution.setObjectName(u"go_execution")
        self.go_execution.setMinimumSize(QSize(200, 30))
        self.go_execution.setMaximumSize(QSize(200, 30))
        self.go_execution.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.go_execution.setIcon(icon5)

        self.gridLayout_41.addWidget(self.go_execution, 0, 1, 1, 1, Qt.AlignRight)


        self.verticalLayout_32.addLayout(self.gridLayout_41)

        self.stackedWidget.addWidget(self.ros_page)
        self.scan = QWidget()
        self.scan.setObjectName(u"scan")
        self.verticalLayout_30 = QVBoxLayout(self.scan)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(15)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setSpacing(10)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.plainTextEdit_16 = QPlainTextEdit(self.scan)
        self.plainTextEdit_16.setObjectName(u"plainTextEdit_16")
        self.plainTextEdit_16.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_19.addWidget(self.plainTextEdit_16, 1, 0, 1, 1)

        self.label_15 = QLabel(self.scan)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_19.addWidget(self.label_15, 2, 0, 1, 1)

        self.plainTextEdit_17 = QPlainTextEdit(self.scan)
        self.plainTextEdit_17.setObjectName(u"plainTextEdit_17")
        self.plainTextEdit_17.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_19.addWidget(self.plainTextEdit_17, 3, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_19, 1, 0, 13, 1)

        self.checkBox_2 = QCheckBox(self.scan)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(120, 30))
        self.checkBox_2.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_4.addWidget(self.checkBox_2, 10, 1, 4, 2)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_49 = QLabel(self.scan)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_21.addWidget(self.label_49, 0, 0, 1, 1)

        self.listWidget_2 = QListWidget(self.scan)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_21.addWidget(self.listWidget_2, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_21, 0, 4, 14, 1)

        self.label_59 = QLabel(self.scan)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_4.addWidget(self.label_59, 0, 1, 1, 3)

        self.listWidget_17 = QListWidget(self.scan)
        self.listWidget_17.setObjectName(u"listWidget_17")
        sizePolicy4.setHeightForWidth(self.listWidget_17.sizePolicy().hasHeightForWidth())
        self.listWidget_17.setSizePolicy(sizePolicy4)
        self.listWidget_17.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget_17.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_4.addWidget(self.listWidget_17, 1, 1, 7, 3)

        self.label_48 = QLabel(self.scan)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_4.addWidget(self.label_48, 0, 0, 1, 1)

        self.progressBar_2 = QProgressBar(self.scan)
        self.progressBar_2.setObjectName(u"progressBar_2")
        sizePolicy.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy)
        self.progressBar_2.setMinimumSize(QSize(315, 30))
        self.progressBar_2.setStyleSheet(u"background-color:black;")
        self.progressBar_2.setValue(0)

        self.gridLayout_4.addWidget(self.progressBar_2, 9, 1, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 8, 1, 1, 3)

        self.btn_scan_process = QPushButton(self.scan)
        self.btn_scan_process.setObjectName(u"btn_scan_process")
        sizePolicy.setHeightForWidth(self.btn_scan_process.sizePolicy().hasHeightForWidth())
        self.btn_scan_process.setSizePolicy(sizePolicy)
        self.btn_scan_process.setMinimumSize(QSize(150, 30))
        self.btn_scan_process.setFont(font)
        self.btn_scan_process.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_scan_process.setStyleSheet(u"background-color:black;\n"
"color:white;")
        self.btn_scan_process.setIcon(icon15)

        self.gridLayout_4.addWidget(self.btn_scan_process, 10, 3, 4, 1)


        self.verticalLayout_30.addLayout(self.gridLayout_4)

        self.gridLayout_38 = QGridLayout()
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setHorizontalSpacing(50)
        self.btn_go_fiplan = QPushButton(self.scan)
        self.btn_go_fiplan.setObjectName(u"btn_go_fiplan")
        sizePolicy.setHeightForWidth(self.btn_go_fiplan.sizePolicy().hasHeightForWidth())
        self.btn_go_fiplan.setSizePolicy(sizePolicy)
        self.btn_go_fiplan.setMinimumSize(QSize(200, 30))
        self.btn_go_fiplan.setMaximumSize(QSize(200, 30))
        self.btn_go_fiplan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_go_fiplan.setStyleSheet(u"font: 11pt \"Ubuntu\";\n"
"background-color: rgb(52, 59, 72);")
        self.btn_go_fiplan.setIcon(icon5)

        self.gridLayout_38.addWidget(self.btn_go_fiplan, 0, 1, 1, 1, Qt.AlignRight)

        self.btn_back_code = QPushButton(self.scan)
        self.btn_back_code.setObjectName(u"btn_back_code")
        sizePolicy.setHeightForWidth(self.btn_back_code.sizePolicy().hasHeightForWidth())
        self.btn_back_code.setSizePolicy(sizePolicy)
        self.btn_back_code.setMinimumSize(QSize(200, 30))
        self.btn_back_code.setMaximumSize(QSize(200, 30))
        self.btn_back_code.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_code.setStyleSheet(u"font: 11pt \"Ubuntu\";\n"
"background-color: rgb(52, 59, 72);")
        self.btn_back_code.setIcon(icon13)

        self.gridLayout_38.addWidget(self.btn_back_code, 0, 0, 1, 1, Qt.AlignLeft)


        self.verticalLayout_30.addLayout(self.gridLayout_38)

        self.stackedWidget.addWidget(self.scan)
        self.fiplan = QWidget()
        self.fiplan.setObjectName(u"fiplan")
        self.verticalLayout_40 = QVBoxLayout(self.fiplan)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(20)
        self.gridLayout_7.setVerticalSpacing(10)
        self.label_34 = QLabel(self.fiplan)
        self.label_34.setObjectName(u"label_34")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy8)
        self.label_34.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_7.addWidget(self.label_34, 0, 3, 1, 3)

        self.btn_start_mutation = QPushButton(self.fiplan)
        self.btn_start_mutation.setObjectName(u"btn_start_mutation")
        self.btn_start_mutation.setMinimumSize(QSize(0, 30))
        self.btn_start_mutation.setMaximumSize(QSize(16777215, 30))
        self.btn_start_mutation.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 13pt \"Ubuntu\";")
        self.btn_start_mutation.setIcon(icon14)

        self.gridLayout_7.addWidget(self.btn_start_mutation, 10, 2, 1, 1)

        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setHorizontalSpacing(6)
        self.gridLayout_30.setVerticalSpacing(10)
        self.listWidget = QListWidget(self.fiplan)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_30.addWidget(self.listWidget, 0, 0, 1, 1)

        self.label_5 = QLabel(self.fiplan)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 30))
        self.label_5.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_30.addWidget(self.label_5, 1, 0, 1, 1)

        self.plainTextEdit_18 = QPlainTextEdit(self.fiplan)
        self.plainTextEdit_18.setObjectName(u"plainTextEdit_18")
        self.plainTextEdit_18.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_18.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.plainTextEdit_18.setReadOnly(True)

        self.gridLayout_30.addWidget(self.plainTextEdit_18, 2, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_30, 1, 0, 11, 1)

        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setHorizontalSpacing(6)
        self.gridLayout_27.setVerticalSpacing(10)
        self.label_6 = QLabel(self.fiplan)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 30))
        self.label_6.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_27.addWidget(self.label_6, 0, 0, 1, 1)

        self.listWidget_3 = QListWidget(self.fiplan)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem1.setFont(font6);
        __qlistwidgetitem1.setFlags(Qt.NoItemFlags);
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem2.setFont(font6);
        __qlistwidgetitem2.setFlags(Qt.NoItemFlags);
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem3.setFont(font6);
        __qlistwidgetitem3.setFlags(Qt.NoItemFlags);
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem4.setFont(font6);
        __qlistwidgetitem4.setFlags(Qt.NoItemFlags);
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setMinimumSize(QSize(300, 0))
        self.listWidget_3.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_27.addWidget(self.listWidget_3, 1, 0, 1, 1)

        self.btn_select_fault = QPushButton(self.fiplan)
        self.btn_select_fault.setObjectName(u"btn_select_fault")
        self.btn_select_fault.setMinimumSize(QSize(0, 30))
        self.btn_select_fault.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_select_fault.setIcon(icon7)

        self.gridLayout_27.addWidget(self.btn_select_fault, 2, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.fiplan)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setMinimumSize(QSize(0, 30))
        font7 = QFont()
        font7.setFamilies([u"Ubuntu"])
        font7.setPointSize(11)
        font7.setBold(False)
        font7.setItalic(False)
        self.checkBox_4.setFont(font7)
        self.checkBox_4.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 11pt \"Ubuntu\";\n"
"")

        self.gridLayout_27.addWidget(self.checkBox_4, 3, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_27, 2, 1, 9, 1)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setHorizontalSpacing(18)
        self.gridLayout_23.setVerticalSpacing(6)
        self.btn_save_fiplan = QPushButton(self.fiplan)
        self.btn_save_fiplan.setObjectName(u"btn_save_fiplan")
        sizePolicy2.setHeightForWidth(self.btn_save_fiplan.sizePolicy().hasHeightForWidth())
        self.btn_save_fiplan.setSizePolicy(sizePolicy2)
        self.btn_save_fiplan.setMinimumSize(QSize(0, 0))
        self.btn_save_fiplan.setMaximumSize(QSize(16777215, 30))
        self.btn_save_fiplan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_fiplan.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_save_fiplan.setIcon(icon16)

        self.gridLayout_23.addWidget(self.btn_save_fiplan, 7, 1, 1, 1)

        self.pushButton = QPushButton(self.fiplan)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton.setIcon(icon12)

        self.gridLayout_23.addWidget(self.pushButton, 2, 0, 3, 2)

        self.label_33 = QLabel(self.fiplan)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_23.addWidget(self.label_33, 6, 0, 1, 1)

        self.btn_slct_fiplan = QPushButton(self.fiplan)
        self.btn_slct_fiplan.setObjectName(u"btn_slct_fiplan")
        sizePolicy2.setHeightForWidth(self.btn_slct_fiplan.sizePolicy().hasHeightForWidth())
        self.btn_slct_fiplan.setSizePolicy(sizePolicy2)
        self.btn_slct_fiplan.setMinimumSize(QSize(0, 30))
        self.btn_slct_fiplan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_slct_fiplan.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_slct_fiplan.setIcon(icon6)

        self.gridLayout_23.addWidget(self.btn_slct_fiplan, 7, 0, 1, 1)

        self.label_76 = QLabel(self.fiplan)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMaximumSize(QSize(16777215, 30))
        self.label_76.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_23.addWidget(self.label_76, 5, 0, 1, 1)

        self.label_17 = QLabel(self.fiplan)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_23.addWidget(self.label_17, 5, 1, 1, 1, Qt.AlignHCenter)

        self.listWidget_11 = QListWidget(self.fiplan)
        self.listWidget_11.setObjectName(u"listWidget_11")
        sizePolicy4.setHeightForWidth(self.listWidget_11.sizePolicy().hasHeightForWidth())
        self.listWidget_11.setSizePolicy(sizePolicy4)
        self.listWidget_11.setMinimumSize(QSize(0, 0))
        self.listWidget_11.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget_11.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_23.addWidget(self.listWidget_11, 5, 2, 2, 1)

        self.listWidget_4 = QListWidget(self.fiplan)
        self.listWidget_4.setObjectName(u"listWidget_4")
        self.listWidget_4.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget_4.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_23.addWidget(self.listWidget_4, 1, 0, 1, 3)

        self.btn_remove_fiplan = QPushButton(self.fiplan)
        self.btn_remove_fiplan.setObjectName(u"btn_remove_fiplan")
        sizePolicy2.setHeightForWidth(self.btn_remove_fiplan.sizePolicy().hasHeightForWidth())
        self.btn_remove_fiplan.setSizePolicy(sizePolicy2)
        self.btn_remove_fiplan.setMinimumSize(QSize(0, 30))
        self.btn_remove_fiplan.setMaximumSize(QSize(16777215, 30))
        self.btn_remove_fiplan.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_remove_fiplan.setIcon(icon12)

        self.gridLayout_23.addWidget(self.btn_remove_fiplan, 7, 2, 1, 1)

        self.label_44 = QLabel(self.fiplan)
        self.label_44.setObjectName(u"label_44")
        sizePolicy8.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy8)
        self.label_44.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_23.addWidget(self.label_44, 2, 2, 3, 1)

        self.plainTextEdit_20 = QPlainTextEdit(self.fiplan)
        self.plainTextEdit_20.setObjectName(u"plainTextEdit_20")
        self.plainTextEdit_20.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_20.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_23.addWidget(self.plainTextEdit_20, 6, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_23, 1, 3, 11, 3)

        self.btn_create_custom = QPushButton(self.fiplan)
        self.btn_create_custom.setObjectName(u"btn_create_custom")
        sizePolicy2.setHeightForWidth(self.btn_create_custom.sizePolicy().hasHeightForWidth())
        self.btn_create_custom.setSizePolicy(sizePolicy2)
        self.btn_create_custom.setMinimumSize(QSize(0, 30))
        self.btn_create_custom.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_create_custom.setIcon(icon11)

        self.gridLayout_7.addWidget(self.btn_create_custom, 1, 2, 1, 1)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setHorizontalSpacing(6)
        self.gridLayout_25.setVerticalSpacing(10)
        self.label_16 = QLabel(self.fiplan)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_25.addWidget(self.label_16, 0, 0, 1, 1)

        self.btn_remove_fault = QPushButton(self.fiplan)
        self.btn_remove_fault.setObjectName(u"btn_remove_fault")
        self.btn_remove_fault.setMinimumSize(QSize(0, 30))
        self.btn_remove_fault.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_remove_fault.setIcon(icon12)

        self.gridLayout_25.addWidget(self.btn_remove_fault, 2, 0, 1, 1)

        self.listWidget_7 = QListWidget(self.fiplan)
        self.listWidget_7.setObjectName(u"listWidget_7")
        self.listWidget_7.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_25.addWidget(self.listWidget_7, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_25, 7, 2, 3, 1)

        self.progressBar = QProgressBar(self.fiplan)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 30))
        self.progressBar.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.progressBar.setValue(0)

        self.gridLayout_7.addWidget(self.progressBar, 11, 1, 1, 2)

        self.label_30 = QLabel(self.fiplan)
        self.label_30.setObjectName(u"label_30")
        sizePolicy8.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy8)
        self.label_30.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_7.addWidget(self.label_30, 0, 1, 1, 2)

        self.btn_random_fault = QPushButton(self.fiplan)
        self.btn_random_fault.setObjectName(u"btn_random_fault")
        self.btn_random_fault.setMinimumSize(QSize(0, 30))
        self.btn_random_fault.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon17 = QIcon()
        icon17.addFile(u":/icons/images/icons/cil-laptop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_random_fault.setIcon(icon17)

        self.gridLayout_7.addWidget(self.btn_random_fault, 1, 1, 1, 1)

        self.label_12 = QLabel(self.fiplan)
        self.label_12.setObjectName(u"label_12")
        sizePolicy8.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy8)
        self.label_12.setMaximumSize(QSize(16777215, 16777215))
        self.label_12.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_7.addWidget(self.label_12, 0, 0, 1, 1)

        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_52 = QLabel(self.fiplan)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(16777215, 30))
        self.label_52.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_26.addWidget(self.label_52, 0, 0, 1, 1)

        self.plainTextEdit_19 = QPlainTextEdit(self.fiplan)
        self.plainTextEdit_19.setObjectName(u"plainTextEdit_19")
        self.plainTextEdit_19.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.plainTextEdit_19.setReadOnly(True)

        self.gridLayout_26.addWidget(self.plainTextEdit_19, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_26, 2, 2, 5, 1)


        self.verticalLayout_40.addLayout(self.gridLayout_7)

        self.gridLayout_39 = QGridLayout()
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setHorizontalSpacing(50)
        self.pushButton_7 = QPushButton(self.fiplan)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QSize(200, 30))
        self.pushButton_7.setMaximumSize(QSize(200, 30))
        self.pushButton_7.setStyleSheet(u"font: 11pt \"Ubuntu\";\n"
"background-color: rgb(52, 59, 72);")
        self.pushButton_7.setIcon(icon13)

        self.gridLayout_39.addWidget(self.pushButton_7, 0, 0, 1, 1, Qt.AlignLeft)

        self.btn_go_exe = QPushButton(self.fiplan)
        self.btn_go_exe.setObjectName(u"btn_go_exe")
        sizePolicy.setHeightForWidth(self.btn_go_exe.sizePolicy().hasHeightForWidth())
        self.btn_go_exe.setSizePolicy(sizePolicy)
        self.btn_go_exe.setMinimumSize(QSize(200, 30))
        self.btn_go_exe.setMaximumSize(QSize(200, 30))
        self.btn_go_exe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_go_exe.setStyleSheet(u"font: 11pt \"Ubuntu\";\n"
"background-color: rgb(52, 59, 72);")
        self.btn_go_exe.setIcon(icon5)

        self.gridLayout_39.addWidget(self.btn_go_exe, 0, 1, 1, 1, Qt.AlignRight)


        self.verticalLayout_40.addLayout(self.gridLayout_39)

        self.stackedWidget.addWidget(self.fiplan)
        self.execution = QWidget()
        self.execution.setObjectName(u"execution")
        self.verticalLayout_20 = QVBoxLayout(self.execution)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_118 = QLabel(self.execution)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(0, 30))
        self.label_118.setFont(font5)
        self.label_118.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_6.addWidget(self.label_118, 0, 6, 1, 1)

        self.label_40 = QLabel(self.execution)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(0, 30))
        self.label_40.setMaximumSize(QSize(16777215, 30))
        self.label_40.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_6.addWidget(self.label_40, 0, 0, 1, 1)

        self.listWidget_13 = QListWidget(self.execution)
        self.listWidget_13.setObjectName(u"listWidget_13")
        sizePolicy4.setHeightForWidth(self.listWidget_13.sizePolicy().hasHeightForWidth())
        self.listWidget_13.setSizePolicy(sizePolicy4)
        self.listWidget_13.setMinimumSize(QSize(0, 0))
        self.listWidget_13.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_6.addWidget(self.listWidget_13, 7, 6, 1, 1)

        self.label_57 = QLabel(self.execution)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(0, 30))
        self.label_57.setMaximumSize(QSize(16777215, 30))
        self.label_57.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_6.addWidget(self.label_57, 0, 1, 1, 5, Qt.AlignHCenter)

        self.gridLayout_61 = QGridLayout()
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.listWidget_6 = QListWidget(self.execution)
        self.listWidget_6.setObjectName(u"listWidget_6")
        sizePolicy4.setHeightForWidth(self.listWidget_6.sizePolicy().hasHeightForWidth())
        self.listWidget_6.setSizePolicy(sizePolicy4)
        self.listWidget_6.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_61.addWidget(self.listWidget_6, 0, 0, 2, 1)

        self.btn_select_metrics = QPushButton(self.execution)
        self.btn_select_metrics.setObjectName(u"btn_select_metrics")
        sizePolicy4.setHeightForWidth(self.btn_select_metrics.sizePolicy().hasHeightForWidth())
        self.btn_select_metrics.setSizePolicy(sizePolicy4)
        self.btn_select_metrics.setMinimumSize(QSize(0, 30))
        self.btn_select_metrics.setMaximumSize(QSize(16777215, 30))
        self.btn_select_metrics.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_select_metrics.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon18 = QIcon()
        icon18.addFile(u":/icons/images/icons/cil-equalizer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_select_metrics.setIcon(icon18)

        self.gridLayout_61.addWidget(self.btn_select_metrics, 7, 0, 1, 1)

        self.listWidget_23 = QListWidget(self.execution)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        self.listWidget_23.setObjectName(u"listWidget_23")
        self.listWidget_23.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_61.addWidget(self.listWidget_23, 4, 0, 1, 1)

        self.gridLayout_63 = QGridLayout()
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.btn_export_fiplan = QPushButton(self.execution)
        self.btn_export_fiplan.setObjectName(u"btn_export_fiplan")
        sizePolicy2.setHeightForWidth(self.btn_export_fiplan.sizePolicy().hasHeightForWidth())
        self.btn_export_fiplan.setSizePolicy(sizePolicy2)
        self.btn_export_fiplan.setMinimumSize(QSize(0, 30))
        self.btn_export_fiplan.setMaximumSize(QSize(16777215, 30))
        self.btn_export_fiplan.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_export_fiplan.setIcon(icon9)

        self.gridLayout_63.addWidget(self.btn_export_fiplan, 0, 0, 1, 1)

        self.btn_remove_fi = QPushButton(self.execution)
        self.btn_remove_fi.setObjectName(u"btn_remove_fi")
        sizePolicy2.setHeightForWidth(self.btn_remove_fi.sizePolicy().hasHeightForWidth())
        self.btn_remove_fi.setSizePolicy(sizePolicy2)
        self.btn_remove_fi.setMinimumSize(QSize(0, 30))
        self.btn_remove_fi.setMaximumSize(QSize(16777215, 30))
        self.btn_remove_fi.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_remove_fi.setIcon(icon12)

        self.gridLayout_63.addWidget(self.btn_remove_fi, 0, 1, 1, 1)


        self.gridLayout_61.addLayout(self.gridLayout_63, 2, 0, 1, 1)

        self.label_26 = QLabel(self.execution)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_61.addWidget(self.label_26, 5, 0, 1, 1)

        self.label_72 = QLabel(self.execution)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_61.addWidget(self.label_72, 3, 0, 1, 1)

        self.plainTextEdit_21 = QPlainTextEdit(self.execution)
        self.plainTextEdit_21.setObjectName(u"plainTextEdit_21")
        self.plainTextEdit_21.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.plainTextEdit_21.setReadOnly(True)

        self.gridLayout_61.addWidget(self.plainTextEdit_21, 6, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_61, 1, 0, 8, 1)

        self.btn_remove_exe = QPushButton(self.execution)
        self.btn_remove_exe.setObjectName(u"btn_remove_exe")
        sizePolicy4.setHeightForWidth(self.btn_remove_exe.sizePolicy().hasHeightForWidth())
        self.btn_remove_exe.setSizePolicy(sizePolicy4)
        self.btn_remove_exe.setMinimumSize(QSize(150, 30))
        self.btn_remove_exe.setMaximumSize(QSize(16777215, 30))
        self.btn_remove_exe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remove_exe.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_remove_exe.setIcon(icon2)

        self.gridLayout_6.addWidget(self.btn_remove_exe, 8, 6, 1, 1)

        self.gridLayout_40 = QGridLayout()
        self.gridLayout_40.setSpacing(6)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.label_28 = QLabel(self.execution)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_40.addWidget(self.label_28, 4, 0, 1, 1)

        self.plainTextEdit_26 = QPlainTextEdit(self.execution)
        self.plainTextEdit_26.setObjectName(u"plainTextEdit_26")
        self.plainTextEdit_26.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_26.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_26.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.plainTextEdit_26, 4, 1, 1, 1)

        self.label_116 = QLabel(self.execution)
        self.label_116.setObjectName(u"label_116")

        self.gridLayout_40.addWidget(self.label_116, 1, 0, 1, 1)

        self.listWidget_24 = QListWidget(self.execution)
        self.listWidget_24.setObjectName(u"listWidget_24")
        self.listWidget_24.setMinimumSize(QSize(0, 40))
        self.listWidget_24.setMaximumSize(QSize(16777215, 30))
        self.listWidget_24.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.listWidget_24, 2, 3, 1, 1)

        self.plainTextEdit_25 = QPlainTextEdit(self.execution)
        self.plainTextEdit_25.setObjectName(u"plainTextEdit_25")
        self.plainTextEdit_25.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_25.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_25.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.plainTextEdit_25, 3, 1, 1, 1)

        self.label_39 = QLabel(self.execution)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_40.addWidget(self.label_39, 5, 0, 1, 1)

        self.label_20 = QLabel(self.execution)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setBaseSize(QSize(0, 0))

        self.gridLayout_40.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_24 = QLabel(self.execution)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_40.addWidget(self.label_24, 5, 2, 1, 1)

        self.label_83 = QLabel(self.execution)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_40.addWidget(self.label_83, 2, 2, 1, 1)

        self.plainTextEdit_28 = QPlainTextEdit(self.execution)
        self.plainTextEdit_28.setObjectName(u"plainTextEdit_28")
        self.plainTextEdit_28.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_28.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_28.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.plainTextEdit_28, 5, 1, 1, 1)

        self.plainTextEdit_23 = QPlainTextEdit(self.execution)
        self.plainTextEdit_23.setObjectName(u"plainTextEdit_23")
        self.plainTextEdit_23.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_23.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_23.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.plainTextEdit_23, 2, 1, 1, 1)

        self.label_75 = QLabel(self.execution)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_40.addWidget(self.label_75, 3, 0, 1, 1)

        self.pushButton_16 = QPushButton(self.execution)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(0, 40))
        self.pushButton_16.setMaximumSize(QSize(16777215, 40))
        self.pushButton_16.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.pushButton_16, 1, 1, 1, 1)

        self.label_38 = QLabel(self.execution)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_40.addWidget(self.label_38, 2, 0, 1, 1)

        self.label_117 = QLabel(self.execution)
        self.label_117.setObjectName(u"label_117")

        self.gridLayout_40.addWidget(self.label_117, 1, 2, 1, 1)

        self.plainTextEdit_24 = QPlainTextEdit(self.execution)
        self.plainTextEdit_24.setObjectName(u"plainTextEdit_24")
        self.plainTextEdit_24.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_24.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_24.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.plainTextEdit_24.setReadOnly(True)

        self.gridLayout_40.addWidget(self.plainTextEdit_24, 1, 3, 1, 1)

        self.plainTextEdit_22 = QPlainTextEdit(self.execution)
        self.plainTextEdit_22.setObjectName(u"plainTextEdit_22")
        self.plainTextEdit_22.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_22.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.plainTextEdit_22, 0, 1, 1, 1)

        self.label_82 = QLabel(self.execution)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_40.addWidget(self.label_82, 0, 2, 1, 1)

        self.checkBox = QCheckBox(self.execution)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setMinimumSize(QSize(200, 40))
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_40.addWidget(self.checkBox, 0, 3, 1, 1)

        self.gridLayout_62 = QGridLayout()
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.plainTextEdit_4 = QPlainTextEdit(self.execution)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.plainTextEdit_4.setReadOnly(True)

        self.gridLayout_62.addWidget(self.plainTextEdit_4, 8, 0, 1, 2)

        self.plainTextEdit_30 = QPlainTextEdit(self.execution)
        self.plainTextEdit_30.setObjectName(u"plainTextEdit_30")
        self.plainTextEdit_30.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_62.addWidget(self.plainTextEdit_30, 2, 0, 1, 1)

        self.label_119 = QLabel(self.execution)
        self.label_119.setObjectName(u"label_119")

        self.gridLayout_62.addWidget(self.label_119, 7, 0, 1, 2)

        self.label_121 = QLabel(self.execution)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setStyleSheet(u"")

        self.gridLayout_62.addWidget(self.label_121, 4, 0, 1, 2)

        self.btn_show_con = QPushButton(self.execution)
        self.btn_show_con.setObjectName(u"btn_show_con")
        self.btn_show_con.setMinimumSize(QSize(0, 30))
        self.btn_show_con.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_62.addWidget(self.btn_show_con, 6, 0, 1, 2)

        self.label_120 = QLabel(self.execution)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setStyleSheet(u"")

        self.gridLayout_62.addWidget(self.label_120, 1, 0, 1, 2)

        self.gridLayout_64 = QGridLayout()
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.btn_new_exe = QPushButton(self.execution)
        self.btn_new_exe.setObjectName(u"btn_new_exe")
        sizePolicy2.setHeightForWidth(self.btn_new_exe.sizePolicy().hasHeightForWidth())
        self.btn_new_exe.setSizePolicy(sizePolicy2)
        self.btn_new_exe.setMinimumSize(QSize(0, 30))
        self.btn_new_exe.setMaximumSize(QSize(16777215, 16777215))
        self.btn_new_exe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new_exe.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_new_exe.setIcon(icon9)

        self.gridLayout_64.addWidget(self.btn_new_exe, 0, 3, 1, 1)

        self.btn_kill_containers = QPushButton(self.execution)
        self.btn_kill_containers.setObjectName(u"btn_kill_containers")
        sizePolicy2.setHeightForWidth(self.btn_kill_containers.sizePolicy().hasHeightForWidth())
        self.btn_kill_containers.setSizePolicy(sizePolicy2)
        self.btn_kill_containers.setMinimumSize(QSize(0, 30))
        self.btn_kill_containers.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_64.addWidget(self.btn_kill_containers, 0, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.execution)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setMinimumSize(QSize(0, 30))
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_3.setIcon(icon16)

        self.gridLayout_64.addWidget(self.pushButton_3, 0, 4, 1, 1)

        self.btn_create_container = QPushButton(self.execution)
        self.btn_create_container.setObjectName(u"btn_create_container")
        sizePolicy2.setHeightForWidth(self.btn_create_container.sizePolicy().hasHeightForWidth())
        self.btn_create_container.setSizePolicy(sizePolicy2)
        self.btn_create_container.setMinimumSize(QSize(0, 30))
        self.btn_create_container.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_64.addWidget(self.btn_create_container, 0, 0, 1, 1)

        self.btn_apply_docker = QPushButton(self.execution)
        self.btn_apply_docker.setObjectName(u"btn_apply_docker")
        self.btn_apply_docker.setMinimumSize(QSize(0, 30))
        self.btn_apply_docker.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_64.addWidget(self.btn_apply_docker, 0, 1, 1, 1)

        self.checkBox_10 = QCheckBox(self.execution)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout_64.addWidget(self.checkBox_10, 1, 3, 1, 2)

        self.btn_start_exe = QPushButton(self.execution)
        self.btn_start_exe.setObjectName(u"btn_start_exe")
        sizePolicy4.setHeightForWidth(self.btn_start_exe.sizePolicy().hasHeightForWidth())
        self.btn_start_exe.setSizePolicy(sizePolicy4)
        self.btn_start_exe.setMinimumSize(QSize(0, 30))
        self.btn_start_exe.setMaximumSize(QSize(16777215, 30))
        self.btn_start_exe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start_exe.setStyleSheet(u"background-color:black;\n"
"color:white;")
        icon19 = QIcon()
        icon19.addFile(u":/icons/images/icons/cil-caret-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_start_exe.setIcon(icon19)

        self.gridLayout_64.addWidget(self.btn_start_exe, 1, 1, 1, 2)

        self.btn_create_mutants = QPushButton(self.execution)
        self.btn_create_mutants.setObjectName(u"btn_create_mutants")
        sizePolicy4.setHeightForWidth(self.btn_create_mutants.sizePolicy().hasHeightForWidth())
        self.btn_create_mutants.setSizePolicy(sizePolicy4)
        self.btn_create_mutants.setMinimumSize(QSize(0, 30))
        self.btn_create_mutants.setMaximumSize(QSize(16777215, 30))
        self.btn_create_mutants.setStyleSheet(u"background-color:black;\n"
"color:white;")

        self.gridLayout_64.addWidget(self.btn_create_mutants, 1, 0, 1, 1)


        self.gridLayout_62.addLayout(self.gridLayout_64, 0, 0, 1, 2)

        self.btn_show_di = QPushButton(self.execution)
        self.btn_show_di.setObjectName(u"btn_show_di")
        self.btn_show_di.setMinimumSize(QSize(0, 30))
        self.btn_show_di.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_62.addWidget(self.btn_show_di, 3, 0, 1, 2)

        self.plainTextEdit_31 = QPlainTextEdit(self.execution)
        self.plainTextEdit_31.setObjectName(u"plainTextEdit_31")
        self.plainTextEdit_31.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_62.addWidget(self.plainTextEdit_31, 5, 0, 1, 1)


        self.gridLayout_40.addLayout(self.gridLayout_62, 6, 0, 9, 4)

        self.plainTextEdit_27 = QPlainTextEdit(self.execution)
        self.plainTextEdit_27.setObjectName(u"plainTextEdit_27")
        self.plainTextEdit_27.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_27.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_27.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.plainTextEdit_27, 4, 3, 1, 1)

        self.label_36 = QLabel(self.execution)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_40.addWidget(self.label_36, 4, 2, 1, 1)

        self.label_84 = QLabel(self.execution)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_40.addWidget(self.label_84, 3, 2, 1, 1)

        self.plainTextEdit_29 = QPlainTextEdit(self.execution)
        self.plainTextEdit_29.setObjectName(u"plainTextEdit_29")
        self.plainTextEdit_29.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_29.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_29.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.plainTextEdit_29, 5, 3, 1, 1)

        self.checkBox_7 = QCheckBox(self.execution)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setMinimumSize(QSize(200, 40))
        self.checkBox_7.setStyleSheet(u"")

        self.gridLayout_40.addWidget(self.checkBox_7, 3, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_40, 1, 1, 8, 5)

        self.treeView_2 = QTreeView(self.execution)
        self.treeView_2.setObjectName(u"treeView_2")
        self.treeView_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_6.addWidget(self.treeView_2, 1, 6, 1, 1)

        self.label_11 = QLabel(self.execution)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)
        self.label_11.setMinimumSize(QSize(0, 30))
        self.label_11.setMaximumSize(QSize(16777215, 16777215))
        self.label_11.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_6.addWidget(self.label_11, 2, 6, 5, 1)


        self.verticalLayout_20.addLayout(self.gridLayout_6)

        self.gridLayout_43 = QGridLayout()
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_43.setHorizontalSpacing(50)
        self.gridLayout_43.setContentsMargins(0, -1, -1, -1)
        self.btn_go_monitoring = QPushButton(self.execution)
        self.btn_go_monitoring.setObjectName(u"btn_go_monitoring")
        sizePolicy4.setHeightForWidth(self.btn_go_monitoring.sizePolicy().hasHeightForWidth())
        self.btn_go_monitoring.setSizePolicy(sizePolicy4)
        self.btn_go_monitoring.setMinimumSize(QSize(200, 30))
        self.btn_go_monitoring.setMaximumSize(QSize(200, 30))
        self.btn_go_monitoring.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_go_monitoring.setStyleSheet(u"font: 11pt \"Ubuntu\";\n"
"background-color: rgb(52, 59, 72);")
        self.btn_go_monitoring.setIcon(icon5)

        self.gridLayout_43.addWidget(self.btn_go_monitoring, 0, 1, 1, 1, Qt.AlignRight)

        self.pushButton_6 = QPushButton(self.execution)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QSize(200, 30))
        self.pushButton_6.setMaximumSize(QSize(200, 30))
        self.pushButton_6.setStyleSheet(u"font: 11pt \"Ubuntu\";\n"
"background-color: rgb(52, 59, 72);")
        self.pushButton_6.setIcon(icon13)

        self.gridLayout_43.addWidget(self.pushButton_6, 0, 0, 1, 1, Qt.AlignLeft)


        self.verticalLayout_20.addLayout(self.gridLayout_43)

        self.stackedWidget.addWidget(self.execution)
        self.monitoring = QWidget()
        self.monitoring.setObjectName(u"monitoring")
        self.verticalLayout_10 = QVBoxLayout(self.monitoring)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayout_53 = QGridLayout()
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.gridLayout_53.setHorizontalSpacing(20)
        self.gridLayout_53.setVerticalSpacing(10)
        self.label_10 = QLabel(self.monitoring)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_53.addWidget(self.label_10, 0, 2, 1, 1)

        self.label_73 = QLabel(self.monitoring)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_53.addWidget(self.label_73, 0, 0, 1, 1)

        self.gridLayout_44 = QGridLayout()
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setHorizontalSpacing(20)
        self.gridLayout_44.setVerticalSpacing(8)
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(20)
        self.gridLayout_9.setVerticalSpacing(10)
        self.btn_create_report = QPushButton(self.monitoring)
        self.btn_create_report.setObjectName(u"btn_create_report")
        sizePolicy2.setHeightForWidth(self.btn_create_report.sizePolicy().hasHeightForWidth())
        self.btn_create_report.setSizePolicy(sizePolicy2)
        self.btn_create_report.setMinimumSize(QSize(200, 50))
        self.btn_create_report.setFont(font)
        self.btn_create_report.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_create_report.setStyleSheet(u"background-color: black;\n"
"color:white;")
        icon20 = QIcon()
        icon20.addFile(u":/icons/images/icons/cil-task.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_create_report.setIcon(icon20)

        self.gridLayout_9.addWidget(self.btn_create_report, 1, 0, 1, 1)

        self.btn_new_one = QPushButton(self.monitoring)
        self.btn_new_one.setObjectName(u"btn_new_one")
        sizePolicy2.setHeightForWidth(self.btn_new_one.sizePolicy().hasHeightForWidth())
        self.btn_new_one.setSizePolicy(sizePolicy2)
        self.btn_new_one.setMinimumSize(QSize(200, 50))
        self.btn_new_one.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new_one.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon21 = QIcon()
        icon21.addFile(u":/icons/images/icons/cil-star.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_one.setIcon(icon21)

        self.gridLayout_9.addWidget(self.btn_new_one, 1, 1, 1, 2)

        self.label_87 = QLabel(self.monitoring)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout_9.addWidget(self.label_87, 0, 0, 1, 3)


        self.gridLayout_44.addLayout(self.gridLayout_9, 3, 0, 2, 2)

        self.listWidget_9 = QListWidget(self.monitoring)
        self.listWidget_9.setObjectName(u"listWidget_9")
        self.listWidget_9.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_44.addWidget(self.listWidget_9, 1, 0, 2, 2)

        self.label_7 = QLabel(self.monitoring)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_44.addWidget(self.label_7, 0, 0, 1, 2)


        self.gridLayout_53.addLayout(self.gridLayout_44, 3, 2, 6, 1)

        self.gridLayout_55 = QGridLayout()
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.gridLayout_55.setHorizontalSpacing(20)
        self.gridLayout_55.setVerticalSpacing(6)
        self.bar_chart = QPushButton(self.monitoring)
        self.bar_chart.setObjectName(u"bar_chart")
        self.bar_chart.setMinimumSize(QSize(0, 30))
        self.bar_chart.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_55.addWidget(self.bar_chart, 0, 0, 1, 1)

        self.pie_chart = QPushButton(self.monitoring)
        self.pie_chart.setObjectName(u"pie_chart")
        self.pie_chart.setMinimumSize(QSize(0, 30))
        self.pie_chart.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_55.addWidget(self.pie_chart, 0, 1, 1, 1)


        self.gridLayout_53.addLayout(self.gridLayout_55, 2, 2, 1, 1)

        self.label_74 = QLabel(self.monitoring)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_53.addWidget(self.label_74, 0, 1, 1, 1)

        self.label_47 = QLabel(self.monitoring)
        self.label_47.setObjectName(u"label_47")
        sizePolicy4.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy4)
        self.label_47.setMinimumSize(QSize(0, 0))
        self.label_47.setMaximumSize(QSize(16777215, 480))
        self.label_47.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.label_47.setScaledContents(True)

        self.gridLayout_53.addWidget(self.label_47, 1, 2, 1, 1)

        self.listWidget_19 = QListWidget(self.monitoring)
        self.listWidget_19.setObjectName(u"listWidget_19")
        self.listWidget_19.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_53.addWidget(self.listWidget_19, 1, 1, 2, 1)

        self.listWidget_16 = QListWidget(self.monitoring)
        self.listWidget_16.setObjectName(u"listWidget_16")
        self.listWidget_16.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_53.addWidget(self.listWidget_16, 1, 0, 2, 1)

        self.gridLayout_56 = QGridLayout()
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.listWidget_14 = QListWidget(self.monitoring)
        self.listWidget_14.setObjectName(u"listWidget_14")
        self.listWidget_14.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_56.addWidget(self.listWidget_14, 1, 0, 1, 1)

        self.label_45 = QLabel(self.monitoring)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_56.addWidget(self.label_45, 0, 0, 1, 1)


        self.gridLayout_53.addLayout(self.gridLayout_56, 3, 0, 1, 2)


        self.verticalLayout_10.addLayout(self.gridLayout_53)

        self.stackedWidget.addWidget(self.monitoring)
        self.customFault = QWidget()
        self.customFault.setObjectName(u"customFault")
        self.verticalLayout_19 = QVBoxLayout(self.customFault)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(10)
        self.gridLayout_16.setVerticalSpacing(6)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setVerticalSpacing(6)
        self.btn_create_fault = QPushButton(self.customFault)
        self.btn_create_fault.setObjectName(u"btn_create_fault")
        self.btn_create_fault.setMinimumSize(QSize(0, 30))
        self.btn_create_fault.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_create_fault.setIcon(icon9)

        self.gridLayout_3.addWidget(self.btn_create_fault, 0, 0, 1, 1)

        self.btn_delete_fault = QPushButton(self.customFault)
        self.btn_delete_fault.setObjectName(u"btn_delete_fault")
        self.btn_delete_fault.setMinimumSize(QSize(0, 30))
        self.btn_delete_fault.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_delete_fault.setIcon(icon10)

        self.gridLayout_3.addWidget(self.btn_delete_fault, 0, 1, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_3, 5, 1, 2, 7)

        self.plainTextEdit_39 = QPlainTextEdit(self.customFault)
        self.plainTextEdit_39.setObjectName(u"plainTextEdit_39")
        self.plainTextEdit_39.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_16.addWidget(self.plainTextEdit_39, 1, 0, 8, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setVerticalSpacing(10)
        self.listWidget_5 = QListWidget(self.customFault)
        self.listWidget_5.setObjectName(u"listWidget_5")
        self.listWidget_5.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget_5.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_8.addWidget(self.listWidget_5, 2, 0, 1, 1)

        self.btn_remove_createdFault = QPushButton(self.customFault)
        self.btn_remove_createdFault.setObjectName(u"btn_remove_createdFault")
        self.btn_remove_createdFault.setMinimumSize(QSize(0, 30))
        self.btn_remove_createdFault.setMaximumSize(QSize(16777215, 30))
        self.btn_remove_createdFault.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_remove_createdFault.setIcon(icon12)

        self.gridLayout_8.addWidget(self.btn_remove_createdFault, 3, 0, 1, 1)

        self.label_71 = QLabel(self.customFault)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_8.addWidget(self.label_71, 1, 0, 1, 1)

        self.plainTextEdit_45 = QPlainTextEdit(self.customFault)
        self.plainTextEdit_45.setObjectName(u"plainTextEdit_45")
        self.plainTextEdit_45.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_8.addWidget(self.plainTextEdit_45, 0, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_8, 1, 8, 7, 1)

        self.plainTextEdit_41 = QPlainTextEdit(self.customFault)
        self.plainTextEdit_41.setObjectName(u"plainTextEdit_41")
        self.plainTextEdit_41.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_41.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_41.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_16.addWidget(self.plainTextEdit_41, 2, 2, 1, 6)

        self.label_65 = QLabel(self.customFault)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_16.addWidget(self.label_65, 1, 1, 1, 1)

        self.label_66 = QLabel(self.customFault)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_16.addWidget(self.label_66, 2, 1, 1, 1)

        self.label_70 = QLabel(self.customFault)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.label_70, 0, 8, 1, 1)

        self.label_61 = QLabel(self.customFault)
        self.label_61.setObjectName(u"label_61")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy9)

        self.gridLayout_16.addWidget(self.label_61, 8, 6, 1, 2)

        self.label_43 = QLabel(self.customFault)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(40, 30))
        self.label_43.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_16.addWidget(self.label_43, 8, 3, 1, 1)

        self.btn_back_fi = QPushButton(self.customFault)
        self.btn_back_fi.setObjectName(u"btn_back_fi")
        sizePolicy2.setHeightForWidth(self.btn_back_fi.sizePolicy().hasHeightForWidth())
        self.btn_back_fi.setSizePolicy(sizePolicy2)
        self.btn_back_fi.setMinimumSize(QSize(200, 30))
        self.btn_back_fi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_fi.setStyleSheet(u"background-color: black;\n"
"color:white;")
        self.btn_back_fi.setIcon(icon13)

        self.gridLayout_16.addWidget(self.btn_back_fi, 8, 8, 1, 1)

        self.label_62 = QLabel(self.customFault)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.label_62, 0, 1, 1, 7)

        self.label_68 = QLabel(self.customFault)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_16.addWidget(self.label_68, 4, 1, 1, 1)

        self.label_69 = QLabel(self.customFault)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.label_69, 0, 0, 1, 1)

        self.label_41 = QLabel(self.customFault)
        self.label_41.setObjectName(u"label_41")
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        self.label_41.setMaximumSize(QSize(100, 30))

        self.gridLayout_16.addWidget(self.label_41, 8, 1, 1, 1)

        self.plainTextEdit_40 = QPlainTextEdit(self.customFault)
        self.plainTextEdit_40.setObjectName(u"plainTextEdit_40")
        self.plainTextEdit_40.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_40.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_40.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_16.addWidget(self.plainTextEdit_40, 1, 2, 1, 6)

        self.btn_save_fault = QPushButton(self.customFault)
        self.btn_save_fault.setObjectName(u"btn_save_fault")
        sizePolicy.setHeightForWidth(self.btn_save_fault.sizePolicy().hasHeightForWidth())
        self.btn_save_fault.setSizePolicy(sizePolicy)
        self.btn_save_fault.setMinimumSize(QSize(120, 30))
        self.btn_save_fault.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_save_fault.setIcon(icon16)

        self.gridLayout_16.addWidget(self.btn_save_fault, 8, 4, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_4, 7, 1, 1, 7)

        self.label_67 = QLabel(self.customFault)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_16.addWidget(self.label_67, 3, 1, 1, 1)

        self.plainTextEdit_42 = QPlainTextEdit(self.customFault)
        self.plainTextEdit_42.setObjectName(u"plainTextEdit_42")
        self.plainTextEdit_42.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_42.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_42.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_16.addWidget(self.plainTextEdit_42, 3, 2, 1, 6)

        self.plainTextEdit_43 = QPlainTextEdit(self.customFault)
        self.plainTextEdit_43.setObjectName(u"plainTextEdit_43")
        self.plainTextEdit_43.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_43.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_43.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_16.addWidget(self.plainTextEdit_43, 4, 2, 1, 6)

        self.plainTextEdit_44 = QPlainTextEdit(self.customFault)
        self.plainTextEdit_44.setObjectName(u"plainTextEdit_44")
        self.plainTextEdit_44.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_44.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_44.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_16.addWidget(self.plainTextEdit_44, 8, 2, 1, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_16)

        self.stackedWidget.addWidget(self.customFault)
        self.cWorkload = QWidget()
        self.cWorkload.setObjectName(u"cWorkload")
        self.verticalLayout_18 = QVBoxLayout(self.cWorkload)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(20)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(6)
        self.plainTextEdit_2 = QPlainTextEdit(self.cWorkload)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMinimumSize(QSize(0, 100))
        self.plainTextEdit_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_5.addWidget(self.plainTextEdit_2, 6, 0, 1, 3)

        self.label_107 = QLabel(self.cWorkload)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMinimumSize(QSize(0, 30))
        self.label_107.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.label_107, 5, 0, 1, 3)

        self.label_32 = QLabel(self.cWorkload)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.label_32, 2, 0, 1, 3)

        self.plainTextEdit = QPlainTextEdit(self.cWorkload)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(0, 100))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.plainTextEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.plainTextEdit, 3, 0, 2, 3)

        self.btn_workload_save = QPushButton(self.cWorkload)
        self.btn_workload_save.setObjectName(u"btn_workload_save")
        self.btn_workload_save.setMinimumSize(QSize(0, 30))
        self.btn_workload_save.setMaximumSize(QSize(16777215, 30))
        self.btn_workload_save.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_workload_save.setIcon(icon16)

        self.gridLayout_5.addWidget(self.btn_workload_save, 9, 0, 1, 3)

        self.label_106 = QLabel(self.cWorkload)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMinimumSize(QSize(0, 30))
        self.label_106.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.label_106, 0, 0, 1, 3, Qt.AlignHCenter)

        self.label_105 = QLabel(self.cWorkload)
        self.label_105.setObjectName(u"label_105")

        self.gridLayout_5.addWidget(self.label_105, 1, 0, 1, 1)

        self.checkBox_12 = QCheckBox(self.cWorkload)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setMinimumSize(QSize(0, 30))
        self.checkBox_12.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.checkBox_12, 8, 0, 1, 3)

        self.btn_changeDir = QPushButton(self.cWorkload)
        self.btn_changeDir.setObjectName(u"btn_changeDir")
        self.btn_changeDir.setMinimumSize(QSize(80, 30))
        self.btn_changeDir.setMaximumSize(QSize(80, 30))
        self.btn_changeDir.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        self.btn_changeDir.setIcon(icon6)

        self.gridLayout_5.addWidget(self.btn_changeDir, 1, 2, 1, 1)

        self.label_109 = QLabel(self.cWorkload)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setMinimumSize(QSize(0, 30))
        self.label_109.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.label_109, 7, 0, 1, 1)

        self.plainTextEdit_35 = QPlainTextEdit(self.cWorkload)
        self.plainTextEdit_35.setObjectName(u"plainTextEdit_35")
        self.plainTextEdit_35.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_35.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_35.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_5.addWidget(self.plainTextEdit_35, 1, 1, 1, 1)

        self.plainTextEdit_36 = QPlainTextEdit(self.cWorkload)
        self.plainTextEdit_36.setObjectName(u"plainTextEdit_36")
        self.plainTextEdit_36.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_36.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_36.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_5.addWidget(self.plainTextEdit_36, 7, 1, 1, 2)


        self.gridLayout_13.addLayout(self.gridLayout_5, 0, 0, 5, 1)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_53 = QLabel(self.cWorkload)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_17.addWidget(self.label_53, 0, 0, 1, 1)

        self.plainTextEdit_38 = QPlainTextEdit(self.cWorkload)
        self.plainTextEdit_38.setObjectName(u"plainTextEdit_38")
        self.plainTextEdit_38.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.plainTextEdit_38.setReadOnly(True)

        self.gridLayout_17.addWidget(self.plainTextEdit_38, 1, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_17, 1, 1, 4, 2)

        self.gridLayout_45 = QGridLayout()
        self.gridLayout_45.setSpacing(10)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.btn_take_tasks = QPushButton(self.cWorkload)
        self.btn_take_tasks.setObjectName(u"btn_take_tasks")
        sizePolicy4.setHeightForWidth(self.btn_take_tasks.sizePolicy().hasHeightForWidth())
        self.btn_take_tasks.setSizePolicy(sizePolicy4)
        self.btn_take_tasks.setMinimumSize(QSize(0, 30))
        self.btn_take_tasks.setMaximumSize(QSize(16777215, 30))
        self.btn_take_tasks.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon22 = QIcon()
        icon22.addFile(u":/icons/images/icons/cil-vertical-align-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_take_tasks.setIcon(icon22)

        self.gridLayout_45.addWidget(self.btn_take_tasks, 2, 0, 1, 1)

        self.label = QLabel(self.cWorkload)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_45.addWidget(self.label, 5, 1, 1, 1)

        self.label_29 = QLabel(self.cWorkload)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_45.addWidget(self.label_29, 1, 1, 1, 3)

        self.btn_select_task = QPushButton(self.cWorkload)
        self.btn_select_task.setObjectName(u"btn_select_task")
        sizePolicy4.setHeightForWidth(self.btn_select_task.sizePolicy().hasHeightForWidth())
        self.btn_select_task.setSizePolicy(sizePolicy4)
        self.btn_select_task.setMinimumSize(QSize(0, 30))
        self.btn_select_task.setMaximumSize(QSize(16777215, 30))
        self.btn_select_task.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_select_task.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_select_task.setIcon(icon7)

        self.gridLayout_45.addWidget(self.btn_select_task, 6, 0, 1, 1)

        self.gridLayout_46 = QGridLayout()
        self.gridLayout_46.setSpacing(6)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.btn_save_task = QPushButton(self.cWorkload)
        self.btn_save_task.setObjectName(u"btn_save_task")
        sizePolicy4.setHeightForWidth(self.btn_save_task.sizePolicy().hasHeightForWidth())
        self.btn_save_task.setSizePolicy(sizePolicy4)
        self.btn_save_task.setMinimumSize(QSize(120, 30))
        self.btn_save_task.setMaximumSize(QSize(16777215, 30))
        self.btn_save_task.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_task.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_save_task.setIcon(icon16)

        self.gridLayout_46.addWidget(self.btn_save_task, 0, 0, 1, 1)

        self.btn_remove_task = QPushButton(self.cWorkload)
        self.btn_remove_task.setObjectName(u"btn_remove_task")
        sizePolicy4.setHeightForWidth(self.btn_remove_task.sizePolicy().hasHeightForWidth())
        self.btn_remove_task.setSizePolicy(sizePolicy4)
        self.btn_remove_task.setMinimumSize(QSize(120, 30))
        self.btn_remove_task.setMaximumSize(QSize(16777215, 30))
        self.btn_remove_task.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_remove_task.setIcon(icon12)

        self.gridLayout_46.addWidget(self.btn_remove_task, 0, 1, 1, 1)


        self.gridLayout_45.addLayout(self.gridLayout_46, 6, 1, 1, 3)

        self.listWidget_21 = QListWidget(self.cWorkload)
        self.listWidget_21.setObjectName(u"listWidget_21")
        sizePolicy4.setHeightForWidth(self.listWidget_21.sizePolicy().hasHeightForWidth())
        self.listWidget_21.setSizePolicy(sizePolicy4)
        self.listWidget_21.setMinimumSize(QSize(0, 200))
        self.listWidget_21.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_45.addWidget(self.listWidget_21, 3, 0, 3, 1)

        self.label_4 = QLabel(self.cWorkload)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_45.addWidget(self.label_4, 5, 3, 1, 1)

        self.label_108 = QLabel(self.cWorkload)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMinimumSize(QSize(0, 30))
        self.label_108.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_45.addWidget(self.label_108, 0, 0, 1, 4, Qt.AlignHCenter)

        self.listWidget_22 = QListWidget(self.cWorkload)
        self.listWidget_22.setObjectName(u"listWidget_22")
        sizePolicy4.setHeightForWidth(self.listWidget_22.sizePolicy().hasHeightForWidth())
        self.listWidget_22.setSizePolicy(sizePolicy4)
        self.listWidget_22.setMinimumSize(QSize(0, 250))
        self.listWidget_22.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_45.addWidget(self.listWidget_22, 2, 1, 3, 3)

        self.label_31 = QLabel(self.cWorkload)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_45.addWidget(self.label_31, 1, 0, 1, 1)

        self.plainTextEdit_37 = QPlainTextEdit(self.cWorkload)
        self.plainTextEdit_37.setObjectName(u"plainTextEdit_37")
        self.plainTextEdit_37.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_37.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_37.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_45.addWidget(self.plainTextEdit_37, 5, 2, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_45, 0, 1, 1, 2)


        self.verticalLayout_18.addLayout(self.gridLayout_13)

        self.btn_back_start = QPushButton(self.cWorkload)
        self.btn_back_start.setObjectName(u"btn_back_start")
        sizePolicy.setHeightForWidth(self.btn_back_start.sizePolicy().hasHeightForWidth())
        self.btn_back_start.setSizePolicy(sizePolicy)
        self.btn_back_start.setMinimumSize(QSize(200, 30))
        self.btn_back_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_start.setStyleSheet(u"background-color: black;\n"
"color:white;")
        self.btn_back_start.setIcon(icon13)

        self.verticalLayout_18.addWidget(self.btn_back_start, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.cWorkload)
        self.cSnippets = QWidget()
        self.cSnippets.setObjectName(u"cSnippets")
        self.verticalLayout_54 = QVBoxLayout(self.cSnippets)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(20)
        self.gridLayout_11.setVerticalSpacing(6)
        self.back_snip = QPushButton(self.cSnippets)
        self.back_snip.setObjectName(u"back_snip")
        sizePolicy2.setHeightForWidth(self.back_snip.sizePolicy().hasHeightForWidth())
        self.back_snip.setSizePolicy(sizePolicy2)
        self.back_snip.setMinimumSize(QSize(0, 30))
        self.back_snip.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_snip.setStyleSheet(u"background-color: black;\n"
"color:white;")
        self.back_snip.setIcon(icon13)

        self.gridLayout_11.addWidget(self.back_snip, 7, 4, 1, 4)

        self.label_14 = QLabel(self.cSnippets)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.label_14, 0, 4, 1, 4)

        self.label_63 = QLabel(self.cSnippets)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.label_63, 0, 0, 1, 2)

        self.label_23 = QLabel(self.cSnippets)
        self.label_23.setObjectName(u"label_23")
        sizePolicy9.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy9)

        self.gridLayout_11.addWidget(self.label_23, 5, 4, 1, 2)

        self.label_13 = QLabel(self.cSnippets)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.label_13, 0, 2, 1, 2)

        self.checkBox_6 = QCheckBox(self.cSnippets)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_11.addWidget(self.checkBox_6, 4, 4, 1, 4, Qt.AlignHCenter)

        self.label_60 = QLabel(self.cSnippets)
        self.label_60.setObjectName(u"label_60")
        sizePolicy4.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy4)
        self.label_60.setMinimumSize(QSize(200, 30))
        self.label_60.setMaximumSize(QSize(16777215, 30))
        self.label_60.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_60, 6, 4, 1, 4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_3, 3, 2, 5, 2)

        self.btn_save_snip = QPushButton(self.cSnippets)
        self.btn_save_snip.setObjectName(u"btn_save_snip")
        sizePolicy4.setHeightForWidth(self.btn_save_snip.sizePolicy().hasHeightForWidth())
        self.btn_save_snip.setSizePolicy(sizePolicy4)
        self.btn_save_snip.setMinimumSize(QSize(0, 30))
        self.btn_save_snip.setMaximumSize(QSize(16777215, 30))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setUnderline(False)
        font8.setStrikeOut(False)
        font8.setKerning(False)
        self.btn_save_snip.setFont(font8)
        self.btn_save_snip.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_snip.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_save_snip.setIcon(icon16)

        self.gridLayout_11.addWidget(self.btn_save_snip, 5, 7, 1, 1)

        self.plainTextEdit_46 = QPlainTextEdit(self.cSnippets)
        self.plainTextEdit_46.setObjectName(u"plainTextEdit_46")
        self.plainTextEdit_46.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_11.addWidget(self.plainTextEdit_46, 1, 0, 7, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(10)
        self.label_21 = QLabel(self.cSnippets)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_21, 2, 0, 1, 2)

        self.label_64 = QLabel(self.cSnippets)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_64, 4, 0, 1, 2)

        self.btn_delete_snip = QPushButton(self.cSnippets)
        self.btn_delete_snip.setObjectName(u"btn_delete_snip")
        sizePolicy4.setHeightForWidth(self.btn_delete_snip.sizePolicy().hasHeightForWidth())
        self.btn_delete_snip.setSizePolicy(sizePolicy4)
        self.btn_delete_snip.setMinimumSize(QSize(200, 0))
        self.btn_delete_snip.setMaximumSize(QSize(16777215, 30))
        self.btn_delete_snip.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_delete_snip.setIcon(icon10)

        self.gridLayout_2.addWidget(self.btn_delete_snip, 8, 1, 1, 1)

        self.plainTextEdit_47 = QPlainTextEdit(self.cSnippets)
        self.plainTextEdit_47.setObjectName(u"plainTextEdit_47")
        self.plainTextEdit_47.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_47.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_2.addWidget(self.plainTextEdit_47, 1, 0, 1, 2)

        self.btn_create_snip = QPushButton(self.cSnippets)
        self.btn_create_snip.setObjectName(u"btn_create_snip")
        sizePolicy4.setHeightForWidth(self.btn_create_snip.sizePolicy().hasHeightForWidth())
        self.btn_create_snip.setSizePolicy(sizePolicy4)
        self.btn_create_snip.setMinimumSize(QSize(200, 30))
        self.btn_create_snip.setMaximumSize(QSize(16777215, 30))
        self.btn_create_snip.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_create_snip.setIcon(icon9)

        self.gridLayout_2.addWidget(self.btn_create_snip, 8, 0, 1, 1)

        self.plainTextEdit_49 = QPlainTextEdit(self.cSnippets)
        self.plainTextEdit_49.setObjectName(u"plainTextEdit_49")
        self.plainTextEdit_49.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_49.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_2.addWidget(self.plainTextEdit_49, 5, 0, 1, 2)

        self.plainTextEdit_48 = QPlainTextEdit(self.cSnippets)
        self.plainTextEdit_48.setObjectName(u"plainTextEdit_48")
        self.plainTextEdit_48.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_48.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_2.addWidget(self.plainTextEdit_48, 3, 0, 1, 2)

        self.label_19 = QLabel(self.cSnippets)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_19, 0, 0, 1, 2)

        self.label_22 = QLabel(self.cSnippets)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_22, 6, 0, 1, 2)

        self.plainTextEdit_50 = QPlainTextEdit(self.cSnippets)
        self.plainTextEdit_50.setObjectName(u"plainTextEdit_50")
        self.plainTextEdit_50.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_50.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_2.addWidget(self.plainTextEdit_50, 7, 0, 1, 2)


        self.gridLayout_11.addLayout(self.gridLayout_2, 1, 2, 2, 2)

        self.plainTextEdit_51 = QPlainTextEdit(self.cSnippets)
        self.plainTextEdit_51.setObjectName(u"plainTextEdit_51")
        self.plainTextEdit_51.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_11.addWidget(self.plainTextEdit_51, 1, 4, 3, 4)

        self.plainTextEdit_52 = QPlainTextEdit(self.cSnippets)
        self.plainTextEdit_52.setObjectName(u"plainTextEdit_52")
        self.plainTextEdit_52.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_52.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_11.addWidget(self.plainTextEdit_52, 5, 6, 1, 1)


        self.verticalLayout_54.addLayout(self.gridLayout_11)

        self.stackedWidget.addWidget(self.cSnippets)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 20, 501, 301))
        self.frame.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 10, 121, 31))
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(140, 20, 80, 24))
        self.progressBar_3 = QProgressBar(self.frame)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setGeometry(QRect(10, 260, 118, 23))
        self.progressBar_3.setValue(24)
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(260, 30, 221, 241))
        self.dnn_parameter = QComboBox(self.frame)
        self.dnn_parameter.addItem("")
        self.dnn_parameter.addItem("")
        self.dnn_parameter.addItem("")
        self.dnn_parameter.setObjectName(u"dnn_parameter")
        self.dnn_parameter.setGeometry(QRect(130, 260, 72, 24))
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, -10, 121, 50))
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(9, 339, 501, 301))
        self.frame_3.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.textEdit_2 = QTextEdit(self.frame_3)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(13, 9, 331, 271))
        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(520, 30, 721, 851))
        self.frame_4.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.plainTextEdit_dnn_source = QPlainTextEdit(self.frame_4)
        self.plainTextEdit_dnn_source.setObjectName(u"plainTextEdit_dnn_source")
        self.plainTextEdit_dnn_source.setGeometry(QRect(20, 90, 271, 131))
        self.plainTextEdit_dnn_source.setStyleSheet(u"background-color: rgb(40, 59, 73);")
        self.plainTextEdit_53 = QPlainTextEdit(self.frame_4)
        self.plainTextEdit_53.setObjectName(u"plainTextEdit_53")
        self.plainTextEdit_53.setGeometry(QRect(300, 50, 221, 371))
        self.plainTextEdit_53.setStyleSheet(u"background-color: rgb(40, 59, 72);")
        self.listWidget_dnn_selected_snippet = QListWidget(self.frame_4)
        self.listWidget_dnn_selected_snippet.setObjectName(u"listWidget_dnn_selected_snippet")
        self.listWidget_dnn_selected_snippet.setGeometry(QRect(20, 490, 271, 351))
        self.listWidget_dnn_selected_snippet.setStyleSheet(u"background-color: rgb(40, 59, 73);")
        self.pushButton_dnn_mutate = QPushButton(self.frame_4)
        self.pushButton_dnn_mutate.setObjectName(u"pushButton_dnn_mutate")
        self.pushButton_dnn_mutate.setGeometry(QRect(550, 410, 151, 41))
        self.pushButton_dnn_mutate.setStyleSheet(u"background-color: rgb(80, 59, 73);")
        self.plainTextEdit_mutated_code = QPlainTextEdit(self.frame_4)
        self.plainTextEdit_mutated_code.setObjectName(u"plainTextEdit_mutated_code")
        self.plainTextEdit_mutated_code.setGeometry(QRect(300, 490, 241, 341))
        self.plainTextEdit_mutated_code.setStyleSheet(u"background-color: rgb(40, 59, 73);")
        self.listWidget_mutate_list = QListWidget(self.frame_4)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        QListWidgetItem(self.listWidget_mutate_list)
        self.listWidget_mutate_list.setObjectName(u"listWidget_mutate_list")
        self.listWidget_mutate_list.setGeometry(QRect(530, 30, 171, 191))
        self.listWidget_mutate_list.setStyleSheet(u"background-color: rgb(40, 59, 73);")
        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(100, 460, 91, 20))
        self.label_25 = QLabel(self.frame_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(370, 460, 91, 20))
        self.label_35 = QLabel(self.frame_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(350, 30, 91, 16))
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 20, 281, 61))
        self.frame_2.setStyleSheet(u"background-color: rgb(40, 59, 72);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 181, 31))
        self.btn_load_dnn = QPushButton(self.frame_2)
        self.btn_load_dnn.setObjectName(u"btn_load_dnn")
        self.btn_load_dnn.setGeometry(QRect(190, 10, 80, 41))
        self.btn_load_dnn.setStyleSheet(u"background-color: rgb(80, 59, 73);")
        self.listWidget_selected_mutate_parameters = QListWidget(self.frame_4)
        self.listWidget_selected_mutate_parameters.setObjectName(u"listWidget_selected_mutate_parameters")
        self.listWidget_selected_mutate_parameters.setGeometry(QRect(540, 260, 171, 141))
        self.listWidget_selected_mutate_parameters.setStyleSheet(u"background-color: rgb(40, 59, 73);")
        self.label_37 = QLabel(self.frame_4)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(540, 230, 171, 16))
        self.label_77 = QLabel(self.frame_4)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(540, 10, 151, 16))
        self.progressBar_Mutation = QProgressBar(self.frame_4)
        self.progressBar_Mutation.setObjectName(u"progressBar_Mutation")
        self.progressBar_Mutation.setGeometry(QRect(560, 460, 118, 23))
        self.progressBar_Mutation.setValue(24)
        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(-1, 649, 521, 241))
        self.frame_5.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.dnn_code_snippet_list = QListWidget(self.frame_5)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        QListWidgetItem(self.dnn_code_snippet_list)
        self.dnn_code_snippet_list.setObjectName(u"dnn_code_snippet_list")
        self.dnn_code_snippet_list.setGeometry(QRect(0, 0, 221, 231))
        self.dnn_code_snippet_list.setStyleSheet(u"background-color: rgb(40, 59, 73);")
        self.dnn_selected_snippet = QListWidget(self.frame_5)
        self.dnn_selected_snippet.setObjectName(u"dnn_selected_snippet")
        self.dnn_selected_snippet.setGeometry(QRect(250, 10, 251, 111))
        self.dnn_selected_snippet.setStyleSheet(u"background-color: rgb(40, 59, 73);")
        self.pushButton_dnn_scan = QPushButton(self.frame_5)
        self.pushButton_dnn_scan.setObjectName(u"pushButton_dnn_scan")
        self.pushButton_dnn_scan.setGeometry(QRect(430, 160, 80, 31))
        self.pushButton_dnn_scan.setStyleSheet(u"background-color: rgb(80, 59, 73);")
        self.plainTextEdit_code_snippet_details = QPlainTextEdit(self.frame_5)
        self.plainTextEdit_code_snippet_details.setObjectName(u"plainTextEdit_code_snippet_details")
        self.plainTextEdit_code_snippet_details.setGeometry(QRect(253, 140, 171, 81))
        self.plainTextEdit_code_snippet_details.setStyleSheet(u"background-color: rgb(40, 59, 73);")
        self.stackedWidget.addWidget(self.page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setBold(False)
        font9.setItalic(False)
        self.creditsLabel.setFont(font9)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(10)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"IM-FIT", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Fault Injection Tool", None))
        self.label_46.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.open_ros_page.setText(QCoreApplication.translate("MainWindow", u"ROS Module", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_scan.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.btn_fiplan.setText(QCoreApplication.translate("MainWindow", u"FI Plan", None))
        self.btn_execution.setText(QCoreApplication.translate("MainWindow", u"Execution", None))
        self.btn_monitoring.setText(QCoreApplication.translate("MainWindow", u"Monitoring", None))
        self.btn_dnn.setText(QCoreApplication.translate("MainWindow", u"DNN", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"IM-FIT", None))
#if QT_CONFIG(tooltip)
        self.refresh_page.setToolTip(QCoreApplication.translate("MainWindow", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.refresh_page.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
#if QT_CONFIG(tooltip)
        self.reset_for_all.setToolTip(QCoreApplication.translate("MainWindow", u"Reset", None))
#endif // QT_CONFIG(tooltip)
        self.reset_for_all.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.home.setStyleSheet("")
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("MainWindow", u"	Start\n"
"IM-FIT needs the source code added by the user. User can upload its workload and if it wants to create a new one, it can do it. The user can select the code snippets for customizing the process.", None))
        self.plainTextEdit_7.setPlainText(QCoreApplication.translate("MainWindow", u"	Execute\n"
"The user selects the operating condition for the mutation process. If the user does not want to change anything, it can use deafult settings. After user completed the settings, it can start the execution process. This process runs the mutation codes.", None))
        self.plainTextEdit_5.setPlainText(QCoreApplication.translate("MainWindow", u"	Scan\n"
"IM-FIT scans the source code according to selected workload and code snippets. The user can the place of workload on the source code with purple color. The blue color show the lines for applying to mutation testing.", None))
        self.plainTextEdit_6.setPlainText(QCoreApplication.translate("MainWindow", u"	FI Plan\n"
"The user creates the fault injection plans to execution. All possible lines and all faults are shown to the user to select and create the plan. After completed the selection lines and faults, applies mutation for the lines from the source codes. After all, the user saves the \"FI Plan\" to use in execution.", None))
        self.plainTextEdit_8.setPlainText(QCoreApplication.translate("MainWindow", u"	Monitoring\n"
"After the execution, the user can see the all results about the mutation process. User can see the faults, metrics, codes' AST diagram, mutation state graphic and rosbag scenarios. If the user wants to take a V&V report, IM-FIT gives one V&V report including all details.", None))
        self.label_2.setText("")
        self.btn_go_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Workload", None))
        self.btn_select_workload.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.btn_select_snippet.setText(QCoreApplication.translate("MainWindow", u"Select Snippet", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.btn_create_workload.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.btn_clear_workload.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Codes/Workload Ready", None))

        __sortingEnabled = self.code_snippet_list.isSortingEnabled()
        self.code_snippet_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.code_snippet_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"and", None));
        ___qlistwidgetitem1 = self.code_snippet_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"epoch", None));
        ___qlistwidgetitem2 = self.code_snippet_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"assert", None));
        ___qlistwidgetitem3 = self.code_snippet_list.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"break", None));
        ___qlistwidgetitem4 = self.code_snippet_list.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"continue", None));
        ___qlistwidgetitem5 = self.code_snippet_list.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"del", None));
        ___qlistwidgetitem6 = self.code_snippet_list.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"elif", None));
        ___qlistwidgetitem7 = self.code_snippet_list.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"else", None));
        ___qlistwidgetitem8 = self.code_snippet_list.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"except", None));
        ___qlistwidgetitem9 = self.code_snippet_list.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"False", None));
        ___qlistwidgetitem10 = self.code_snippet_list.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"finally", None));
        ___qlistwidgetitem11 = self.code_snippet_list.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"for", None));
        ___qlistwidgetitem12 = self.code_snippet_list.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"global", None));
        ___qlistwidgetitem13 = self.code_snippet_list.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"if", None));
        ___qlistwidgetitem14 = self.code_snippet_list.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"is", None));
        ___qlistwidgetitem15 = self.code_snippet_list.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"lambda", None));
        ___qlistwidgetitem16 = self.code_snippet_list.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"None", None));
        ___qlistwidgetitem17 = self.code_snippet_list.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"nonlocal", None));
        ___qlistwidgetitem18 = self.code_snippet_list.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"not", None));
        ___qlistwidgetitem19 = self.code_snippet_list.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"or", None));
        ___qlistwidgetitem20 = self.code_snippet_list.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"pass", None));
        ___qlistwidgetitem21 = self.code_snippet_list.item(21)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("MainWindow", u"raise", None));
        ___qlistwidgetitem22 = self.code_snippet_list.item(22)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("MainWindow", u"return", None));
        ___qlistwidgetitem23 = self.code_snippet_list.item(23)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("MainWindow", u"True", None));
        ___qlistwidgetitem24 = self.code_snippet_list.item(24)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("MainWindow", u"try", None));
        ___qlistwidgetitem25 = self.code_snippet_list.item(25)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("MainWindow", u"while", None));
        ___qlistwidgetitem26 = self.code_snippet_list.item(26)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("MainWindow", u"with", None));
        ___qlistwidgetitem27 = self.code_snippet_list.item(27)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("MainWindow", u"yield", None));
        ___qlistwidgetitem28 = self.code_snippet_list.item(28)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("MainWindow", u"abs()", None));
        ___qlistwidgetitem29 = self.code_snippet_list.item(29)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("MainWindow", u"all()", None));
        ___qlistwidgetitem30 = self.code_snippet_list.item(30)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("MainWindow", u"ascii()", None));
        ___qlistwidgetitem31 = self.code_snippet_list.item(31)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("MainWindow", u"bin()", None));
        ___qlistwidgetitem32 = self.code_snippet_list.item(32)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("MainWindow", u"bool()", None));
        ___qlistwidgetitem33 = self.code_snippet_list.item(33)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("MainWindow", u"bytearray()", None));
        ___qlistwidgetitem34 = self.code_snippet_list.item(34)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("MainWindow", u"bytes()", None));
        ___qlistwidgetitem35 = self.code_snippet_list.item(35)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("MainWindow", u"chr()", None));
        ___qlistwidgetitem36 = self.code_snippet_list.item(36)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("MainWindow", u"delattr()", None));
        ___qlistwidgetitem37 = self.code_snippet_list.item(37)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("MainWindow", u"dict()", None));
        ___qlistwidgetitem38 = self.code_snippet_list.item(38)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("MainWindow", u"divmod()", None));
        ___qlistwidgetitem39 = self.code_snippet_list.item(39)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("MainWindow", u"enumerate()", None));
        ___qlistwidgetitem40 = self.code_snippet_list.item(40)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("MainWindow", u"eval()", None));
        ___qlistwidgetitem41 = self.code_snippet_list.item(41)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("MainWindow", u"exec()", None));
        ___qlistwidgetitem42 = self.code_snippet_list.item(42)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("MainWindow", u"filter()", None));
        ___qlistwidgetitem43 = self.code_snippet_list.item(43)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("MainWindow", u"float()", None));
        ___qlistwidgetitem44 = self.code_snippet_list.item(44)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("MainWindow", u"frozenset()", None));
        ___qlistwidgetitem45 = self.code_snippet_list.item(45)
        ___qlistwidgetitem45.setText(QCoreApplication.translate("MainWindow", u"getattr()", None));
        ___qlistwidgetitem46 = self.code_snippet_list.item(46)
        ___qlistwidgetitem46.setText(QCoreApplication.translate("MainWindow", u"hasattr()", None));
        ___qlistwidgetitem47 = self.code_snippet_list.item(47)
        ___qlistwidgetitem47.setText(QCoreApplication.translate("MainWindow", u"hash()", None));
        ___qlistwidgetitem48 = self.code_snippet_list.item(48)
        ___qlistwidgetitem48.setText(QCoreApplication.translate("MainWindow", u"help()", None));
        ___qlistwidgetitem49 = self.code_snippet_list.item(49)
        ___qlistwidgetitem49.setText(QCoreApplication.translate("MainWindow", u"hex()", None));
        ___qlistwidgetitem50 = self.code_snippet_list.item(50)
        ___qlistwidgetitem50.setText(QCoreApplication.translate("MainWindow", u"id()", None));
        ___qlistwidgetitem51 = self.code_snippet_list.item(51)
        ___qlistwidgetitem51.setText(QCoreApplication.translate("MainWindow", u"int()", None));
        ___qlistwidgetitem52 = self.code_snippet_list.item(52)
        ___qlistwidgetitem52.setText(QCoreApplication.translate("MainWindow", u"isinstance()", None));
        ___qlistwidgetitem53 = self.code_snippet_list.item(53)
        ___qlistwidgetitem53.setText(QCoreApplication.translate("MainWindow", u"iter()", None));
        ___qlistwidgetitem54 = self.code_snippet_list.item(54)
        ___qlistwidgetitem54.setText(QCoreApplication.translate("MainWindow", u"len()", None));
        ___qlistwidgetitem55 = self.code_snippet_list.item(55)
        ___qlistwidgetitem55.setText(QCoreApplication.translate("MainWindow", u"list()", None));
        ___qlistwidgetitem56 = self.code_snippet_list.item(56)
        ___qlistwidgetitem56.setText(QCoreApplication.translate("MainWindow", u"map()", None));
        ___qlistwidgetitem57 = self.code_snippet_list.item(57)
        ___qlistwidgetitem57.setText(QCoreApplication.translate("MainWindow", u"max()", None));
        ___qlistwidgetitem58 = self.code_snippet_list.item(58)
        ___qlistwidgetitem58.setText(QCoreApplication.translate("MainWindow", u"memoryview()", None));
        ___qlistwidgetitem59 = self.code_snippet_list.item(59)
        ___qlistwidgetitem59.setText(QCoreApplication.translate("MainWindow", u"min()", None));
        ___qlistwidgetitem60 = self.code_snippet_list.item(60)
        ___qlistwidgetitem60.setText(QCoreApplication.translate("MainWindow", u"next()", None));
        ___qlistwidgetitem61 = self.code_snippet_list.item(61)
        ___qlistwidgetitem61.setText(QCoreApplication.translate("MainWindow", u"oct()", None));
        ___qlistwidgetitem62 = self.code_snippet_list.item(62)
        ___qlistwidgetitem62.setText(QCoreApplication.translate("MainWindow", u"open()", None));
        ___qlistwidgetitem63 = self.code_snippet_list.item(63)
        ___qlistwidgetitem63.setText(QCoreApplication.translate("MainWindow", u"ord()", None));
        ___qlistwidgetitem64 = self.code_snippet_list.item(64)
        ___qlistwidgetitem64.setText(QCoreApplication.translate("MainWindow", u"pow()", None));
        ___qlistwidgetitem65 = self.code_snippet_list.item(65)
        ___qlistwidgetitem65.setText(QCoreApplication.translate("MainWindow", u"property()", None));
        ___qlistwidgetitem66 = self.code_snippet_list.item(66)
        ___qlistwidgetitem66.setText(QCoreApplication.translate("MainWindow", u"range()", None));
        ___qlistwidgetitem67 = self.code_snippet_list.item(67)
        ___qlistwidgetitem67.setText(QCoreApplication.translate("MainWindow", u"reversed()", None));
        ___qlistwidgetitem68 = self.code_snippet_list.item(68)
        ___qlistwidgetitem68.setText(QCoreApplication.translate("MainWindow", u"round()", None));
        ___qlistwidgetitem69 = self.code_snippet_list.item(69)
        ___qlistwidgetitem69.setText(QCoreApplication.translate("MainWindow", u"set()", None));
        ___qlistwidgetitem70 = self.code_snippet_list.item(70)
        ___qlistwidgetitem70.setText(QCoreApplication.translate("MainWindow", u"setattr()", None));
        ___qlistwidgetitem71 = self.code_snippet_list.item(71)
        ___qlistwidgetitem71.setText(QCoreApplication.translate("MainWindow", u"slice()", None));
        ___qlistwidgetitem72 = self.code_snippet_list.item(72)
        ___qlistwidgetitem72.setText(QCoreApplication.translate("MainWindow", u"sorted()", None));
        ___qlistwidgetitem73 = self.code_snippet_list.item(73)
        ___qlistwidgetitem73.setText(QCoreApplication.translate("MainWindow", u"str()", None));
        ___qlistwidgetitem74 = self.code_snippet_list.item(74)
        ___qlistwidgetitem74.setText(QCoreApplication.translate("MainWindow", u"sum()", None));
        ___qlistwidgetitem75 = self.code_snippet_list.item(75)
        ___qlistwidgetitem75.setText(QCoreApplication.translate("MainWindow", u"tuple()", None));
        ___qlistwidgetitem76 = self.code_snippet_list.item(76)
        ___qlistwidgetitem76.setText(QCoreApplication.translate("MainWindow", u"type()", None));
        ___qlistwidgetitem77 = self.code_snippet_list.item(77)
        ___qlistwidgetitem77.setText(QCoreApplication.translate("MainWindow", u"vars()", None));
        ___qlistwidgetitem78 = self.code_snippet_list.item(78)
        ___qlistwidgetitem78.setText(QCoreApplication.translate("MainWindow", u"zip()", None));
        ___qlistwidgetitem79 = self.code_snippet_list.item(79)
        ___qlistwidgetitem79.setText(QCoreApplication.translate("MainWindow", u"count()", None));
        ___qlistwidgetitem80 = self.code_snippet_list.item(80)
        ___qlistwidgetitem80.setText(QCoreApplication.translate("MainWindow", u"index()", None));
        ___qlistwidgetitem81 = self.code_snippet_list.item(81)
        ___qlistwidgetitem81.setText(QCoreApplication.translate("MainWindow", u"fromkeys()", None));
        ___qlistwidgetitem82 = self.code_snippet_list.item(82)
        ___qlistwidgetitem82.setText(QCoreApplication.translate("MainWindow", u"get()", None));
        ___qlistwidgetitem83 = self.code_snippet_list.item(83)
        ___qlistwidgetitem83.setText(QCoreApplication.translate("MainWindow", u"update()", None));
        ___qlistwidgetitem84 = self.code_snippet_list.item(84)
        ___qlistwidgetitem84.setText(QCoreApplication.translate("MainWindow", u"append()", None));
        ___qlistwidgetitem85 = self.code_snippet_list.item(85)
        ___qlistwidgetitem85.setText(QCoreApplication.translate("MainWindow", u"extend()", None));
        ___qlistwidgetitem86 = self.code_snippet_list.item(86)
        ___qlistwidgetitem86.setText(QCoreApplication.translate("MainWindow", u"insert()", None));
        ___qlistwidgetitem87 = self.code_snippet_list.item(87)
        ___qlistwidgetitem87.setText(QCoreApplication.translate("MainWindow", u"remove()", None));
        ___qlistwidgetitem88 = self.code_snippet_list.item(88)
        ___qlistwidgetitem88.setText(QCoreApplication.translate("MainWindow", u"seek()", None));
        ___qlistwidgetitem89 = self.code_snippet_list.item(89)
        ___qlistwidgetitem89.setText(QCoreApplication.translate("MainWindow", u"truncate()", None));
        ___qlistwidgetitem90 = self.code_snippet_list.item(90)
        ___qlistwidgetitem90.setText(QCoreApplication.translate("MainWindow", u"write()", None));
        ___qlistwidgetitem91 = self.code_snippet_list.item(91)
        ___qlistwidgetitem91.setText(QCoreApplication.translate("MainWindow", u"writelines()", None));
        ___qlistwidgetitem92 = self.code_snippet_list.item(92)
        ___qlistwidgetitem92.setText(QCoreApplication.translate("MainWindow", u"add()", None));
        ___qlistwidgetitem93 = self.code_snippet_list.item(93)
        ___qlistwidgetitem93.setText(QCoreApplication.translate("MainWindow", u"difference()", None));
        ___qlistwidgetitem94 = self.code_snippet_list.item(94)
        ___qlistwidgetitem94.setText(QCoreApplication.translate("MainWindow", u"difference_update()", None));
        ___qlistwidgetitem95 = self.code_snippet_list.item(95)
        ___qlistwidgetitem95.setText(QCoreApplication.translate("MainWindow", u"discard()", None));
        ___qlistwidgetitem96 = self.code_snippet_list.item(96)
        ___qlistwidgetitem96.setText(QCoreApplication.translate("MainWindow", u"intersection()", None));
        ___qlistwidgetitem97 = self.code_snippet_list.item(97)
        ___qlistwidgetitem97.setText(QCoreApplication.translate("MainWindow", u"intersection_update()", None));
        ___qlistwidgetitem98 = self.code_snippet_list.item(98)
        ___qlistwidgetitem98.setText(QCoreApplication.translate("MainWindow", u"isdisjoint()", None));
        ___qlistwidgetitem99 = self.code_snippet_list.item(99)
        ___qlistwidgetitem99.setText(QCoreApplication.translate("MainWindow", u"issubset()", None));
        ___qlistwidgetitem100 = self.code_snippet_list.item(100)
        ___qlistwidgetitem100.setText(QCoreApplication.translate("MainWindow", u"issuperset()", None));
        ___qlistwidgetitem101 = self.code_snippet_list.item(101)
        ___qlistwidgetitem101.setText(QCoreApplication.translate("MainWindow", u"symmetric_difference()", None));
        ___qlistwidgetitem102 = self.code_snippet_list.item(102)
        ___qlistwidgetitem102.setText(QCoreApplication.translate("MainWindow", u"symmetric_difference_update()", None));
        ___qlistwidgetitem103 = self.code_snippet_list.item(103)
        ___qlistwidgetitem103.setText(QCoreApplication.translate("MainWindow", u"union()", None));
        ___qlistwidgetitem104 = self.code_snippet_list.item(104)
        ___qlistwidgetitem104.setText(QCoreApplication.translate("MainWindow", u"update()", None));
        ___qlistwidgetitem105 = self.code_snippet_list.item(105)
        ___qlistwidgetitem105.setText(QCoreApplication.translate("MainWindow", u"center()", None));
        ___qlistwidgetitem106 = self.code_snippet_list.item(106)
        ___qlistwidgetitem106.setText(QCoreApplication.translate("MainWindow", u"endswith()", None));
        ___qlistwidgetitem107 = self.code_snippet_list.item(107)
        ___qlistwidgetitem107.setText(QCoreApplication.translate("MainWindow", u"expandtabs()", None));
        ___qlistwidgetitem108 = self.code_snippet_list.item(108)
        ___qlistwidgetitem108.setText(QCoreApplication.translate("MainWindow", u"find()", None));
        ___qlistwidgetitem109 = self.code_snippet_list.item(109)
        ___qlistwidgetitem109.setText(QCoreApplication.translate("MainWindow", u"join()", None));
        ___qlistwidgetitem110 = self.code_snippet_list.item(110)
        ___qlistwidgetitem110.setText(QCoreApplication.translate("MainWindow", u"ljust()", None));
        ___qlistwidgetitem111 = self.code_snippet_list.item(111)
        ___qlistwidgetitem111.setText(QCoreApplication.translate("MainWindow", u"maketrans()", None));
        ___qlistwidgetitem112 = self.code_snippet_list.item(112)
        ___qlistwidgetitem112.setText(QCoreApplication.translate("MainWindow", u"partition()", None));
        ___qlistwidgetitem113 = self.code_snippet_list.item(113)
        ___qlistwidgetitem113.setText(QCoreApplication.translate("MainWindow", u"replace()", None));
        ___qlistwidgetitem114 = self.code_snippet_list.item(114)
        ___qlistwidgetitem114.setText(QCoreApplication.translate("MainWindow", u"rfind()", None));
        ___qlistwidgetitem115 = self.code_snippet_list.item(115)
        ___qlistwidgetitem115.setText(QCoreApplication.translate("MainWindow", u"rindex()", None));
        ___qlistwidgetitem116 = self.code_snippet_list.item(116)
        ___qlistwidgetitem116.setText(QCoreApplication.translate("MainWindow", u"rjust()", None));
        ___qlistwidgetitem117 = self.code_snippet_list.item(117)
        ___qlistwidgetitem117.setText(QCoreApplication.translate("MainWindow", u"rpartition()", None));
        ___qlistwidgetitem118 = self.code_snippet_list.item(118)
        ___qlistwidgetitem118.setText(QCoreApplication.translate("MainWindow", u"startswith()", None));
        ___qlistwidgetitem119 = self.code_snippet_list.item(119)
        ___qlistwidgetitem119.setText(QCoreApplication.translate("MainWindow", u"zfill()", None));
        ___qlistwidgetitem120 = self.code_snippet_list.item(120)
        ___qlistwidgetitem120.setText(QCoreApplication.translate("MainWindow", u"CUSTOM SNIPPETS", None));
        self.code_snippet_list.setSortingEnabled(__sortingEnabled)

        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Specifications Of Selected Code Snippets:", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Code Snippets List", None))
        self.btn_create_code.setText(QCoreApplication.translate("MainWindow", u"Create Code Snippets", None))
        self.btn_add_custom.setText(QCoreApplication.translate("MainWindow", u"Add Custom Snippet", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Selected Code Snippets:", None))
        self.btn_remove_snip.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.plainTextEdit_11.setPlainText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Exe File:", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Source Code", None))
        self.btn_open_folder.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Edit Source Code", None))
        self.btn_clear_codes.setText(QCoreApplication.translate("MainWindow", u"Clear Source Codes", None))
        self.btn_go_scan.setText(QCoreApplication.translate("MainWindow", u"Scan Page", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"Ready", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Node List", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Run Order", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Parameter List", None))
        self.remove_order_btn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Topic List", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Service List", None))
        self.add_order_btn.setText(QCoreApplication.translate("MainWindow", u"Add to Run Order", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Selected Line & Fault", None))

        __sortingEnabled1 = self.listWidget_34.isSortingEnabled()
        self.listWidget_34.setSortingEnabled(False)
        ___qlistwidgetitem121 = self.listWidget_34.item(0)
        ___qlistwidgetitem121.setText(QCoreApplication.translate("MainWindow", u"ROS Initializing Node Mutation", None));
        ___qlistwidgetitem122 = self.listWidget_34.item(1)
        ___qlistwidgetitem122.setText(QCoreApplication.translate("MainWindow", u"ROS Pub-Sub Mutation", None));
        ___qlistwidgetitem123 = self.listWidget_34.item(2)
        ___qlistwidgetitem123.setText(QCoreApplication.translate("MainWindow", u"ROS Time Mutation", None));
        ___qlistwidgetitem124 = self.listWidget_34.item(3)
        ___qlistwidgetitem124.setText(QCoreApplication.translate("MainWindow", u"ROS Service Mutation", None));
        ___qlistwidgetitem125 = self.listWidget_34.item(4)
        ___qlistwidgetitem125.setText(QCoreApplication.translate("MainWindow", u"ROS Parameter Mutation", None));
        ___qlistwidgetitem126 = self.listWidget_34.item(5)
        ___qlistwidgetitem126.setText(QCoreApplication.translate("MainWindow", u"ROS Log Mutation", None));
        self.listWidget_34.setSortingEnabled(__sortingEnabled1)

        self.add_ros_btn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.mutate_ros_btn.setText(QCoreApplication.translate("MainWindow", u"Apply Mutation", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Found Lines for Mutation", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"Apply All Mutations", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Fault Library", None))
        self.remove_ros_btn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.rosrun_btn.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.scan_ros_btn.setText(QCoreApplication.translate("MainWindow", u"Scan Codes for Mutation", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"ROS Package Contents", None))
        self.label_81.setText("")
        self.ros_fiplan_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.ros_slct_fiplan.setText(QCoreApplication.translate("MainWindow", u"Select FI Plan", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Mutant Codes", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"FI Plan List", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Total Mutants:", None))
        self.remove_ros_mutant.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.ros_fiplan_remove.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.select_trgt_btn.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"File Path:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Launch File", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"File Name:", None))
        self.label_86.setText("")
        self.open_target_ros.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"File:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Single ROS File", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"FI Plan Name:", None))
        self.back_start_page.setText(QCoreApplication.translate("MainWindow", u"Start Page", None))
        self.go_execution.setText(QCoreApplication.translate("MainWindow", u"Execution Page", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Workload", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Ready To Scan", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Detected Parts", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Selected Code Snippets", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Source Codes", None))
        self.btn_scan_process.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.btn_go_fiplan.setText(QCoreApplication.translate("MainWindow", u"FI Plan Page", None))
        self.btn_back_code.setText(QCoreApplication.translate("MainWindow", u"Start Page", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Mutation List", None))
        self.btn_start_mutation.setText(QCoreApplication.translate("MainWindow", u"Start Mutation", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Selected Line", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Fault Library", None))

        __sortingEnabled2 = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem127 = self.listWidget_3.item(0)
        ___qlistwidgetitem127.setText(QCoreApplication.translate("MainWindow", u"OPERATORS", None));
        ___qlistwidgetitem128 = self.listWidget_3.item(1)
        ___qlistwidgetitem128.setText(QCoreApplication.translate("MainWindow", u"(AOM) Arithmetic Operator Missing", None));
        ___qlistwidgetitem129 = self.listWidget_3.item(2)
        ___qlistwidgetitem129.setText(QCoreApplication.translate("MainWindow", u"(AOW) Arithmetic Operator Wrong", None));
        ___qlistwidgetitem130 = self.listWidget_3.item(3)
        ___qlistwidgetitem130.setText(QCoreApplication.translate("MainWindow", u"(AOE) Arithmetic Operator Extraneous", None));
        ___qlistwidgetitem131 = self.listWidget_3.item(4)
        ___qlistwidgetitem131.setText(QCoreApplication.translate("MainWindow", u"(COM) Comparison Operator Missing", None));
        ___qlistwidgetitem132 = self.listWidget_3.item(5)
        ___qlistwidgetitem132.setText(QCoreApplication.translate("MainWindow", u"(COW) Comparison Operator Wrong", None));
        ___qlistwidgetitem133 = self.listWidget_3.item(6)
        ___qlistwidgetitem133.setText(QCoreApplication.translate("MainWindow", u"(COE) Comparison Operator Extraneous", None));
        ___qlistwidgetitem134 = self.listWidget_3.item(7)
        ___qlistwidgetitem134.setText(QCoreApplication.translate("MainWindow", u"(AOM) Assignment Operator Missing", None));
        ___qlistwidgetitem135 = self.listWidget_3.item(8)
        ___qlistwidgetitem135.setText(QCoreApplication.translate("MainWindow", u"(AOW) Assignment Operator Wrong", None));
        ___qlistwidgetitem136 = self.listWidget_3.item(9)
        ___qlistwidgetitem136.setText(QCoreApplication.translate("MainWindow", u"(AOE) Assignment Operator Extraneous", None));
        ___qlistwidgetitem137 = self.listWidget_3.item(10)
        ___qlistwidgetitem137.setText(QCoreApplication.translate("MainWindow", u"(LOM) Logical Operator Missing", None));
        ___qlistwidgetitem138 = self.listWidget_3.item(11)
        ___qlistwidgetitem138.setText(QCoreApplication.translate("MainWindow", u"(LOW) Logical Operator Wrong", None));
        ___qlistwidgetitem139 = self.listWidget_3.item(12)
        ___qlistwidgetitem139.setText(QCoreApplication.translate("MainWindow", u"(LOE) Logical Operator Extraneous", None));
        ___qlistwidgetitem140 = self.listWidget_3.item(13)
        ___qlistwidgetitem140.setText(QCoreApplication.translate("MainWindow", u"(MOM) Membership Operator Missing", None));
        ___qlistwidgetitem141 = self.listWidget_3.item(14)
        ___qlistwidgetitem141.setText(QCoreApplication.translate("MainWindow", u"(MOW) Membership Operator Wrong", None));
        ___qlistwidgetitem142 = self.listWidget_3.item(15)
        ___qlistwidgetitem142.setText(QCoreApplication.translate("MainWindow", u"(MOE) Membership Operator Extraneous", None));
        ___qlistwidgetitem143 = self.listWidget_3.item(16)
        ___qlistwidgetitem143.setText(QCoreApplication.translate("MainWindow", u"(IOM) Identity Operator Missing", None));
        ___qlistwidgetitem144 = self.listWidget_3.item(17)
        ___qlistwidgetitem144.setText(QCoreApplication.translate("MainWindow", u"(IOW) Identity  Operator Wrong", None));
        ___qlistwidgetitem145 = self.listWidget_3.item(18)
        ___qlistwidgetitem145.setText(QCoreApplication.translate("MainWindow", u"(IOE) Identity Operator Extraneous", None));
        ___qlistwidgetitem146 = self.listWidget_3.item(19)
        ___qlistwidgetitem146.setText(QCoreApplication.translate("MainWindow", u"STATEMENTS", None));
        ___qlistwidgetitem147 = self.listWidget_3.item(20)
        ___qlistwidgetitem147.setText(QCoreApplication.translate("MainWindow", u"(bM) break Missing", None));
        ___qlistwidgetitem148 = self.listWidget_3.item(21)
        ___qlistwidgetitem148.setText(QCoreApplication.translate("MainWindow", u"(bW) break Wrong", None));
        ___qlistwidgetitem149 = self.listWidget_3.item(22)
        ___qlistwidgetitem149.setText(QCoreApplication.translate("MainWindow", u"(bE) break Extraneous", None));
        ___qlistwidgetitem150 = self.listWidget_3.item(23)
        ___qlistwidgetitem150.setText(QCoreApplication.translate("MainWindow", u"(cM) continue Missing", None));
        ___qlistwidgetitem151 = self.listWidget_3.item(24)
        ___qlistwidgetitem151.setText(QCoreApplication.translate("MainWindow", u"(cW) continue Wrong", None));
        ___qlistwidgetitem152 = self.listWidget_3.item(25)
        ___qlistwidgetitem152.setText(QCoreApplication.translate("MainWindow", u"(cE) continue Extraneous", None));
        ___qlistwidgetitem153 = self.listWidget_3.item(26)
        ___qlistwidgetitem153.setText(QCoreApplication.translate("MainWindow", u"(FM) False Missing", None));
        ___qlistwidgetitem154 = self.listWidget_3.item(27)
        ___qlistwidgetitem154.setText(QCoreApplication.translate("MainWindow", u"(FW) False Wrong", None));
        ___qlistwidgetitem155 = self.listWidget_3.item(28)
        ___qlistwidgetitem155.setText(QCoreApplication.translate("MainWindow", u"(FE) False Extraneous", None));
        ___qlistwidgetitem156 = self.listWidget_3.item(29)
        ___qlistwidgetitem156.setText(QCoreApplication.translate("MainWindow", u"(pM) pass Missing", None));
        ___qlistwidgetitem157 = self.listWidget_3.item(30)
        ___qlistwidgetitem157.setText(QCoreApplication.translate("MainWindow", u"(pW) pass Wrong", None));
        ___qlistwidgetitem158 = self.listWidget_3.item(31)
        ___qlistwidgetitem158.setText(QCoreApplication.translate("MainWindow", u"(pE) pass Extraneous", None));
        ___qlistwidgetitem159 = self.listWidget_3.item(32)
        ___qlistwidgetitem159.setText(QCoreApplication.translate("MainWindow", u"(TM) True Missing", None));
        ___qlistwidgetitem160 = self.listWidget_3.item(33)
        ___qlistwidgetitem160.setText(QCoreApplication.translate("MainWindow", u"(TW) True Wrong", None));
        ___qlistwidgetitem161 = self.listWidget_3.item(34)
        ___qlistwidgetitem161.setText(QCoreApplication.translate("MainWindow", u"(TE) True Extraneous", None));
        ___qlistwidgetitem162 = self.listWidget_3.item(35)
        ___qlistwidgetitem162.setText(QCoreApplication.translate("MainWindow", u"(aM) assert Missing", None));
        ___qlistwidgetitem163 = self.listWidget_3.item(36)
        ___qlistwidgetitem163.setText(QCoreApplication.translate("MainWindow", u"(aW) assert Wrong", None));
        ___qlistwidgetitem164 = self.listWidget_3.item(37)
        ___qlistwidgetitem164.setText(QCoreApplication.translate("MainWindow", u"(aE) assert Extraneous", None));
        ___qlistwidgetitem165 = self.listWidget_3.item(38)
        ___qlistwidgetitem165.setText(QCoreApplication.translate("MainWindow", u"(dM) del Missing", None));
        ___qlistwidgetitem166 = self.listWidget_3.item(39)
        ___qlistwidgetitem166.setText(QCoreApplication.translate("MainWindow", u"(dW) del Wrong", None));
        ___qlistwidgetitem167 = self.listWidget_3.item(40)
        ___qlistwidgetitem167.setText(QCoreApplication.translate("MainWindow", u"(dE) del Extraneous", None));
        ___qlistwidgetitem168 = self.listWidget_3.item(41)
        ___qlistwidgetitem168.setText(QCoreApplication.translate("MainWindow", u"(iM) if Missing", None));
        ___qlistwidgetitem169 = self.listWidget_3.item(42)
        ___qlistwidgetitem169.setText(QCoreApplication.translate("MainWindow", u"(iW) if Wrong", None));
        ___qlistwidgetitem170 = self.listWidget_3.item(43)
        ___qlistwidgetitem170.setText(QCoreApplication.translate("MainWindow", u"(iE) if Extraneous", None));
        ___qlistwidgetitem171 = self.listWidget_3.item(44)
        ___qlistwidgetitem171.setText(QCoreApplication.translate("MainWindow", u"(elM) elif Missing", None));
        ___qlistwidgetitem172 = self.listWidget_3.item(45)
        ___qlistwidgetitem172.setText(QCoreApplication.translate("MainWindow", u"(elW) elif Wrong", None));
        ___qlistwidgetitem173 = self.listWidget_3.item(46)
        ___qlistwidgetitem173.setText(QCoreApplication.translate("MainWindow", u"(elE) elif Extraneous", None));
        ___qlistwidgetitem174 = self.listWidget_3.item(47)
        ___qlistwidgetitem174.setText(QCoreApplication.translate("MainWindow", u"(elsM) else Missing", None));
        ___qlistwidgetitem175 = self.listWidget_3.item(48)
        ___qlistwidgetitem175.setText(QCoreApplication.translate("MainWindow", u"(elsW) else Wrong", None));
        ___qlistwidgetitem176 = self.listWidget_3.item(49)
        ___qlistwidgetitem176.setText(QCoreApplication.translate("MainWindow", u"(elsE) else Extraneous", None));
        ___qlistwidgetitem177 = self.listWidget_3.item(50)
        ___qlistwidgetitem177.setText(QCoreApplication.translate("MainWindow", u"(tryM) try Missing", None));
        ___qlistwidgetitem178 = self.listWidget_3.item(51)
        ___qlistwidgetitem178.setText(QCoreApplication.translate("MainWindow", u"(tryW) try Wrong", None));
        ___qlistwidgetitem179 = self.listWidget_3.item(52)
        ___qlistwidgetitem179.setText(QCoreApplication.translate("MainWindow", u"(tryE) try Extraneous", None));
        ___qlistwidgetitem180 = self.listWidget_3.item(53)
        ___qlistwidgetitem180.setText(QCoreApplication.translate("MainWindow", u"(excM) except Missing", None));
        ___qlistwidgetitem181 = self.listWidget_3.item(54)
        ___qlistwidgetitem181.setText(QCoreApplication.translate("MainWindow", u"(excW) except Wrong", None));
        ___qlistwidgetitem182 = self.listWidget_3.item(55)
        ___qlistwidgetitem182.setText(QCoreApplication.translate("MainWindow", u"(excE) except Extraneous", None));
        ___qlistwidgetitem183 = self.listWidget_3.item(56)
        ___qlistwidgetitem183.setText(QCoreApplication.translate("MainWindow", u"(finM) finally Missing", None));
        ___qlistwidgetitem184 = self.listWidget_3.item(57)
        ___qlistwidgetitem184.setText(QCoreApplication.translate("MainWindow", u"(finW) finally Wrong", None));
        ___qlistwidgetitem185 = self.listWidget_3.item(58)
        ___qlistwidgetitem185.setText(QCoreApplication.translate("MainWindow", u"(finE) finally Extraneous", None));
        ___qlistwidgetitem186 = self.listWidget_3.item(59)
        ___qlistwidgetitem186.setText(QCoreApplication.translate("MainWindow", u"(forM) for Missing", None));
        ___qlistwidgetitem187 = self.listWidget_3.item(60)
        ___qlistwidgetitem187.setText(QCoreApplication.translate("MainWindow", u"(forW) for Wrong", None));
        ___qlistwidgetitem188 = self.listWidget_3.item(61)
        ___qlistwidgetitem188.setText(QCoreApplication.translate("MainWindow", u"(forE) for Extraneous", None));
        ___qlistwidgetitem189 = self.listWidget_3.item(62)
        ___qlistwidgetitem189.setText(QCoreApplication.translate("MainWindow", u"(gM) global Missing", None));
        ___qlistwidgetitem190 = self.listWidget_3.item(63)
        ___qlistwidgetitem190.setText(QCoreApplication.translate("MainWindow", u"(gW) global Wrong", None));
        ___qlistwidgetitem191 = self.listWidget_3.item(64)
        ___qlistwidgetitem191.setText(QCoreApplication.translate("MainWindow", u"(gE) global Extraneous", None));
        ___qlistwidgetitem192 = self.listWidget_3.item(65)
        ___qlistwidgetitem192.setText(QCoreApplication.translate("MainWindow", u"(laM) lambda Missing", None));
        ___qlistwidgetitem193 = self.listWidget_3.item(66)
        ___qlistwidgetitem193.setText(QCoreApplication.translate("MainWindow", u"(laW) lambda Wrong", None));
        ___qlistwidgetitem194 = self.listWidget_3.item(67)
        ___qlistwidgetitem194.setText(QCoreApplication.translate("MainWindow", u"(laE) lambda Extraneous", None));
        ___qlistwidgetitem195 = self.listWidget_3.item(68)
        ___qlistwidgetitem195.setText(QCoreApplication.translate("MainWindow", u"(NoM) None Missing", None));
        ___qlistwidgetitem196 = self.listWidget_3.item(69)
        ___qlistwidgetitem196.setText(QCoreApplication.translate("MainWindow", u"(NoW) None Wrong", None));
        ___qlistwidgetitem197 = self.listWidget_3.item(70)
        ___qlistwidgetitem197.setText(QCoreApplication.translate("MainWindow", u"(NoE) None Extraneous", None));
        ___qlistwidgetitem198 = self.listWidget_3.item(71)
        ___qlistwidgetitem198.setText(QCoreApplication.translate("MainWindow", u"(nonM) nonlocal Missing", None));
        ___qlistwidgetitem199 = self.listWidget_3.item(72)
        ___qlistwidgetitem199.setText(QCoreApplication.translate("MainWindow", u"(nonW) nonlocal Wrong", None));
        ___qlistwidgetitem200 = self.listWidget_3.item(73)
        ___qlistwidgetitem200.setText(QCoreApplication.translate("MainWindow", u"(nonE) nonlocal Extraneous", None));
        ___qlistwidgetitem201 = self.listWidget_3.item(74)
        ___qlistwidgetitem201.setText(QCoreApplication.translate("MainWindow", u"(raM) raise Missing", None));
        ___qlistwidgetitem202 = self.listWidget_3.item(75)
        ___qlistwidgetitem202.setText(QCoreApplication.translate("MainWindow", u"(raW) raise Wrong", None));
        ___qlistwidgetitem203 = self.listWidget_3.item(76)
        ___qlistwidgetitem203.setText(QCoreApplication.translate("MainWindow", u"(raE) raise Extraneous", None));
        ___qlistwidgetitem204 = self.listWidget_3.item(77)
        ___qlistwidgetitem204.setText(QCoreApplication.translate("MainWindow", u"(retM) return Missing", None));
        ___qlistwidgetitem205 = self.listWidget_3.item(78)
        ___qlistwidgetitem205.setText(QCoreApplication.translate("MainWindow", u"(retW) return Wrong", None));
        ___qlistwidgetitem206 = self.listWidget_3.item(79)
        ___qlistwidgetitem206.setText(QCoreApplication.translate("MainWindow", u"(retE) return Extraneous", None));
        ___qlistwidgetitem207 = self.listWidget_3.item(80)
        ___qlistwidgetitem207.setText(QCoreApplication.translate("MainWindow", u"(whM) while Missing", None));
        ___qlistwidgetitem208 = self.listWidget_3.item(81)
        ___qlistwidgetitem208.setText(QCoreApplication.translate("MainWindow", u"(whW) while Wrong", None));
        ___qlistwidgetitem209 = self.listWidget_3.item(82)
        ___qlistwidgetitem209.setText(QCoreApplication.translate("MainWindow", u"(whE) while Extraneous", None));
        ___qlistwidgetitem210 = self.listWidget_3.item(83)
        ___qlistwidgetitem210.setText(QCoreApplication.translate("MainWindow", u"(wiM) with Missing", None));
        ___qlistwidgetitem211 = self.listWidget_3.item(84)
        ___qlistwidgetitem211.setText(QCoreApplication.translate("MainWindow", u"(wiW) with Wrong", None));
        ___qlistwidgetitem212 = self.listWidget_3.item(85)
        ___qlistwidgetitem212.setText(QCoreApplication.translate("MainWindow", u"(wiE) with Extraneous", None));
        ___qlistwidgetitem213 = self.listWidget_3.item(86)
        ___qlistwidgetitem213.setText(QCoreApplication.translate("MainWindow", u"(yiM) yield Missing", None));
        ___qlistwidgetitem214 = self.listWidget_3.item(87)
        ___qlistwidgetitem214.setText(QCoreApplication.translate("MainWindow", u"(yiW) yield Wrong", None));
        ___qlistwidgetitem215 = self.listWidget_3.item(88)
        ___qlistwidgetitem215.setText(QCoreApplication.translate("MainWindow", u"(yiE) yield Extraneous", None));
        ___qlistwidgetitem216 = self.listWidget_3.item(89)
        ___qlistwidgetitem216.setText(QCoreApplication.translate("MainWindow", u"FUNCTIONS", None));
        ___qlistwidgetitem217 = self.listWidget_3.item(90)
        ___qlistwidgetitem217.setText(QCoreApplication.translate("MainWindow", u"abs()", None));
        ___qlistwidgetitem218 = self.listWidget_3.item(91)
        ___qlistwidgetitem218.setText(QCoreApplication.translate("MainWindow", u"all()", None));
        ___qlistwidgetitem219 = self.listWidget_3.item(92)
        ___qlistwidgetitem219.setText(QCoreApplication.translate("MainWindow", u"ascii()", None));
        ___qlistwidgetitem220 = self.listWidget_3.item(93)
        ___qlistwidgetitem220.setText(QCoreApplication.translate("MainWindow", u"bin()", None));
        ___qlistwidgetitem221 = self.listWidget_3.item(94)
        ___qlistwidgetitem221.setText(QCoreApplication.translate("MainWindow", u"bool()", None));
        ___qlistwidgetitem222 = self.listWidget_3.item(95)
        ___qlistwidgetitem222.setText(QCoreApplication.translate("MainWindow", u"bytearray()", None));
        ___qlistwidgetitem223 = self.listWidget_3.item(96)
        ___qlistwidgetitem223.setText(QCoreApplication.translate("MainWindow", u"bytes()", None));
        ___qlistwidgetitem224 = self.listWidget_3.item(97)
        ___qlistwidgetitem224.setText(QCoreApplication.translate("MainWindow", u"chr()", None));
        ___qlistwidgetitem225 = self.listWidget_3.item(98)
        ___qlistwidgetitem225.setText(QCoreApplication.translate("MainWindow", u"delattr()", None));
        ___qlistwidgetitem226 = self.listWidget_3.item(99)
        ___qlistwidgetitem226.setText(QCoreApplication.translate("MainWindow", u"dict()", None));
        ___qlistwidgetitem227 = self.listWidget_3.item(100)
        ___qlistwidgetitem227.setText(QCoreApplication.translate("MainWindow", u"divmod()", None));
        ___qlistwidgetitem228 = self.listWidget_3.item(101)
        ___qlistwidgetitem228.setText(QCoreApplication.translate("MainWindow", u"enumerate()", None));
        ___qlistwidgetitem229 = self.listWidget_3.item(102)
        ___qlistwidgetitem229.setText(QCoreApplication.translate("MainWindow", u"eval()", None));
        ___qlistwidgetitem230 = self.listWidget_3.item(103)
        ___qlistwidgetitem230.setText(QCoreApplication.translate("MainWindow", u"exec()", None));
        ___qlistwidgetitem231 = self.listWidget_3.item(104)
        ___qlistwidgetitem231.setText(QCoreApplication.translate("MainWindow", u"filter()", None));
        ___qlistwidgetitem232 = self.listWidget_3.item(105)
        ___qlistwidgetitem232.setText(QCoreApplication.translate("MainWindow", u"float()", None));
        ___qlistwidgetitem233 = self.listWidget_3.item(106)
        ___qlistwidgetitem233.setText(QCoreApplication.translate("MainWindow", u"frozenset()", None));
        ___qlistwidgetitem234 = self.listWidget_3.item(107)
        ___qlistwidgetitem234.setText(QCoreApplication.translate("MainWindow", u"getattr()", None));
        ___qlistwidgetitem235 = self.listWidget_3.item(108)
        ___qlistwidgetitem235.setText(QCoreApplication.translate("MainWindow", u"hasattr()", None));
        ___qlistwidgetitem236 = self.listWidget_3.item(109)
        ___qlistwidgetitem236.setText(QCoreApplication.translate("MainWindow", u"hash()", None));
        ___qlistwidgetitem237 = self.listWidget_3.item(110)
        ___qlistwidgetitem237.setText(QCoreApplication.translate("MainWindow", u"help()", None));
        ___qlistwidgetitem238 = self.listWidget_3.item(111)
        ___qlistwidgetitem238.setText(QCoreApplication.translate("MainWindow", u"hex()", None));
        ___qlistwidgetitem239 = self.listWidget_3.item(112)
        ___qlistwidgetitem239.setText(QCoreApplication.translate("MainWindow", u"id()", None));
        ___qlistwidgetitem240 = self.listWidget_3.item(113)
        ___qlistwidgetitem240.setText(QCoreApplication.translate("MainWindow", u"int()", None));
        ___qlistwidgetitem241 = self.listWidget_3.item(114)
        ___qlistwidgetitem241.setText(QCoreApplication.translate("MainWindow", u"isinstance()", None));
        ___qlistwidgetitem242 = self.listWidget_3.item(115)
        ___qlistwidgetitem242.setText(QCoreApplication.translate("MainWindow", u"iter()", None));
        ___qlistwidgetitem243 = self.listWidget_3.item(116)
        ___qlistwidgetitem243.setText(QCoreApplication.translate("MainWindow", u"len()", None));
        ___qlistwidgetitem244 = self.listWidget_3.item(117)
        ___qlistwidgetitem244.setText(QCoreApplication.translate("MainWindow", u"list()", None));
        ___qlistwidgetitem245 = self.listWidget_3.item(118)
        ___qlistwidgetitem245.setText(QCoreApplication.translate("MainWindow", u"map()", None));
        ___qlistwidgetitem246 = self.listWidget_3.item(119)
        ___qlistwidgetitem246.setText(QCoreApplication.translate("MainWindow", u"max()", None));
        ___qlistwidgetitem247 = self.listWidget_3.item(120)
        ___qlistwidgetitem247.setText(QCoreApplication.translate("MainWindow", u"memoryview()", None));
        ___qlistwidgetitem248 = self.listWidget_3.item(121)
        ___qlistwidgetitem248.setText(QCoreApplication.translate("MainWindow", u"min()", None));
        ___qlistwidgetitem249 = self.listWidget_3.item(122)
        ___qlistwidgetitem249.setText(QCoreApplication.translate("MainWindow", u"next()", None));
        ___qlistwidgetitem250 = self.listWidget_3.item(123)
        ___qlistwidgetitem250.setText(QCoreApplication.translate("MainWindow", u"oct()", None));
        ___qlistwidgetitem251 = self.listWidget_3.item(124)
        ___qlistwidgetitem251.setText(QCoreApplication.translate("MainWindow", u"open()", None));
        ___qlistwidgetitem252 = self.listWidget_3.item(125)
        ___qlistwidgetitem252.setText(QCoreApplication.translate("MainWindow", u"ord()", None));
        ___qlistwidgetitem253 = self.listWidget_3.item(126)
        ___qlistwidgetitem253.setText(QCoreApplication.translate("MainWindow", u"pow()", None));
        ___qlistwidgetitem254 = self.listWidget_3.item(127)
        ___qlistwidgetitem254.setText(QCoreApplication.translate("MainWindow", u"property()", None));
        ___qlistwidgetitem255 = self.listWidget_3.item(128)
        ___qlistwidgetitem255.setText(QCoreApplication.translate("MainWindow", u"range()", None));
        ___qlistwidgetitem256 = self.listWidget_3.item(129)
        ___qlistwidgetitem256.setText(QCoreApplication.translate("MainWindow", u"reversed()", None));
        ___qlistwidgetitem257 = self.listWidget_3.item(130)
        ___qlistwidgetitem257.setText(QCoreApplication.translate("MainWindow", u"round()", None));
        ___qlistwidgetitem258 = self.listWidget_3.item(131)
        ___qlistwidgetitem258.setText(QCoreApplication.translate("MainWindow", u"set()", None));
        ___qlistwidgetitem259 = self.listWidget_3.item(132)
        ___qlistwidgetitem259.setText(QCoreApplication.translate("MainWindow", u"setattr()", None));
        ___qlistwidgetitem260 = self.listWidget_3.item(133)
        ___qlistwidgetitem260.setText(QCoreApplication.translate("MainWindow", u"slice()", None));
        ___qlistwidgetitem261 = self.listWidget_3.item(134)
        ___qlistwidgetitem261.setText(QCoreApplication.translate("MainWindow", u"sorted()", None));
        ___qlistwidgetitem262 = self.listWidget_3.item(135)
        ___qlistwidgetitem262.setText(QCoreApplication.translate("MainWindow", u"str()", None));
        ___qlistwidgetitem263 = self.listWidget_3.item(136)
        ___qlistwidgetitem263.setText(QCoreApplication.translate("MainWindow", u"sum()", None));
        ___qlistwidgetitem264 = self.listWidget_3.item(137)
        ___qlistwidgetitem264.setText(QCoreApplication.translate("MainWindow", u"tuple()", None));
        ___qlistwidgetitem265 = self.listWidget_3.item(138)
        ___qlistwidgetitem265.setText(QCoreApplication.translate("MainWindow", u"type()", None));
        ___qlistwidgetitem266 = self.listWidget_3.item(139)
        ___qlistwidgetitem266.setText(QCoreApplication.translate("MainWindow", u"vars()", None));
        ___qlistwidgetitem267 = self.listWidget_3.item(140)
        ___qlistwidgetitem267.setText(QCoreApplication.translate("MainWindow", u"zip()", None));
        ___qlistwidgetitem268 = self.listWidget_3.item(141)
        ___qlistwidgetitem268.setText(QCoreApplication.translate("MainWindow", u"count()", None));
        ___qlistwidgetitem269 = self.listWidget_3.item(142)
        ___qlistwidgetitem269.setText(QCoreApplication.translate("MainWindow", u"index()", None));
        ___qlistwidgetitem270 = self.listWidget_3.item(143)
        ___qlistwidgetitem270.setText(QCoreApplication.translate("MainWindow", u"fromkeys()", None));
        ___qlistwidgetitem271 = self.listWidget_3.item(144)
        ___qlistwidgetitem271.setText(QCoreApplication.translate("MainWindow", u"get()", None));
        ___qlistwidgetitem272 = self.listWidget_3.item(145)
        ___qlistwidgetitem272.setText(QCoreApplication.translate("MainWindow", u"update()", None));
        ___qlistwidgetitem273 = self.listWidget_3.item(146)
        ___qlistwidgetitem273.setText(QCoreApplication.translate("MainWindow", u"append()", None));
        ___qlistwidgetitem274 = self.listWidget_3.item(147)
        ___qlistwidgetitem274.setText(QCoreApplication.translate("MainWindow", u"extend()", None));
        ___qlistwidgetitem275 = self.listWidget_3.item(148)
        ___qlistwidgetitem275.setText(QCoreApplication.translate("MainWindow", u"insert()", None));
        ___qlistwidgetitem276 = self.listWidget_3.item(149)
        ___qlistwidgetitem276.setText(QCoreApplication.translate("MainWindow", u"remove()", None));
        ___qlistwidgetitem277 = self.listWidget_3.item(150)
        ___qlistwidgetitem277.setText(QCoreApplication.translate("MainWindow", u"seek()", None));
        ___qlistwidgetitem278 = self.listWidget_3.item(151)
        ___qlistwidgetitem278.setText(QCoreApplication.translate("MainWindow", u"truncate()", None));
        ___qlistwidgetitem279 = self.listWidget_3.item(152)
        ___qlistwidgetitem279.setText(QCoreApplication.translate("MainWindow", u"write()", None));
        ___qlistwidgetitem280 = self.listWidget_3.item(153)
        ___qlistwidgetitem280.setText(QCoreApplication.translate("MainWindow", u"writelines()", None));
        ___qlistwidgetitem281 = self.listWidget_3.item(154)
        ___qlistwidgetitem281.setText(QCoreApplication.translate("MainWindow", u"add()", None));
        ___qlistwidgetitem282 = self.listWidget_3.item(155)
        ___qlistwidgetitem282.setText(QCoreApplication.translate("MainWindow", u"difference()", None));
        ___qlistwidgetitem283 = self.listWidget_3.item(156)
        ___qlistwidgetitem283.setText(QCoreApplication.translate("MainWindow", u"difference_update()", None));
        ___qlistwidgetitem284 = self.listWidget_3.item(157)
        ___qlistwidgetitem284.setText(QCoreApplication.translate("MainWindow", u"discard()", None));
        ___qlistwidgetitem285 = self.listWidget_3.item(158)
        ___qlistwidgetitem285.setText(QCoreApplication.translate("MainWindow", u"intersection()", None));
        ___qlistwidgetitem286 = self.listWidget_3.item(159)
        ___qlistwidgetitem286.setText(QCoreApplication.translate("MainWindow", u"intersection_update()", None));
        ___qlistwidgetitem287 = self.listWidget_3.item(160)
        ___qlistwidgetitem287.setText(QCoreApplication.translate("MainWindow", u"isdisjoint()", None));
        ___qlistwidgetitem288 = self.listWidget_3.item(161)
        ___qlistwidgetitem288.setText(QCoreApplication.translate("MainWindow", u"issubset()", None));
        ___qlistwidgetitem289 = self.listWidget_3.item(162)
        ___qlistwidgetitem289.setText(QCoreApplication.translate("MainWindow", u"issuperset()", None));
        ___qlistwidgetitem290 = self.listWidget_3.item(163)
        ___qlistwidgetitem290.setText(QCoreApplication.translate("MainWindow", u"symetric_difference()", None));
        ___qlistwidgetitem291 = self.listWidget_3.item(164)
        ___qlistwidgetitem291.setText(QCoreApplication.translate("MainWindow", u"symetric_difference_update()", None));
        ___qlistwidgetitem292 = self.listWidget_3.item(165)
        ___qlistwidgetitem292.setText(QCoreApplication.translate("MainWindow", u"union()", None));
        ___qlistwidgetitem293 = self.listWidget_3.item(166)
        ___qlistwidgetitem293.setText(QCoreApplication.translate("MainWindow", u"update()", None));
        ___qlistwidgetitem294 = self.listWidget_3.item(167)
        ___qlistwidgetitem294.setText(QCoreApplication.translate("MainWindow", u"center()", None));
        ___qlistwidgetitem295 = self.listWidget_3.item(168)
        ___qlistwidgetitem295.setText(QCoreApplication.translate("MainWindow", u"endswith()", None));
        ___qlistwidgetitem296 = self.listWidget_3.item(169)
        ___qlistwidgetitem296.setText(QCoreApplication.translate("MainWindow", u"expandtabs()", None));
        ___qlistwidgetitem297 = self.listWidget_3.item(170)
        ___qlistwidgetitem297.setText(QCoreApplication.translate("MainWindow", u"find()", None));
        ___qlistwidgetitem298 = self.listWidget_3.item(171)
        ___qlistwidgetitem298.setText(QCoreApplication.translate("MainWindow", u"index()", None));
        ___qlistwidgetitem299 = self.listWidget_3.item(172)
        ___qlistwidgetitem299.setText(QCoreApplication.translate("MainWindow", u"join()", None));
        ___qlistwidgetitem300 = self.listWidget_3.item(173)
        ___qlistwidgetitem300.setText(QCoreApplication.translate("MainWindow", u"ljust()", None));
        ___qlistwidgetitem301 = self.listWidget_3.item(174)
        ___qlistwidgetitem301.setText(QCoreApplication.translate("MainWindow", u"maketrans()", None));
        ___qlistwidgetitem302 = self.listWidget_3.item(175)
        ___qlistwidgetitem302.setText(QCoreApplication.translate("MainWindow", u"partition()", None));
        ___qlistwidgetitem303 = self.listWidget_3.item(176)
        ___qlistwidgetitem303.setText(QCoreApplication.translate("MainWindow", u"replace()", None));
        ___qlistwidgetitem304 = self.listWidget_3.item(177)
        ___qlistwidgetitem304.setText(QCoreApplication.translate("MainWindow", u"rfind()", None));
        ___qlistwidgetitem305 = self.listWidget_3.item(178)
        ___qlistwidgetitem305.setText(QCoreApplication.translate("MainWindow", u"rindex()", None));
        ___qlistwidgetitem306 = self.listWidget_3.item(179)
        ___qlistwidgetitem306.setText(QCoreApplication.translate("MainWindow", u"rjust()", None));
        ___qlistwidgetitem307 = self.listWidget_3.item(180)
        ___qlistwidgetitem307.setText(QCoreApplication.translate("MainWindow", u"rpartition()", None));
        ___qlistwidgetitem308 = self.listWidget_3.item(181)
        ___qlistwidgetitem308.setText(QCoreApplication.translate("MainWindow", u"startswith()", None));
        ___qlistwidgetitem309 = self.listWidget_3.item(182)
        ___qlistwidgetitem309.setText(QCoreApplication.translate("MainWindow", u"zfill()", None));
        ___qlistwidgetitem310 = self.listWidget_3.item(183)
        ___qlistwidgetitem310.setText(QCoreApplication.translate("MainWindow", u"CREATED FAULTS", None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled2)

        self.btn_select_fault.setText(QCoreApplication.translate("MainWindow", u"Select Fault", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Apply Mutation for All Possible Line", None))
#if QT_CONFIG(tooltip)
        self.btn_save_fiplan.setToolTip(QCoreApplication.translate("MainWindow", u"Save Button", None))
#endif // QT_CONFIG(tooltip)
        self.btn_save_fiplan.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Remove Mutant Code Line", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"FI Plan Name:", None))
        self.btn_slct_fiplan.setText(QCoreApplication.translate("MainWindow", u"Add FI Plan", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Total Mutants:", None))
        self.label_17.setText("")
        self.btn_remove_fiplan.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"FI Plan List", None))
        self.btn_create_custom.setText(QCoreApplication.translate("MainWindow", u"Create Custom Fault", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Selected Line & Fault", None))
        self.btn_remove_fault.setText(QCoreApplication.translate("MainWindow", u"Remove L\u0130ne Fault", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Fault Settings", None))
        self.btn_random_fault.setText(QCoreApplication.translate("MainWindow", u"Use Random Fault", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Possible Lines", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Fault Information", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Scan Page", None))
        self.btn_go_exe.setText(QCoreApplication.translate("MainWindow", u"Execution Page", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Mutant Files", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"FI Plan List", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Execution Settings", None))
        self.btn_select_metrics.setText(QCoreApplication.translate("MainWindow", u"Select Metrics", None))

        __sortingEnabled3 = self.listWidget_23.isSortingEnabled()
        self.listWidget_23.setSortingEnabled(False)
        ___qlistwidgetitem311 = self.listWidget_23.item(0)
        ___qlistwidgetitem311.setText(QCoreApplication.translate("MainWindow", u"Detected", None));
        ___qlistwidgetitem312 = self.listWidget_23.item(1)
        ___qlistwidgetitem312.setText(QCoreApplication.translate("MainWindow", u"Undetected", None));
        ___qlistwidgetitem313 = self.listWidget_23.item(2)
        ___qlistwidgetitem313.setText(QCoreApplication.translate("MainWindow", u"Covered", None));
        ___qlistwidgetitem314 = self.listWidget_23.item(3)
        ___qlistwidgetitem314.setText(QCoreApplication.translate("MainWindow", u"Valid", None));
        ___qlistwidgetitem315 = self.listWidget_23.item(4)
        ___qlistwidgetitem315.setText(QCoreApplication.translate("MainWindow", u"Killed", None));
        ___qlistwidgetitem316 = self.listWidget_23.item(5)
        ___qlistwidgetitem316.setText(QCoreApplication.translate("MainWindow", u"Survived", None));
        ___qlistwidgetitem317 = self.listWidget_23.item(6)
        ___qlistwidgetitem317.setText(QCoreApplication.translate("MainWindow", u"No Coverage", None));
        ___qlistwidgetitem318 = self.listWidget_23.item(7)
        ___qlistwidgetitem318.setText(QCoreApplication.translate("MainWindow", u"Timeout", None));
        ___qlistwidgetitem319 = self.listWidget_23.item(8)
        ___qlistwidgetitem319.setText(QCoreApplication.translate("MainWindow", u"Runtime Error", None));
        ___qlistwidgetitem320 = self.listWidget_23.item(9)
        ___qlistwidgetitem320.setText(QCoreApplication.translate("MainWindow", u"Compile Error", None));
        ___qlistwidgetitem321 = self.listWidget_23.item(10)
        ___qlistwidgetitem321.setText(QCoreApplication.translate("MainWindow", u"Ignored", None));
        self.listWidget_23.setSortingEnabled(__sortingEnabled3)

        self.btn_export_fiplan.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.btn_remove_fi.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Information of Metric & State", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Metrics and States", None))
        self.btn_remove_exe.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Image Name:", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Select Location:", None))
        self.plainTextEdit_25.setPlainText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Containers:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Terminals:", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Selected Metrics:", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Time Limit:", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Select the Location of Mutant Codes", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Selected FI Plan:", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Target Location:", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Default Settings:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Use Default Settings", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Terminal:", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Active Containers", None))
        self.btn_show_con.setText(QCoreApplication.translate("MainWindow", u"Show All Active Containers", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"All Images", None))
        self.btn_new_exe.setText(QCoreApplication.translate("MainWindow", u"New Execution Plan", None))
        self.btn_kill_containers.setText(QCoreApplication.translate("MainWindow", u"Kill Containers", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_create_container.setText(QCoreApplication.translate("MainWindow", u"Create Container", None))
        self.btn_apply_docker.setText(QCoreApplication.translate("MainWindow", u"Apply Faults on Docker", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"Use Docker for Execution", None))
        self.btn_start_exe.setText(QCoreApplication.translate("MainWindow", u"Start Execution", None))
        self.btn_create_mutants.setText(QCoreApplication.translate("MainWindow", u"Create Mutants", None))
        self.btn_show_di.setText(QCoreApplication.translate("MainWindow", u"Show All Docker Images", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Image Version:", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Delete / Keep:", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Delete Mutants", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Execution Plan List", None))
        self.btn_go_monitoring.setText(QCoreApplication.translate("MainWindow", u"Monitoring Page", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"FI Plan Page", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Mutation Score", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Mutant Lists:", None))
        self.btn_create_report.setText(QCoreApplication.translate("MainWindow", u"Create Report", None))
        self.btn_new_one.setText(QCoreApplication.translate("MainWindow", u"Start The New One", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"V&V Report", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Metrics:", None))
        self.bar_chart.setText(QCoreApplication.translate("MainWindow", u"Bar Chart", None))
        self.pie_chart.setText(QCoreApplication.translate("MainWindow", u"Pie Chart", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Killed Mutants Output:", None))
        self.label_47.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Mutants & Faults:", None))
        self.customFault.setStyleSheet("")
        self.btn_create_fault.setText(QCoreApplication.translate("MainWindow", u"Create Fault", None))
        self.btn_delete_fault.setText(QCoreApplication.translate("MainWindow", u"Delete Fault", None))
        self.plainTextEdit_39.setPlainText(QCoreApplication.translate("MainWindow", u"\"fault\":{\n"
"            \"Fault_Name\": \"(AOW) Arithmetic Operator Wrong\",\n"
"            \"Target_to_Change\": \"\\\\+,\\\\-,\\\\*,\\\\/,[%]{1},[**]{2},[\\//]{2}\",\n"
"            \"Changed\":\"+,-,*,/,%,**,//\",\n"
"            \"Explanation\":\"Arithmetic Operators Wrong\\nOriginal Code: x + y\\nMutated Code: x - y\"\n"
"            }", None))
        self.btn_remove_createdFault.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Created Fault List", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Fault Name:", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Target to Change:", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Created Fault", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"NOT SAVED!", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u".json", None))
        self.btn_back_fi.setText(QCoreApplication.translate("MainWindow", u"Back To FI Plan Page", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Create Custom Fault", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Explanation:", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Fault Example", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"File Name:", None))
        self.btn_save_fault.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Changed:", None))
        self.cWorkload.setStyleSheet("")
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"If you just want to change workoad's content, use the section below!", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Workload Content:", None))
        self.plainTextEdit.setPlainText("")
        self.btn_workload_save.setText(QCoreApplication.translate("MainWindow", u"Change Workload", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Create or Change Workload", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Workload D\u0130rectory:", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"Applied All Changes", None))
        self.btn_changeDir.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Changed Workplan Name:", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Task Details", None))
        self.btn_take_tasks.setText(QCoreApplication.translate("MainWindow", u"Download Tasks", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Workload Name:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Selected Tasks:", None))
        self.btn_select_task.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.btn_save_task.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_remove_task.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"NOT SAVE!", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"All Tasks:", None))
        self.btn_back_start.setText(QCoreApplication.translate("MainWindow", u"Back To Start Step", None))
        self.cSnippets.setStyleSheet("")
        self.back_snip.setText(QCoreApplication.translate("MainWindow", u"Back To Code Snippets Step", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Created Code Snipet", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Example Code Snippet", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"File Name:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Your Code Snippet", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Use The Created Code Snippet", None))
        self.label_60.setText("")
        self.btn_save_snip.setText(QCoreApplication.translate("MainWindow", u"Save Code Snippet", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Title:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Process:", None))
        self.btn_delete_snip.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btn_create_snip.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Snippet Name:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Regex Code:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Batch size", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Dropout rate", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Epoch", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Learning rate", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"MUTATE", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Process</p></body></html>", None))
        self.dnn_parameter.setItemText(0, QCoreApplication.translate("MainWindow", u"for", None))
        self.dnn_parameter.setItemText(1, QCoreApplication.translate("MainWindow", u"if", None))
        self.dnn_parameter.setItemText(2, QCoreApplication.translate("MainWindow", u"epoch", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DNN MUTATOR", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mutants &amp; Faults</p></body></html>", None))
        self.pushButton_dnn_mutate.setText(QCoreApplication.translate("MainWindow", u"Mutate", None))

        __sortingEnabled4 = self.listWidget_mutate_list.isSortingEnabled()
        self.listWidget_mutate_list.setSortingEnabled(False)
        ___qlistwidgetitem322 = self.listWidget_mutate_list.item(0)
        ___qlistwidgetitem322.setText(QCoreApplication.translate("MainWindow", u"epochs", None));
        ___qlistwidgetitem323 = self.listWidget_mutate_list.item(1)
        ___qlistwidgetitem323.setText(QCoreApplication.translate("MainWindow", u"ConvLSTM1D", None));
        ___qlistwidgetitem324 = self.listWidget_mutate_list.item(2)
        ___qlistwidgetitem324.setText(QCoreApplication.translate("MainWindow", u"ConvLSTM2D", None));
        ___qlistwidgetitem325 = self.listWidget_mutate_list.item(3)
        ___qlistwidgetitem325.setText(QCoreApplication.translate("MainWindow", u"ConvLSTM3D", None));
        ___qlistwidgetitem326 = self.listWidget_mutate_list.item(4)
        ___qlistwidgetitem326.setText(QCoreApplication.translate("MainWindow", u"Convolution1D", None));
        ___qlistwidgetitem327 = self.listWidget_mutate_list.item(5)
        ___qlistwidgetitem327.setText(QCoreApplication.translate("MainWindow", u"Convolution1DTranspose", None));
        ___qlistwidgetitem328 = self.listWidget_mutate_list.item(6)
        ___qlistwidgetitem328.setText(QCoreApplication.translate("MainWindow", u"Convolution2D", None));
        ___qlistwidgetitem329 = self.listWidget_mutate_list.item(7)
        ___qlistwidgetitem329.setText(QCoreApplication.translate("MainWindow", u"Convolution2DTranspose", None));
        ___qlistwidgetitem330 = self.listWidget_mutate_list.item(8)
        ___qlistwidgetitem330.setText(QCoreApplication.translate("MainWindow", u"Convolution3D", None));
        ___qlistwidgetitem331 = self.listWidget_mutate_list.item(9)
        ___qlistwidgetitem331.setText(QCoreApplication.translate("MainWindow", u"Convolution3DTranspose", None));
        ___qlistwidgetitem332 = self.listWidget_mutate_list.item(10)
        ___qlistwidgetitem332.setText(QCoreApplication.translate("MainWindow", u"Cropping1D", None));
        ___qlistwidgetitem333 = self.listWidget_mutate_list.item(11)
        ___qlistwidgetitem333.setText(QCoreApplication.translate("MainWindow", u"Cropping2D", None));
        ___qlistwidgetitem334 = self.listWidget_mutate_list.item(12)
        ___qlistwidgetitem334.setText(QCoreApplication.translate("MainWindow", u"Cropping3D", None));
        ___qlistwidgetitem335 = self.listWidget_mutate_list.item(13)
        ___qlistwidgetitem335.setText(QCoreApplication.translate("MainWindow", u"SpectralNormalization", None));
        ___qlistwidgetitem336 = self.listWidget_mutate_list.item(14)
        ___qlistwidgetitem336.setText(QCoreApplication.translate("MainWindow", u"StackedRNNCells", None));
        ___qlistwidgetitem337 = self.listWidget_mutate_list.item(15)
        ___qlistwidgetitem337.setText(QCoreApplication.translate("MainWindow", u"StringLookup", None));
        ___qlistwidgetitem338 = self.listWidget_mutate_list.item(16)
        ___qlistwidgetitem338.setText(QCoreApplication.translate("MainWindow", u"Subtract", None));
        ___qlistwidgetitem339 = self.listWidget_mutate_list.item(17)
        ___qlistwidgetitem339.setText(QCoreApplication.translate("MainWindow", u"TextVectorization", None));
        ___qlistwidgetitem340 = self.listWidget_mutate_list.item(18)
        ___qlistwidgetitem340.setText(QCoreApplication.translate("MainWindow", u"ThresholdedReLU", None));
        ___qlistwidgetitem341 = self.listWidget_mutate_list.item(19)
        ___qlistwidgetitem341.setText(QCoreApplication.translate("MainWindow", u"TimeDistributed", None));
        ___qlistwidgetitem342 = self.listWidget_mutate_list.item(20)
        ___qlistwidgetitem342.setText(QCoreApplication.translate("MainWindow", u"UnitNormalization", None));
        ___qlistwidgetitem343 = self.listWidget_mutate_list.item(21)
        ___qlistwidgetitem343.setText(QCoreApplication.translate("MainWindow", u"UpSampling1D", None));
        ___qlistwidgetitem344 = self.listWidget_mutate_list.item(22)
        ___qlistwidgetitem344.setText(QCoreApplication.translate("MainWindow", u"UpSampling2D", None));
        ___qlistwidgetitem345 = self.listWidget_mutate_list.item(23)
        ___qlistwidgetitem345.setText(QCoreApplication.translate("MainWindow", u"UpSampling3D", None));
        ___qlistwidgetitem346 = self.listWidget_mutate_list.item(24)
        ___qlistwidgetitem346.setText(QCoreApplication.translate("MainWindow", u"Wrapper", None));
        ___qlistwidgetitem347 = self.listWidget_mutate_list.item(25)
        ___qlistwidgetitem347.setText(QCoreApplication.translate("MainWindow", u"ZeroPadding1D", None));
        ___qlistwidgetitem348 = self.listWidget_mutate_list.item(26)
        ___qlistwidgetitem348.setText(QCoreApplication.translate("MainWindow", u"ZeroPadding2D", None));
        ___qlistwidgetitem349 = self.listWidget_mutate_list.item(27)
        ___qlistwidgetitem349.setText(QCoreApplication.translate("MainWindow", u"ZeroPadding3D", None));
        ___qlistwidgetitem350 = self.listWidget_mutate_list.item(28)
        ___qlistwidgetitem350.setText(QCoreApplication.translate("MainWindow", u"AvgPool1D", None));
        ___qlistwidgetitem351 = self.listWidget_mutate_list.item(29)
        ___qlistwidgetitem351.setText(QCoreApplication.translate("MainWindow", u"AvgPool2D", None));
        ___qlistwidgetitem352 = self.listWidget_mutate_list.item(30)
        ___qlistwidgetitem352.setText(QCoreApplication.translate("MainWindow", u"AvgPool3D", None));
        ___qlistwidgetitem353 = self.listWidget_mutate_list.item(31)
        ___qlistwidgetitem353.setText(QCoreApplication.translate("MainWindow", u"BatchNormalization", None));
        ___qlistwidgetitem354 = self.listWidget_mutate_list.item(32)
        ___qlistwidgetitem354.setText(QCoreApplication.translate("MainWindow", u"Bidirectional", None));
        ___qlistwidgetitem355 = self.listWidget_mutate_list.item(33)
        ___qlistwidgetitem355.setText(QCoreApplication.translate("MainWindow", u"CategoryEncoding", None));
        ___qlistwidgetitem356 = self.listWidget_mutate_list.item(34)
        ___qlistwidgetitem356.setText(QCoreApplication.translate("MainWindow", u"CenterCrop", None));
        ___qlistwidgetitem357 = self.listWidget_mutate_list.item(35)
        ___qlistwidgetitem357.setText(QCoreApplication.translate("MainWindow", u"Concatenate", None));
        ___qlistwidgetitem358 = self.listWidget_mutate_list.item(36)
        ___qlistwidgetitem358.setText(QCoreApplication.translate("MainWindow", u"Conv1D", None));
        ___qlistwidgetitem359 = self.listWidget_mutate_list.item(37)
        ___qlistwidgetitem359.setText(QCoreApplication.translate("MainWindow", u"Conv1DTranspose", None));
        ___qlistwidgetitem360 = self.listWidget_mutate_list.item(38)
        ___qlistwidgetitem360.setText(QCoreApplication.translate("MainWindow", u"Conv2D", None));
        ___qlistwidgetitem361 = self.listWidget_mutate_list.item(39)
        ___qlistwidgetitem361.setText(QCoreApplication.translate("MainWindow", u"Conv2DTranspose", None));
        ___qlistwidgetitem362 = self.listWidget_mutate_list.item(40)
        ___qlistwidgetitem362.setText(QCoreApplication.translate("MainWindow", u"Conv3D", None));
        ___qlistwidgetitem363 = self.listWidget_mutate_list.item(41)
        ___qlistwidgetitem363.setText(QCoreApplication.translate("MainWindow", u"Conv3DTranspose", None));
        ___qlistwidgetitem364 = self.listWidget_mutate_list.item(42)
        ___qlistwidgetitem364.setText(QCoreApplication.translate("MainWindow", u"AbstractRNNCell", None));
        ___qlistwidgetitem365 = self.listWidget_mutate_list.item(43)
        ___qlistwidgetitem365.setText(QCoreApplication.translate("MainWindow", u"Activation", None));
        ___qlistwidgetitem366 = self.listWidget_mutate_list.item(44)
        ___qlistwidgetitem366.setText(QCoreApplication.translate("MainWindow", u"ActivityRegularization", None));
        ___qlistwidgetitem367 = self.listWidget_mutate_list.item(45)
        ___qlistwidgetitem367.setText(QCoreApplication.translate("MainWindow", u"Average", None));
        ___qlistwidgetitem368 = self.listWidget_mutate_list.item(46)
        ___qlistwidgetitem368.setText(QCoreApplication.translate("MainWindow", u"AveragePooling1D", None));
        ___qlistwidgetitem369 = self.listWidget_mutate_list.item(47)
        ___qlistwidgetitem369.setText(QCoreApplication.translate("MainWindow", u"AveragePooling2D", None));
        ___qlistwidgetitem370 = self.listWidget_mutate_list.item(48)
        ___qlistwidgetitem370.setText(QCoreApplication.translate("MainWindow", u"AveragePooling3D", None));
        ___qlistwidgetitem371 = self.listWidget_mutate_list.item(49)
        ___qlistwidgetitem371.setText(QCoreApplication.translate("MainWindow", u"momentum", None));
        ___qlistwidgetitem372 = self.listWidget_mutate_list.item(50)
        ___qlistwidgetitem372.setText(QCoreApplication.translate("MainWindow", u"input_shape", None));
        ___qlistwidgetitem373 = self.listWidget_mutate_list.item(51)
        ___qlistwidgetitem373.setText(QCoreApplication.translate("MainWindow", u"AlphaDropout", None));
        ___qlistwidgetitem374 = self.listWidget_mutate_list.item(52)
        ___qlistwidgetitem374.setText(QCoreApplication.translate("MainWindow", u"MaxPooling2D", None));
        ___qlistwidgetitem375 = self.listWidget_mutate_list.item(53)
        ___qlistwidgetitem375.setText(QCoreApplication.translate("MainWindow", u"Conv2D", None));
        ___qlistwidgetitem376 = self.listWidget_mutate_list.item(54)
        ___qlistwidgetitem376.setText(QCoreApplication.translate("MainWindow", u"learning_rate", None));
        ___qlistwidgetitem377 = self.listWidget_mutate_list.item(55)
        ___qlistwidgetitem377.setText(QCoreApplication.translate("MainWindow", u"batch_size", None));
        ___qlistwidgetitem378 = self.listWidget_mutate_list.item(56)
        ___qlistwidgetitem378.setText(QCoreApplication.translate("MainWindow", u"dropout_rate", None));
        ___qlistwidgetitem379 = self.listWidget_mutate_list.item(57)
        ___qlistwidgetitem379.setText(QCoreApplication.translate("MainWindow", u"Dropout", None));
        ___qlistwidgetitem380 = self.listWidget_mutate_list.item(58)
        ___qlistwidgetitem380.setText(QCoreApplication.translate("MainWindow", u"regularization", None));
        ___qlistwidgetitem381 = self.listWidget_mutate_list.item(59)
        ___qlistwidgetitem381.setText(QCoreApplication.translate("MainWindow", u"loss", None));
        ___qlistwidgetitem382 = self.listWidget_mutate_list.item(60)
        ___qlistwidgetitem382.setText(QCoreApplication.translate("MainWindow", u"activation", None));
        self.listWidget_mutate_list.setSortingEnabled(__sortingEnabled4)

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Code Snippet", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Mutated Code", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Source Code", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Load The Model Source Code", None))
        self.btn_load_dnn.setText(QCoreApplication.translate("MainWindow", u"DNN LOAD", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Selected Test Parameters", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Select Parameter for Test", None))

        __sortingEnabled5 = self.dnn_code_snippet_list.isSortingEnabled()
        self.dnn_code_snippet_list.setSortingEnabled(False)
        ___qlistwidgetitem383 = self.dnn_code_snippet_list.item(0)
        ___qlistwidgetitem383.setText(QCoreApplication.translate("MainWindow", u"tf.keras.layers.MaxPooling2D", None));
        ___qlistwidgetitem384 = self.dnn_code_snippet_list.item(1)
        ___qlistwidgetitem384.setText(QCoreApplication.translate("MainWindow", u"epochs", None));
        ___qlistwidgetitem385 = self.dnn_code_snippet_list.item(2)
        ___qlistwidgetitem385.setText(QCoreApplication.translate("MainWindow", u"epoch", None));
        ___qlistwidgetitem386 = self.dnn_code_snippet_list.item(3)
        ___qlistwidgetitem386.setText(QCoreApplication.translate("MainWindow", u"layer.activation", None));
        ___qlistwidgetitem387 = self.dnn_code_snippet_list.item(4)
        ___qlistwidgetitem387.setText(QCoreApplication.translate("MainWindow", u"model.add", None));
        ___qlistwidgetitem388 = self.dnn_code_snippet_list.item(5)
        ___qlistwidgetitem388.setText(QCoreApplication.translate("MainWindow", u"model.pop", None));
        ___qlistwidgetitem389 = self.dnn_code_snippet_list.item(6)
        ___qlistwidgetitem389.setText(QCoreApplication.translate("MainWindow", u"optimizer.lr", None));
        ___qlistwidgetitem390 = self.dnn_code_snippet_list.item(7)
        ___qlistwidgetitem390.setText(QCoreApplication.translate("MainWindow", u"layer.dropout", None));
        ___qlistwidgetitem391 = self.dnn_code_snippet_list.item(8)
        ___qlistwidgetitem391.setText(QCoreApplication.translate("MainWindow", u"layer.filters", None));
        ___qlistwidgetitem392 = self.dnn_code_snippet_list.item(9)
        ___qlistwidgetitem392.setText(QCoreApplication.translate("MainWindow", u"layer.units", None));
        ___qlistwidgetitem393 = self.dnn_code_snippet_list.item(10)
        ___qlistwidgetitem393.setText(QCoreApplication.translate("MainWindow", u"layer.kernel_initializer", None));
        ___qlistwidgetitem394 = self.dnn_code_snippet_list.item(11)
        ___qlistwidgetitem394.setText(QCoreApplication.translate("MainWindow", u"layer.kernel_constraint", None));
        ___qlistwidgetitem395 = self.dnn_code_snippet_list.item(12)
        ___qlistwidgetitem395.setText(QCoreApplication.translate("MainWindow", u"tf.keras.layers.InputLayer", None));
        ___qlistwidgetitem396 = self.dnn_code_snippet_list.item(13)
        ___qlistwidgetitem396.setText(QCoreApplication.translate("MainWindow", u"model.loss", None));
        ___qlistwidgetitem397 = self.dnn_code_snippet_list.item(14)
        ___qlistwidgetitem397.setText(QCoreApplication.translate("MainWindow", u"model.optimizer", None));
        ___qlistwidgetitem398 = self.dnn_code_snippet_list.item(15)
        ___qlistwidgetitem398.setText(QCoreApplication.translate("MainWindow", u"layer.bias_initializer", None));
        ___qlistwidgetitem399 = self.dnn_code_snippet_list.item(16)
        ___qlistwidgetitem399.setText(QCoreApplication.translate("MainWindow", u"tf.keras.layers.Dropout", None));
        ___qlistwidgetitem400 = self.dnn_code_snippet_list.item(17)
        ___qlistwidgetitem400.setText(QCoreApplication.translate("MainWindow", u"tf.data.Dataset", None));
        ___qlistwidgetitem401 = self.dnn_code_snippet_list.item(18)
        ___qlistwidgetitem401.setText(QCoreApplication.translate("MainWindow", u"tf.keras.initializers.Constant", None));
        ___qlistwidgetitem402 = self.dnn_code_snippet_list.item(19)
        ___qlistwidgetitem402.setText(QCoreApplication.translate("MainWindow", u"tf.keras.layers.AvgPooling2D", None));
        ___qlistwidgetitem403 = self.dnn_code_snippet_list.item(20)
        ___qlistwidgetitem403.setText(QCoreApplication.translate("MainWindow", u"tf.keras.layers.Flatten", None));
        ___qlistwidgetitem404 = self.dnn_code_snippet_list.item(21)
        ___qlistwidgetitem404.setText(QCoreApplication.translate("MainWindow", u"tf.keras.layers.Input", None));
        self.dnn_code_snippet_list.setSortingEnabled(__sortingEnabled5)

        self.pushButton_dnn_scan.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.creditsLabel.setText("")
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

