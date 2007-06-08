# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, Unsigned32, mib_2
from SNMPv2_TC import TEXTUAL_CONVENTION

class T11_TC_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/T11-TC-MIB'
	conformance = 5
	name = 'T11-TC-MIB'
	language = 2
	description = 'This module defines textual conventions used in T11 MIBs.\n\nCopyright (C) The Internet Society (2006).  This version\nof this MIB module is part of RFC 4439;  see the RFC\nitself for full legal notices.'

# nodes
class t11TcMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 136])
	name = 't11TcMIB'


# macros
# types 

class T11FabricIndex(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(0, 4095))
	format = 'd'

# scalars 
# columns
# rows 
# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)