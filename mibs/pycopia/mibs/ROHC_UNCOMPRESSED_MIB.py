# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32, mib_2
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from ROHC_MIB import rohcChannelID, rohcContextCID

class ROHC_UNCOMPRESSED_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/ROHC-UNCOMPRESSED-MIB'
	name = 'ROHC-UNCOMPRESSED-MIB'
	language = 2
	description = 'This MIB module defines a set of objects for monitoring\nand configuring RObust Header Compression (ROHC).\nThe objects are specific to ROHC uncompressed\n(profile 0x0000).\n\nCopyright (C) The Internet Society (2004). The\ninitial version of this MIB module was published\nin RFC 3816. For full legal notices see the RFC\nitself or see:\nhttp://www.ietf.org/copyrights/ianamib.html'

# nodes
class rohcUncmprMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 113])
	name = 'rohcUncmprMIB'

class rohcUncmprObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 113, 1])
	name = 'rohcUncmprObjects'

class rohcUncmprConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 113, 2])
	name = 'rohcUncmprConformance'

class rohcUncmprCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 113, 2, 1])
	name = 'rohcUncmprCompliances'

class rohcUncmprGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 113, 2, 2])
	name = 'rohcUncmprGroups'


# macros
# types 
# scalars 
# columns
class rohcUncmprContextState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 113, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'initAndRefresh'), Enum(2, 'normal'), Enum(3, 'noContext'), Enum(4, 'fullContext')]


class rohcUncmprContextMode(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 113, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unidirectional'), Enum(2, 'bidirectional')]


class rohcUncmprContextACKs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 113, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# rows 
class rohcUncmprContextEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([rohcChannelID, rohcContextCID], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 113, 1, 1, 1])
	access = 2
	columns = {'rohcUncmprContextState': rohcUncmprContextState, 'rohcUncmprContextMode': rohcUncmprContextMode, 'rohcUncmprContextACKs': rohcUncmprContextACKs}


# notifications (traps) 
# groups 
class rohcUncmprContextGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 113, 2, 2, 1])
	group = [rohcUncmprContextState, rohcUncmprContextMode]

class rohcUncmprStatisticsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 113, 2, 2, 2])
	group = [rohcUncmprContextACKs]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)