# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from  import dsx1ConfigEntry
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Counter32, Integer32, TimeTicks
from CISCO_SMI import ciscoMgmt
from RFC1213_MIB import ifIndex
from SNMPv2_TC import DisplayString, TruthValue, TimeStamp

class CISCO_ICSUDSU_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-ICSUDSU-MIB'
	conformance = 1
	name = 'CISCO-ICSUDSU-MIB'
	language = 2
	description = 'Integrated CSU/DSU MIB module.  For T1 and Switched 56 kbps\ninterfaces.'

# nodes
class ciscoICsuDsuMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44])
	name = 'ciscoICsuDsuMIB'

class ciscoICsuDsuObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1])
	name = 'ciscoICsuDsuObjects'

class ciscoICsuDsuGeneral(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1])
	name = 'ciscoICsuDsuGeneral'

class ciscoICsuDsuT1(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2])
	name = 'ciscoICsuDsuT1'

class ciscoICsuDsuSw56k(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3])
	name = 'ciscoICsuDsuSw56k'

class ciscoICsuDsuMIBNotificationEnables(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 2])
	name = 'ciscoICsuDsuMIBNotificationEnables'

class ciscoICsuDsuMIBNotificationPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 3])
	name = 'ciscoICsuDsuMIBNotificationPrefix'

class ciscoICsuDsuMIBNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 3, 0])
	name = 'ciscoICsuDsuMIBNotifications'

class ciscoICsuDsuMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 4])
	name = 'ciscoICsuDsuMIBConformance'

class ciscoICsuDsuMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 1])
	name = 'ciscoICsuDsuMIBCompliances'

class ciscoICsuDsuMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 2])
	name = 'ciscoICsuDsuMIBGroups'


# macros
# types 
# scalars 
class ciscoICsuDsuEnableT1LoopStatusNotification(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class ciscoICsuDsuEnableSw56kLoopStatusNotification(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 2, 2])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


# columns
class ciscoICsuDsuType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'fractionalT1'), Enum(2, 'twoWireSwitched56k'), Enum(3, 'fourWireSwitched56k'), Enum(4, 'unknown')]


class ciscoICsuDsuHwRevision(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class ciscoICsuDsuSwRevision(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class ciscoICsuDsuProtocolRevision(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class ciscoICsuDsuLastSelfTestResult(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ciscoICsuDsuTimeOfLastSelfTest(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class ciscoICsuDsuNumResets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoICsuDsuTimeOfLastReset(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class ciscoICsuDsuLoopbackStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'completed'), Enum(2, 'inProgress'), Enum(3, 'neverPerformed'), Enum(4, 'failed'), Enum(5, 'noSyncWithTestPattern')]


class ciscoICsuDsuLoopbackNumErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ciscoICsuDsuLoopbackDuration(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class ciscoICsuDsuLoopbackPoint(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'dtePayload'), Enum(2, 'dteFull'), Enum(3, 'lineFull'), Enum(4, 'linePayload'), Enum(5, 'remoteSmartJack'), Enum(6, 'remoteFull'), Enum(7, 'remotePayload')]


class ciscoICsuDsuLoopbackPattern(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'noPattern'), Enum(2, 'patternQRW'), Enum(3, 'pattern0In1'), Enum(4, 'pattern1In1'), Enum(5, 'pattern1In2'), Enum(6, 'pattern1In3'), Enum(7, 'pattern1In5'), Enum(8, 'pattern1In8'), Enum(9, 'pattern3In24'), Enum(10, 'patternUser'), Enum(11, 'pattern2047'), Enum(12, 'pattern511'), Enum(13, 'patternStressDDS1'), Enum(14, 'patternStressDDS2'), Enum(15, 'patternStressDDS3'), Enum(16, 'patternStressDDS4')]


class ciscoICsuDsuUserDefinedPattern(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class ciscoICsuDsuLoopbackCode(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'standard'), Enum(2, 'alternate'), Enum(3, 'v54')]


class ciscoICsuDsuEndTimeOfLastLoopback(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class ciscoICsuDsuT1LineBuildOut(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'buildOut0'), Enum(2, 'buildOut7p5'), Enum(3, 'buildOut15')]


class ciscoICsuDsuT1DteLineCode(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'normal'), Enum(2, 'inverted')]


class ciscoICsuDsuT1SupportRemoteAlarmIndication(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class ciscoICsuDsuT1FullBandwidthRemoteLoopcode(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'standard'), Enum(2, 'alternate'), Enum(3, 'disabled')]


class ciscoICsuDsuT1PayloadRemoteLoopcode(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'standard'), Enum(2, 'alternate'), Enum(3, 'disabled'), Enum(4, 'v54')]


class ciscoICsuDsuT1LoopStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ciscoICsuDsuT1LossOfSignals(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoICsuDsuT1LossOfFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoICsuDsuT1RemoteAlarmIndications(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoICsuDsuT1AlarmIndicationSignals(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoICsuDsuSw56kNetworkType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'dds'), Enum(2, 'att'), Enum(3, 'sprint'), Enum(4, 'otherCarrier')]


class ciscoICsuDsuSw56kClockSource(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'internal'), Enum(2, 'line')]


class ciscoICsuDsuSw56kLoopRate(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'bps2400'), Enum(2, 'bps4800'), Enum(3, 'bps9600'), Enum(4, 'bps19k'), Enum(5, 'bps38k'), Enum(6, 'bps56k'), Enum(7, 'bps64k')]


class ciscoICsuDsuSw56kScramblerEnabled(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class ciscoICsuDsuSw56kRemoteLoopbackEnabled(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class ciscoICsuDsuSw56kDialingStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'idle'), Enum(2, 'dialing'), Enum(3, 'online'), Enum(4, 'noWinkFromSwitch'), Enum(5, 'numberBusy'), Enum(6, 'noAnswer')]


class ciscoICsuDsuSw56kLoopStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ciscoICsuDsuSw56kReceivedOosOofs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoICsuDsuSw56kLostSealingCurrents(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoICsuDsuSw56kLostReceiveSignals(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoICsuDsuSw56kLostFrameSyncs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoICsuDsuSw56kLoopRateSearches(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# rows 
class ciscoICsuDsuStaticConfigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1, 1])
	access = 2
	columns = {'ciscoICsuDsuType': ciscoICsuDsuType, 'ciscoICsuDsuHwRevision': ciscoICsuDsuHwRevision, 'ciscoICsuDsuSwRevision': ciscoICsuDsuSwRevision, 'ciscoICsuDsuProtocolRevision': ciscoICsuDsuProtocolRevision}


class ciscoICsuDsuTestReportEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1])
	access = 2
	columns = {'ciscoICsuDsuLastSelfTestResult': ciscoICsuDsuLastSelfTestResult, 'ciscoICsuDsuTimeOfLastSelfTest': ciscoICsuDsuTimeOfLastSelfTest, 'ciscoICsuDsuNumResets': ciscoICsuDsuNumResets, 'ciscoICsuDsuTimeOfLastReset': ciscoICsuDsuTimeOfLastReset, 'ciscoICsuDsuLoopbackStatus': ciscoICsuDsuLoopbackStatus, 'ciscoICsuDsuLoopbackNumErrors': ciscoICsuDsuLoopbackNumErrors, 'ciscoICsuDsuLoopbackDuration': ciscoICsuDsuLoopbackDuration, 'ciscoICsuDsuLoopbackPoint': ciscoICsuDsuLoopbackPoint, 'ciscoICsuDsuLoopbackPattern': ciscoICsuDsuLoopbackPattern, 'ciscoICsuDsuUserDefinedPattern': ciscoICsuDsuUserDefinedPattern, 'ciscoICsuDsuLoopbackCode': ciscoICsuDsuLoopbackCode, 'ciscoICsuDsuEndTimeOfLastLoopback': ciscoICsuDsuEndTimeOfLastLoopback}


class ciscoICsuDsuT1ConfigEntry(RowObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1])
	access = 2
	columns = {'ciscoICsuDsuT1LineBuildOut': ciscoICsuDsuT1LineBuildOut, 'ciscoICsuDsuT1DteLineCode': ciscoICsuDsuT1DteLineCode, 'ciscoICsuDsuT1SupportRemoteAlarmIndication': ciscoICsuDsuT1SupportRemoteAlarmIndication, 'ciscoICsuDsuT1FullBandwidthRemoteLoopcode': ciscoICsuDsuT1FullBandwidthRemoteLoopcode, 'ciscoICsuDsuT1PayloadRemoteLoopcode': ciscoICsuDsuT1PayloadRemoteLoopcode}


class ciscoICsuDsuT1StatusEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1])
	access = 2
	columns = {'ciscoICsuDsuT1LoopStatus': ciscoICsuDsuT1LoopStatus, 'ciscoICsuDsuT1LossOfSignals': ciscoICsuDsuT1LossOfSignals, 'ciscoICsuDsuT1LossOfFrames': ciscoICsuDsuT1LossOfFrames, 'ciscoICsuDsuT1RemoteAlarmIndications': ciscoICsuDsuT1RemoteAlarmIndications, 'ciscoICsuDsuT1AlarmIndicationSignals': ciscoICsuDsuT1AlarmIndicationSignals}


class ciscoICsuDsuSw56kConfigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1])
	access = 2
	columns = {'ciscoICsuDsuSw56kNetworkType': ciscoICsuDsuSw56kNetworkType, 'ciscoICsuDsuSw56kClockSource': ciscoICsuDsuSw56kClockSource, 'ciscoICsuDsuSw56kLoopRate': ciscoICsuDsuSw56kLoopRate, 'ciscoICsuDsuSw56kScramblerEnabled': ciscoICsuDsuSw56kScramblerEnabled, 'ciscoICsuDsuSw56kRemoteLoopbackEnabled': ciscoICsuDsuSw56kRemoteLoopbackEnabled}


class ciscoICsuDsuSw56kLineStatusEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1])
	access = 2
	columns = {'ciscoICsuDsuSw56kDialingStatus': ciscoICsuDsuSw56kDialingStatus, 'ciscoICsuDsuSw56kLoopStatus': ciscoICsuDsuSw56kLoopStatus, 'ciscoICsuDsuSw56kReceivedOosOofs': ciscoICsuDsuSw56kReceivedOosOofs, 'ciscoICsuDsuSw56kLostSealingCurrents': ciscoICsuDsuSw56kLostSealingCurrents, 'ciscoICsuDsuSw56kLostReceiveSignals': ciscoICsuDsuSw56kLostReceiveSignals, 'ciscoICsuDsuSw56kLostFrameSyncs': ciscoICsuDsuSw56kLostFrameSyncs, 'ciscoICsuDsuSw56kLoopRateSearches': ciscoICsuDsuSw56kLoopRateSearches}


# notifications (traps) 
class ciscoICsuDsuT1LoopStatusNotification(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 3, 0, 1])

class ciscoICsuDsuSw56kLoopStatusNotification(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 3, 0, 2])

# groups 
class ciscoICsuDsuMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 2, 1])
	group = [ciscoICsuDsuType, ciscoICsuDsuHwRevision, ciscoICsuDsuSwRevision, ciscoICsuDsuProtocolRevision, ciscoICsuDsuLastSelfTestResult, ciscoICsuDsuTimeOfLastSelfTest, ciscoICsuDsuNumResets, ciscoICsuDsuTimeOfLastReset, ciscoICsuDsuLoopbackStatus, ciscoICsuDsuLoopbackNumErrors, ciscoICsuDsuLoopbackDuration, ciscoICsuDsuLoopbackPoint, ciscoICsuDsuLoopbackPattern, ciscoICsuDsuUserDefinedPattern, ciscoICsuDsuLoopbackCode, ciscoICsuDsuEndTimeOfLastLoopback]

class ciscoICsuDsuMIBT1Group(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 2, 2])
	group = [ciscoICsuDsuT1LineBuildOut, ciscoICsuDsuT1DteLineCode, ciscoICsuDsuT1SupportRemoteAlarmIndication, ciscoICsuDsuT1FullBandwidthRemoteLoopcode, ciscoICsuDsuT1PayloadRemoteLoopcode, ciscoICsuDsuT1LoopStatus, ciscoICsuDsuT1LossOfSignals, ciscoICsuDsuT1LossOfFrames, ciscoICsuDsuT1RemoteAlarmIndications, ciscoICsuDsuT1AlarmIndicationSignals, ciscoICsuDsuEnableT1LoopStatusNotification]

class ciscoICsuDsuMIBSw56kGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 2, 3])
	group = [ciscoICsuDsuSw56kNetworkType, ciscoICsuDsuSw56kClockSource, ciscoICsuDsuSw56kLoopRate, ciscoICsuDsuSw56kScramblerEnabled, ciscoICsuDsuSw56kRemoteLoopbackEnabled, ciscoICsuDsuSw56kDialingStatus, ciscoICsuDsuSw56kLoopStatus, ciscoICsuDsuSw56kReceivedOosOofs, ciscoICsuDsuSw56kLostSealingCurrents, ciscoICsuDsuSw56kLostReceiveSignals, ciscoICsuDsuSw56kLostFrameSyncs, ciscoICsuDsuSw56kLoopRateSearches, ciscoICsuDsuEnableSw56kLoopStatusNotification]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)