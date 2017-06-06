# $Id$
# -*- coding: utf-8 -*-

DEFINE = {
	"name": "on_enter",
	"tag": "pymod",
	"input": {
		"obj": ("any", "", ""),
	},
	"output": {
		"obj": ("any", "", ""),
	},
	"code": """
def on_enter(%(input)s):
	%(output)s
""",
}

def generate():
	pass