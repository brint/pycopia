# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoExperiment
from IF_MIB import ifIndex

class CISCO_C12000_IF_HC_COUNTERS_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-C12000-IF-HC-COUNTERS-MIB'
	conformance = 3
	name = 'CISCO-C12000-IF-HC-COUNTERS-MIB'
	language = 2
	description = 'A MIB module to describe and store IF-MIB High \nCapacity (ie 64 bit) Counters as two 32 bit \nobjects. This mib will ONLY be supported in the \n11.2GS version of IOS and will NOT be ported to \nany later versions.'

# nodes
class ciscoC12000IfHcCountersMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 31])
	name = 'ciscoC12000IfHcCountersMIB'

class cHCCounterMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 31, 1])
	name = 'cHCCounterMIBObjects'

class ciscoHCCountersMIBNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 31, 2])
	name = 'ciscoHCCountersMIBNotifications'

class ciscoHCCountersMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 31, 3])
	name = 'ciscoHCCountersMIBConformance'

class ciscoHCCountersMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 31, 3, 1])
	name = 'ciscoHCCountersMIBCompliances'

class ciscoHCCountersMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 31, 3, 2])
	name = 'ciscoHCCountersMIBGroups'


# macros
# types 
# scalars 
# columns
class cHCCounterIfInOctetsUpper(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cHCCounterIfInOctetsLower(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cHCCounterIfInUcastPktsUpper(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cHCCounterIfInUcastPktsLower(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cHCCounterIfOutOctetsUpper(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cHCCounterIfOutOctetsLower(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cHCCounterIfOutUcastPktsUpper(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cHCCounterIfOutUcastPktsLower(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# rows 
class cHCCounterEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1])
	access = 2
	columns = {'cHCCounterIfInOctetsUpper': cHCCounterIfInOctetsUpper, 'cHCCounterIfInOctetsLower': cHCCounterIfInOctetsLower, 'cHCCounterIfInUcastPktsUpper': cHCCounterIfInUcastPktsUpper, 'cHCCounterIfInUcastPktsLower': cHCCounterIfInUcastPktsLower, 'cHCCounterIfOutOctetsUpper': cHCCounterIfOutOctetsUpper, 'cHCCounterIfOutOctetsLower': cHCCounterIfOutOctetsLower, 'cHCCounterIfOutUcastPktsUpper': cHCCounterIfOutUcastPktsUpper, 'cHCCounterIfOutUcastPktsLower': cHCCounterIfOutUcastPktsLower}


# notifications (traps) 
# groups 
class ciscoHCCountersMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 31, 3, 2, 1])
	group = [cHCCounterIfInOctetsUpper, cHCCounterIfInOctetsLower, cHCCounterIfInUcastPktsUpper, cHCCounterIfInUcastPktsLower, cHCCounterIfOutOctetsUpper, cHCCounterIfOutOctetsLower, cHCCounterIfOutUcastPktsUpper, cHCCounterIfOutUcastPktsLower]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)