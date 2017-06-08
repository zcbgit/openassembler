# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.08
#
# #####################################################################################

# #####################################################################################################################################
#
# This file is to handle the setup file and to init the software, collect the nodes and so..
#
# #####################################################################################################################################

import os, sys
import collections
import imp
from Core.Dbase.variables import oas_variablechecker


class oas_setup(oas_variablechecker):
	# #####################################################################################################################################
	# Here we load and parse the setup file
	# #####################################################################################################################################

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

	# #####################################################################################################################################
	# to collect the variabletypes settings (for the connection check procedure)
	# #####################################################################################################################################

	def oas_register_variable_with_cat(self, variablecategory, nodelist):
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


# #####################################################################################################################################
# This definition is collecting all the nodes from the directiories and parse them for the parameters
# #####################################################################################################################################
	def oas_collect_nodes_from_dirs(self, dirlist):
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
