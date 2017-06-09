# $Id$
# -*- coding: utf-8 -*-

import collections
import copy
import inspect
import variables


class CPin(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		s = []
		for key, value in self.__dict__.iteritems():
			if "__" in key:
				continue
			s.append("%s: %s" %(key, value))
		return "[" + ", ".join(s) + "]"


class CBaseNode(object):
	'''
	define
	{
		name base
		tag flowControl
		pre ""
		pre_addable True
		next ""
		next_addable True
		input any input "" ""
		input_addable True
		output any output "" ""
		output_addable True
	}
	'''

	def __init__(self, ID="", posx=100, posy=100):
		super(CBaseNode, self).__init__()
		self.ID = "Node" + ID
		self.posx = posx
		self.posy = posy
		if not hasattr(self, "node_type"):
			self.setup()
		self.name = self.node_type + ID
		self.pre_pin = copy.deepcopy(self.__class__.pre_pin)
		self.next_pin = copy.deepcopy(self.__class__.next_pin)
		self.input_pin = copy.deepcopy(self.__class__.input_pin)
		self.output_pin = copy.deepcopy(self.__class__.output_pin)

	def __str__(self):
		return """
Node %(ID)s[%(node_type)s|%(tag)s]
	name            : %(name)s
	pre_pin         : %(pre_pin)s
	pre_addable     : %(pre_addable)s
	next_pin        : %(next_pin)s
	next_addable    : %(next_addable)s
	input_pin       : %(input_pin)s
	input_addable   : %(input_addable)s
	output_pin      : %(output_pin)s
	output_addable  : %(output_addable)s""" % {
			"node_type": self.node_type,
			"tag": self.tag,
			"name": self.name,
			"ID": self.ID,
			"pre_pin": "{%s}" % ", ".join(["%s: %s" % (key, value) for key, value in self.pre_pin.iteritems()]),
			"pre_addable": self.pre_addable,
			"next_pin": "{%s}" % ", ".join(["%s: %s" % (key, value) for key, value in self.next_pin.iteritems()]),
			"next_addable": self.next_addable,
			"input_pin": "{%s}" % ", ".join(["%s: %s" % (key, value) for key, value in self.input_pin.iteritems()]),
			"input_addable": self.input_addable,
			"output_pin": "{%s}" % ", ".join(["%s: %s" % (key, value) for key, value in self.output_pin.iteritems()]),
			"output_addable": self.output_addable,
		}

	@classmethod
	def setup(cls):
		doc = inspect.getdoc(cls)
		doc = doc.replace("\r\n", "\n")
		if "define\n{" in doc:
			doc = doc.split("define\n{", 1)[1].split("}", 1)[0]
			doc = doc.split("\n")
			lines = []
			for line in doc:
				if line:
					lines.append(line.lstrip().strip())
			important_lines = []
			for line in lines:
				im_line = []
				for data in line.split(" ", 3):
					if data:
						im_line.append(data)
				if im_line:
					important_lines.append(im_line)

			setattr(cls, "pre_addable", False)
			setattr(cls, "next_addable", False)
			setattr(cls, "input_addable", False)
			setattr(cls, "output_addable", False)
			setattr(cls, "pre_pin", collections.OrderedDict())
			setattr(cls, "next_pin", collections.OrderedDict())
			setattr(cls, "input_pin", collections.OrderedDict())
			setattr(cls, "output_pin", collections.OrderedDict())

			for line in important_lines:
					item_name = line[0]
					if item_name == "name":
						setattr(cls, "node_type", line[1])
					elif item_name == "tag":
						setattr(cls, "tag", line[1])
					elif item_name in ("pre_addable", "next_addable", "input_addable", "output_addable") and line[1] == "True":
						setattr(cls, item_name, True)
					elif item_name in ("pre", "next"):
						pin_name = line[1].lstrip("\"").strip("\"")
						pin_dict = getattr(cls, "%s_pin" % item_name)
						if pin_name in pin_dict:
							raise RuntimeError("Redeclared %s_pin [%s] in %s." % (item_name, pin_name, cls.__name__))
						pin_dict[pin_name] = CPin(pin_name)
					elif item_name in ("input", "output"):
						pin_name = line[2]
						pin_dict = getattr(cls, "%s_pin" % item_name)
						if pin_name in pin_dict:
							raise RuntimeError("Redeclared %s_pin [%s] in %s." % (item_name, pin_name, cls.__name__))

						pin = CPin(pin_name)
						pin.variable_type = str(line[1])
						pin.value = ""
						pin.options = ""

						if len(line) > 3:
							cleanarray = []
							if "\"" in line[3]:
								for porc in line[3].split("\""):
									if porc == "":
										pass
									else:
										cleanarray.append(porc)
							else:
								for porc in line[3].split():
									if porc == "":
										pass
									else:
										cleanarray.append(porc)

							if len(cleanarray) > 1:
								default = cleanarray[0]
								default = default.lstrip("\"").strip("\"")
								pin.value = variables.oas_variablechecker.oas_variable(pin.variable_type, default)
								pin.options = cleanarray[1]

						pin_dict[pin_name] = pin

	def duplicate(self, ID, posx=100, posy=100):
		node = self.__class__(ID, posx, posy)
		node.pre_pin = copy.deepcopy(self.pre_pin)
		node.next_pin = copy.deepcopy(self.next_pin)
		node.input_pin = copy.deepcopy(self.input_pin)
		node.output_pin = copy.deepcopy(self.output_pin)
		return node


	@classmethod
	def generate(cls, node, inputs):
		raise NotImplementedError
