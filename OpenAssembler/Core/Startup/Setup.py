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

	def oas_menucategory_settings(self, parsed):
		mncline = {}
		for liness in parsed:
			if liness[0] == "menucategory":
				mncline[liness[1]] = []
				for i in range(2, len(liness)):
					for nd in self.oas_node_list.keys():
						if self.oas_node_list[nd]['tag'] == str(liness[i]):
							mncline[liness[1]].append(str(nd))
		mncline["OpenAssembler Core"] = ["_def"]
		return mncline

	# #####################################################################################################################################
	# to collect the variabletypes settings (for the connection check procedure)
	# #####################################################################################################################################

	def oas_register_variable_with_cat(self, setupfilecontent, variablecategory, var):
		cat = "undefined"
		for i in range(0, len(setupfilecontent)):
			if setupfilecontent[i][0] == "variablecategory":
				if setupfilecontent[i][2].find(str(var)) > -1:
					cat = str(setupfilecontent[i][1])
		variablecategory[str(var)] = cat

	def manuPath(self, setupfilecontent):
		folders = []
		for i in range(0, len(setupfilecontent)):
			if setupfilecontent[i][0] == "manualpath":
				cur_dir = os.getcwd()
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
					inputs = {}
					outputs = {}
					entry_name = module.DEFINE["name"]
					entry_tag = module.DEFINE["tag"]
					for in_key, in_value in module.DEFINE["input"].iteritems():
						variable_type, default, options = in_value
						self.oas_register_variable_with_cat(self.setup_contents, self.oas_variablecategory,
															variable_type)
						default = self.oas_variable(variable_type, default)
						inputs[in_key] = {'variable_type': variable_type, 'value': str(default), 'options': options}
					for out_key, out_value in module.DEFINE["output"].iteritems():
						variable_type, default, options = out_value
						self.oas_register_variable_with_cat(self.setup_contents, self.oas_variablecategory,
															variable_type)
						default = self.oas_variable(variable_type, default)
						outputs[out_key] = {'variable_type': variable_type, 'value': str(default), 'options': options}

						settings = {"_do_cache": "False"}
						nodelist[entry_name] = {
							'tag': entry_tag,
							'path': path,
							'inputs': inputs,
							'outputs': outputs,
							"settings": settings
						}

		settings_def = {"_do_cache": "False", "QtMainWindowUi": ""}
		nodelist["_def"] = {'tag': str("oascore"), 'path': str("OpenAssembler internal function"),
							'inputs': {"Input": {'variable_type': "any", 'value': "", 'options': ""},
									   "Hython": {'variable_type': "int", 'value': "0", 'options': ""},
									   "Nuke": {'variable_type': "int", 'value': "0", 'options': ""}}, 'outputs': {},
							"settings": settings_def}
		return nodelist
