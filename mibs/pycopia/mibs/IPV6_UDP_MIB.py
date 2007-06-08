# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, mib_2, experimental
from IPV6_TC import Ipv6Address, Ipv6IfIndexOrZero

class IPV6_UDP_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/IPV6-UDP-MIB'
	conformance = 3
	name = 'IPV6-UDP-MIB'
	language = 2
	description = 'The MIB module for entities implementing UDP over IPv6.'

# nodes
class udp(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 7])
	name = 'udp'

class ipv6UdpMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 87])
	name = 'ipv6UdpMIB'

class ipv6UdpConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 87, 2])
	name = 'ipv6UdpConformance'

class ipv6UdpCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 87, 2, 1])
	name = 'ipv6UdpCompliances'

class ipv6UdpGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 87, 2, 2])
	name = 'ipv6UdpGroups'


# macros
# types 
# scalars 
# columns
class ipv6UdpLocalAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 7, 6, 1, 1])
	syntaxobject = Ipv6Address


class ipv6UdpLocalPort(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 7, 6, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipv6UdpIfIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 7, 6, 1, 3])
	syntaxobject = Ipv6IfIndexOrZero


# rows 
class ipv6UdpEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ipv6UdpLocalAddress, ipv6UdpLocalPort, ipv6UdpIfIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 7, 6, 1])
	access = 2
	columns = {'ipv6UdpLocalAddress': ipv6UdpLocalAddress, 'ipv6UdpLocalPort': ipv6UdpLocalPort, 'ipv6UdpIfIndex': ipv6UdpIfIndex}


# notifications (traps) 
# groups 
class ipv6UdpGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 87, 2, 2, 1])
	group = [ipv6UdpIfIndex]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)