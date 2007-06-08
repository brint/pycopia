# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Integer32, Counter32, IpAddress
from RFC1155_SMI import enterprises
from RFC1271_MIB import OwnerString
from SNMPv2_TC import RowStatus, TruthValue
from IGMP_STD_MIB import igmpInterfaceEntry

class CISCO_IPMCAST_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-IPMCAST-MIB'
	conformance = 2
	name = 'CISCO-IPMCAST-MIB'
	language = 2
	description = 'The MIB module for Cisco-specific management of IP\nMulticast in Cisco devices.'

# nodes
class ciscoMcastMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4])
	name = 'ciscoMcastMIB'

class ciscoMcastMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1])
	name = 'ciscoMcastMIBObjects'

class mcastAccess(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 1])
	name = 'mcastAccess'

class mcastTrace(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2])
	name = 'mcastTrace'

class mcastTraceRequest(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 1])
	name = 'mcastTraceRequest'

class mcastTraceResponse(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2])
	name = 'mcastTraceResponse'

class mcastFilter(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3])
	name = 'mcastFilter'

class ciscoMcastMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 2])
	name = 'ciscoMcastMIBConformance'

class ciscoMcastMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 2, 1])
	name = 'ciscoMcastMIBCompliances'

class ciscoMcastMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 2, 2])
	name = 'ciscoMcastMIBGroups'


# macros
# types 
# scalars 
class mrbranchState(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'inactive'), Enum(2, 'active')]


class mrbranchGroup(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class mrbranchBranch(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class mrbranchTimeout(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class mrbranchRequestor(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 1, 5])
	syntaxobject = OwnerString
	access = 5
	units = 'seconds'


class igmpConditionalFilteringEnable(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 1])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class igmpMemberReportTimeout(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


# columns
class pimRpAccessListRP(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class pimRpAccessListNumber(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class pimRpAccessListStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class igmpAccessListNumber(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mrbranchResponseResponder(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class mrbranchResponseRtt(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mrbranchResponseRPF(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class mrbranchInterfaceListAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class mrbranchInterfaceListNetMask(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class igmpCondFilterIfIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class igmpCondFilterIfStatus(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'routerPresent'), Enum(2, 'noRouter'), Enum(3, 'dynamic')]


class igmpCondFilterIfRouter(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class igmpCondFilterMcastIfIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class igmpCondFilterMcastAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class igmpCondFilterMcastMember(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class igmpCondFilterMcastInPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class igmpCondFilterMcastOutPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 4, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class igmpCondFilterMcastStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 4, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class pimRpAccessListEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([pimRpAccessListRP], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 1, 1, 1])
	access = 2
	rowstatus = pimRpAccessListStatus
	columns = {'pimRpAccessListRP': pimRpAccessListRP, 'pimRpAccessListNumber': pimRpAccessListNumber, 'pimRpAccessListStatus': pimRpAccessListStatus}


from IGMP_STD_MIB import igmpInterfaceIfIndex
class igmpAccessListEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([igmpInterfaceIfIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 1, 2, 1])
	access = 2
	columns = {'igmpAccessListNumber': igmpAccessListNumber}


class mrbranchResponseEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mrbranchResponseResponder], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2, 1, 1])
	access = 2
	columns = {'mrbranchResponseResponder': mrbranchResponseResponder, 'mrbranchResponseRtt': mrbranchResponseRtt, 'mrbranchResponseRPF': mrbranchResponseRPF}


class mrbranchInterfaceListEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mrbranchResponseResponder, mrbranchInterfaceListAddress], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2, 2, 1])
	access = 2
	columns = {'mrbranchInterfaceListAddress': mrbranchInterfaceListAddress, 'mrbranchInterfaceListNetMask': mrbranchInterfaceListNetMask}


class igmpCondFilterIfEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([igmpCondFilterIfIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 3, 1])
	access = 2
	columns = {'igmpCondFilterIfIndex': igmpCondFilterIfIndex, 'igmpCondFilterIfStatus': igmpCondFilterIfStatus, 'igmpCondFilterIfRouter': igmpCondFilterIfRouter}


class igmpCondFilterMcastEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([igmpCondFilterMcastIfIndex, igmpCondFilterMcastAddress], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 4, 1])
	access = 2
	rowstatus = igmpCondFilterMcastStatus
	columns = {'igmpCondFilterMcastIfIndex': igmpCondFilterMcastIfIndex, 'igmpCondFilterMcastAddress': igmpCondFilterMcastAddress, 'igmpCondFilterMcastMember': igmpCondFilterMcastMember, 'igmpCondFilterMcastInPkts': igmpCondFilterMcastInPkts, 'igmpCondFilterMcastOutPkts': igmpCondFilterMcastOutPkts, 'igmpCondFilterMcastStatus': igmpCondFilterMcastStatus}


# notifications (traps) 
# groups 
class ciscoMcastAccessMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 2, 2, 1])
	group = [pimRpAccessListNumber, pimRpAccessListStatus, igmpAccessListNumber]

class ciscoMrbranchMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 2, 2, 2])
	group = [mrbranchState, mrbranchGroup, mrbranchBranch, mrbranchTimeout, mrbranchRequestor, mrbranchResponseRtt, mrbranchResponseRPF, mrbranchInterfaceListNetMask]

class ciscoMcastFilterMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 4, 2, 2, 3])
	group = [igmpConditionalFilteringEnable, igmpMemberReportTimeout, igmpCondFilterIfStatus, igmpCondFilterIfRouter, igmpCondFilterMcastMember, igmpCondFilterMcastInPkts, igmpCondFilterMcastOutPkts, igmpCondFilterMcastStatus]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)