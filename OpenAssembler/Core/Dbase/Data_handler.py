# $Id$
# -*- coding: utf-8 -*-

from random import *
from basenode import CPin
from variables import oas_variablechecker


class oas_data_handler(oas_variablechecker):
	"""this module is responsible for the runtime data management (and for all other data
	which is stored in memory)
	"""
	def oas_data_name2ID(self, mode="normal", name=""):

		for key in self.oas_rt.iterkeys():
			if self.oas_rt[key].name == name:
				return key
		else:
			if mode == "normal":
				print "[Error] Problem with name2ID with name: "+ name
			return 0

	def oas_data_ID2name(self,mode="normal",ID=""):
		try:
			return self.oas_rt[ID].name
		except:
			if mode == "normal":
				print "[Error] Problem with ID2name with ID: "+ ID
			return 0

	def oas_data_nodeInputs(self,mode="normal",ID=""):
		try:
			return self.oas_rt[ID].inputs_pin
		except:
			if mode == "normal":
				print "[Error] Problem with nodeInputs request on ID: " + ID
			return 0

	def oas_data_nodeOutputs(self,mode="normal",ID=""):
		try:
			return self.oas_rt[ID].output_pin
		except:
			if mode == "normal":
				print "[Error] Problem with nodeOutputs request on ID: " + ID
			return 0

	def generate_random_with_check(self):
		"""random generator for the nodes """
		while True:
			randomized = randrange(1000, 1000000)
			if not str("Node"+str(randomized)) in self.oas_rt:
				return randomized

	def generate_random_with_check_for_connection(self):
		"""random generator for the connections"""
		while True:
			randomized = randrange(1000, 1000000)
			if not str("Connection"+str(randomized)) in self.oas_rt_connections:
				return randomized

	def oas_data_list(self, mode="normal", listtype="nodetypes", searchtag=""):
		"""list the nodes or connections if the mode is normal it will give you back a list of the sorted nodes/connections
		:param mode:
		:param listtype:
		:param searchtag:
		:return nodes: list the nodes or connections
		"""
		returnvalue = []
		if listtype == "nodetypes":
			for ndtps in self.oas_node_list.iterkeys():
				if searchtag:
					if ndtps == searchtag:
						returnvalue.append(ndtps)
				else:
					returnvalue.append(ndtps)
		elif listtype == "scene":
			for ID, node in self.oas_rt.iteritems():
				if searchtag:
					if node.name == searchtag:
						returnvalue.append(node.name)
				else:
					returnvalue.append(node.name)
		elif listtype == "variables":
			for vtps in self.oas_variablecategory.iterkeys():
				returnvalue.append(vtps)
		elif listtype == "connections":
			for cns in self.oas_rt_connections.iterkeys():
				if searchtag:
					in_node = self.oas_rt_connections[cns]['in_node']
					out_node = self.oas_rt_connections[cns]['out_node']
					if searchtag in (self.oas_rt[in_node].name, self.oas_rt[out_node].name):
						returnvalue.append(cns)
				else:
					returnvalue.append(cns)
		if mode=="normal":
			print ""
			print "List ("+str(listtype)+"):"
			for v in returnvalue:
				print v	
			print ""
		return returnvalue

	def oas_show_attribute_parameters(self, mode="normal", node=""):
		"""this will show you the inputs and the outputs of the scene if mode is "silent" than doing nothing at this time
		:param mode:
		:param node:
		:return list: the inputs and the outputs
		"""
		global_return=[]
		ID = self.oas_data_name2ID(mode="normal", node="")
		node_obj = self.oas_rt.get(ID, None)
		if node_obj:
			for pin in node_obj.input_pin.itervalues():
					for con in self.oas_rt_connections.iterkeys():
						in_node = self.oas_rt_connections[con]['in_node']
						in_value = self.oas_rt_connections[con]['in_value']
						if self.oas_rt[in_node].name == node and in_value == pin.name:
							global_return.append((pin.name, pin.variable_type, pin.value, pin.options, True))
					else:
						global_return.append((pin.name, pin.variable_type, pin.value, pin.options, False))
		if mode == "normal":
			print global_return
		else:
			return global_return
			
	def oas_data_show(self,mode="normal",showtype="node"):
		nodlist=[]
		try:
			for kes in self.oas_rt.keys():
				if str(self.oas_rt[kes]['name'])==str(showtype):
					showtype=str(kes)
		except:
			pass
		if self.oas_rt.has_key(str(showtype)):
			if mode=="normal":
				print ""
				print "ID of the node: "+str(showtype)
				print "Name of the node: "+str(self.oas_rt[showtype]['name'])
				print "This node is a scene node!"
				print "Inputs:"
			nodlist.append(str(self.oas_rt[showtype]['name'])+":"+str(self.oas_rt[showtype]['nodetype'])+":"+str(showtype))
			nodlist.append(str(self.oas_rt[showtype]['posx'])+":"+str(self.oas_rt[showtype]['posy']))
			for ins in self.oas_rt[str(showtype)]['inputs'].keys():
				con_chk=0
				for con in self.oas_rt_connections.keys():
					if (self.oas_rt_connections[con]['in_node']==str(showtype) and self.oas_rt_connections[con]['in_value']==str(ins)):
						con_chk=1
				if con_chk==1:
					if mode=="normal":
						print "\t"+str(ins)+" = "+str(self.oas_rt[str(showtype)]['inputs'][str(ins)]['value'])+"\tConnected"
					nodlist.append("input."+str(ins)+"=*"+str(self.oas_rt[str(showtype)]['inputs'][str(ins)]['value']))
				else:
					if mode=="normal":
						print "\t"+str(ins)+" = "+str(self.oas_rt[str(showtype)]['inputs'][str(ins)]['value'])
					nodlist.append("input."+str(ins)+"="+str(self.oas_rt[str(showtype)]['inputs'][str(ins)]['value']))
			if mode=="normal":
				print "Outputs:"
			for ins in self.oas_rt[str(showtype)]['outputs'].keys():
				if mode=="normal":
					print "\t"+str(ins)+" = "+str(self.oas_rt[str(showtype)]['outputs'][str(ins)]['value'])
				nodlist.append("output."+str(ins)+"="+str(self.oas_rt[str(showtype)]['outputs'][str(ins)]['value']))
			if mode=="normal":
				print ""	
			return nodlist
		elif self.oas_node_list.has_key(str(showtype)):
			if mode=="normal":
				print ""
				print "Name of the node: "+str(showtype)
				print "This node is a nodetype template node!"
				print "Path to the sourcefile: "+str(self.oas_node_list[str(showtype)]['path'])
				print "Inputs:"
			nodlist.append((str(showtype)+":"+str(self.oas_node_list[showtype]['tag'])))
			for ins in self.oas_node_list[str(showtype)]['inputs'].keys():
				if mode=="normal":
					print "\t"+str(ins)+" = "+str(self.oas_node_list[str(showtype)]['inputs'][str(ins)]['value'])
				nodlist.append("input."+str(ins)+"="+str(self.oas_node_list[str(showtype)]['inputs'][str(ins)]['value']))
			if mode=="normal":
				print "Outputs:"
			for ins in self.oas_node_list[str(showtype)]['outputs'].keys():
				if mode=="normal":
					print "\t"+str(ins)+" = "+str(self.oas_node_list[str(showtype)]['outputs'][str(ins)]['value'])
				nodlist.append("output."+str(ins)+"="+str(self.oas_node_list[str(showtype)]['outputs'][str(ins)]['value']))
			if mode=="normal":
				print ""
			return nodlist
		elif self.oas_rt_connections.has_key(str(showtype)):
			if mode=="normal":
				print ""
				print self.oas_rt[self.oas_rt_connections[str(showtype)]['out_node']]['name']+"."+self.oas_rt_connections[str(showtype)]['out_value']+" --> "+self.oas_rt[self.oas_rt_connections[str(showtype)]['in_node']]['name']+"."+self.oas_rt_connections[str(showtype)]['in_value']
			nodlist=[str(self.oas_rt[self.oas_rt_connections[str(showtype)]['out_node']]['name']+"."+self.oas_rt_connections[str(showtype)]['out_value']),str(self.oas_rt[self.oas_rt_connections[str(showtype)]['in_node']]['name']+"."+self.oas_rt_connections[str(showtype)]['in_value'])]
			return nodlist
		elif showtype=="endnode":
			if mode=="normal":
				print "Endnode is: "+str(self.oas_scene_setup['endnode'])
			nodlist=[str(self.oas_scene_setup['endnode'])]
			return nodlist
		elif showtype=="framerange":
			if mode=="normal":
				print "From: "+str(self.oas_scene_setup['startframe'])+" to: "+str(self.oas_scene_setup['endframe'])
			return [str(self.oas_scene_setup['startframe']),str(self.oas_scene_setup['endframe'])]
		elif showtype=="frame":
			if mode=="normal":
				print "Frame: "+str(self.oas_scene_setup['frame'])
			return [str(self.oas_scene_setup['frame'])]
		elif showtype=="setup":
			if mode=="normal":
				print ""
			for ks in self.oas_scene_setup.keys():
				if mode=="normal":
					print str(ks)+" = "+ str(self.oas_scene_setup[ks])
				nodlist.append(str(ks)+" = "+ str(self.oas_scene_setup[ks]))
			if mode=="normal":
				print ""
			return nodlist
		else:
			if mode=="normal":
				print "[Error] In show: No node named: "+str(showtype)
			return 0

	def oas_data_count(self,mode="normal", counttype="nodetypes"):
		"""counts a node or a connection in the scene or in the oas_node_list if the mode is "silent" it is doing nothing.
		:param mode:
		:param counttype:
		:return:
		"""
		if counttype == "nodetypes":
			if mode == "normal":
				print "There is " + str(len(self.oas_node_list)) + " node in memory."
			return [str(len(self.oas_node_list))]
		elif counttype == "scene":
			if mode == "normal":
				print "There is "+str(len(self.oas_rt))+" node in the scene."
			return [str(len(self.oas_rt))]
		elif counttype == "connections":
			if mode == "normal":
				print "There is "+str(len(self.oas_rt_connections))+" connection."
			return [str(len(self.oas_rt_connections))]
		else: 
			if mode == "normal":
				print "[Error] In count: None-valid option given."
			return 0			

	def oas_data_create(self, mode="normal", nodetype="", posx=100, posy=100):
		"""this function creates a node with a given type.
		:param mode:
		:param nodetype:
		:param posx:
		:param posy:
		:return ID:
		"""
		node_class = self.oas_node_list.get(nodetype, None)
		if node_class:
			generated_random = str(self.generate_random_with_check())
			self.oas_rt["Node" + generated_random] = node_class(generated_random, posx, posy)
			self.oas_last_node_created = nodetype + generated_random
			if mode == "normal":
				print "Node "+str(str(nodetype)+generated_random)+" created."
			return str(str(nodetype)+generated_random)
		else:
			if mode == "normal":
				print "[Error] In create: Unknown nodetype"
			return 0

	def oas_data_duplicate(self, mode="normal", ID="", posx=100, posy=100):
		"""
		this function duplicate a node with a given ID.
		:param mode:
		:param ID:
		:param posx:
		:param posy:
		:return ID:
		"""
		if ID in self.oas_rt:
			old_node = self.oas_rt[ID]
			generated_random = str(self.generate_random_with_check())
			new_node = old_node.duplicate(generated_random, posx, posy)
			self.oas_rt["Node"+generated_random] = new_node
			self.oas_last_node_created = new_node.name
			if mode == "normal":
				print "Node "+ new_node.name + " created."
			return new_node.name
		else:
			if mode == "normal":
				print "[Error] In duplicate:Unknown nodetype"
			return 0

	def nameChecker(self, mode="normal", name=""):
		nameout=name
		for key in self.oas_rt.keys():
			if self.oas_rt[key].name == name:
				n=1
				while n==1:
					if self.oas_rt[key].name == name+str(n).zfill(3):
						pass
					else:
						nameout=name+str(n).zfill(3)
						n=2
		return str(nameout)

	def oas_data_delete(self, mode="normal", deletetype="node", target=""):
		"""
		this is deleting a node or connection(disconnect)
		:param mode:
		:param deletetype:
		:param target:
		:return node or connection:
		"""
		if str(deletetype) == "node":
			for node in self.oas_rt.values():
				if target in (node.ID, node.name):
					line_delete_list = self.oas_data_list(mode="silent", listtype="connections", searchtag=node.name)
					del self.oas_rt[node.ID]
					for con in line_delete_list:
						self.oas_data_delete(mode=mode, deletetype="connection", target=con)
					if mode == "normal":
						print "Node "+str(target)+" deleted."
					return node.name
			else:
				if mode == "normal":
					print "[Error] In delete: Node "+str(target)+" not found."
				return 0
		elif str(deletetype) == "connection":
			if target in self.oas_rt_connections:
				del self.oas_rt_connections[target]
				if mode == "normal":
					print "Connection "+str(target)+" deleted."
				return target
			else:
				if mode == "normal":
					print "[Error] In delete: Wrong connection name."
				return 0
		else:
			if mode == "normal":
				print "[Error] In delete: Wrong type option."
			return 0

	def oas_data_addInput(self,mode="normal",node="",variablename="",variabletype="any",defaultvalue=""):
		return self.oas_data_addPin("input", mode, node, variablename, variabletype, defaultvalue)

	def oas_data_addOutput(self, mode="normal", node="", variablename="", variabletype="string", defaultvalue=""):
		return self.oas_data_addPin("output", mode, node, variablename, variabletype, defaultvalue)

	def oas_data_addPin(self, type="input", mode="normal", node="", variablename="", variabletype="string", defaultvalue=""):
		if node != "" and variablename != "":
			ref_string = "qwertyuiopasdfghjklzxcvbnm1234567890_QWERTYUIOPASDFGHJKLZXCVBNM"
			result_new_name = ""
			for char in str(variablename):
				if ref_string.find(char) > -1:
					result_new_name += char
			variablename = result_new_name
			ID = self.oas_data_name2ID("normal", variablename)
			if not ID:
				if mode == "normal":
					print "[Error] In add %s_pin: Node not existing..." % type
				return 0
			node_obj = self.oas_rt[ID]
			pins = getattr(node_obj, "%s_pin" % type)
			if variablename in pins:
				if mode == "normal":
					print "[Error] In add %s_pin: Attribute already exsisting." % type
				return 0
			pin = CPin(variablename)
			if type in ("input", "output"):
				pin.variable_type = variabletype
				pin.value = defaultvalue
				pin.options = ""
			pins[variablename] = pin

			if mode == "normal":
				print "Attribute " + variablename + " was added to node " + node + " !"
			return variablename
		else:
			if mode == "normal":
				print "[Error] In add %s_pin: Problematic description." % type
			return 0

	def oas_data_delInput(self,mode="normal",node="", variablename=""):
		return self.oas_data_delPin("input", mode, node, variablename)

	def oas_data_delOutput(self,mode="normal",node="", variablename=""):
		return self.oas_data_delPin("output", mode, node, variablename)

	def oas_data_delPin(self, type="input", mode="normal", node="", variablename=""):
		if node and variablename:
			ID = self.oas_data_name2ID("normal", node)
			if not ID:
				if mode == "normal":
					print "[Error] In del %s_pin: Node not existing..." % type
				return 0
			node_obj = self.oas_rt[ID]
			pins = getattr(node_obj, "%s_pin" % type)
			if variablename not in pins:
				if mode == "normal":
					print "[Error] In del %s_pin: Attribute not existing." % type
				return 0
			original_pins = getattr(node_obj.__class__,  "%s_pin" % type)
			if variablename in original_pins:
				if mode == "normal":
					print "[Error] In del %s_pin: This is an original attribute for the node, you can not delete it!" % type
				return 0
			for cons in self.oas_rt_connections.keys():
				node_type = "in_node" if type == "input" else "out_node"
				value_type = "in_value" if type == "input" else "out_value"
				if self.oas_rt[self.oas_rt_connections[cons][node_type]] == ID and \
								self.oas_rt_connections[cons][value_type] == variablename:
					if not self.oas_data_delete(mode=mode, deletetype="connection", target=cons):
						if mode == "normal":
							print "[Error] In del %s_pin: Problem during the conneciton deletion" % type
						return 0
			del pins[variablename]
			if mode == "normal":
				print "Attribute " + str(variablename) + " was deleted!"
			return variablename
		else:
			if mode == "normal":
				print "[Error] In del %s_pin: Problematic description." % type
			return 0

	def oas_data_set(self,mode="normal",nodevalue="",value=""):
		if nodevalue!="":
			if len(nodevalue.split(".")):
				nodelists={}
				for noddd in self.oas_rt.keys():
					nodelists[self.oas_rt[noddd]['name']]=noddd
				if nodelists.has_key(nodevalue.split(".")[0]):
					if self.oas_rt[nodelists[nodevalue.split(".")[0]]]['inputs'].has_key(nodevalue.split(".")[1]):
						value=self.oas_variable(self.oas_rt[nodelists[nodevalue.split(".")[0]]]['inputs'][nodevalue.split(".")[1]]['variable_type'],value)
						self.oas_rt[nodelists[nodevalue.split(".")[0]]]['inputs'][nodevalue.split(".")[1]]['value']=value
						if mode=="normal":
							print str(nodevalue)+" was set to "+str(value)
						return [str(value)]
					elif self.oas_rt[nodelists[nodevalue.split(".")[0]]]['settings'].has_key(nodevalue.split(".")[1]):
						self.oas_rt[nodelists[nodevalue.split(".")[0]]]['settings'][nodevalue.split(".")[1]]=value
						if mode=="normal":
							print str(nodevalue)+" was set to "+str(value)
						return [str(value)]
					else:
						if mode=="normal":
							print "[Error] In set: Non existing input variable"
						return 0
				else:
					if mode=="normal":
						print "[Error] In set: None existing node..."
					return 0
			else:
				if mode=="normal":
					print "[Error] In set: Problematic description.."
				return 0

	def oas_data_positions(self, mode="normal", nodevalue="", posx=100, posy=100):
		if nodevalue and posx and posy:
			ID = self.oas_data_name2ID("normal", nodevalue)
			if ID:
				node = self.oas_rt[ID]
				node.posx = int(posx)
				node.posy = int(posy)
				return [posx, posy]
			else:
				if mode=="normal":
					print "[Error] In positions: None existing node..."
				return 0

	def oas_get_positions(self, mode="normal", nodevalue=""):
		if nodevalue:
			ID = self.oas_data_name2ID("normal", nodevalue)
			if ID:
				node = self.oas_rt[ID]
				return [node.posx, node.posy]
			else:
				if mode=="normal":
					print "[Error] In getpositions: None existing node..."
				return 0

# ##########################################################################
# rename a node can be normal 1 or silent 0 mode
# ##########################################################################
	
	def oas_data_rename(self,mode="normal",old="",new=""):
			if old!="" and new!="":
				if old == new:
					return [str(new)]
				ref_string="qwertyuiopasdfghjklzxcvbnm1234567890_QWERTYUIOPASDFGHJKLZXCVBNM"
				numb="1234567890"
				result_new_name=""
				for char in str(new):
					if ref_string.find(char)>-1:
						result_new_name+=char
				try:
					if numb.find(result_new_name[0])>-1:
						result_new_name=""
				except:
					result_new_name=""		
				new=result_new_name
				node=""
				for nds in self.oas_rt.keys():
					if str(self.oas_rt[nds]['name'])==str(old):
						node=str(nds)
				chk=False
				if str(new)!="":
					chk=True
					for nds in self.oas_rt.keys():
						if str(self.oas_rt[nds]['name'])==str(new):
							chk=False
				if self.oas_rt.has_key(node) and chk:
					self.oas_rt[node]['name']=str(new)
					if str(self.oas_last_node_created)==str(old):
						self.oas_last_node_created=str(new)
					if str(self.oas_scene_setup['endnode'])==str(old):
						self.oas_scene_setup['endnode']=str(new)
					if mode =="normal":
						print "Node "+str(old)+" is known as "+str(new)+" now."
					return [str(new)]
				else:
					if mode=="normal":
						print "[Error] In rename: Problem with the parameters!"
					return 0
			else:
				if mode =="normal":
					print "[Error] In rename: Not enough parameter!"
				return 0

# ####################################################################################
# this call will mark a node as an end node
# ####################################################################################
				
	def oas_data_end(self,mode="normal",endnode=""):
		chk=0
		if endnode!="":
			for nds in self.oas_rt.keys():
				if str(self.oas_rt[nds]['name'])==str(endnode):
					self.oas_scene_setup['endnode']=str(endnode)
					chk=1
		if chk==1:
			if mode=="normal":
				print "Node "+str(endnode)+" marked as endnode."
			return [str(endnode)]
		else:
			if mode=="normal":
				print "[Error] In set end: Wrong node."
			return 0	
		
		
# ####################################################################################
# set the framerange
# ####################################################################################
				
	def oas_data_framerange(self,mode="normal",firstframe="",endframe=""):
			if firstframe!="" and endframe!="":
				try:
					a=int(firstframe)
					b=int(endframe)
					if a>b:
						if mode=="normal":
							print "[Error] In framerange: Startframe is bigger than endframe!!"
						return 0
					else:
						self.oas_scene_setup['startframe']=a
						self.oas_scene_setup['endframe']=b
						if mode=="normal":
							print "Frame range are set."
						return [a,b]
				except:
					if mode=="normal":
						print "[Error] In framerange: Framerange values are wrong!"
					return 0
			else:
				if mode=="normal":
					print "[Error] In framerange: Wrong parameterlist!"
				return 0
		
		
# ####################################################################################
# set the currentframe
# ####################################################################################
				
	def oas_data_frame(self,mode="normal",frame=""):
		if frame!="":
			try:
				a=int(frame)
				self.oas_scene_setup['frame']=a
				if mode=="normal":
					print "Frame is set."
				return [a]
			except:
				if mode=="normal":
					print "[Error] In frame: Frame value are wrong!"
				return 0
		else:
			if mode=="normal":
				print "[Error] In frame: Wrong parameterlist!"
			return 0
		
				
# ####################################################################################
# create a connection between the nodes
# ####################################################################################
				
	def oas_data_connect(self,mode="normal",from_variable="",to_variable=""):
		if from_variable!="" and to_variable!="":
			node_out=""
			value_out=""
			if str(from_variable).find(".")>-1:
				for nds in self.oas_rt.keys():
					if str(self.oas_rt[nds]['name'])==str(from_variable.split(".")[0]):
						node_out=str(nds)
						for ots in self.oas_rt[node_out]['outputs'].keys():
							if str(ots)==str(from_variable.split(".")[1]):
								value_out=str(ots)
			else:
				pass
			node_in=""
			value_in=""
			if str(to_variable).find(".")>-1:
				for nds in self.oas_rt.keys():
					if str(self.oas_rt[nds]['name'])==str(to_variable.split(".")[0]):
						node_in=str(nds)
						for ots in self.oas_rt[node_in]['inputs'].keys():
							if str(ots)==str(to_variable.split(".")[1]):
								value_in=str(ots)
			else:
				pass
			con_chk=0
			for con in self.oas_rt_connections.keys():
				if (self.oas_rt_connections[con]['in_node']==str(node_in) and self.oas_rt_connections[con]['in_value']==str(value_in)):
					con_chk=1
			if con_chk==1:
				if mode=="normal":
					print "[Error] In connect: This node input is already connected, you need to disconnect first."
				return 0
			if node_out=="" or node_in=="" or value_out=="" or value_in=="" or node_in==node_out:
				if mode =="normal":
					print "[Error] In connect: Wrong parameters!"
				return 0
			else:
				# uncomment this if you want the: "input gets the output value on connection"
				#self.oas_rt[node_in]['inputs'][value_in]['value']=self.oas_rt[node_out]['outputs'][value_out]['value']
				in_type=str(self.oas_rt[node_in]['inputs'][value_in]['variable_type'])
				out_type=str(self.oas_rt[node_out]['outputs'][value_out]['variable_type'])
				if self.oas_variablecategory[in_type]==self.oas_variablecategory[out_type] or in_type=="any" or out_type=="any":
					rnd=self.generate_random_with_check_for_connection()
					self.oas_rt_connections[str("Connection"+str(rnd))]={'in_node':node_in,'out_node':node_out,'in_value':value_in,'out_value':value_out}
				else:
					if mode =="normal":
						print "[Error] In connect: You can not connect different parametertypes!"
					return 0
			if mode=="normal":
				print str(from_variable)+" ---> "+ str(to_variable) +" Connected."
			return [node_out+"."+value_out,node_in+"."+value_in,str("Connection"+str(rnd))]
		else:
			if mode =="normal":
				print "[Error] In connect: Not enough parameter."
			return 0
