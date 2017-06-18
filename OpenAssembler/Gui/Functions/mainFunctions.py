# -*- coding: utf-8 -*-

import os
import json
import copy
from PyQt4 import QtCore, QtGui
import Gui.Node.nodeview as nodeview
from Gui.Window.ui_attribute_string import Ui_attribute_widget
import Core.Dbase.datahandler as datahandler


class CMainFunctions(datahandler.CDataHandler):

	def do_search(self):
		pass

	def attributeE(self, ID):
		if ID == self.inAE.get("ID", None):
			return
		self.cleanE()
		node_data = self.rt_nodes_tmp.get(ID)
		if not node_data:
			return
		self.inAE = {
			"ID": ID,
			"widget": {},
		}
		if not self.oas_splitter.sizes()[1]:
			self.oas_splitter.setSizes([700, 300])

		self.oas_nodeName.setText(node_data.name)
		self.oas_attribute_nodetype.setText(node_data.node_type)

		for key, pin in node_data.input_pin.iteritems():
			connections = self.get_pin_connections(ID, "input", key)
			status = "connected" if connections else "free"
			varT = pin.variable_type
			sablock = QtGui.QWidget(self.oas_attribute_area)
			Ui_attribute_widget().setupUi(sablock, key, pin.value, status, varT, self.nodeSetE)
			self.place_to_widgets.addWidget(sablock)
			self.inAE["widget"][key] = sablock

	def nodeSetE(self, attribute, value):
		self.set_input_value(self.inAE["ID"], attribute, value)
		self.oas_scene.mark_dirty()

	def cleanE(self):
		for widget in self.inAE.get("widget", {}).itervalues():
			self.place_to_widgets.removeWidget(widget)
			widget.close()
		self.inAE = {}
		self.oas_attribute_nodetype.setText("empty")
		self.oas_nodeName.setText("")

	def add_newAttribute(self, ID, add_type):
		if add_type not in ("pre", "next", "input", "output"):
			return
		node_data = self.rt_nodes_tmp.get(ID)
		if not node_data:
			print "[Error] In add_newAttribute: node %s not existed."
		if not getattr(node_data, "%s_auto_name" % add_type):
			ret_name = QtGui.QInputDialog.getText(self, "AddAttribute", "Name of the attribute:")
			attr_name = str(ret_name[0]).strip()
			if str(ret_name[1]) is not "True" or not attr_name:
				return
			attr_type = ""
			if add_type in ("input", "output"):
				ret_type = QtGui.QInputDialog.getText(self, "AddAttribute", "Type of the attribute:")
				attr_type = str(ret_type[0]).strip()
				if str(ret_type[1]) is not "True" and not attr_type:
					return
		else:
			attr_name = node_data.get_auto_name(add_type)
			attr_type = "any" if add_type not in ("input", "output") else ""

		if self.data_add_pin(ID, add_type, attr_name, attr_type):
			for item in self.oas_scene.items():
				if item.backID() == ID:
					item.add_pin(attr_name, attr_type)

		self.attributeE(ID)

	def remove_Attribute(self, ID, pin_type, attribute):
		for item in self.oas_scene.items():
			if item.backID() == ID:
				connections = self.get_pin_connections(ID, pin_type, attribute)
				if self.data_del_pin(ID, pin_type, attribute):
					item.remove_pin(pin_type, attribute)
					for cid in connections:
						self.connectionCollector.remove_connection(cid)

		self.attributeE(ID)

	def connect_finally(self, in_node_id, in_type, in_attr, out_node_id, out_type, out_attr):
		cid = self.data_connect(in_node_id, in_type, in_attr, out_node_id, out_type, out_attr)
		if not cid:
			return

		oitem, iitem = None, None
		for item in self.oas_scene.items():
			if item.backID() == out_node_id:
				oitem = item
			elif item.backID() == in_node_id:
				iitem = item

		if oitem and iitem:
			oitem.mark_connection(out_type, out_attr)
			iitem.mark_connection(in_type, in_attr)
		self.connectionCollector.add_connection(oitem, out_type, out_attr, iitem, in_type, in_attr, cid)

		if "ID" in self.inAE:
			self.attributeE(self.inAE["ID"])

	def addNode(self, nodetype):
		ID = self.data_create(nodetype)
		if ID:
			node_data = self.rt_nodes_tmp.get(ID)
			item = nodeview.CNodeView(ID, self.node_collection, node_data)
			item.setPos(self.last_point)
			self.data_positions(ID, self.last_point.x(), self.last_point.y())
			self.oas_scene.addItem(item)

	def duplicateNode(self, ID):
		ID = self.data_duplicate(ID)
		if ID:
			node_data = self.rt_nodes_tmp.get(ID)
			item = nodeview.CNodeView(ID, self.node_collection, node_data)
			item.setPos(self.last_point)
			self.data_positions(ID, self.last_point.x(), self.last_point.y())
			self.oas_scene.addItem(item)

	def expend_compound_node(self, nid):
		compound_node = self.rt_nodes_tmp.get(nid)
		if not compound_node:
			print "[ERROR] compound node %s not existed!" % nid
			return
		compound_data = self.rt_compounds_tmp.get(nid)
		if not compound_data:
			print "[ERROR] data of compound node %s not existed!" % nid
			return
		self.new_graphics_view(nid, str(nid))
		self.show_graphics_view(compound_data)
		self.cleanE()

	def do_generate(self):
		currentfile = QtGui.QFileDialog.getSaveFileName(self, 'Save Python Script from Network!', 'untitled.py')
		if currentfile=="":
			return 0
		self.oas_run_execute(file=currentfile)

	def delete_node(self, ID):
		node_data = self.rt_nodes_tmp.get(ID)
		if node_data.is_compound:
			self.close_graphics_view(str(ID))
		if not self.data_delete("node", ID):
			return
		if ID == self.inAE.get("ID"):
			self.cleanE()
		for item in self.oas_scene.items():
			if item.backID() == ID:
				for pin_type, pin_name in item.all_pins:
					self.delete_connection(ID, pin_type, pin_name)
				self.oas_scene.removeItem(item)

	def delete_connection(self, ID, pin_type, pin_name):
		connections = self.get_pin_connections(ID, pin_type, pin_name)
		for cid in connections:
			conn = self.rt_connections_tmp[cid]
			for item in self.oas_scene.items():
				if item.backID() == conn.in_node:
					item.unmark_connection(conn.in_type, conn.in_attr)
				elif item.backID() == conn.out_node:
					item.unmark_connection(conn.out_type, conn.out_attr)
			if not self.data_delete("connection", cid):
				print "Serious Problem with the nodes and connections, please restart!"
			self.connectionCollector.remove_connection(cid)

		if "ID" in self.inAE:
			self.attributeE(self.inAE["ID"])

	def node_position(self):
		for item in self.oas_scene.selectedItems():
			if item.backID() != "connection":
				pos = item.scenePos()
				self.data_positions(item.backID(), pos.x(), pos.y())

	def save_file(self):
		if not self.cur_save_filename:
			self.cur_save_filename = QtGui.QFileDialog.getSaveFileName(self, 'Save OpenAssebler Network!',
																	   'untitled.json')
			if not self.cur_save_filename:
				return 0
		self.oas_file_save(self.cur_save_filename)

	def show_root_view(self):
		root_data = self.rt_compounds_tmp[self.root_id]
		self.new_graphics_view(self.root_id, str(self.root_id))
		self.show_graphics_view(root_data)

	def new_file(self):
		self.tab_close_requested(0)
		self.rebuild_runtime()
		self.root_id = self.data_create("compound")
		self.show_root_view()
		self.fit_in_view()
		self.cleanE()

	def open_file(self):
		currentfile = QtGui.QFileDialog.getOpenFileName(self, 'Open OpenAssembler Nerwork!', '', self.tr("Files (*.*)"))
		if not currentfile:
			return
		self.tab_close_requested(0)
		self.rebuild_runtime()
		if not self.oas_file_open(str(currentfile)):
			return

		self.show_root_view()
		self.cleanE()

	def show_graphics_view(self, data):
		if data:
			nodes = data.get("nodes", [])
			connections = data.get("connections", [])
			for nid in nodes:
				node_data = self.rt_nodes_tmp.get(nid)
				item = nodeview.CNodeView(nid, self.node_collection, node_data)
				item.setPos(QtCore.QPointF(node_data.posx, node_data.posy))
				self.oas_scene.addItem(item)
			for cid in connections:
				conn = self.rt_connections_tmp[cid]
				in_node, in_type, in_attr = conn.in_node, conn.in_type, conn.in_attr
				out_node, out_type, out_attr = conn.out_node, conn.out_type, conn.out_attr
				oitem, iitem = None, None
				for item in self.oas_scene.items():
					if item.backID() == out_node:
						oitem = item
					elif item.backID() == in_node:
						iitem = item
				if oitem and iitem:
					oitem.mark_connection(out_type, out_attr)
					iitem.mark_connection(in_type, in_attr)
					self.connectionCollector.add_connection(oitem, out_type, out_attr, iitem, in_type, in_attr, cid)

			self.fit_in_view()
		self.oas_scene.is_init_finished = True
		self.cleanE()

	def fit_in_view(self, selected=None):
		fx, fy, sx, sy = [], [], [], []
		if not selected:
			selected = self.oas_scene.items()
		for item in selected:
			if str(item.backID()) != "connection":
				bb = item.boundingRect()
				fx.append(item.mapToScene(bb).value(0).x())
				fy.append(item.mapToScene(bb).value(0).y())
				sx.append(item.mapToScene(bb).value(2).x())
				sy.append(item.mapToScene(bb).value(2).y())

		if not fx:
			return

		lx, ly, ux, uy = min(fx), min(fy), max(sx), max(sy)
		cx, cy = (lx + ux) / 2, (ly + uy) / 2
		w = ux - lx
		if w < 800:
			w = 800
		h = uy - ly
		if h < 800:
			h = 800
		self.graphicsView.fitInView(QtCore.QRectF(cx - (w / 2), cy - (h / 2), w, h), QtCore.Qt.KeepAspectRatio)

	def lastPosition(self, x, y):
		self.last_point = QtCore.QPointF(x, y)

	def connect_tmp(self, node_id, pin_type, pin_name):
		for item in self.oas_scene.items():
			if item.backID() == node_id:
				oitem = item
				self.connectionCollector.addTmpConnection(oitem, pin_type, pin_name)
				self.oas_scene.update()
				return

	def pos_tmp(self, x, y):
		self.connectionCollector.mousePos(x, y)
		self.oas_scene.update()

	def oas_file_save(self, filename=""):
		if filename:
			if os.path.exists(os.path.dirname(str(filename))):
				all_rt = {"root": self.root_id}
				for compound_nid, compound_data in self.rt_compounds.iteritems():
					nodes, connections = [], []
					for nid in compound_data["nodes"]:
						nodes.append(self.rt_nodes[nid].get_rt())
					for cid in compound_data["connections"]:
						connections.append(self.rt_connections[cid].get_rt())
					all_rt[str(compound_nid)] = {
						"nodes": nodes,
						"connections": connections,
					}

				with open(str(filename), "w") as fw:
					json.dump(all_rt, fw, ensure_ascii=False)
				print "File saved."
				self.cur_save_filename = str(filename)
				return str(filename)
			else:
				print "[Error] In save: Wrong path."
				return 0
		else:
			print "[Error] In save: Wrong parameters."
			return 0

	def oas_file_open(self, filename=""):
		if not filename:
			print "[Error] In open: Wrong parameters."
			return 0
		if not os.path.exists(str(filename)):
			print "[Error] In open: Wrong path."
			return 0

		with open(str(filename), "r") as fr:
			try:
				rt = json.load(fr)
			except:
				print "[Error] In open: File format error."
				return
			self.root_id = self.data_create("compound", 0, 0, rt.pop("root"))
			for compound_nid, compound_data in rt.iteritems():
				compound_nodes, compound_connections = set(), set()
				for node_rt in compound_data["nodes"]:
					node_id, node_type, posx, posy = node_rt["id"], str(node_rt["node_type"]), node_rt["posx"], node_rt[
						"posy"]
					node_name = self.data_create(node_type, posx, posy, node_id)
					if not node_name:
						print "[Error] In open: Problem with: " + node_type
						continue
					if not self.data_positions(node_id, posx, posy):
						print "[Error] In open: Problem with the positions..."
						continue
					node = self.rt_nodes_tmp.get(node_id)
					compound_nodes.add(node_id)
					for pin_type in ["pre", "next", "input", "output"]:
						pin_dict = getattr(node, "%s_pin" % pin_type)
						for pin_rt in node_rt[pin_type]:
							pin_name = str(pin_rt["name"])
							variable_type = str(pin_rt.get("variable_type", ""))
							value = pin_rt.get("value", "")
							if pin_name not in pin_dict:
								if not self.data_add_pin(node_id, pin_type, pin_name, variable_type, value):
									print "[Error] In open: Problem with %s pin [%s] of %s creation!" % (
									pin_type, pin_name, node_name)
									continue
							if pin_type == "input":
								node.input_pin[pin_name].value = value

				for con_rt in compound_data["connections"]:
					in_node, in_type, in_attr = con_rt["in_node"], str(con_rt["in_type"]), str(con_rt["in_attr"])
					out_node, out_type, out_attr = con_rt["out_node"], str(con_rt["out_type"]), str(con_rt["out_attr"])
					cid = self.data_connect(in_node, in_type, in_attr, out_node, out_type, out_attr)
					if not cid:
						print "[Error] In open: Problem when connectiong nodes."
						continue
					compound_connections.add(cid)

				self.rt_compounds_tmp[int(compound_nid)] = {
					"nodes": compound_nodes,
					"connections": compound_connections
				}
			# 拷贝
			self.rt_nodes = copy.deepcopy(self.rt_nodes_tmp)
			self.rt_connections = copy.deepcopy(self.rt_connections_tmp)
			self.rt_compounds = copy.deepcopy(self.rt_compounds_tmp)
			self.cur_save_filename = filename
			return filename

	def get_pin_connections(self, node_id, pin_type, pin_name):
		clist = []
		for conn in self.rt_connections_tmp.itervalues():
			if (conn.in_node == node_id and conn.in_type == pin_type and conn.in_attr == pin_name) or \
					(conn.out_node == node_id and conn.out_type == pin_type and conn.out_attr == pin_name):
				clist.append(conn.cid)
		return clist

	def oas_run_execute(self, save_file="", runmode="normal", softwarename=""):
		self.runmode = runmode
		self.softwarename = softwarename

		entrance_functions = {}
		for node in self.rt_nodes.itervalues():
			if node.node_type == "entry":
				entrance_functions[node.name] = self.node_generate(node)

		py = self.oas_create_pyfile(entrance_functions)
		if save_file:
			with open(save_file, "w") as fw:
				fw.write(py)

	def node_generate(self, node):
		in_next = {}
		node_id = node.ID
		for con in self.rt_connections.itervalues():
			if con.in_node == node_id:
				out_node_id = con.out_node
				out_node = self.rt_nodes[out_node_id]
				in_type = con.in_type
				in_attr = con, in_attr
				nodetype = out_node["nodetype"]
				if out_node.node_type == "entry":
					in_value = out_node.name + "_" + con.out_attr
				else:
					in_value = self.node_generate(out_node)
				in_next[in_attr] = in_value
		for key, pin in node.input_pin.iteritems():
			if key in in_next:
				continue
			# variable_type = pin.variable_type
			in_next[key] = pin.value
		return node.generate(in_next)

	def oas_create_pyfile(self, entrance_functions):
		py = """from x_event import *
	%(functions)s
	"""
		functions = "\n".join(entrance_functions.values())
		return py % {"functions": functions}
