#!/usr/bin/python

# This file generated by a program. do not edit.


import pycopia.XML.POM

#  xfdesktop-menu.dtd defines xfce4 desktop menu files. 


class Xfdesktop_menu(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'xfdesktop-menu'


class Menu(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('icon', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('visible', pycopia.XML.POM.Enumeration(['true', 'false']), 13, u'true'), 
         ])
	_name = u'menu'


#  name="Name in menu" icon="iconfile" visible="true" 


class App(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('cmd', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('icon', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('term', pycopia.XML.POM.Enumeration(['true', 'false']), 13, u'false'), 
         pycopia.XML.POM.XMLAttribute('snotify', pycopia.XML.POM.Enumeration(['true', 'false']), 13, u'false'), 
         pycopia.XML.POM.XMLAttribute('visible', pycopia.XML.POM.Enumeration(['true', 'false']), 13, u'true'), 
         ])
	_name = u'app'


#  name="Name" cmd="Command to run" term="false" icon="iconfile"  snotify="false" visible="true" 


class Separator(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('visible', pycopia.XML.POM.Enumeration(['true', 'false']), 13, u'true'), 
         ])
	_name = u'separator'


#  visible="true" 


class Include(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('type', pycopia.XML.POM.Enumeration(['file', 'system']), 13, u'file'), 
         pycopia.XML.POM.XMLAttribute('src', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('style', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('unique', pycopia.XML.POM.Enumeration(['true', 'false']), 13, u'true'), 
         pycopia.XML.POM.XMLAttribute('visible', pycopia.XML.POM.Enumeration(['true', 'false']), 13, u'true'), 
         ])
	_name = u'include'


#  type="file" src="menu2.xml" visible="true" 


#  type="system" style="simple" unique="true" 


class Title(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('icon', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('visible', pycopia.XML.POM.Enumeration(['true', 'false']), 13, u'true'), 
         ])
	_name = u'title'


#  title name="Name in menu" icon="iconfile" visible="true" 


class Builtin(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('cmd', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('icon', 1, 12, None), 
         ])
	_name = u'builtin'


#  name="Quit" cmd="quit" icon="gnome-logout" 


GENERAL_ENTITIES = {}