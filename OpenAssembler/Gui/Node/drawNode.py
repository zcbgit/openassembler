# $Id$
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from nodeFunctions import nodeFunctions
import Core.common as common


class DrawNode(QtGui. QGraphicsItem, nodeFunctions):
	def __init__(self, ID, collectedFunctions, node_data):
		QtGui.QGraphicsItem.__init__(self)
		self.node_data = node_data
		self.sizex = common.NODE_SIZEX
		num_left = len(self.pre_pin) + len(self.input_pin)
		num_right = len(self.next_pin) + len(self.output_pin)
		if self.pre_addable:
			num_left += 1
		if self.input_addable:
			num_left += 1
		if self.next_addable:
			num_right += 1
		if self.output_addable:
			num_right += 1
		if num_left > num_right:
			self.sizey = num_left * common.NODE_PIN_SIZEY + 60
		else:
			self.sizey = num_right * common.NODE_PIN_SIZEY + 60
		if self.sizey < common.NODE_MIN_SIZEY:
			self.sizey = common.NODE_MIN_SIZEY
		self.sizey += 20
		self.setZValue(1)
		self.ID = ID
		self.nodeUpperLabel = node_data.node_type
		self.pres = []
		self.nexts = []
		self.outs = []
		self.ins = []
		self.connected_pres = []
		self.connected_nexts = []
		self.connected_outs = []
		self.connected_ins = []
		self.out_register = ""
		self.in_register = ""
		self.final_connect = collectedFunctions["connect_finally"]
		self.tmp_connect = collectedFunctions["connect_tmp"]
		self.delete_connection = collectedFunctions["delete_connection"]
		self.tmp_pos = collectedFunctions["pos_tmp"]
		self.delete_node = collectedFunctions["delete_node"]
		self.del_tmp = collectedFunctions["del_tmp"]
		self.scene = collectedFunctions["oas_scene"]
		self.duplicateNode = collectedFunctions["duplicateNode"]
		self.node_position = collectedFunctions["node_position"]
		self.setEndNode = collectedFunctions["setEndNode"]
		self.attributeE = collectedFunctions["attributeE"]
		self.add_newAttribute = collectedFunctions["add_newAttribute"]
		self.remove_Attribute = collectedFunctions["remove_Attribute"]
		self.varCategory = collectedFunctions["varCategory"]
		self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable | QtGui.QGraphicsItem.ItemIsMovable | QtGui.QGraphicsItem.ItemIsFocusable)
		self.setAcceptsHoverEvents(True)

	def paint(self, painter, option, unused_widget=None):
		font = QtGui.QFont("Sans", 10)
		font.setBold(True)
		font.setStyleStrategy(QtGui.QFont.ForceOutline)
		painter.setFont(font)
		if option.state & QtGui.QStyle.State_Selected:
			borderColor = common.NODE_BORDERCOLOR_SELECTED
		else:
			borderColor = common.NODE_BORDERCOLOR_UNSELECTED

		if option.state & QtGui.QStyle.State_MouseOver:
			fillColor = common.NODE_FILLCOLOR_MOUSEOVER
		else:
			fillColor = common.NODE_FILLCOLOR_MOUSELEAVE

		connectioncolor = QtGui.QColor(51, 51, 51)
		trianglecolor = QtGui.QColor(210, 210, 210)
		greencolor = QtGui.QColor(90, 160, 44)

		pen = QtGui.QPen()
		pen.setWidthF(1)
		pen.setColor(borderColor)
		painter.setPen(pen)

		painter.setBrush(QtGui.QBrush(borderColor))
		painter.drawRoundedRect(QtCore.QRect(40, 0, self.sizex - 80, 60), 10, 10)

		pen.setColor(QtGui.QColor(125, 125, 125))
		painter.setPen(pen)
		painter.drawText(40, 0, self.sizex - 80, common.NODE_LABEL_SIZEY, 0x0084, self.nodeUpperLabel)

		blank_edge = common.NODE_BLANK_EDGE
		painter.setBrush(QtGui.QBrush(fillColor))
		painter.drawRoundedRect(QtCore.QRect(blank_edge, common.NODE_LABEL_SIZEY, self.sizex - 40, self.sizey - 30), 10, 10)

		pen.setColor(connectioncolor)
		painter.setPen(pen)

		painter.setBrush(QtGui.QBrush(connectioncolor))

		pz = self.pre_pin.keys()
		iz = self.input_pin.keys()
		nz = self.next_pin.keys()
		oz = self.output_pin.keys()

		pin_sizex = common.NODE_PIN_SIZEX
		if pin_sizex > blank_edge:
			pin_sizex = blank_edge
		pin_sizey = common.NODE_PIN_SIZEY
		pin_icon_size = common.NODE_PIN_ICON_SIZE
		add_size = common.NODE_ADD_SIZE
		# 左边的pin
		idx_left = 1
		for key in pz:
			if self.connected_pres.count(key) > 0:
				pen.setColor(greencolor)
				painter.setPen(pen)
				painter.setBrush(QtGui.QBrush(greencolor))
			else:
				pen.setColor(connectioncolor)
				painter.setPen(pen)
				painter.setBrush(QtGui.QBrush(connectioncolor))
			self.pres.append([0, idx_left * pin_sizey, pin_sizex - 10, pin_sizey - 10, key])
			painter.drawRoundedRect(QtCore.QRect(0, idx_left * pin_sizey + 5, blank_edge, pin_sizey - 10), 5, 5)
			pen.setColor(trianglecolor)
			painter.setPen(pen)
			painter.setBrush(QtGui.QBrush(trianglecolor))
			offx = (pin_sizex - pin_icon_size) / 2
			offy = (pin_sizey - pin_icon_size) / 2
			painter.drawPolygon(QtCore.QPoint(offx, idx_left * pin_sizey + offy),
								QtCore.QPoint(offx, (idx_left + 1) * pin_sizey - offy),
								QtCore.QPoint(offx + pin_icon_size, idx_left * pin_sizey + pin_sizey / 2))
			self.paint_text(painter, blank_edge + 5, idx_left * pin_sizey, self.sizex / 2, pin_sizey, 0x0081, key)
			idx_left += 1

		if self.pre_addable:
			offy = (pin_sizey - add_size) / 2
			self.paint_add(painter, 2, idx_left * pin_sizey + offy, add_size, add_size)
			idx_left += 1

		for key in iz:
			if self.connected_ins.count(key) > 0:
				pen.setColor(greencolor)
				painter.setPen(pen)
				painter.setBrush(QtGui.QBrush(greencolor))
			else:
				pen.setColor(connectioncolor)
				painter.setPen(pen)
				painter.setBrush(QtGui.QBrush(connectioncolor))
			self.ins.append([0, idx_left * pin_sizey, pin_sizex - 10, pin_sizey - 10, key])
			painter.drawRoundedRect(QtCore.QRect(0, idx_left * pin_sizey + 5, blank_edge, pin_sizey - 10), 5, 5)
			typ = self.input_pin[key].variable_type
			icolor = self.getArrtibuteColor(typ)
			pen.setColor(icolor)
			painter.setPen(pen)
			painter.setBrush(QtGui.QBrush(icolor))
			offx = (pin_sizex - pin_icon_size) / 2
			offy = (pin_sizey - pin_icon_size) / 2
			painter.drawEllipse(offx, idx_left * pin_sizey + offy, pin_icon_size, pin_icon_size)
			self.paint_text(painter, blank_edge + 5, idx_left * pin_sizey, self.sizex / 2, pin_sizey, 0x0081, key)
			idx_left += 1

		if self.input_addable:
			offy = (pin_sizey - add_size) / 2
			self.paint_add(painter, 2, idx_left * pin_sizey + offy, add_size, add_size)

		# 右边的pin
		idx_right = 1
		for key in nz:
			if self.connected_nexts.count(key) > 0:
				pen.setColor(greencolor)
				painter.setPen(pen)
				painter.setBrush(QtGui.QBrush(greencolor))
			else:
				pen.setColor(connectioncolor)
				painter.setPen(pen)
				painter.setBrush(QtGui.QBrush(connectioncolor))
			self.nexts.append([self.sizex - 30, idx_right * pin_sizey, pin_sizex - 10, pin_sizey - 10, key])
			painter.drawRoundedRect(QtCore.QRect(self.sizex - blank_edge, idx_right * pin_sizey + 5, blank_edge, pin_sizey - 10), 5, 5)
			pen.setColor(trianglecolor)
			painter.setPen(pen)
			painter.setBrush(QtGui.QBrush(trianglecolor))
			offx = (pin_sizex - pin_icon_size) / 2
			offy = (pin_sizey - pin_icon_size) / 2
			painter.drawPolygon(QtCore.QPoint(self.sizex - pin_icon_size - offx, idx_right * pin_sizey + offy),
								QtCore.QPoint(self.sizex - pin_icon_size - offx, (idx_right + 1) * pin_sizey - offy),
								QtCore.QPoint(self.sizex - offx, idx_right * pin_sizey + pin_sizey / 2))
			self.paint_text(painter, self.sizex / 2, idx_right * pin_sizey, self.sizex / 2 - blank_edge - 5, pin_sizey, 0x0082, key)
			idx_right += 1

		if self.next_addable:
			offy = (pin_sizey - add_size) / 2
			self.paint_add(painter, self.sizex - add_size - 2, idx_right * pin_sizey + offy, add_size, add_size)
			idx_right += 1

		for key in oz:
			if self.connected_outs.count(key) > 0:
				pen.setColor(greencolor)
				painter.setPen(pen)
				painter.setBrush(QtGui.QBrush(greencolor))
			else:
				pen.setColor(connectioncolor)
				painter.setPen(pen)
				painter.setBrush(QtGui.QBrush(connectioncolor))
			self.outs.append([self.sizex - 30, idx_right * pin_sizey, pin_sizex - 10, pin_sizey - 10, key])
			painter.drawRoundedRect(QtCore.QRect(self.sizex - blank_edge, idx_right * pin_sizey + 5, blank_edge, pin_sizey - 10), 5, 5)
			typ = self.output_pin[key].variable_type
			icolor = self.getArrtibuteColor(typ)
			pen.setColor(icolor)
			painter.setPen(pen)
			painter.setBrush(QtGui.QBrush(icolor))
			offx = (pin_sizex - pin_icon_size) / 2
			offy = (pin_sizey - pin_icon_size) / 2
			painter.drawEllipse(self.sizex - pin_icon_size - offx, idx_right * pin_sizey + offy, pin_icon_size, pin_icon_size)
			self.paint_text(painter, self.sizex / 2, idx_right * pin_sizey, self.sizex / 2 - blank_edge - 5, pin_sizey, 0x0082, key)

		if self.output_addable:
			offy = (pin_sizey - add_size) / 2
			self.paint_add(painter, self.sizex - add_size - 2, idx_left * pin_sizey + offy, add_size, add_size)

	def paint_text(self, painter, x, y, width, height, flags, key):
		font = QtGui.QFont("Sans", 10)
		font.setStyleStrategy(QtGui.QFont.ForceOutline)
		font.setBold(False)
		painter.setFont(font)
		pen = QtGui.QPen()
		pen.setColor(QtGui.QColor(0, 0, 0))
		pen.setWidth(2)
		painter.setPen(pen)
		painter.drawText(x, y, width, height, flags, key)

	def paint_add(self, painter, x, y, width, height):
		trianglecolor = QtGui.QColor(210, 210, 210)
		orangecolor = QtGui.QColor(160, 130, 44)

		pen = QtGui.QPen()
		pen.setColor(orangecolor)
		pen.setWidth(2)
		painter.setPen(pen)

		painter.setBrush(QtGui.QBrush(orangecolor))

		painter.drawEllipse(x, y, width, height)

		font = QtGui.QFont("Sans", 10)
		font.setBold(True)
		font.setStyleStrategy(QtGui.QFont.ForceOutline)
		painter.setFont(font)
		pen.setColor(trianglecolor)
		pen.setWidth(2)
		painter.setPen(pen)

		painter.drawText(x, y, width, height, 0x0084, "+")

	def mousePressEvent(self, event):
		ax = event.pos().x()
		ay = event.pos().y()
		if event.button() == 1:
			if (self.sizey - 40) < ay < (self.sizey - 24):
				if 2 < ax < 16 and self.input_addable:
					self.add_newAttribute(self.ID, 0)
				elif 182 < ax < 198 and self.output_addable:
					self.add_newAttribute(self.ID, 1)

		if event.button() == 2:
			result = ""
			for ots in self.outs:
				if ots[0] < ax < ots[0] + ots[2] and ots[1] < ay < ots[1] + ots[3]:
					result = ots[4]
			for ots in self.ins:
				if ots[0] < ax < ots[0] + ots[2] and ots[1] < ay < ots[1] + ots[3]:
					result = ots[4]
			if result != "":
				eventpos = event.screenPos()
				mainmenu = QtGui.QMenu()
				mainmenu.setTitle("MainMenu")
				mainmenu.addAction("Kill Connection",
								   lambda id=self.ID, result=result: self.delete_connection(id, result))
				mainmenu.addAction("Delete Attribute",
								   lambda id=self.ID, result=result: self.remove_Attribute(id, result))
				mainmenu.exec_(QtCore.QPoint(eventpos.x(), eventpos.y()))
				return
			else:
				eventpos = event.screenPos()
				mainmenu = QtGui.QMenu()
				mainmenu.setTitle("MainMenu")
				mainmenu.addAction("Delete", lambda id=self.ID: self.do_oas_del_sel(id))
				mainmenu.addSeparator()
				mainmenu.addAction("Duplicate", lambda id=self.ID: self.do_oas_duplicate(id))
				mainmenu.exec_(QtCore.QPoint(eventpos.x(), eventpos.y()))
				return
		self.setZValue(3)
		QtGui.QGraphicsItem.mousePressEvent(self, event)

	def mouseMoveEvent(self, event):
		ax = event.pos().x()
		ay = event.pos().y()
		if event.modifiers() & QtCore.Qt.ShiftModifier:
			self.tmp_pos(self.mapToScene(event.pos()).x(), self.mapToScene(event.pos()).y())
			result = ""
			for ots in self.outs:
				if ots[0] < ax < ots[0] + ots[2] and ots[1] < ay < ots[1] + ots[3]:
					result = ots[4]
			if result != "":
				self.out_register = str(self.ID) + "." + str(result)
				self.tmp_connect(self.out_register)
				self.update()
				return
			self.update()
			return
		self.node_position()
		QtGui.QGraphicsItem.mouseMoveEvent(self, event)
		self.scene.update()

	def mouseDoubleClickEvent(self, event):
		self.attributeE(self.ID)
		QtGui.QGraphicsItem.mouseDoubleClickEvent(self, event)
		self.scene.update()

	def mouseReleaseEvent(self, event):
		self.del_tmp()
		try:
			self.setZValue(2)
			scenepos = self.mapToScene(event.pos())
			releaseitem = self.scene.itemAt(event.scenePos())
			itemlocalpos = releaseitem.mapFromScene(scenepos)
			ax = itemlocalpos.x()
			ay = itemlocalpos.y()
			result = releaseitem.define_ins(ax, ay)
			if result != "":
				self.in_register = str(releaseitem.backID()) + "." + str(result)
				self.final_connect(self.out_register, self.in_register)
				self.scene.update()
				return
			self.out_register = ""
			self.in_register = ""
			QtGui.QGraphicsItem.mouseReleaseEvent(self, event)
		except:
			QtGui.QGraphicsItem.mouseReleaseEvent(self, event)
			self.out_register = ""
			self.in_register = ""

	@property
	def pre_pin(self):
		return self.node_data.pre_pin

	@property
	def pre_addable(self):
		return self.node_data.pre_addable

	@property
	def next_pin(self):
		return self.node_data.next_pin

	@property
	def next_addable(self):
		return self.node_data.next_addable

	@property
	def input_pin(self):
		return self.node_data.input_pin

	@property
	def input_addable(self):
		return self.node_data.input_addable

	@property
	def output_pin(self):
		return self.node_data.output_pin

	@property
	def output_addable(self):
		return self.node_data.output_addable
