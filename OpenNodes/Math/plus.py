# $Id$
# -*- coding: utf-8 -*-

from Core.Dbase.basenode import CBaseNode

class CPlus(CBaseNode):
	'''
	define
	{
		name plus
		tag math
		input float A "" ""
		input float B "" ""
		output float result "" ""
	}
	'''

	@classmethod
	def generate(cls, node, inputs):
		code = """%(A)s + %(B)s"""
		return code % inputs
