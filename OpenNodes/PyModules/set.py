# $Id$
# -*- coding: utf-8 -*-

from Core.Dbase.basenode import CBaseNode


class CSet(CBaseNode):
	'''
	define
	{
		name set
		tag pymod
		pre ""
		next ""
		input any obj "" ""
		input string attr "" ""
		input any value "" ""
		output any result "" ""
	}
	'''

	@classmethod
	def generate(cls, node, inputs):
		code = """%(obj)s.%(attr)s = %(value)s\n"""
		return code % inputs
