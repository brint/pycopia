# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE
from CISCO_TC import Unsigned32
from CISCO_SMI import ciscoMgmt
from SNMPv2_TC import TEXTUAL_CONVENTION, TimeStamp
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP

class CISCO_C8500_REDUNDANCY_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-C8500-REDUNDANCY-MIB'
	conformance = 3
	name = 'CISCO-C8500-REDUNDANCY-MIB'
	language = 2
	description = 'This MIB allows management of redundancy of CPU and \nswitch cards for the Catalyst 8540 switch, and other \nproducts with similar implementations.\n\n The Catalyst 8540 is an ATM switch. It has 13 (or, in\n some models, 14) slots, of which 2 slots can hold CPU\n cards, and 3 (or, in some models, 4) slots can hold\n switch cards. A switch card is one that contains the\n ATM switching fabric. Two switch cards are combined \n to operate in 20Gbps switching mode.\nFor CPU cards, 1+1 redundancy is supported.\nFor switch cards, 2+1 redundancy is supported.'

# nodes
class ciscoC8500RedundancyMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105])
	name = 'ciscoC8500RedundancyMIB'

class ciscoC8500RedundancyMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 1])
	name = 'ciscoC8500RedundancyMIBObjects'

class ccrCpu(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1])
	name = 'ccrCpu'

class ccrSwitch(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2])
	name = 'ccrSwitch'

class ciscoC8500RedundancyMIBNotificationPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 2])
	name = 'ciscoC8500RedundancyMIBNotificationPrefix'

class ccrMIBNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 2, 0])
	name = 'ccrMIBNotifications'

class ciscoC8500RedundancyMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 3])
	name = 'ciscoC8500RedundancyMIBConformance'

class ciscoC8500RedundancyMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 1])
	name = 'ciscoC8500RedundancyMIBCompliances'

class ciscoC8500RedundancyMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2])
	name = 'ciscoC8500RedundancyMIBGroups'


# macros
# types 

class RedundancyStatus(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'notPresent'), Enum(2, 'ok'), Enum(3, 'fault')]


class RedundancyMode(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'active'), Enum(2, 'standby'), Enum(3, 'unused'), Enum(4, 'notPresent')]


class RedundancySlotIndex(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(1, 65535))

# scalars 
class ccrSyncConfigOnSet(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class ccrSwitchLastSwitchoverTime(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 2])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class ccrSwitchLastSwitchoverReason(ScalarObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'none'), Enum(2, 'notKnown'), Enum(3, 'userInitiated'), Enum(4, 'cardFailed'), Enum(5, 'cardRecovered'), Enum(6, 'cardRemoved'), Enum(7, 'cardInserted')]


class ccrSwitchBw(ScalarObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'tenGbps'), Enum(2, 'twentyGbps')]


class ccrDesiredSwitchBw(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'tenGbps'), Enum(2, 'twentyGbps')]


# columns
class ccrCpuSlotIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1, 1, 1])
	syntaxobject = RedundancySlotIndex


class ccrCpuMode(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1, 1, 2])
	syntaxobject = RedundancyMode


class ccrCpuStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1, 1, 3])
	syntaxobject = RedundancyStatus


class ccrSwitchSlotIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1, 1, 1])
	syntaxobject = RedundancySlotIndex


class ccrSwitchMode(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1, 1, 2])
	syntaxobject = RedundancyMode


class ccrSwitchStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1, 1, 3])
	syntaxobject = RedundancyStatus


# rows 
class ccrCpuEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ccrCpuSlotIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1, 1])
	access = 2
	columns = {'ccrCpuSlotIndex': ccrCpuSlotIndex, 'ccrCpuMode': ccrCpuMode, 'ccrCpuStatus': ccrCpuStatus}


class ccrSwitchEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ccrSwitchSlotIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1, 1])
	access = 2
	columns = {'ccrSwitchSlotIndex': ccrSwitchSlotIndex, 'ccrSwitchMode': ccrSwitchMode, 'ccrSwitchStatus': ccrSwitchStatus}


# notifications (traps) 
class ccrCpuStatusChange(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 2, 0, 1])

class ccrSwitchStatusChange(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 2, 0, 2])

class ccrSwitchModeChange(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 2, 0, 3])

# groups 
class ccrCpuMibGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2, 1])
	group = [ccrCpuMode, ccrCpuStatus, ccrSyncConfigOnSet]

class ccrSwitchMibGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2, 2])
	group = [ccrSwitchMode, ccrSwitchStatus, ccrSwitchLastSwitchoverTime, ccrSwitchLastSwitchoverReason, ccrSwitchBw, ccrDesiredSwitchBw]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)