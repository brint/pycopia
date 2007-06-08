# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Counter32, Integer32, IpAddress
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoMgmt
from SNMPv2_TC import TEXTUAL_CONVENTION, RowStatus, TruthValue
from IF_MIB import ifIndex

class CISCO_VLAN_MEMBERSHIP_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-VLAN-MEMBERSHIP-MIB'
	conformance = 3
	name = 'CISCO-VLAN-MEMBERSHIP-MIB'
	language = 2
	description = 'The  MIB module for    the management    of   the\nVLAN Membership within  the frame  work of Cisco\nVLAN Architecture, v 2.0 by Keith McCloghrie. The MIB\nprovides information on VLAN Membership Policy Servers\nused by a device and VLAN membership assignments of\nnon-trunk bridge ports of the device.'

# nodes
class ciscoVlanMembershipMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68])
	name = 'ciscoVlanMembershipMIB'

class ciscoVlanMembershipMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1])
	name = 'ciscoVlanMembershipMIBObjects'

class vmVmps(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1])
	name = 'vmVmps'

class vmMembership(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2])
	name = 'vmMembership'

class vmStatistics(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3])
	name = 'vmStatistics'

class vmNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 2])
	name = 'vmNotifications'

class vmNotificationsPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 2, 0])
	name = 'vmNotificationsPrefix'

class vmMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 3])
	name = 'vmMIBConformance'

class vmMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1])
	name = 'vmMIBCompliances'

class vmMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2])
	name = 'vmMIBGroups'


# macros
# types 

class VlanIndex(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(1, 1023))

# scalars 
class vmVmpsVQPVersion(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class vmVmpsRetries(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class vmVmpsReconfirmInterval(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'Minutes'


class vmVmpsReconfirm(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'ready'), Enum(2, 'execute')]


class vmVmpsReconfirmResult(ScalarObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'inProgress'), Enum(3, 'success'), Enum(4, 'noResponse'), Enum(5, 'noVmps'), Enum(6, 'noDynamicPort'), Enum(7, 'noHostConnected')]


class vmVmpsCurrent(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class vmVQPQueries(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vmVQPResponses(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vmVmpsChanges(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vmVQPShutdown(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vmVQPDenied(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vmVQPWrongDomain(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vmVQPWrongVersion(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vmInsufficientResources(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# columns
class vmVmpsIpAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 7, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class vmVmpsPrimary(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 7, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class vmVmpsRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 7, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class vmMembershipSummaryVlanIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 1, 1, 1])
	syntaxobject = VlanIndex


class vmMembershipSummaryMemberPorts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class vmVlanType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'static'), Enum(2, 'dynamic')]


class vmVlan(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class vmPortStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'inactive'), Enum(2, 'active'), Enum(3, 'shutdown')]


# rows 
class vmVmpsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([vmVmpsIpAddress], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 7, 1])
	access = 2
	rowstatus = vmVmpsRowStatus
	columns = {'vmVmpsIpAddress': vmVmpsIpAddress, 'vmVmpsPrimary': vmVmpsPrimary, 'vmVmpsRowStatus': vmVmpsRowStatus}


class vmMembershipSummaryEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([vmMembershipSummaryVlanIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 1, 1])
	access = 2
	columns = {'vmMembershipSummaryVlanIndex': vmMembershipSummaryVlanIndex, 'vmMembershipSummaryMemberPorts': vmMembershipSummaryMemberPorts}


class vmMembershipEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1])
	access = 2
	columns = {'vmVlanType': vmVlanType, 'vmVlan': vmVlan, 'vmPortStatus': vmPortStatus}


# notifications (traps) 
class vmVmpsChange(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 2, 0, 1])

# groups 
class vmMembershipGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 1])
	group = [vmMembershipSummaryMemberPorts, vmVlan, vmVlanType, vmPortStatus]

class vmVQPClientGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 2])
	group = [vmVmpsVQPVersion, vmVmpsRetries, vmVmpsReconfirm, vmVmpsReconfirmInterval, vmVmpsReconfirmResult, vmVmpsCurrent, vmVmpsIpAddress, vmVmpsPrimary, vmVmpsRowStatus, vmVQPQueries, vmVQPResponses, vmVmpsChanges, vmVQPShutdown, vmVQPDenied, vmVQPWrongDomain, vmVQPWrongVersion, vmInsufficientResources]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)