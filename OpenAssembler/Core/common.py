# $Id$
# -*- coding: utf-8 -*-

NODE_SIZEX = 200  # 节点宽度
NODE_BLANK_EDGE = 20  # 节点左右两边的空白大小
NODE_LABEL_SIZEY = 20  # 节点标题高度
NODE_MIN_SIZEY = 100  # 节点最小高度
NODE_PIN_SIZEX = 40  # 针脚外框宽度
NODE_PIN_SIZEY = 40  # 针脚外框高度
NODE_PIN_ICON_SIZE = 10  # 针脚大小
NODE_ADD_SIZE = 16  # 加按钮大小

from PyQt4 import QtGui
NODE_BORDERCOLOR_SELECTED = QtGui.QColor(212, 255, 42)
NODE_BORDERCOLOR_UNSELECTED = QtGui.QColor(51, 51, 51)
NODE_FILLCOLOR_MOUSEOVER = QtGui.QColor(204, 204, 204).dark(120)
NODE_FILLCOLOR_MOUSELEAVE = QtGui.QColor(204, 204, 204)
