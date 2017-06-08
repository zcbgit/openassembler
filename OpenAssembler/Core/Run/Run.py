# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.08
#
# #####################################################################################

import time, sys, os, shutil, time
from Core.Dbase.Data_handler import oas_data_handler
from Core.Dbase.FileIO import oas_fileio

A = {'Connection148276': {'out_value': 'result', 'in_node': 'Node315916', 'in_value': 'procedure',
						  'out_node': 'Node350307'},
	 'Connection847542': {'out_value': 'result', 'in_node': 'Node286903', 'in_value': 'value', 'out_node': 'Node77717'},
	 'Connection185577': {'out_value': 'result', 'in_node': 'Node350307', 'in_value': 'in1', 'out_node': 'Node286903'},
	 'Connection124600': {'out_value': 'obj', 'in_node': 'Node286903', 'in_value': 'obj', 'out_node': 'Node315916'},
	 'Connection631061': {'out_value': 'obj', 'in_node': 'Node826438', 'in_value': 'obj', 'out_node': 'Node315916'},
	 'Connection185060': {'out_value': 'result', 'in_node': 'Node77717', 'in_value': 'A', 'out_node': 'Node826438'}}


class oas_execute(oas_data_handler, oas_fileio):
	def oas_run_execute(self, save_file="", runmode="normal", softwarename=""):
		self.runmode = runmode
		self.softwarename = softwarename

		entrance_functions = {}
		for node_id in self.oas_rt.iterkeys():
			node = self.oas_rt[node_id]
			nodetype = node["nodetype"]
			if self.oas_node_list[nodetype]['tag'] != "entrance":
				continue
			entrance_functions[node["name"]] = self.node_generate(node)

		py = self.oas_create_pyfile(entrance_functions)
		if save_file:
			with open(save_file, "w") as fw:
				fw.write(py)

	def node_generate(self, node):
		inputs = {}
		for con in self.oas_rt_connections.iterkeys():
			if self.oas_rt[self.oas_rt_connections[con]['in_node']]['name'] == node["name"]:
				out_node = self.oas_rt[self.oas_rt_connections[con]['out_node']]
				in_name = self.oas_rt_connections[con]['in_value']
				nodetype = out_node["nodetype"]
				if self.oas_node_list[nodetype]['tag'] == "entrance":
					in_value = out_node["name"] +"_" + self.oas_rt_connections[con]['out_value']
				else:
					in_value = self.node_generate(out_node)
				inputs[in_name] = in_value
		for key, value in node["inputs"].iteritems():
			if key in inputs:
				continue
			variable_type = value["variable_type"]
			value_str = value["value"]
			if variable_type == 'string':
				value_str = "'%s'" % value_str
			inputs[key] = value_str
		nodetype = node["nodetype"]
		gen_func = self.oas_node_list[nodetype]["gen_func"]
		return gen_func(node, inputs)


	def oas_make_piramid(self, fin_node):
		level = []
		level_number = 0
		next_level_counter = 1
		level.append([fin_node])
		while next_level_counter != 0:
			tmp = self.oas_input_connections(level[level_number])
			if tmp == []:
				next_level_counter = 0
			else:
				level.append(tmp)
				level_number += 1
				next_level_counter = len(level[level_number])
		return level

	# ##############################################################################
	# calculate the final order from the levels, check vhen the node firs appear
	# ##############################################################################
	def oas_make_optimization(self, level):
		finallist = []
		for x in range(0, len(level)):
			reverse_x = len(level) - x - 1
			exist_chk = 0
			for lev in level[reverse_x]:
				for flm in finallist:
					if flm == lev:
						exist_chk = 1
				if exist_chk == 1:
					exist_chk = 0
				else:
					finallist.append(lev)
					exist_chk = 0
		return finallist

	def oas_input_connections(self, node_ins):
		ret = []
		for node in node_ins:
			for con in self.oas_rt_connections.keys():
				if self.oas_rt[self.oas_rt_connections[con]['in_node']]['name'] == str(node):
					ret.append(self.oas_rt[self.oas_rt_connections[con]['out_node']]['name'])
		return ret

	def oas_create_pyfile(self, entrance_functions):
		py = """from x_event import *
%(functions)s
"""
		functions = "\n".join(entrance_functions.values())
		return py % {"functions": functions}
