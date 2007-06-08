# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from RFC1316_MIB import InstancePointer
from RFC1381_MIB import PositiveInteger
from RFC1155_SMI import Counter, TimeTicks
from RFC_1212 import OBJECT_TYPE
from RFC1382_MIB import X121Address
from RFC1213_MIB import DisplayString, transmission, ifIndex

class MIOX25_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/MIOX25-MIB'
	conformance = 2
	name = 'MIOX25-MIB'
	language = 1

# nodes
class miox(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38])
	name = 'miox'

class mioxPle(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1])
	name = 'mioxPle'

class mioxPeer(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 2])
	name = 'mioxPeer'


# macros
# types 
# scalars 
# columns
class mioxPleMaxCircuits(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mioxPleRefusedConnections(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mioxPleEnAddrToX121LkupFlrs(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mioxPleLastFailedEnAddr(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class mioxPleEnAddrToX121LkupFlrTime(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class mioxPleX121ToEnAddrLkupFlrs(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mioxPleLastFailedX121Address(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 7])
	syntaxobject = X121Address


class mioxPleX121ToEnAddrLkupFlrTime(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class mioxPleQbitFailures(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mioxPleQbitFailureRemoteAddress(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 10])
	syntaxobject = X121Address


class mioxPleQbitFailureTime(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class mioxPleMinimumOpenTimer(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 12])
	syntaxobject = PositiveInteger


class mioxPleInactivityTimer(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 13])
	syntaxobject = PositiveInteger


class mioxPleHoldDownTimer(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 14])
	syntaxobject = PositiveInteger


class mioxPleCollisionRetryTimer(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 15])
	syntaxobject = PositiveInteger


class mioxPleDefaultPeerId(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.InstancePointer


class mioxPeerIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 1])
	syntaxobject = PositiveInteger


class mioxPeerStatus(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'valid'), Enum(2, 'createRequest'), Enum(3, 'underCreation'), Enum(4, 'invalid'), Enum(5, 'clearCall'), Enum(6, 'makeCall')]


class mioxPeerMaxCircuits(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 3])
	syntaxobject = PositiveInteger


class mioxPeerIfIndex(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 4])
	syntaxobject = PositiveInteger


class mioxPeerConnectSeconds(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mioxPeerX25CallParamId(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.InstancePointer


class mioxPeerEnAddr(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class mioxPeerX121Address(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 8])
	syntaxobject = X121Address


class mioxPeerX25CircuitId(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.InstancePointer


class mioxPeerDescr(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class mioxPeerEncIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 2, 2, 1, 1])
	syntaxobject = PositiveInteger


class mioxPeerEncType(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# rows 
class mioxPleEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1])
	access = 2
	columns = {'mioxPleMaxCircuits': mioxPleMaxCircuits, 'mioxPleRefusedConnections': mioxPleRefusedConnections, 'mioxPleEnAddrToX121LkupFlrs': mioxPleEnAddrToX121LkupFlrs, 'mioxPleLastFailedEnAddr': mioxPleLastFailedEnAddr, 'mioxPleEnAddrToX121LkupFlrTime': mioxPleEnAddrToX121LkupFlrTime, 'mioxPleX121ToEnAddrLkupFlrs': mioxPleX121ToEnAddrLkupFlrs, 'mioxPleLastFailedX121Address': mioxPleLastFailedX121Address, 'mioxPleX121ToEnAddrLkupFlrTime': mioxPleX121ToEnAddrLkupFlrTime, 'mioxPleQbitFailures': mioxPleQbitFailures, 'mioxPleQbitFailureRemoteAddress': mioxPleQbitFailureRemoteAddress, 'mioxPleQbitFailureTime': mioxPleQbitFailureTime, 'mioxPleMinimumOpenTimer': mioxPleMinimumOpenTimer, 'mioxPleInactivityTimer': mioxPleInactivityTimer, 'mioxPleHoldDownTimer': mioxPleHoldDownTimer, 'mioxPleCollisionRetryTimer': mioxPleCollisionRetryTimer, 'mioxPleDefaultPeerId': mioxPleDefaultPeerId}


class mioxPeerEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([mioxPeerIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1])
	access = 2
	columns = {'mioxPeerIndex': mioxPeerIndex, 'mioxPeerStatus': mioxPeerStatus, 'mioxPeerMaxCircuits': mioxPeerMaxCircuits, 'mioxPeerIfIndex': mioxPeerIfIndex, 'mioxPeerConnectSeconds': mioxPeerConnectSeconds, 'mioxPeerX25CallParamId': mioxPeerX25CallParamId, 'mioxPeerEnAddr': mioxPeerEnAddr, 'mioxPeerX121Address': mioxPeerX121Address, 'mioxPeerX25CircuitId': mioxPeerX25CircuitId, 'mioxPeerDescr': mioxPeerDescr}


class mioxPeerEncEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([mioxPeerIndex, mioxPeerEncIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 38, 2, 2, 1])
	access = 2
	columns = {'mioxPeerEncIndex': mioxPeerEncIndex, 'mioxPeerEncType': mioxPeerEncType}


# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)