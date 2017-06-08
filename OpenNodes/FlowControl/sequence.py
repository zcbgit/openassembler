# $Id$
# -*- coding: utf-8 -*-

from Core.Dbase.basenode import CBaseNode

class CSequence(CBaseNode):
	'''
	define
	{
		name sequence
		tag flowControl
		pre ""
		next "Then 0"
		next_addable True
	}
'''

	@classmethod
	def generate(cls, node, inputs):
		pass