# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Counter32, Gauge32, Unsigned32, mib_2
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from SNMPv2_TC import RowStatus, RowPointer, TEXTUAL_CONVENTION, DateAndTime, StorageType
from SNMP_FRAMEWORK_MIB import SnmpAdminString

class POLICY_BASED_MANAGEMENT_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/POLICY-BASED-MANAGEMENT-MIB'
	conformance = 3
	name = 'POLICY-BASED-MANAGEMENT-MIB'
	language = 2
	description = 'The MIB module for policy-based configuration of SNMP\ninfrastructures.\n\nCopyright (C) The Internet Society (2005).  This version of\nthis MIB module is part of RFC 4011; see the RFC itself for\nfull legal notices.'

# nodes
class pmMib(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124])
	name = 'pmMib'

class pmNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 0])
	name = 'pmNotifications'

class pmConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 12])
	name = 'pmConformance'

class pmCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 12, 1])
	name = 'pmCompliances'

class pmGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 12, 2])
	name = 'pmGroups'

class pmBaseFunctionLibrary(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 12, 2, 4])
	name = 'pmBaseFunctionLibrary'


# macros
# types 

class PmUTF8String(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 65535))

# scalars 
class pmSchedLocalTime(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 7])
	syntaxobject = pycopia.SMI.Basetypes.DateAndTime


# columns
class pmPolicyAdminGroup(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 1])
	syntaxobject = PmUTF8String


class pmPolicyIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class pmPolicyPrecedenceGroup(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 3])
	syntaxobject = PmUTF8String


class pmPolicyPrecedence(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class pmPolicySchedule(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class pmPolicyElementTypeFilter(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 6])
	syntaxobject = PmUTF8String


class pmPolicyConditionScriptIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class pmPolicyActionScriptIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class pmPolicyParameters(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class pmPolicyConditionMaxLatency(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'milliseconds'


class pmPolicyActionMaxLatency(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'milliseconds'


class pmPolicyMaxIterations(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class pmPolicyDescription(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 13])
	syntaxobject = PmUTF8String


class pmPolicyMatches(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'elements'


class pmPolicyAbnormalTerminations(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'elements'


class pmPolicyExecutionErrors(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'errors'


class pmPolicyDebugging(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'off'), Enum(2, 'on')]


class pmPolicyAdminStatus(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'disabled'), Enum(2, 'enabled'), Enum(3, 'enabledAutoRemove')]


class pmPolicyStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class pmPolicyRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class pmPolicyCodeScriptIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class pmPolicyCodeSegment(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class pmPolicyCodeText(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 2, 1, 3])
	syntaxobject = PmUTF8String


class pmPolicyCodeStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class pmElementTypeRegOIDPrefix(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class pmElementTypeRegMaxLatency(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'milliseconds'


class pmElementTypeRegDescription(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 3, 1, 4])
	syntaxobject = PmUTF8String


class pmElementTypeRegStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class pmElementTypeRegRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class pmRoleElement(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class pmRoleContextName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 4, 1, 2])
	syntaxobject = SnmpAdminString


class pmRoleContextEngineID(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class pmRoleString(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 4, 1, 4])
	syntaxobject = PmUTF8String


class pmRoleStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 4, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class pmCapabilitiesType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 5, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class pmCapabilitiesOverrideType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 6, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class pmCapabilitiesOverrideState(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 6, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'invalid'), Enum(2, 'valid')]


class pmCapabilitiesOverrideRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 6, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class pmSchedIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 8, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class pmSchedGroupIndex(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 8, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class pmSchedDescr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 8, 1, 3])
	syntaxobject = PmUTF8String


class pmSchedTimePeriod(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 8, 1, 4])
	syntaxobject = PmUTF8String


class pmSchedMonth(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 8, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class pmSchedDay(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 8, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class pmSchedWeekDay(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 8, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class pmSchedTimeOfDay(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 8, 1, 8])
	syntaxobject = PmUTF8String


class pmSchedLocalOrUtc(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 8, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'localTime'), Enum(2, 'utcTime')]


class pmSchedStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 8, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class pmSchedRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 8, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class pmTrackingPEElement(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 9, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class pmTrackingPEContextName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 9, 1, 2])
	syntaxobject = SnmpAdminString


class pmTrackingPEContextEngineID(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 9, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class pmTrackingPEInfo(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 9, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class pmTrackingEPElement(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 10, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class pmTrackingEPContextName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 10, 1, 2])
	syntaxobject = SnmpAdminString


class pmTrackingEPContextEngineID(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 10, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class pmTrackingEPStatus(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 10, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'on'), Enum(2, 'forceOff')]


class pmDebuggingElement(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 11, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class pmDebuggingContextName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 11, 1, 2])
	syntaxobject = SnmpAdminString


class pmDebuggingContextEngineID(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 11, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class pmDebuggingLogIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 11, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class pmDebuggingMessage(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 11, 1, 5])
	syntaxobject = PmUTF8String


# rows 
class pmPolicyEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([pmPolicyAdminGroup, pmPolicyIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 1, 1])
	access = 2
	rowstatus = pmPolicyRowStatus
	columns = {'pmPolicyAdminGroup': pmPolicyAdminGroup, 'pmPolicyIndex': pmPolicyIndex, 'pmPolicyPrecedenceGroup': pmPolicyPrecedenceGroup, 'pmPolicyPrecedence': pmPolicyPrecedence, 'pmPolicySchedule': pmPolicySchedule, 'pmPolicyElementTypeFilter': pmPolicyElementTypeFilter, 'pmPolicyConditionScriptIndex': pmPolicyConditionScriptIndex, 'pmPolicyActionScriptIndex': pmPolicyActionScriptIndex, 'pmPolicyParameters': pmPolicyParameters, 'pmPolicyConditionMaxLatency': pmPolicyConditionMaxLatency, 'pmPolicyActionMaxLatency': pmPolicyActionMaxLatency, 'pmPolicyMaxIterations': pmPolicyMaxIterations, 'pmPolicyDescription': pmPolicyDescription, 'pmPolicyMatches': pmPolicyMatches, 'pmPolicyAbnormalTerminations': pmPolicyAbnormalTerminations, 'pmPolicyExecutionErrors': pmPolicyExecutionErrors, 'pmPolicyDebugging': pmPolicyDebugging, 'pmPolicyAdminStatus': pmPolicyAdminStatus, 'pmPolicyStorageType': pmPolicyStorageType, 'pmPolicyRowStatus': pmPolicyRowStatus}


class pmPolicyCodeEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([pmPolicyAdminGroup, pmPolicyCodeScriptIndex, pmPolicyCodeSegment], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 2, 1])
	access = 2
	rowstatus = pmPolicyCodeStatus
	columns = {'pmPolicyCodeScriptIndex': pmPolicyCodeScriptIndex, 'pmPolicyCodeSegment': pmPolicyCodeSegment, 'pmPolicyCodeText': pmPolicyCodeText, 'pmPolicyCodeStatus': pmPolicyCodeStatus}


class pmElementTypeRegEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([pmElementTypeRegOIDPrefix], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 3, 1])
	access = 2
	rowstatus = pmElementTypeRegRowStatus
	columns = {'pmElementTypeRegOIDPrefix': pmElementTypeRegOIDPrefix, 'pmElementTypeRegMaxLatency': pmElementTypeRegMaxLatency, 'pmElementTypeRegDescription': pmElementTypeRegDescription, 'pmElementTypeRegStorageType': pmElementTypeRegStorageType, 'pmElementTypeRegRowStatus': pmElementTypeRegRowStatus}


class pmRoleEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([pmRoleElement, pmRoleContextName, pmRoleContextEngineID, pmRoleString], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 4, 1])
	access = 2
	rowstatus = pmRoleStatus
	columns = {'pmRoleElement': pmRoleElement, 'pmRoleContextName': pmRoleContextName, 'pmRoleContextEngineID': pmRoleContextEngineID, 'pmRoleString': pmRoleString, 'pmRoleStatus': pmRoleStatus}


class pmCapabilitiesEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([pmCapabilitiesType], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 5, 1])
	access = 2
	columns = {'pmCapabilitiesType': pmCapabilitiesType}


class pmCapabilitiesOverrideEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([pmCapabilitiesOverrideType], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 6, 1])
	access = 2
	rowstatus = pmCapabilitiesOverrideRowStatus
	columns = {'pmCapabilitiesOverrideType': pmCapabilitiesOverrideType, 'pmCapabilitiesOverrideState': pmCapabilitiesOverrideState, 'pmCapabilitiesOverrideRowStatus': pmCapabilitiesOverrideRowStatus}


class pmSchedEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([pmSchedIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 8, 1])
	access = 2
	rowstatus = pmSchedRowStatus
	columns = {'pmSchedIndex': pmSchedIndex, 'pmSchedGroupIndex': pmSchedGroupIndex, 'pmSchedDescr': pmSchedDescr, 'pmSchedTimePeriod': pmSchedTimePeriod, 'pmSchedMonth': pmSchedMonth, 'pmSchedDay': pmSchedDay, 'pmSchedWeekDay': pmSchedWeekDay, 'pmSchedTimeOfDay': pmSchedTimeOfDay, 'pmSchedLocalOrUtc': pmSchedLocalOrUtc, 'pmSchedStorageType': pmSchedStorageType, 'pmSchedRowStatus': pmSchedRowStatus}


class pmTrackingPEEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([pmPolicyIndex, pmTrackingPEElement, pmTrackingPEContextName, pmTrackingPEContextEngineID], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 9, 1])
	access = 2
	columns = {'pmTrackingPEElement': pmTrackingPEElement, 'pmTrackingPEContextName': pmTrackingPEContextName, 'pmTrackingPEContextEngineID': pmTrackingPEContextEngineID, 'pmTrackingPEInfo': pmTrackingPEInfo}


class pmTrackingEPEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([pmTrackingEPElement, pmTrackingEPContextName, pmTrackingEPContextEngineID, pmPolicyIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 10, 1])
	access = 2
	columns = {'pmTrackingEPElement': pmTrackingEPElement, 'pmTrackingEPContextName': pmTrackingEPContextName, 'pmTrackingEPContextEngineID': pmTrackingEPContextEngineID, 'pmTrackingEPStatus': pmTrackingEPStatus}


class pmDebuggingEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([pmPolicyIndex, pmDebuggingElement, pmDebuggingContextName, pmDebuggingContextEngineID, pmDebuggingLogIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 11, 1])
	access = 2
	columns = {'pmDebuggingElement': pmDebuggingElement, 'pmDebuggingContextName': pmDebuggingContextName, 'pmDebuggingContextEngineID': pmDebuggingContextEngineID, 'pmDebuggingLogIndex': pmDebuggingLogIndex, 'pmDebuggingMessage': pmDebuggingMessage}


# notifications (traps) 
class pmNewRoleNotification(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 0, 1])

class pmNewCapabilityNotification(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 0, 2])

class pmAbnormalTermNotification(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 0, 3])

# groups 
class pmPolicyManagementGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 12, 2, 1])
	group = [pmPolicyPrecedenceGroup, pmPolicyPrecedence, pmPolicySchedule, pmPolicyElementTypeFilter, pmPolicyConditionScriptIndex, pmPolicyActionScriptIndex, pmPolicyParameters, pmPolicyConditionMaxLatency, pmPolicyActionMaxLatency, pmPolicyMaxIterations, pmPolicyDescription, pmPolicyMatches, pmPolicyAbnormalTerminations, pmPolicyExecutionErrors, pmPolicyDebugging, pmPolicyStorageType, pmPolicyAdminStatus, pmPolicyRowStatus, pmPolicyCodeText, pmPolicyCodeStatus, pmElementTypeRegMaxLatency, pmElementTypeRegDescription, pmElementTypeRegStorageType, pmElementTypeRegRowStatus, pmRoleStatus, pmCapabilitiesType, pmCapabilitiesOverrideState, pmCapabilitiesOverrideRowStatus, pmTrackingPEInfo, pmTrackingEPStatus, pmDebuggingMessage]

class pmSchedGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 12, 2, 2])
	group = [pmSchedLocalTime, pmSchedGroupIndex, pmSchedDescr, pmSchedTimePeriod, pmSchedMonth, pmSchedDay, pmSchedWeekDay, pmSchedTimeOfDay, pmSchedLocalOrUtc, pmSchedStorageType, pmSchedRowStatus]

class pmNotificationGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 124, 12, 2, 3])
	group = [pmNewRoleNotification, pmNewCapabilityNotification, pmAbnormalTermNotification]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)