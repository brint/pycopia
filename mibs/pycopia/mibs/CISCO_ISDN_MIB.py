# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, NOTIFICATION_TYPE, Counter32, OBJECT_TYPE, Integer32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoMgmt
from SNMPv2_TC import DisplayString, TimeStamp, RowStatus

class CISCO_ISDN_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-ISDN-MIB'
	conformance = 2
	name = 'CISCO-ISDN-MIB'
	language = 2
	description = 'The MIB module to describe the status of the ISDN \nInterfaces on the routers.'

# nodes
class ciscoIsdnMib(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26])
	name = 'ciscoIsdnMib'

class ciscoIsdnMibObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1])
	name = 'ciscoIsdnMibObjects'

class isdnNeighbor(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1])
	name = 'isdnNeighbor'

class ciscoIsdnMibTrapPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 2])
	name = 'ciscoIsdnMibTrapPrefix'

class ciscoIsdnMibTraps(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 2, 0])
	name = 'ciscoIsdnMibTraps'

class ciscoIsdnMibConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 3])
	name = 'ciscoIsdnMibConformance'

class ciscoIsdnMibCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 3, 1])
	name = 'ciscoIsdnMibCompliances'

class ciscoIsdnMibGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 3, 2])
	name = 'ciscoIsdnMibGroups'


# macros
# types 
# scalars 
# columns
class demandNbrPhysIf(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class demandNbrId(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class demandNbrLogIf(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class demandNbrName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class demandNbrAddress(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class demandNbrPermission(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'iCanCallHim'), Enum(2, 'heCanCallMe'), Enum(3, 'weCanCallEachOther')]


class demandNbrMaxDuration(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class demandNbrLastDuration(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 4
	units = 'seconds'


class demandNbrClearReason(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class demandNbrClearCode(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class demandNbrSuccessCalls(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class demandNbrFailCalls(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class demandNbrAcceptCalls(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class demandNbrRefuseCalls(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class demandNbrLastAttemptTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class demandNbrStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class demandNbrCallOrigin(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'originate'), Enum(2, 'answer'), Enum(3, 'callback')]


# rows 
class demandNbrEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([demandNbrPhysIf, demandNbrId], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1])
	access = 2
	rowstatus = demandNbrStatus
	columns = {'demandNbrPhysIf': demandNbrPhysIf, 'demandNbrId': demandNbrId, 'demandNbrLogIf': demandNbrLogIf, 'demandNbrName': demandNbrName, 'demandNbrAddress': demandNbrAddress, 'demandNbrPermission': demandNbrPermission, 'demandNbrMaxDuration': demandNbrMaxDuration, 'demandNbrLastDuration': demandNbrLastDuration, 'demandNbrClearReason': demandNbrClearReason, 'demandNbrClearCode': demandNbrClearCode, 'demandNbrSuccessCalls': demandNbrSuccessCalls, 'demandNbrFailCalls': demandNbrFailCalls, 'demandNbrAcceptCalls': demandNbrAcceptCalls, 'demandNbrRefuseCalls': demandNbrRefuseCalls, 'demandNbrLastAttemptTime': demandNbrLastAttemptTime, 'demandNbrStatus': demandNbrStatus, 'demandNbrCallOrigin': demandNbrCallOrigin}


# notifications (traps) 
class demandNbrCallInformation(NotificationObject):
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 2, 0, 1])

class demandNbrCallDetails(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 2, 0, 2])

# groups 
class ciscoIsdnMibGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 3, 2, 1])
	group = [demandNbrLogIf, demandNbrName, demandNbrAddress, demandNbrPermission, demandNbrMaxDuration, demandNbrLastDuration, demandNbrClearReason, demandNbrClearCode, demandNbrSuccessCalls, demandNbrFailCalls, demandNbrAcceptCalls, demandNbrRefuseCalls, demandNbrLastAttemptTime, demandNbrStatus]

class ciscoIsdnMibGroupRev1(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 26, 3, 2, 2])
	group = [demandNbrLogIf, demandNbrName, demandNbrAddress, demandNbrPermission, demandNbrMaxDuration, demandNbrLastDuration, demandNbrClearReason, demandNbrClearCode, demandNbrSuccessCalls, demandNbrFailCalls, demandNbrAcceptCalls, demandNbrRefuseCalls, demandNbrLastAttemptTime, demandNbrStatus, demandNbrCallOrigin]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)