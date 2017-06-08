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

try:
	from PyQt4 import QtOpenGL
except:
	pass

from Gui.OAS_Window.oas_main import Ui_oasWindow
import Gui.Connection.drawConnection as DC
import Gui.Connection.inConnection as IC
from Gui.Menu_Shortcut.keyHandler import keyHandler
from Gui.Functions.assistantFunctions import assistantFunctions
from Gui.Functions.mainFunctions import mainFunctions
from Gui.Menu_Shortcut.mainMenu import mainmenu
from Gui.Timeline.timelineMain import timelineMain
import Gui.Console.guiConsole as GuiCo
from Core.Dbase.Dbase_init import dBase_Init

import sys


class OASWindow(QtGui.QMainWindow, Ui_oasWindow):
	def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
		QtGui.QMainWindow.__init__(self, parent, f)
		Ui_oasWindow.setupUi(self, self)


class GUI_main(OASWindow,keyHandler,assistantFunctions,mainFunctions,dBase_Init,timelineMain):

	def __init__(self,args):
		OASWindow.__init__(self)
		self.last_point=QtCore.QPointF(3,1)
		self.dBase_builder()
		self.oas_splitter.setSizes([3,1])
		self.oas_splitter02.setSizes([0,1,0])
		self.oas_splitter03.setSizes([200,70])

		self.inAE={}

		sys.stdout = GuiCo.guiConsole(self.consoleOutArea, sys.stdout)
		sys.stderr = GuiCo.guiConsole(self.consoleOutArea, sys.stderr, QtGui.QColor(255, 0, 0))

		self.consoleInArea.hide()

		try:
			if str(args[0])=="-gl":
				self.oas_graphicsView.setViewport(QtOpenGL.QGLWidget(QtOpenGL.QGLFormat(QtOpenGL.QGL.SampleBuffers | QtOpenGL.QGL.AlphaChannel)))
				self.oas_graphicsView.setViewportUpdateMode(QtGui.QGraphicsView.SmartViewportUpdate)
				self.oas_graphicsView.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform)
				self.oas_graphicsView.setOptimizationFlags(QtGui.QGraphicsView.DontClipPainter | QtGui.QGraphicsView.DontSavePainterState)
			else:
				self.oas_graphicsView.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform)
				self.oas_graphicsView.setViewportUpdateMode(QtGui.QGraphicsView.SmartViewportUpdate)
		except:
			self.oas_graphicsView.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform)
			self.oas_graphicsView.setViewportUpdateMode(QtGui.QGraphicsView.SmartViewportUpdate)

		self.oas_scene=QtGui.QGraphicsScene()
		self.oas_graphicsView.setDragMode(QtGui.QGraphicsView.RubberBandDrag)

	
		self.oas_graphicsView.setScene(self.oas_scene)
		self.connectionCollector=DC.DrawConnection(self.oas_scene)
		self.oas_scene.addItem(self.connectionCollector)

		self.inC_inputs_collection={
								"oas_scene":self.oas_scene, 
								"lastPosition":self.lastPosition, 
								"addNode":self.addNode, 
								"getavailableNodeList":self.getavailableNodeList, 
								"save_file":self.save_file, 
								"save_fileAs":self.save_fileAs, 
								"new_file":self.new_file, 
								"open_file":self.open_file, 
								"import_file":self.import_file, 
								"delete_node":self.delete_node, 
								"duplicateNode":self.duplicateNode, 
								"do_run":self.do_run,
								"cleanE":self.cleanE,
								"do_generate":self.do_generate
								}

		self.nodeDraw_inputs_collection={
								"oas_scene":self.oas_scene,
								"connect_finally":self.connect_finally,
								"connect_tmp":self.connect_tmp,
								"pos_tmp":self.pos_tmp,
								"del_tmp":self.del_tmp,
								"delete_connection":self.delete_connection,
								"delete_node":self.delete_node,
								"node_position":self.node_position,
								"duplicateNode":self.duplicateNode,
								"setEndNode":self.setEndNode,
								"attributeE":self.attributeE,
								"add_newAttribute":self.add_newAttribute,
								"remove_Attribute":self.remove_Attribute,
								"varCategory":self.varCategory
								}

		self.inC=IC.DrawConnection(self.inC_inputs_collection)
		self.oas_scene.addItem(self.inC)

		self.oas_graphicsView.centerOn(QtCore.QPointF(-2000,-2000))

		self.timeline_start()

		QtCore.QObject.connect(self.oas_nodeName, QtCore.SIGNAL("editingFinished()"),self.rename)

		QtCore.QObject.connect(self.oas_new_bu, QtCore.SIGNAL("clicked()"),self.new_file)
		QtCore.QObject.connect(self.oas_open_bu, QtCore.SIGNAL("clicked()"),self.open_file)
		QtCore.QObject.connect(self.oas_save_bu, QtCore.SIGNAL("clicked()"),self.save_file)
		QtCore.QObject.connect(self.oas_saveas_bu, QtCore.SIGNAL("clicked()"),self.save_fileAs)
		QtCore.QObject.connect(self.oas_run_bu, QtCore.SIGNAL("clicked()"),self.do_run)
		QtCore.QObject.connect(self.oas_search_bu, QtCore.SIGNAL("clicked()"),self.do_search)

		QtCore.QObject.connect(self.oas_attribute_cache, QtCore.SIGNAL("stateChanged(int)"),self.nodeSettingE)

		QtCore.QObject.connect(self.oas_sframe_spin, QtCore.SIGNAL("valueChanged(int)"),self.setFramerange)
		QtCore.QObject.connect(self.oas_eframe_spin, QtCore.SIGNAL("valueChanged(int)"),self.setFramerange)
		QtCore.QObject.connect(self.oas_cframe_spin, QtCore.SIGNAL("valueChanged(int)"),self.setFrame)
		QtCore.QObject.connect(self.oas_firstF, QtCore.SIGNAL("clicked()"),self.setToFirstFrame)
		QtCore.QObject.connect(self.oas_lastF, QtCore.SIGNAL("clicked()"),self.setToLastFrame)


def main(args):
	a=QtGui.QApplication(args)
	ui = GUI_main(args)
	ui.show()
	sys.exit(a.exec_())

if __name__ == "__main__":
	main(sys.argv[1:])
