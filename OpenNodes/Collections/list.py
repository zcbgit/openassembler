# $Id$
# -*- coding: utf-8 -*-


from Core.Dbase.basenode import CBaseNode


class CList(CBaseNode):
	'''
	define
	{
		name list
		tag collections
		pre ""
		next ""
		input any in0 "" ""
		input_addable True
		output array1D result "" ""
	}
	'''

	@classmethod
	def generate(cls, node, inputs):
		code = """list_%s = [%s]"""
		return code % (node.name, ", ".join(inputs))
