# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoExperiment
from SNMPv2_TC import TEXTUAL_CONVENTION, RowStatus
from IF_MIB import ifIndex

class CISCO_ATM_ADDR_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-ATM-ADDR-MIB'
	conformance = 132
	name = 'CISCO-ATM-ADDR-MIB'
	language = 2
	description = 'ATM address MIB'

# nodes
class ciscoAtmAddrMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 12])
	name = 'ciscoAtmAddrMIB'

class ciscoAtmAddrMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 12, 1])
	name = 'ciscoAtmAddrMIBObjects'

class ciscoAtmIfAdminAddrMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 12, 3])
	name = 'ciscoAtmIfAdminAddrMIBConformance'

class ciscoAtmIfAdminAddrMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 1])
	name = 'ciscoAtmIfAdminAddrMIBCompliances'

class ciscoAtmIfAdminAddrMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 2])
	name = 'ciscoAtmIfAdminAddrMIBGroups'


# macros
# types 

class AtmAddr(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 0), Range(8, 8), Range(13, 13), Range(20, 20))

# scalars 
# columns
class ciscoAtmIfAdminAddrAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1, 1])
	syntaxobject = AtmAddr


class ciscoAtmIfAdminAddrRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class ciscoAtmIfAdminAddrEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, ciscoAtmIfAdminAddrAddress], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1])
	access = 2
	rowstatus = ciscoAtmIfAdminAddrRowStatus
	columns = {'ciscoAtmIfAdminAddrAddress': ciscoAtmIfAdminAddrAddress, 'ciscoAtmIfAdminAddrRowStatus': ciscoAtmIfAdminAddrRowStatus}


# notifications (traps) 
# groups 
class ciscoAtmIfAdminAddrMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 2, 1])
	group = [ciscoAtmIfAdminAddrRowStatus]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)