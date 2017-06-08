#! /usr/bin/env python

# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.04
#
# #####################################################################################

from PyQt4 import QtCore, QtGui

class nodePainter():
	def paint(self, painter, option, unused_widget):
		font=QtGui.QFont("Sans",10)
		font.setBold(True)
		font.setStyleStrategy(QtGui.QFont.ForceOutline)
		painter.setFont(font)
		if option.state & QtGui.QStyle.State_Selected:
			borderColor = QtGui.QColor(212,255,42)
		else:
			borderColor = QtGui.QColor(51,51,51)

		if option.state & QtGui.QStyle.State_MouseOver:
			fillColor = QtGui.QColor(204,204,204).dark(120)
		else:
			fillColor=QtGui.QColor(204,204,204)

		connectioncolor=QtGui.QColor(51,51,51)
		trianglecolor=QtGui.QColor(210,210,210)
		greencolor=QtGui.QColor(90,160,44)
		yellowcolor=QtGui.QColor(192,185,115)
		bluecolor=QtGui.QColor(90,44,160)

		pen = QtGui.QPen()
		pen.setWidthF(1)
		pen.setColor(borderColor)
		painter.setPen(pen)
		
		painter.setBrush(QtGui.QBrush(borderColor))
		painter.drawRoundedRect(QtCore.QRect(40,0,self.sizex-80,60),10,10)

		pen.setColor(QtGui.QColor(125,125,125))
		painter.setPen(pen)
		painter.drawText(40,0,self.sizex-80,20,0x0084,self.nodeUpperLabel)

		font.setBold(False)
		painter.setFont(font)

		pen.setColor(connectioncolor)
		painter.setPen(pen)

		painter.setBrush(QtGui.QBrush(connectioncolor))

		iz = self.Input.keys()
		oz = self.Output.keys()

		for i, key in enumerate(iz):
			if self.connected_ins.count(key) > 0:
						pen.setColor(greencolor)
						painter.setPen(pen)
						painter.setBrush(QtGui.QBrush(greencolor))
			if str(self.Input[key]["value"])[:1]==">" or str(self.Input[key]["value"])[:1] == "$":
						pen.setColor(yellowcolor)
						painter.setPen(pen)
						painter.setBrush(QtGui.QBrush(yellowcolor))
			if str(self.Input[key]["value"])[:1]=="=":
						pen.setColor(bluecolor)
						painter.setPen(pen)
						painter.setBrush(QtGui.QBrush(bluecolor))
			self.ins.append([0, (i + 1)*40, 30, 30, key])
			painter.drawRoundedRect(QtCore.QRect(0, (i + 1)*40, 50, 30), 5, 5)
			pen.setColor(connectioncolor)
			painter.setPen(pen)
			painter.setBrush(QtGui.QBrush(connectioncolor))

		for i, key in enumerate(oz):
			if self.connected_outs.count(key)>0:
						pen.setColor(greencolor)
						painter.setPen(pen)
						painter.setBrush(QtGui.QBrush(greencolor))
			self.outs.append([self.sizex-30, (i + 1)*40, 30, 30, key])
			painter.drawRoundedRect(QtCore.QRect(self.sizex-30, (i + 1)*40, 30, 30), 5, 5)
			pen.setColor(connectioncolor)
			painter.setPen(pen)
			painter.setBrush(QtGui.QBrush(connectioncolor))

		pen.setColor(trianglecolor)
		painter.setPen(pen)

		painter.setBrush(QtGui.QBrush(trianglecolor))

		for i, key in enumerate(iz):
			typ = self.Input[key]["variable_type"]
			icolor=self.getArrtibuteColor(typ)
			pen.setColor(icolor)
			painter.setPen(pen)
			painter.setBrush(QtGui.QBrush(icolor))
			painter.drawPolygon(QtCore.QPoint(9, (i + 1)*40+7),
								QtCore.QPoint(9, (i + 1)*40+23),
								QtCore.QPoint(15, (i + 1)*40+15))

		for i, key in enumerate(oz):
			typ = self.Output[key]["variable_type"]
			icolor=self.getArrtibuteColor(typ)
			pen.setColor(icolor)
			painter.setPen(pen)
			painter.setBrush(QtGui.QBrush(icolor))
			painter.drawPolygon(QtCore.QPoint(self.sizex-13, (i + 1)*40+7),
								QtCore.QPoint(self.sizex-13, (i + 1)*40+23),
								QtCore.QPoint(self.sizex-7, (i + 1)*40+15))

		pen.setColor(QtGui.QColor(0,0,0))
		pen.setWidth(2)
		painter.setPen(pen)

		painter.setBrush(QtGui.QBrush(fillColor))
		painter.drawRoundedRect(QtCore.QRect(20,20,self.sizex-40,self.sizey-30),10,10)

		for i, key in enumerate(iz):
			painter.drawText(25, (i+1)*40, self.sizex/2, 30, 0x0081, key)
		for i, key in enumerate(oz):
			painter.drawText(self.sizex/2, (i+1)*40, self.sizex/2-25, 30, 0x0082, key)

		trianglecolor=QtGui.QColor(210,210,210)
		orangecolor=QtGui.QColor(160,130,44)

		pen.setColor(orangecolor)
		pen.setWidth(2)
		painter.setPen(pen)

		painter.setBrush(QtGui.QBrush(orangecolor))

		if self.input_addable:
			painter.drawEllipse(2,self.sizey-40,16,16)
		if self.output_addable:
			painter.drawEllipse(182, self.sizey - 40, 16, 16)

		font.setBold(True)
		painter.setFont(font)
		pen.setColor(trianglecolor)
		pen.setWidth(2)
		painter.setPen(pen)

		if self.input_addable:
			painter.drawText(2, self.sizey - 40, 16, 16, 0x0084, "+")
		if self.output_addable:
			painter.drawText(182, self.sizey - 40, 16, 16, 0x0084, "+")
