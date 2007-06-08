# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import Integer32, OBJECT_TYPE, MODULE_IDENTITY
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_TC import DisplayString, TruthValue
from ENTITY_MIB import entPhysicalIndex
from HP_ICF_OID import hpicfObjectModules, hpicfCommon

class HP_ICF_STACK(ModuleObject):
	path = '/usr/share/snmp/mibs/site/HP-ICF-STACK'
	conformance = 5
	name = 'HP-ICF-STACK'
	language = 2
	description = 'This MIB module contains object definitions for\nmanaging HP stackable devices.'

# nodes
class hpicfStackMib(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 6])
	name = 'hpicfStackMib'

class hpicfStackConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 6, 1])
	name = 'hpicfStackConformance'

class hpicfStackCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 6, 1, 1])
	name = 'hpicfStackCompliances'

class hpicfStackGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 6, 1, 2])
	name = 'hpicfStackGroups'

class hpicfStack(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5])
	name = 'hpicfStack'


# macros
# types 
# scalars 
class hpicfStackActiveAgent(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpicfStackAgentForced(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5, 4])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


# columns
class hpicfStackBoxId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class hpicfStackBoxName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class hpicfStackAgentBoxId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


# rows 
class hpicfStackBoxEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([entPhysicalIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5, 1, 1])
	access = 2
	columns = {'hpicfStackBoxId': hpicfStackBoxId, 'hpicfStackBoxName': hpicfStackBoxName}


class hpicfStackAgentEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([entPhysicalIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5, 2, 1])
	access = 2
	columns = {'hpicfStackAgentBoxId': hpicfStackAgentBoxId}


# notifications (traps) 
# groups 
class hpicfStackBasicGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 6, 1, 2, 1])
	group = [hpicfStackBoxId, hpicfStackBoxName]

class hpicfStackMultiAgentGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 6, 1, 2, 2])
	group = [hpicfStackAgentBoxId, hpicfStackActiveAgent, hpicfStackAgentForced]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)