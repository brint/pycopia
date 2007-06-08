# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, TimeTicks, Integer32, Counter32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoMgmt
from TCP_MIB import tcpConnEntry

class CISCO_TCP_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-TCP-MIB'
	name = 'CISCO-TCP-MIB'
	language = 2
	description = 'An extension to the IETF MIB module for managing\nTCP implementations'

# nodes
class ciscoTcpMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 6])
	name = 'ciscoTcpMIB'

class ciscoTcpMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 6, 1])
	name = 'ciscoTcpMIBObjects'

class ciscoTcpMIBTraps(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 6, 2])
	name = 'ciscoTcpMIBTraps'

class ciscoTcpMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 6, 3])
	name = 'ciscoTcpMIBConformance'

class ciscoTcpMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 1])
	name = 'ciscoTcpMIBCompliances'

class ciscoTcpMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 2])
	name = 'ciscoTcpMIBGroups'


# macros
# types 
# scalars 
# columns
class ciscoTcpConnInBytes(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoTcpConnOutBytes(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoTcpConnInPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoTcpConnOutPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoTcpConnElapsed(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class ciscoTcpConnSRTT(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 4
	units = 'milliseconds'


# rows 
from TCP_MIB import tcpConnLocalAddress
from TCP_MIB import tcpConnLocalPort
from TCP_MIB import tcpConnRemAddress
from TCP_MIB import tcpConnRemPort
class ciscoTcpConnEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([tcpConnLocalAddress, tcpConnLocalPort, tcpConnRemAddress, tcpConnRemPort], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1])
	access = 2
	columns = {'ciscoTcpConnInBytes': ciscoTcpConnInBytes, 'ciscoTcpConnOutBytes': ciscoTcpConnOutBytes, 'ciscoTcpConnInPkts': ciscoTcpConnInPkts, 'ciscoTcpConnOutPkts': ciscoTcpConnOutPkts, 'ciscoTcpConnElapsed': ciscoTcpConnElapsed, 'ciscoTcpConnSRTT': ciscoTcpConnSRTT}


# notifications (traps) 
# groups 
class ciscoTcpMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 2, 1])
	group = [ciscoTcpConnInBytes, ciscoTcpConnOutBytes, ciscoTcpConnInPkts, ciscoTcpConnOutPkts, ciscoTcpConnElapsed, ciscoTcpConnSRTT]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)