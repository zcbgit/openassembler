# $Id$
# -*- coding: utf-8 -*-


from Core.Dbase.basenode import CBaseNode


class CGet(CBaseNode):
	'''
	define
	{
		name get
		tag pymod
		input any obj "" ""
		input string attr "" ""
		output any result "" ""
	}
	'''

	@classmethod
	def generate(cls, node, inputs):
		code = """%(obj)s.%(attr)s"""
		return code % inputs
