# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from RFC_1212 import OBJECT_TYPE
from RFC1213_MIB import mib_2
from RFC1155_SMI import NetworkAddress, IpAddress, Counter
from RFC_1215 import TRAP_TYPE

class RFC1269_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/RFC1269-MIB'
	conformance = 5
	name = 'RFC1269-MIB'
	language = 1

# nodes
class bgp(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15])
	name = 'bgp'


# macros
# types 
# scalars 
class bgpVersion(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 1])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class bgpLocalAs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class bgpIdentifier(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 4])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


# columns
class bgpPeerIdentifier(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class bgpPeerState(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'idle'), Enum(2, 'connect'), Enum(3, 'active'), Enum(4, 'opensent'), Enum(5, 'openconfirm'), Enum(6, 'established')]


class bgpPeerAdminStatus(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class bgpPeerNegotiatedVersion(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class bgpPeerLocalAddr(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class bgpPeerLocalPort(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class bgpPeerRemoteAddr(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class bgpPeerRemotePort(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class bgpPeerRemoteAs(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 3, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class bgpPeerInUpdates(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 3, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class bgpPeerOutUpdates(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 3, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class bgpPeerInTotalMessages(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 3, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class bgpPeerOutTotalMessages(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 3, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class bgpPeerLastError(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 3, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class bgpPathAttrPeer(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 5, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class bgpPathAttrDestNetwork(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 5, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class bgpPathAttrOrigin(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 5, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'igp'), Enum(2, 'egp'), Enum(3, 'incomplete')]


class bgpPathAttrASPath(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 5, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class bgpPathAttrNextHop(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 5, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class bgpPathAttrInterASMetric(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 5, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# rows 
class bgpPeerEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([bgpPeerRemoteAddr], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 3, 1])
	access = 2
	columns = {'bgpPeerIdentifier': bgpPeerIdentifier, 'bgpPeerState': bgpPeerState, 'bgpPeerAdminStatus': bgpPeerAdminStatus, 'bgpPeerNegotiatedVersion': bgpPeerNegotiatedVersion, 'bgpPeerLocalAddr': bgpPeerLocalAddr, 'bgpPeerLocalPort': bgpPeerLocalPort, 'bgpPeerRemoteAddr': bgpPeerRemoteAddr, 'bgpPeerRemotePort': bgpPeerRemotePort, 'bgpPeerRemoteAs': bgpPeerRemoteAs, 'bgpPeerInUpdates': bgpPeerInUpdates, 'bgpPeerOutUpdates': bgpPeerOutUpdates, 'bgpPeerInTotalMessages': bgpPeerInTotalMessages, 'bgpPeerOutTotalMessages': bgpPeerOutTotalMessages, 'bgpPeerLastError': bgpPeerLastError}


class bgpPathAttrEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([bgpPathAttrDestNetwork, bgpPathAttrPeer], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 5, 1])
	access = 2
	columns = {'bgpPathAttrPeer': bgpPathAttrPeer, 'bgpPathAttrDestNetwork': bgpPathAttrDestNetwork, 'bgpPathAttrOrigin': bgpPathAttrOrigin, 'bgpPathAttrASPath': bgpPathAttrASPath, 'bgpPathAttrNextHop': bgpPathAttrNextHop, 'bgpPathAttrInterASMetric': bgpPathAttrInterASMetric}


# notifications (traps) 
class bgpEstablished(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 0, 1])

class bgpBackwardTransition(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 15, 0, 2])

# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)