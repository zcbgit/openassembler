# $Id$
# -*- coding: utf-8 -*-

import sys
import os
import imp

class dBase_Init(object):

	def dBase_builder(self):
		self.oas_rt = {}
		self.oas_rt_connections = {}
		self.oas_scene_setup = {'startframe': 100,'frame':100,'endframe':200,'endnode':""}
		self.oas_save_filename = ""
		self.oas_last_node_created = ""
		self.setup_contents = self.oas_load_setup()
		self.manualPath = self.manuPath(self.setup_contents)
		self.oas_variablecategory = self.register_variable(self.setup_contents)
		self.oas_node_list = self.oas_collect_nodes_from_dirs(self.manualPath)
		self.oas_menucategories = self.oas_menucategory_settings(self.oas_load_setup(), self.oas_node_list)
		self.oas_register_variable_with_cat(self.oas_variablecategory, self.oas_node_list)

	def reloadMenucats(self):
		self.setup_contents=self.oas_load_setup()
		self.manualPath=self.manuPath(self.setup_contents)
		self.oas_node_list=self.oas_collect_nodes_from_dirs(self.manualPath)
		self.oas_menucategories=self.oas_menucategory_settings(self.oas_load_setup())

	def register_variable(self, setupfilecontent):
		variablecategory = {}
		for i in range(0, len(setupfilecontent)):
			if setupfilecontent[i][0] == "variablecategory":
				variable_types = setupfilecontent[i][2].split(",")
				for variable_type in variable_types:
					variablecategory[variable_type] = setupfilecontent[i][1]
		return variablecategory

	def oas_load_setup(self):
		cur_dir = os.getcwd()
		oas_setupFile = os.path.join(cur_dir, "settings/OpenAssembler.ini")
		if not os.path.isfile(oas_setupFile):
			sys.exit()
		file = open(oas_setupFile, "r")
		setupFile_Content = file.read()
		setupFile_Content = setupFile_Content.replace("\r\n", "\n")
		file.close()
		setupFile_Content = setupFile_Content.split("\n")
		setup_parsed = []
		for rws in setupFile_Content:
			ret = rws.split()
			if len(ret) > 0:
				if str(rws[:1]) != str("#"):
					setup_parsed.append(ret)
		return setup_parsed

	def oas_menucategory_settings(self, parsed, nodelist):
		mncline = {}
		for lines in parsed:
			if lines[0] == "menucategory":
				mncline[lines[1]] = []
				for i in range(2, len(lines)):
					for name, node in nodelist.iteritems():
						if node.tag == str(lines[i]):
							mncline[lines[1]].append(name)
		return mncline

	def oas_register_variable_with_cat(self, variablecategory, nodelist):
		"""to collect the variabletypes settings (for the connection check procedure)
		:param variablecategory:
		:param nodelist:
		:return:
		"""
		for node in nodelist.itervalues():
			for pin in node.input_pin.itervalues():
				variable_type = pin.variable_type
				if variable_type not in variablecategory:
					variablecategory[variable_type] = "undefined"
			for pin in node.output_pin.itervalues():
				variable_type = pin.variable_type
				if variable_type not in variablecategory:
					variablecategory[variable_type] = "undefined"

	def manuPath(self, setupfilecontent):
		folders = []
		cur_dir = os.getcwd()
		for i in range(0, len(setupfilecontent)):
			if setupfilecontent[i][0] == "manualpath":
				for it in setupfilecontent[i][1].split(","):
					folders.append(os.path.join(cur_dir, it))
		return folders

	def oas_collect_nodes_from_dirs(self, dirlist):
		"""
		This definition is collecting all the nodes from the directiories and parse them for the parameters
		:param dirlist:
		:return nodelist:
		"""
		nodelist = {}
		for singledir in dirlist:
			for root, dirs, files in os.walk(singledir):
				for file_name in files:
					suffix = os.path.basename(file_name)
					path = os.path.join(root, suffix)
					name, ext = os.path.splitext(suffix)
					if ext != ".py" or name == "__init__":
						continue
					module = imp.load_source(name, path)
					node = getattr(module, "C%s" % name.capitalize())
					node.setup()
					nodelist[node.node_type] = node

		return nodelist
