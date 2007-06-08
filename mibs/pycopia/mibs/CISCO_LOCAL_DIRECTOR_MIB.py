# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, NOTIFICATION_TYPE, OBJECT_TYPE, IpAddress, Counter32
from CISCO_TC import CiscoPort, Unsigned32
from CISCO_SMI import ciscoMgmt
from SNMPv2_TC import TEXTUAL_CONVENTION, TimeStamp
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP

class CISCO_LOCAL_DIRECTOR_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-LOCAL-DIRECTOR-MIB'
	conformance = 3
	name = 'CISCO-LOCAL-DIRECTOR-MIB'
	language = 2
	description = "The MIB module to view information about\nLocalDirector.\n\nThe Cisco LocalDirector is a device designed for the\npurpose of load balancing TCP traffic at an Internet\nsite.  To implement load balancing, an IP address (and\noptionally a port and a 'bind ID') is chosen to be the\npublically accessible 'virtual machine'. Then a number\nof actual Internet servers are 'bound' to this virtual\nmachine. The servers are called 'real machines'. The\nrelationships between virtual and real machines can be\none to many, many to one, or many to many.  More\ndetailed information about the LocalDirector is\navailable in the 'Cisco LocalDirector Installation and\nConfiguration Guide', available online at\nwww.cisco.com."

# nodes
class ciscoLocalDirectorMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99])
	name = 'ciscoLocalDirectorMIB'

class ciscoLocalDirectorMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1])
	name = 'ciscoLocalDirectorMIBObjects'

class cldVirtualMachine(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1])
	name = 'cldVirtualMachine'

class cldRealMachine(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2])
	name = 'cldRealMachine'

class cldFailover(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 3])
	name = 'cldFailover'

class ciscoLocalDirectorMIBNotificationPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 2])
	name = 'ciscoLocalDirectorMIBNotificationPrefix'

class ciscoLocalDirectorMIBNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 2, 0])
	name = 'ciscoLocalDirectorMIBNotifications'

class ciscoLocalDirectorMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 3])
	name = 'ciscoLocalDirectorMIBConformance'

class ciscoLocalDirectorMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 3, 1])
	name = 'ciscoLocalDirectorMIBCompliances'

class ciscoLocalDirectorMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 3, 2])
	name = 'ciscoLocalDirectorMIBGroups'


# macros
# types 

class CldMachineState(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'inService'), Enum(2, 'outOfService'), Enum(3, 'testing'), Enum(4, 'failed'), Enum(5, 'maxCapacity')]


class CldFailoverEnabledState(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'failoverOn'), Enum(2, 'failoverOff')]


class CldFailoverCableState(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'normalConnected'), Enum(2, 'otherSidePoweredOff'), Enum(3, 'mySideNotConnected'), Enum(4, 'otherSideNotConnected'), Enum(5, 'badCable')]


class CldFailoverUnitTypeDescriptor(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'primary'), Enum(2, 'secondary')]


class CldFailoverUnitStatusDescriptor(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'active'), Enum(2, 'standby')]

# scalars 
class cldFailoverEnabled(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 3, 1])
	syntaxobject = CldFailoverEnabledState


class cldFailoverCableStatus(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 3, 2])
	syntaxobject = CldFailoverCableState


class cldFailoverUnitType(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 3, 3])
	syntaxobject = CldFailoverUnitTypeDescriptor


class cldFailoverUnitStatus(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 3, 4])
	syntaxobject = CldFailoverUnitStatusDescriptor


class cldFailoverActiveTimeStamp(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 3, 5])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


# columns
class cldVirtualIpAddress(ColumnObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class cldVirtualPort(ColumnObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1, 2])
	syntaxobject = CiscoPort


class cldVirtualBindID(ColumnObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class cldVirtualState(ColumnObject):
	access = 4
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1, 4])
	syntaxobject = CldMachineState


class cldVirtualTotalConnections(ColumnObject):
	access = 4
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cldVirtualTotalPackets(ColumnObject):
	access = 4
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cldVirtualTotalBytes(ColumnObject):
	access = 4
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cldVirtualWeight(ColumnObject):
	access = 4
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class cldRealIpAddress(ColumnObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class cldRealPort(ColumnObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1, 1, 2])
	syntaxobject = CiscoPort


class cldRealState(ColumnObject):
	access = 4
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1, 1, 3])
	syntaxobject = CldMachineState


class cldRealTotalConnections(ColumnObject):
	access = 4
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cldRealTotalPackets(ColumnObject):
	access = 4
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cldRealTotalBytes(ColumnObject):
	access = 4
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cldRealWeight(ColumnObject):
	access = 5
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


# rows 
class cldVirtualTableEntry(RowObject):
	status = 2
	index = pycopia.SMI.Objects.IndexObjects([cldVirtualIpAddress, cldVirtualPort, cldVirtualBindID], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 1, 1, 1])
	access = 2
	columns = {'cldVirtualIpAddress': cldVirtualIpAddress, 'cldVirtualPort': cldVirtualPort, 'cldVirtualBindID': cldVirtualBindID, 'cldVirtualState': cldVirtualState, 'cldVirtualTotalConnections': cldVirtualTotalConnections, 'cldVirtualTotalPackets': cldVirtualTotalPackets, 'cldVirtualTotalBytes': cldVirtualTotalBytes, 'cldVirtualWeight': cldVirtualWeight}


class cldRealTableEntry(RowObject):
	status = 2
	index = pycopia.SMI.Objects.IndexObjects([cldRealIpAddress, cldRealPort], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 1, 2, 1, 1])
	access = 2
	columns = {'cldRealIpAddress': cldRealIpAddress, 'cldRealPort': cldRealPort, 'cldRealState': cldRealState, 'cldRealTotalConnections': cldRealTotalConnections, 'cldRealTotalPackets': cldRealTotalPackets, 'cldRealTotalBytes': cldRealTotalBytes, 'cldRealWeight': cldRealWeight}


# notifications (traps) 
class ciscoLocalDirectorVirtualStateChange(NotificationObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 2, 0, 1])

class ciscoLocalDirectorRealStateChange(NotificationObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 2, 0, 2])

class ciscoLocalDirectorFailoverEnableChange(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 2, 0, 3])

class ciscoLocalDirectorFailoverCableChange(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 2, 0, 4])

class ciscoLocalDirectorFailoverUnitStatus(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 2, 0, 5])

# groups 
class ciscoLocalDirectorMIBGroup(GroupObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 3, 2, 1])
	group = [cldVirtualState, cldVirtualTotalConnections, cldVirtualTotalPackets, cldVirtualTotalBytes, cldVirtualWeight, cldRealState, cldRealTotalConnections, cldRealTotalPackets, cldRealTotalBytes, cldRealWeight, cldFailoverEnabled, cldFailoverCableStatus, cldFailoverUnitType, cldFailoverUnitStatus, cldFailoverActiveTimeStamp]

class ciscoLocalDirectorFailoverGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 99, 3, 2, 2])
	group = [cldFailoverEnabled, cldFailoverCableStatus, cldFailoverUnitType, cldFailoverUnitStatus, cldFailoverActiveTimeStamp]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)