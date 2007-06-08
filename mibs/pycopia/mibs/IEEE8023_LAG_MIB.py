# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32, TimeTicks
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from Q_BRIDGE_MIB import PortList
from SNMPv2_TC import DisplayString, MacAddress, TEXTUAL_CONVENTION, TruthValue
from IF_MIB import InterfaceIndex

class IEEE8023_LAG_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/IEEE8023-LAG-MIB'
	conformance = 2
	name = 'IEEE8023-LAG-MIB'
	language = 2
	description = 'The Link Aggregation module for managing IEEE Std\n802.3ad.'

# nodes
class lagMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43])
	name = 'lagMIB'

class lagMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1])
	name = 'lagMIBObjects'

class dot3adAgg(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 1])
	name = 'dot3adAgg'

class dot3adAggPort(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2])
	name = 'dot3adAggPort'

class dot3adAggConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 2])
	name = 'dot3adAggConformance'

class dot3adAggGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 2, 1])
	name = 'dot3adAggGroups'

class dot3adAggCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 2, 2])
	name = 'dot3adAggCompliances'


# macros
# types 

class LacpKey(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 65535))


class LacpState(pycopia.SMI.Basetypes.BITS):
	status = 1
	enumerations = [Enum(0, 'lacpActivity'), Enum(1, 'lacpTimeout'), Enum(2, 'aggregation'), Enum(3, 'synchronization'), Enum(4, 'collecting'), Enum(5, 'distributing'), Enum(6, 'defaulted'), Enum(7, 'expired')]


class ChurnState(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'noChurn'), Enum(2, 'churn'), Enum(3, 'churnMonitor')]

# scalars 
class dot3adTablesLastChanged(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


# columns
class dot3adAggIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 1])
	syntaxobject = InterfaceIndex


class dot3adAggMACAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class dot3adAggActorSystemPriority(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot3adAggActorSystemID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class dot3adAggAggregateOrIndividual(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class dot3adAggActorAdminKey(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 6])
	syntaxobject = LacpKey


class dot3adAggActorOperKey(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 7])
	syntaxobject = LacpKey


class dot3adAggPartnerSystemID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class dot3adAggPartnerSystemPriority(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot3adAggPartnerOperKey(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 10])
	syntaxobject = LacpKey


class dot3adAggCollectorMaxDelay(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot3adAggPortListPorts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 1, 2, 1, 1])
	syntaxobject = PortList


class dot3adAggPortIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 1])
	syntaxobject = InterfaceIndex


class dot3adAggPortActorSystemPriority(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot3adAggPortActorSystemID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class dot3adAggPortActorAdminKey(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 4])
	syntaxobject = LacpKey


class dot3adAggPortActorOperKey(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 5])
	syntaxobject = LacpKey


class dot3adAggPortPartnerAdminSystemPriority(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot3adAggPortPartnerOperSystemPriority(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot3adAggPortPartnerAdminSystemID(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class dot3adAggPortPartnerOperSystemID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class dot3adAggPortPartnerAdminKey(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 10])
	syntaxobject = LacpKey


class dot3adAggPortPartnerOperKey(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 11])
	syntaxobject = LacpKey


class dot3adAggPortSelectedAggID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 12])
	syntaxobject = InterfaceIndex


class dot3adAggPortAttachedAggID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 13])
	syntaxobject = InterfaceIndex


class dot3adAggPortActorPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot3adAggPortActorPortPriority(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot3adAggPortPartnerAdminPort(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot3adAggPortPartnerOperPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot3adAggPortPartnerAdminPortPriority(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot3adAggPortPartnerOperPortPriority(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot3adAggPortActorAdminState(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 20])
	syntaxobject = LacpState


class dot3adAggPortActorOperState(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 21])
	syntaxobject = LacpState


class dot3adAggPortPartnerAdminState(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 22])
	syntaxobject = LacpState


class dot3adAggPortPartnerOperState(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 23])
	syntaxobject = LacpState


class dot3adAggPortAggregateOrIndividual(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 24])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class dot3adAggPortStatsLACPDUsRx(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot3adAggPortStatsMarkerPDUsRx(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot3adAggPortStatsMarkerResponsePDUsRx(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot3adAggPortStatsUnknownRx(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot3adAggPortStatsIllegalRx(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot3adAggPortStatsLACPDUsTx(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot3adAggPortStatsMarkerPDUsTx(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot3adAggPortStatsMarkerResponsePDUsTx(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot3adAggPortDebugRxState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'currentRx'), Enum(2, 'expired'), Enum(3, 'defaulted'), Enum(4, 'initialize'), Enum(5, 'lacpDisabled'), Enum(6, 'portDisabled')]


class dot3adAggPortDebugLastRxTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class dot3adAggPortDebugMuxState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'detached'), Enum(2, 'waiting'), Enum(3, 'attached'), Enum(4, 'collecting'), Enum(5, 'distributing'), Enum(6, 'collectingDistributing')]


class dot3adAggPortDebugMuxReason(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class dot3adAggPortDebugActorChurnState(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 5])
	syntaxobject = ChurnState


class dot3adAggPortDebugPartnerChurnState(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 6])
	syntaxobject = ChurnState


class dot3adAggPortDebugActorChurnCount(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot3adAggPortDebugPartnerChurnCount(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot3adAggPortDebugActorSyncTransitionCount(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot3adAggPortDebugPartnerSyncTransitionCount(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot3adAggPortDebugActorChangeCount(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot3adAggPortDebugPartnerChangeCount(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# rows 
class dot3adAggEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot3adAggIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 1, 1, 1])
	access = 2
	columns = {'dot3adAggIndex': dot3adAggIndex, 'dot3adAggMACAddress': dot3adAggMACAddress, 'dot3adAggActorSystemPriority': dot3adAggActorSystemPriority, 'dot3adAggActorSystemID': dot3adAggActorSystemID, 'dot3adAggAggregateOrIndividual': dot3adAggAggregateOrIndividual, 'dot3adAggActorAdminKey': dot3adAggActorAdminKey, 'dot3adAggActorOperKey': dot3adAggActorOperKey, 'dot3adAggPartnerSystemID': dot3adAggPartnerSystemID, 'dot3adAggPartnerSystemPriority': dot3adAggPartnerSystemPriority, 'dot3adAggPartnerOperKey': dot3adAggPartnerOperKey, 'dot3adAggCollectorMaxDelay': dot3adAggCollectorMaxDelay}


class dot3adAggPortListEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot3adAggIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 1, 2, 1])
	access = 2
	columns = {'dot3adAggPortListPorts': dot3adAggPortListPorts}


class dot3adAggPortEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot3adAggPortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 1, 1])
	access = 2
	columns = {'dot3adAggPortIndex': dot3adAggPortIndex, 'dot3adAggPortActorSystemPriority': dot3adAggPortActorSystemPriority, 'dot3adAggPortActorSystemID': dot3adAggPortActorSystemID, 'dot3adAggPortActorAdminKey': dot3adAggPortActorAdminKey, 'dot3adAggPortActorOperKey': dot3adAggPortActorOperKey, 'dot3adAggPortPartnerAdminSystemPriority': dot3adAggPortPartnerAdminSystemPriority, 'dot3adAggPortPartnerOperSystemPriority': dot3adAggPortPartnerOperSystemPriority, 'dot3adAggPortPartnerAdminSystemID': dot3adAggPortPartnerAdminSystemID, 'dot3adAggPortPartnerOperSystemID': dot3adAggPortPartnerOperSystemID, 'dot3adAggPortPartnerAdminKey': dot3adAggPortPartnerAdminKey, 'dot3adAggPortPartnerOperKey': dot3adAggPortPartnerOperKey, 'dot3adAggPortSelectedAggID': dot3adAggPortSelectedAggID, 'dot3adAggPortAttachedAggID': dot3adAggPortAttachedAggID, 'dot3adAggPortActorPort': dot3adAggPortActorPort, 'dot3adAggPortActorPortPriority': dot3adAggPortActorPortPriority, 'dot3adAggPortPartnerAdminPort': dot3adAggPortPartnerAdminPort, 'dot3adAggPortPartnerOperPort': dot3adAggPortPartnerOperPort, 'dot3adAggPortPartnerAdminPortPriority': dot3adAggPortPartnerAdminPortPriority, 'dot3adAggPortPartnerOperPortPriority': dot3adAggPortPartnerOperPortPriority, 'dot3adAggPortActorAdminState': dot3adAggPortActorAdminState, 'dot3adAggPortActorOperState': dot3adAggPortActorOperState, 'dot3adAggPortPartnerAdminState': dot3adAggPortPartnerAdminState, 'dot3adAggPortPartnerOperState': dot3adAggPortPartnerOperState, 'dot3adAggPortAggregateOrIndividual': dot3adAggPortAggregateOrIndividual}


class dot3adAggPortStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot3adAggPortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 2, 1])
	access = 2
	columns = {'dot3adAggPortStatsLACPDUsRx': dot3adAggPortStatsLACPDUsRx, 'dot3adAggPortStatsMarkerPDUsRx': dot3adAggPortStatsMarkerPDUsRx, 'dot3adAggPortStatsMarkerResponsePDUsRx': dot3adAggPortStatsMarkerResponsePDUsRx, 'dot3adAggPortStatsUnknownRx': dot3adAggPortStatsUnknownRx, 'dot3adAggPortStatsIllegalRx': dot3adAggPortStatsIllegalRx, 'dot3adAggPortStatsLACPDUsTx': dot3adAggPortStatsLACPDUsTx, 'dot3adAggPortStatsMarkerPDUsTx': dot3adAggPortStatsMarkerPDUsTx, 'dot3adAggPortStatsMarkerResponsePDUsTx': dot3adAggPortStatsMarkerResponsePDUsTx}


class dot3adAggPortDebugEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot3adAggPortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 1, 2, 3, 1])
	access = 2
	columns = {'dot3adAggPortDebugRxState': dot3adAggPortDebugRxState, 'dot3adAggPortDebugLastRxTime': dot3adAggPortDebugLastRxTime, 'dot3adAggPortDebugMuxState': dot3adAggPortDebugMuxState, 'dot3adAggPortDebugMuxReason': dot3adAggPortDebugMuxReason, 'dot3adAggPortDebugActorChurnState': dot3adAggPortDebugActorChurnState, 'dot3adAggPortDebugPartnerChurnState': dot3adAggPortDebugPartnerChurnState, 'dot3adAggPortDebugActorChurnCount': dot3adAggPortDebugActorChurnCount, 'dot3adAggPortDebugPartnerChurnCount': dot3adAggPortDebugPartnerChurnCount, 'dot3adAggPortDebugActorSyncTransitionCount': dot3adAggPortDebugActorSyncTransitionCount, 'dot3adAggPortDebugPartnerSyncTransitionCount': dot3adAggPortDebugPartnerSyncTransitionCount, 'dot3adAggPortDebugActorChangeCount': dot3adAggPortDebugActorChangeCount, 'dot3adAggPortDebugPartnerChangeCount': dot3adAggPortDebugPartnerChangeCount}


# notifications (traps) 
# groups 
class dot3adAggGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 2, 1, 1])
	group = [dot3adAggActorSystemID, dot3adAggActorSystemPriority, dot3adAggAggregateOrIndividual, dot3adAggActorAdminKey, dot3adAggMACAddress, dot3adAggActorOperKey, dot3adAggPartnerSystemID, dot3adAggPartnerSystemPriority, dot3adAggPartnerOperKey, dot3adAggCollectorMaxDelay]

class dot3adTablesLastChangedGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 2, 1, 1, 6])
	group = [dot3adTablesLastChanged]

class dot3adAggPortListGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 2, 1, 2])
	group = [dot3adAggPortListPorts]

class dot3adAggPortGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 2, 1, 3])
	group = [dot3adAggPortActorSystemPriority, dot3adAggPortActorSystemID, dot3adAggPortActorAdminKey, dot3adAggPortActorOperKey, dot3adAggPortPartnerAdminSystemPriority, dot3adAggPortPartnerOperSystemPriority, dot3adAggPortPartnerAdminSystemID, dot3adAggPortPartnerOperSystemID, dot3adAggPortPartnerAdminKey, dot3adAggPortPartnerOperKey, dot3adAggPortSelectedAggID, dot3adAggPortAttachedAggID, dot3adAggPortActorPort, dot3adAggPortActorPortPriority, dot3adAggPortPartnerAdminPort, dot3adAggPortPartnerOperPort, dot3adAggPortPartnerAdminPortPriority, dot3adAggPortPartnerOperPortPriority, dot3adAggPortActorAdminState, dot3adAggPortActorOperState, dot3adAggPortPartnerAdminState, dot3adAggPortPartnerOperState, dot3adAggPortAggregateOrIndividual]

class dot3adAggPortStatsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 2, 1, 4])
	group = [dot3adAggPortStatsLACPDUsRx, dot3adAggPortStatsMarkerPDUsRx, dot3adAggPortStatsMarkerResponsePDUsRx, dot3adAggPortStatsUnknownRx, dot3adAggPortStatsIllegalRx, dot3adAggPortStatsLACPDUsTx, dot3adAggPortStatsMarkerPDUsTx, dot3adAggPortStatsMarkerResponsePDUsTx]

class dot3adAggPortDebugGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 2, 840, 10006, 300, 43, 2, 1, 5])
	group = [dot3adAggPortDebugRxState, dot3adAggPortDebugLastRxTime, dot3adAggPortDebugMuxState, dot3adAggPortDebugMuxReason, dot3adAggPortDebugActorChurnState, dot3adAggPortDebugPartnerChurnState, dot3adAggPortDebugActorChurnCount, dot3adAggPortDebugPartnerChurnCount, dot3adAggPortDebugActorSyncTransitionCount, dot3adAggPortDebugPartnerSyncTransitionCount, dot3adAggPortDebugActorChangeCount, dot3adAggPortDebugPartnerChangeCount]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)