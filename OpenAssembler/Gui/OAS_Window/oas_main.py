# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oas_main.ui'
#
# Created: Wed Jul 15 10:23:49 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_oasWindow(object):
    def setupUi(self, oasWindow):
        oasWindow.setObjectName("oasWindow")
        oasWindow.setVisible(True)
        oasWindow.resize(885, 533)
        self.oas_centralwidget = QtGui.QWidget(oasWindow)
        self.oas_centralwidget.setObjectName("oas_centralwidget")
        self.gridLayout_6 = QtGui.QGridLayout(self.oas_centralwidget)
        self.gridLayout_6.setMargin(2)
        self.gridLayout_6.setSpacing(2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.oas_splitter = QtGui.QSplitter(self.oas_centralwidget)
        self.oas_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.oas_splitter.setObjectName("oas_splitter")
        self.oas_splitter02 = QtGui.QSplitter(self.oas_splitter)
        self.oas_splitter02.setOrientation(QtCore.Qt.Vertical)
        self.oas_splitter02.setObjectName("oas_splitter02")
        self.oas_menuline_frame = QtGui.QFrame(self.oas_splitter02)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oas_menuline_frame.sizePolicy().hasHeightForWidth())
        self.oas_menuline_frame.setSizePolicy(sizePolicy)
        self.oas_menuline_frame.setMinimumSize(QtCore.QSize(0, 30))
        self.oas_menuline_frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.oas_menuline_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.oas_menuline_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.oas_menuline_frame.setObjectName("oas_menuline_frame")
        self.gridLayout_3 = QtGui.QGridLayout(self.oas_menuline_frame)
        self.gridLayout_3.setMargin(2)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.oas_horizontalLayout_3 = QtGui.QHBoxLayout()
        self.oas_horizontalLayout_3.setSpacing(2)
        self.oas_horizontalLayout_3.setObjectName("oas_horizontalLayout_3")
        self.oas_new_bu = QtGui.QToolButton(self.oas_menuline_frame)
        self.oas_new_bu.setObjectName("oas_new_bu")
        self.oas_horizontalLayout_3.addWidget(self.oas_new_bu)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.oas_horizontalLayout_3.addItem(spacerItem)
        self.oas_open_bu = QtGui.QToolButton(self.oas_menuline_frame)
        self.oas_open_bu.setObjectName("oas_open_bu")
        self.oas_horizontalLayout_3.addWidget(self.oas_open_bu)
        self.oas_save_bu = QtGui.QToolButton(self.oas_menuline_frame)
        self.oas_save_bu.setObjectName("oas_save_bu")
        self.oas_horizontalLayout_3.addWidget(self.oas_save_bu)
        self.oas_saveas_bu = QtGui.QToolButton(self.oas_menuline_frame)
        self.oas_saveas_bu.setObjectName("oas_saveas_bu")
        self.oas_horizontalLayout_3.addWidget(self.oas_saveas_bu)
        spacerItem1 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.oas_horizontalLayout_3.addItem(spacerItem1)
        self.oas_run_bu = QtGui.QToolButton(self.oas_menuline_frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(86, 255, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 255, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 255, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 255, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 255, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 255, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 255, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.oas_run_bu.setPalette(palette)
        self.oas_run_bu.setObjectName("oas_run_bu")
        self.oas_horizontalLayout_3.addWidget(self.oas_run_bu)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.oas_horizontalLayout_3.addItem(spacerItem2)
        self.oas_search_entry = QtGui.QLineEdit(self.oas_menuline_frame)
        self.oas_search_entry.setObjectName("oas_search_entry")
        self.oas_horizontalLayout_3.addWidget(self.oas_search_entry)
        self.oas_search_bu = QtGui.QToolButton(self.oas_menuline_frame)
        self.oas_search_bu.setObjectName("oas_search_bu")
        self.oas_horizontalLayout_3.addWidget(self.oas_search_bu)
        self.gridLayout_3.addLayout(self.oas_horizontalLayout_3, 0, 0, 1, 1)
        self.oas_graphicsView = QtGui.QGraphicsView(self.oas_splitter02)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(187, 187, 187))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(187, 187, 187))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(187, 187, 187))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.oas_graphicsView.setPalette(palette)
        self.oas_graphicsView.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.oas_graphicsView.setObjectName("oas_graphicsView")
        self.oas_timeline_frame = QtGui.QFrame(self.oas_splitter02)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oas_timeline_frame.sizePolicy().hasHeightForWidth())
        self.oas_timeline_frame.setSizePolicy(sizePolicy)
        self.oas_timeline_frame.setMinimumSize(QtCore.QSize(0, 70))
        self.oas_timeline_frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.oas_timeline_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.oas_timeline_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.oas_timeline_frame.setObjectName("oas_timeline_frame")
        self.gridLayout = QtGui.QGridLayout(self.oas_timeline_frame)
        self.gridLayout.setMargin(2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.oas_verticalLayout = QtGui.QVBoxLayout()
        self.oas_verticalLayout.setObjectName("oas_verticalLayout")
        self.oas_horizontalLayout = QtGui.QHBoxLayout()
        self.oas_horizontalLayout.setObjectName("oas_horizontalLayout")
        self.oas_sframe_spin = QtGui.QSpinBox(self.oas_timeline_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oas_sframe_spin.sizePolicy().hasHeightForWidth())
        self.oas_sframe_spin.setSizePolicy(sizePolicy)
        self.oas_sframe_spin.setMinimum(-100000)
        self.oas_sframe_spin.setMaximum(100000)
        self.oas_sframe_spin.setObjectName("oas_sframe_spin")
        self.oas_horizontalLayout.addWidget(self.oas_sframe_spin)
        self.oas_time_slider = QtGui.QSlider(self.oas_timeline_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oas_time_slider.sizePolicy().hasHeightForWidth())
        self.oas_time_slider.setSizePolicy(sizePolicy)
        self.oas_time_slider.setSliderPosition(0)
        self.oas_time_slider.setOrientation(QtCore.Qt.Horizontal)
        self.oas_time_slider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.oas_time_slider.setTickInterval(0)
        self.oas_time_slider.setObjectName("oas_time_slider")
        self.oas_horizontalLayout.addWidget(self.oas_time_slider)
        self.oas_eframe_spin = QtGui.QSpinBox(self.oas_timeline_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oas_eframe_spin.sizePolicy().hasHeightForWidth())
        self.oas_eframe_spin.setSizePolicy(sizePolicy)
        self.oas_eframe_spin.setMinimum(-100000)
        self.oas_eframe_spin.setMaximum(100000)
        self.oas_eframe_spin.setObjectName("oas_eframe_spin")
        self.oas_horizontalLayout.addWidget(self.oas_eframe_spin)
        self.oas_verticalLayout.addLayout(self.oas_horizontalLayout)
        self.oas_horizontalLayout_2 = QtGui.QHBoxLayout()
        self.oas_horizontalLayout_2.setObjectName("oas_horizontalLayout_2")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.oas_horizontalLayout_2.addItem(spacerItem3)
        self.oas_firstF = QtGui.QToolButton(self.oas_timeline_frame)
        self.oas_firstF.setMinimumSize(QtCore.QSize(20, 20))
        self.oas_firstF.setMaximumSize(QtCore.QSize(20, 20))
        self.oas_firstF.setObjectName("oas_firstF")
        self.oas_horizontalLayout_2.addWidget(self.oas_firstF)
        self.oas_prewF = QtGui.QToolButton(self.oas_timeline_frame)
        self.oas_prewF.setMinimumSize(QtCore.QSize(20, 20))
        self.oas_prewF.setMaximumSize(QtCore.QSize(20, 20))
        self.oas_prewF.setObjectName("oas_prewF")
        self.oas_horizontalLayout_2.addWidget(self.oas_prewF)
        self.oas_cframe_spin = QtGui.QSpinBox(self.oas_timeline_frame)
        self.oas_cframe_spin.setMinimumSize(QtCore.QSize(0, 20))
        self.oas_cframe_spin.setMaximumSize(QtCore.QSize(16777215, 20))
        self.oas_cframe_spin.setMinimum(-100000)
        self.oas_cframe_spin.setMaximum(100000)
        self.oas_cframe_spin.setObjectName("oas_cframe_spin")
        self.oas_horizontalLayout_2.addWidget(self.oas_cframe_spin)
        self.oas_nextF = QtGui.QToolButton(self.oas_timeline_frame)
        self.oas_nextF.setMinimumSize(QtCore.QSize(20, 20))
        self.oas_nextF.setMaximumSize(QtCore.QSize(20, 20))
        self.oas_nextF.setObjectName("oas_nextF")
        self.oas_horizontalLayout_2.addWidget(self.oas_nextF)
        self.oas_lastF = QtGui.QToolButton(self.oas_timeline_frame)
        self.oas_lastF.setMinimumSize(QtCore.QSize(20, 20))
        self.oas_lastF.setMaximumSize(QtCore.QSize(20, 20))
        self.oas_lastF.setObjectName("oas_lastF")
        self.oas_horizontalLayout_2.addWidget(self.oas_lastF)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.oas_horizontalLayout_2.addItem(spacerItem4)
        self.oas_verticalLayout.addLayout(self.oas_horizontalLayout_2)
        self.gridLayout.addLayout(self.oas_verticalLayout, 0, 0, 1, 1)
        self.oas_splitter03 = QtGui.QSplitter(self.oas_splitter)
        self.oas_splitter03.setOrientation(QtCore.Qt.Vertical)
        self.oas_splitter03.setObjectName("oas_splitter03")
        self.oas_attribute_frame = QtGui.QFrame(self.oas_splitter03)
        self.oas_attribute_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.oas_attribute_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.oas_attribute_frame.setObjectName("oas_attribute_frame")
        self.gridLayout_2 = QtGui.QGridLayout(self.oas_attribute_frame)
        self.gridLayout_2.setMargin(2)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.oas_verticalLayout_2 = QtGui.QVBoxLayout()
        self.oas_verticalLayout_2.setObjectName("oas_verticalLayout_2")
        self.oas_nodeName = QtGui.QLineEdit(self.oas_attribute_frame)
        self.oas_nodeName.setObjectName("oas_nodeName")
        self.oas_verticalLayout_2.addWidget(self.oas_nodeName)
        self.oas_horizontalLayout_4 = QtGui.QHBoxLayout()
        self.oas_horizontalLayout_4.setObjectName("oas_horizontalLayout_4")
        self.oas_label_2 = QtGui.QLabel(self.oas_attribute_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oas_label_2.sizePolicy().hasHeightForWidth())
        self.oas_label_2.setSizePolicy(sizePolicy)
        self.oas_label_2.setObjectName("oas_label_2")
        self.oas_horizontalLayout_4.addWidget(self.oas_label_2)
        self.oas_attribute_nodetype = QtGui.QLabel(self.oas_attribute_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oas_attribute_nodetype.sizePolicy().hasHeightForWidth())
        self.oas_attribute_nodetype.setSizePolicy(sizePolicy)
        self.oas_attribute_nodetype.setObjectName("oas_attribute_nodetype")
        self.oas_horizontalLayout_4.addWidget(self.oas_attribute_nodetype)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.oas_horizontalLayout_4.addItem(spacerItem5)
        self.oas_attribute_cache = QtGui.QCheckBox(self.oas_attribute_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oas_attribute_cache.sizePolicy().hasHeightForWidth())
        self.oas_attribute_cache.setSizePolicy(sizePolicy)
        self.oas_attribute_cache.setObjectName("oas_attribute_cache")
        self.oas_horizontalLayout_4.addWidget(self.oas_attribute_cache)
        self.oas_verticalLayout_2.addLayout(self.oas_horizontalLayout_4)
        self.oas_attribute_area = QtGui.QScrollArea(self.oas_attribute_frame)
        self.oas_attribute_area.setWidgetResizable(True)
        self.oas_attribute_area.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.oas_attribute_area.setObjectName("oas_attribute_area")
        self.oas_attribute_areaContents = QtGui.QWidget(self.oas_attribute_area)
        self.oas_attribute_areaContents.setGeometry(QtCore.QRect(0, 0, 267, 127))
        self.oas_attribute_areaContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.oas_attribute_areaContents.setObjectName("oas_attribute_areaContents")
        self.gridLayout_5 = QtGui.QGridLayout(self.oas_attribute_areaContents)
        self.gridLayout_5.setMargin(2)
        self.gridLayout_5.setSpacing(2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.oas_attribute_layout = QtGui.QVBoxLayout()
        self.oas_attribute_layout.setObjectName("oas_attribute_layout")
        self.place_to_widgets = QtGui.QVBoxLayout()
        self.place_to_widgets.setObjectName("place_to_widgets")
        self.oas_attribute_layout.addLayout(self.place_to_widgets)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.oas_attribute_layout.addItem(spacerItem6)
        self.gridLayout_5.addLayout(self.oas_attribute_layout, 0, 0, 1, 1)
        self.oas_attribute_area.setWidget(self.oas_attribute_areaContents)
        self.oas_verticalLayout_2.addWidget(self.oas_attribute_area)
        self.gridLayout_2.addLayout(self.oas_verticalLayout_2, 0, 0, 1, 1)
        self.frame = QtGui.QFrame(self.oas_splitter03)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtGui.QGridLayout(self.frame)
        self.gridLayout_4.setMargin(2)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.consoleOutArea = QtGui.QTextEdit(self.frame)
        self.consoleOutArea.setReadOnly(True)
        self.consoleOutArea.setObjectName("consoleOutArea")
        self.verticalLayout.addWidget(self.consoleOutArea)
        self.consoleInArea = QtGui.QLineEdit(self.frame)
        self.consoleInArea.setObjectName("consoleInArea")
        self.verticalLayout.addWidget(self.consoleInArea)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.oas_splitter, 0, 0, 1, 1)
        oasWindow.setCentralWidget(self.oas_centralwidget)
        self.oas_menubar = QtGui.QMenuBar(oasWindow)
        self.oas_menubar.setEnabled(False)
        self.oas_menubar.setGeometry(QtCore.QRect(0, 0, 885, 25))
        self.oas_menubar.setObjectName("oas_menubar")
        oasWindow.setMenuBar(self.oas_menubar)

        self.retranslateUi(oasWindow)
        QtCore.QObject.connect(self.oas_nextF, QtCore.SIGNAL("clicked()"), self.oas_cframe_spin.stepUp)
        QtCore.QObject.connect(self.oas_prewF, QtCore.SIGNAL("clicked()"), self.oas_cframe_spin.stepDown)
        QtCore.QObject.connect(self.oas_time_slider, QtCore.SIGNAL("sliderMoved(int)"), self.oas_cframe_spin.setValue)
        QtCore.QObject.connect(self.oas_cframe_spin, QtCore.SIGNAL("valueChanged(int)"), self.oas_time_slider.setValue)
        QtCore.QMetaObject.connectSlotsByName(oasWindow)

    def retranslateUi(self, oasWindow):
        oasWindow.setWindowTitle(QtGui.QApplication.translate("oasWindow", "OpenAssembler", None, QtGui.QApplication.UnicodeUTF8))
        self.oas_new_bu.setText(QtGui.QApplication.translate("oasWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.oas_open_bu.setText(QtGui.QApplication.translate("oasWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.oas_save_bu.setText(QtGui.QApplication.translate("oasWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.oas_saveas_bu.setText(QtGui.QApplication.translate("oasWindow", "SaveAs", None, QtGui.QApplication.UnicodeUTF8))
        self.oas_run_bu.setText(QtGui.QApplication.translate("oasWindow", "   RUN  ", None, QtGui.QApplication.UnicodeUTF8))
        self.oas_search_bu.setText(QtGui.QApplication.translate("oasWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.oas_firstF.setText(QtGui.QApplication.translate("oasWindow", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.oas_prewF.setText(QtGui.QApplication.translate("oasWindow", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.oas_nextF.setText(QtGui.QApplication.translate("oasWindow", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.oas_lastF.setText(QtGui.QApplication.translate("oasWindow", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.oas_label_2.setText(QtGui.QApplication.translate("oasWindow", "Node Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.oas_attribute_nodetype.setText(QtGui.QApplication.translate("oasWindow", "empty", None, QtGui.QApplication.UnicodeUTF8))
        self.oas_attribute_cache.setText(QtGui.QApplication.translate("oasWindow", "cache", None, QtGui.QApplication.UnicodeUTF8))

