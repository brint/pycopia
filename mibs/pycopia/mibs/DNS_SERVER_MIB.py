# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, OBJECT_IDENTITY, IpAddress, Counter32, Gauge32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from RFC1213_MIB import mib_2
from SNMPv2_TC import TEXTUAL_CONVENTION, RowStatus, DisplayString, TruthValue

class DNS_SERVER_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/DNS-SERVER-MIB'
	conformance = 3
	name = 'DNS-SERVER-MIB'
	language = 2
	description = 'The MIB module for entities implementing the server side\nof the Domain Name System (DNS) protocol.'

# nodes
class dns(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32])
	name = 'dns'

class dnsServMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1])
	name = 'dnsServMIB'

class dnsServMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1])
	name = 'dnsServMIBObjects'

class dnsServConfig(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 1])
	name = 'dnsServConfig'

class dnsServCounter(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2])
	name = 'dnsServCounter'

class dnsServOptCounter(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3])
	name = 'dnsServOptCounter'

class dnsServZone(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 4])
	name = 'dnsServZone'

class dnsServMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 2])
	name = 'dnsServMIBGroups'

class dnsServMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 3])
	name = 'dnsServMIBCompliances'


# macros
# types 

class DnsName(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 255))


class DnsNameAsIndex(pycopia.SMI.Basetypes.OctetString):
	status = 1


class DnsClass(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 65535))
	format = 'd'


class DnsType(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 65535))
	format = 'd'


class DnsQClass(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 65535))
	format = 'd'


class DnsQType(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 65535))
	format = 'd'


class DnsTime(pycopia.SMI.Basetypes.Gauge32):
	status = 1
	format = 'd'


class DnsOpCode(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 15))


class DnsRespCode(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 15))

# scalars 
class dnsServConfigImplementIdent(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class dnsServConfigRecurs(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'available'), Enum(2, 'restricted'), Enum(3, 'unavailable')]


class dnsServConfigUpTime(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 3])
	syntaxobject = DnsTime


class dnsServConfigResetTime(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 4])
	syntaxobject = DnsTime


class dnsServConfigReset(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'reset'), Enum(3, 'initializing'), Enum(4, 'running')]


class dnsServCounterAuthAns(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServCounterAuthNoNames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServCounterAuthNoDataResps(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServCounterNonAuthDatas(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServCounterNonAuthNoDatas(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServCounterReferrals(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServCounterErrors(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServCounterRelNames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServCounterReqRefusals(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServCounterReqUnparses(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServCounterOtherErrors(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterSelfAuthAns(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterSelfAuthNoNames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterSelfAuthNoDataResps(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterSelfNonAuthDatas(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterSelfNonAuthNoDatas(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterSelfReferrals(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterSelfErrors(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterSelfRelNames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterSelfReqRefusals(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterSelfReqUnparses(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterSelfOtherErrors(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterFriendsAuthAns(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterFriendsAuthNoNames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterFriendsAuthNoDataResps(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterFriendsNonAuthDatas(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterFriendsNonAuthNoDatas(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterFriendsReferrals(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterFriendsErrors(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterFriendsRelNames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterFriendsReqRefusals(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 20])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterFriendsReqUnparses(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 21])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServOptCounterFriendsOtherErrors(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 22])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# columns
class dnsServCounterOpCode(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 1])
	syntaxobject = DnsOpCode


class dnsServCounterQClass(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 2])
	syntaxobject = DnsClass


class dnsServCounterQType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 3])
	syntaxobject = DnsType


class dnsServCounterTransport(ColumnObject):
	status = 1
	access = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'udp'), Enum(2, 'tcp'), Enum(3, 'other')]


class dnsServCounterRequests(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServCounterResponses(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServZoneName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 1])
	syntaxobject = DnsNameAsIndex


class dnsServZoneClass(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 2])
	syntaxobject = DnsClass


class dnsServZoneLastReloadSuccess(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 3])
	syntaxobject = DnsTime


class dnsServZoneLastReloadAttempt(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 4])
	syntaxobject = DnsTime


class dnsServZoneLastSourceAttempt(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class dnsServZoneStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class dnsServZoneSerial(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dnsServZoneCurrent(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class dnsServZoneLastSourceSuccess(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class dnsServZoneSrcName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 1])
	syntaxobject = DnsNameAsIndex


class dnsServZoneSrcClass(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 2])
	syntaxobject = DnsClass


class dnsServZoneSrcAddr(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class dnsServZoneSrcStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class dnsServCounterEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dnsServCounterOpCode, dnsServCounterQClass, dnsServCounterQType, dnsServCounterTransport], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1])
	access = 2
	columns = {'dnsServCounterOpCode': dnsServCounterOpCode, 'dnsServCounterQClass': dnsServCounterQClass, 'dnsServCounterQType': dnsServCounterQType, 'dnsServCounterTransport': dnsServCounterTransport, 'dnsServCounterRequests': dnsServCounterRequests, 'dnsServCounterResponses': dnsServCounterResponses}


class dnsServZoneEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dnsServZoneName, dnsServZoneClass], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1])
	access = 2
	rowstatus = dnsServZoneStatus
	columns = {'dnsServZoneName': dnsServZoneName, 'dnsServZoneClass': dnsServZoneClass, 'dnsServZoneLastReloadSuccess': dnsServZoneLastReloadSuccess, 'dnsServZoneLastReloadAttempt': dnsServZoneLastReloadAttempt, 'dnsServZoneLastSourceAttempt': dnsServZoneLastSourceAttempt, 'dnsServZoneStatus': dnsServZoneStatus, 'dnsServZoneSerial': dnsServZoneSerial, 'dnsServZoneCurrent': dnsServZoneCurrent, 'dnsServZoneLastSourceSuccess': dnsServZoneLastSourceSuccess}


class dnsServZoneSrcEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dnsServZoneSrcName, dnsServZoneSrcClass, dnsServZoneSrcAddr], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1])
	access = 2
	rowstatus = dnsServZoneSrcStatus
	columns = {'dnsServZoneSrcName': dnsServZoneSrcName, 'dnsServZoneSrcClass': dnsServZoneSrcClass, 'dnsServZoneSrcAddr': dnsServZoneSrcAddr, 'dnsServZoneSrcStatus': dnsServZoneSrcStatus}


# notifications (traps) 
# groups 
class dnsServConfigGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 2, 1])
	group = [dnsServConfigImplementIdent, dnsServConfigRecurs, dnsServConfigUpTime, dnsServConfigResetTime, dnsServConfigReset]

class dnsServCounterGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 2, 2])
	group = [dnsServCounterAuthAns, dnsServCounterAuthNoNames, dnsServCounterAuthNoDataResps, dnsServCounterNonAuthDatas, dnsServCounterNonAuthNoDatas, dnsServCounterReferrals, dnsServCounterErrors, dnsServCounterRelNames, dnsServCounterReqRefusals, dnsServCounterReqUnparses, dnsServCounterOtherErrors, dnsServCounterOpCode, dnsServCounterQClass, dnsServCounterQType, dnsServCounterTransport, dnsServCounterRequests, dnsServCounterResponses]

class dnsServOptCounterGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 2, 3])
	group = [dnsServOptCounterSelfAuthAns, dnsServOptCounterSelfAuthNoNames, dnsServOptCounterSelfAuthNoDataResps, dnsServOptCounterSelfNonAuthDatas, dnsServOptCounterSelfNonAuthNoDatas, dnsServOptCounterSelfReferrals, dnsServOptCounterSelfErrors, dnsServOptCounterSelfRelNames, dnsServOptCounterSelfReqRefusals, dnsServOptCounterSelfReqUnparses, dnsServOptCounterSelfOtherErrors, dnsServOptCounterFriendsAuthAns, dnsServOptCounterFriendsAuthNoNames, dnsServOptCounterFriendsAuthNoDataResps, dnsServOptCounterFriendsNonAuthDatas, dnsServOptCounterFriendsNonAuthNoDatas, dnsServOptCounterFriendsReferrals, dnsServOptCounterFriendsErrors, dnsServOptCounterFriendsRelNames, dnsServOptCounterFriendsReqRefusals, dnsServOptCounterFriendsReqUnparses, dnsServOptCounterFriendsOtherErrors]

class dnsServZoneGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 32, 1, 2, 4])
	group = [dnsServZoneName, dnsServZoneClass, dnsServZoneLastReloadSuccess, dnsServZoneLastReloadAttempt, dnsServZoneLastSourceAttempt, dnsServZoneLastSourceSuccess, dnsServZoneStatus, dnsServZoneSerial, dnsServZoneCurrent, dnsServZoneSrcName, dnsServZoneSrcClass, dnsServZoneSrcAddr, dnsServZoneSrcStatus]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)