# $Id$
# -*- coding: utf-8 -*-

from Core.Dbase.basenode import CBaseNode

class CReturn(CBaseNode):
	'''
	define
	{
		name return
		tag flowControl
		pre ""
		input_addable True
	}
	'''

	@classmethod
	def generate(cls, node, inputs):
		code = """return %s"""
		return code % ", ".join(inputs)
