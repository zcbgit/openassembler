# $Id: basenode.py 274620 2017-06-16 03:26:53Z gzzhangchuanbin@CORP.NETEASE.COM $
# -*- coding: utf-8 -*-

import collections
import copy


class CPin(object):
	def __init__(self, name, is_original=False):
		self.name = name
		self.is_original = is_original

	def get_rt(self):
		ret = {
			"name": self.name,
			"is_original": self.is_original
		}
		if hasattr(self, "value") and hasattr(self, "variable_type") and hasattr(self, "options"):
			ret["value"] = self.value
			ret["variable_type"] = self.variable_type
			ret["options"] = self.options
		return ret

	def __str__(self):
		s = []
		for key, value in self.__dict__.iteritems():
			if "__" in key:
				continue
			s.append("%s: %s" %(key, value))
		return "[" + ", ".join(s) + "]"


class CBaseNode(object):
	def __init__(self, ID, posx=100, posy=100, base=None):
		super(CBaseNode, self).__init__()
		self.ID = ID
		self.posx = posx
		self.posy = posy
		self.node_type = None
		self.tag = None
		self.menu_name = None
		self.is_compound = False
		self.pre_addable = False
		self.pre_auto_name = False
		self.next_addable = False
		self.next_auto_name = False
		self.input_addable = False
		self.input_auto_name = False
		self.output_addable = False
		self.output_auto_name = False
		self.pre_pin = None
		self.next_pin = None
		self.input_pin = None
		self.output_pin = None
		self.code = None
		if base:
			self.on_create(base)

	def __str__(self):
		return """
Node %(ID)s[%(node_type)s|%(tag)s]
	name            : %(name)s
	pre_pin         : %(pre_pin)s
	pre_addable     : %(pre_addable)s
	pre_auto_name   : %(pre_auto_name)s
	next_pin        : %(next_pin)s
	next_addable    : %(next_addable)s
	next_auto_name  : %(next_auto_name)s
	input_pin       : %(input_pin)s
	input_addable   : %(input_addable)s
	input_auto_name : %(input_auto_name)s
	output_pin      : %(output_pin)s
	output_addable  : %(output_addable)s
	output_auto_name: %(output_auto_name)s""" % {
			"node_type": self.node_type,
			"tag": self.tag,
			"name": self.name,
			"ID": self.ID,
			"pre_pin": "{%s}" % ", ".join(["%s: %s" % (key, value) for key, value in self.pre_pin.iteritems()]),
			"pre_addable": self.pre_addable,
			"pre_auto_name": self.pre_auto_name,
			"next_pin": "{%s}" % ", ".join(["%s: %s" % (key, value) for key, value in self.next_pin.iteritems()]),
			"next_addable": self.next_addable,
			"next_auto_name": self.next_auto_name,
			"input_pin": "{%s}" % ", ".join(["%s: %s" % (key, value) for key, value in self.input_pin.iteritems()]),
			"input_addable": self.input_addable,
			"input_auto_name": self.input_auto_name,
			"output_pin": "{%s}" % ", ".join(["%s: %s" % (key, value) for key, value in self.output_pin.iteritems()]),
			"output_addable": self.output_addable,
			"output_auto_name": self.output_auto_name,
		}

	def on_create(self, base):
		for key, value in base.iteritems():
			if key in ("pre_pin", "next_pin", "input_pin", "output_pin"):
				pin_dict = collections.OrderedDict()
				if value:
					for pin_name, data in value.iteritems():
						pin = CPin(pin_name)
						for p_attr, pin_value in data.iteritems():
							setattr(pin, p_attr, pin_value)
						pin_dict[pin_name] = pin
				setattr(self, key, pin_dict)
			else:
				setattr(self, key, copy.deepcopy(value))

	@property
	def name(self):
		return "%s%d" % (self.node_type, self.ID)

	def duplicate(self, ID, posx=100, posy=100):
		duplicate_data = {
			"node_type": self.node_type,
			"tag": self.tag,
			"code": self.code,
			"menu_name": self.menu_name,
			"is_compound": self.is_compound,
			"pre_addable": self.pre_addable,
			"next_addable": self.next_addable,
			"input_addable": self.input_addable,
			"output_addable": self.output_addable,
			"pre_auto_name": self.pre_auto_name,
			"next_auto_name": self.next_auto_name,
			"input_auto_name": self.input_auto_name,
			"output_auto_name": self.output_auto_name,
		}
		for pin_type in ("pre_pin", "next_pin", "input_pin", "output_pin"):
			pin_data = collections.OrderedDict()
			pin_dict = getattr(self, pin_type, None)
			if pin_dict:
				for pin_name, pin in pin_dict.iteritems():
					pin_data[pin_name] = pin.get_rt()
			duplicate_data[pin_type] = pin_data

		node = self.__class__(ID, posx, posy, duplicate_data)
		return node

	def get_auto_name(self, pin_type):
		pin_dict = getattr(self, "%s_pin" % pin_type)
		pin_keys = pin_dict.keys()
		if not pin_keys:
			return "%s_0" % pin_type
		else:
			last = pin_keys[-1]
			next_num = int(last.split("_")[1]) + 1
			return "%s_%d" % (pin_type, next_num)

	def get_rt(self):
		return {
			"id": self.ID,
			"node_type": self.node_type,
			"pre": [pin.get_rt() for pin in self.pre_pin.itervalues()],
			"next": [pin.get_rt() for pin in self.next_pin.itervalues()],
			"input": [pin.get_rt() for pin in self.input_pin.itervalues()],
			"output": [pin.get_rt() for pin in self.output_pin.itervalues()],
			"posx": self.posx,
			"posy": self.posy,
		}

	def generate(self, in_next):
		raise NotImplementedError


def test():
	import Core.glb as glb
	doc = '''
			node_type base
			tag flowControl
			is_compound False
			menu_name 节点
			desc ""
			pre pre
			pre_auto_name True
			pre_addable True
			next next
			next_auto_name True
			next_addable True
			input any input "" ""
			input_auto_name True
			input_addable True
			output any output "" ""
			output_addable True
			output_auto_name True
			code ""
		'''
	define = glb.parse_node_doc(doc)
	A = CBaseNode("A", 0, 0, define)
	B = A.duplicate('B')
	B.input_pin["input"].value = "B"
	print A
	print B


if __name__ == '__main__':
	test()
