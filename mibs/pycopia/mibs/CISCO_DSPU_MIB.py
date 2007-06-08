# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Counter32, Integer32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoMgmt
from SNMPv2_TC import DisplayString, MacAddress, TruthValue, TimeStamp, RowStatus

class CISCO_DSPU_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-DSPU-MIB'
	conformance = 2
	name = 'CISCO-DSPU-MIB'
	language = 2
	description = 'Used to define and manage DSPU objects.'

# nodes
class ciscoDspuMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24])
	name = 'ciscoDspuMIB'

class dspuObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1])
	name = 'dspuObjects'

class dspuNode(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1])
	name = 'dspuNode'

class dspuPoolClass(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 2])
	name = 'dspuPoolClass'

class dspuPooledLu(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 3])
	name = 'dspuPooledLu'

class dspuPu(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4])
	name = 'dspuPu'

class dspuPuTraps(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 4])
	name = 'dspuPuTraps'

class dspuPuTrapsPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 4, 0])
	name = 'dspuPuTrapsPrefix'

class dspuLu(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5])
	name = 'dspuLu'

class dspuLuTraps(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 3])
	name = 'dspuLuTraps'

class dspuLuTrapsPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 3, 0])
	name = 'dspuLuTrapsPrefix'

class dspuSap(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6])
	name = 'dspuSap'

class dspuSapTraps(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 2])
	name = 'dspuSapTraps'

class ciscoDspuMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 2])
	name = 'ciscoDspuMIBConformance'

class ciscoDspuMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 1])
	name = 'ciscoDspuMIBCompliances'

class ciscoDspuMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 2])
	name = 'ciscoDspuMIBGroups'


# macros
# types 
# scalars 
class dspuNodeRsrb(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class dspuNodeRsrbLocalVirtualRing(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuNodeRsrbBridgeNumber(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuNodeRsrbTargetVirtualRing(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuNodeRsrbVirtualMacAddress(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class dspuNodeDefaultPu(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class dspuNodeDefaultPuWindowSize(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuNodeDefaultPuMaxIframe(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuNodeActivationWindow(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuNodeLastConfigChgTime(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


# columns
class dspuPoolClassIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPoolClassName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class dspuPoolClassInactivityTimeout(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPoolClassOperUpStreamLuDefs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPoolClassOperDnStreamLuDefs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPooledLuPeerPuIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 3, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPooledLuPeerLuLocalAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuAdminIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuAdminName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class dspuPuAdminType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'upstreamPu'), Enum(2, 'dnstreamPu')]


class dspuPuAdminRemoteMacAddress(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class dspuPuAdminRemoteSapAddress(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuAdminLocalSapAddress(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuAdminXid(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuAdminXidFmt(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'formatUnknown'), Enum(2, 'format0'), Enum(3, 'format3')]


class dspuPuAdminWindowSize(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuAdminMaxIframe(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuAdminLinkRetryCount(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuAdminLinkRetryTimeout(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuAdminStartPu(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class dspuPuAdminDlcType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'undefined'), Enum(2, 'sdlc'), Enum(5, 'ethernet'), Enum(6, 'tokenRing'), Enum(8, 'rsrb'), Enum(9, 'framerelay'), Enum(10, 'fddi'), Enum(11, 'qllc')]


class dspuPuAdminDlcUnit(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuAdminDlcPort(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuAdminFocalPoint(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class dspuPuAdminRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class dspuPuAdminRemoteAddress(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class dspuPuOperIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuOperName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class dspuPuOperType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'upstreamPu'), Enum(2, 'dnstreamPu')]


class dspuPuOperRemoteMacAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class dspuPuOperRemoteSapAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuOperLocalSapAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuOperXid(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuOperXidFmt(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'formatUnknown'), Enum(2, 'format0'), Enum(3, 'format3')]


class dspuPuOperWindowSize(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuOperMaxIframe(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuOperLinkRetryCount(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuOperLinkRetryTimeout(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuOperStartPu(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class dspuPuOperDlcType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'undefined'), Enum(2, 'sdlc'), Enum(5, 'ethernet'), Enum(6, 'tokenRing'), Enum(8, 'rsrb'), Enum(9, 'framerelay'), Enum(10, 'fddi'), Enum(11, 'qllc')]


class dspuPuOperDlcUnit(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuOperDlcPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuPuOperFocalPoint(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class dspuPuOperState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'active'), Enum(2, 'inactive')]


class dspuPuOperFsmState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'linkReset'), Enum(2, 'linkPendConnOut'), Enum(3, 'linkPendConnIn'), Enum(4, 'linkPendXid'), Enum(5, 'linkXidNeg'), Enum(6, 'linkConnOut'), Enum(7, 'linkConnIn'), Enum(8, 'linkConnected'), Enum(9, 'puPendAct'), Enum(10, 'puActive'), Enum(11, 'puBusy'), Enum(12, 'puPendInact'), Enum(13, 'linkPendDisc'), Enum(14, 'linkPendClose')]


class dspuPuOperStartTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class dspuPuOperLastStateChgTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 21])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class dspuPuOperRemoteAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 22])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class dspuPuStatsSentBytes(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dspuPuStatsRcvdBytes(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dspuPuStatsSentFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dspuPuStatsRcvdFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dspuPuStatsSentNegativeRsps(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dspuPuStatsRcvdNegativeRsps(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dspuPuStatsActiveLus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dspuPuStatsInactiveLus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dspuPuStatsBindLus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dspuPuStatsActivationFailures(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dspuPuStatsLastActivationFailureReason(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'noError'), Enum(2, 'otherError'), Enum(3, 'internalError'), Enum(4, 'configurationError'), Enum(5, 'puNegativeResponse'), Enum(6, 'puAlreadyActive')]


class dspuLuAdminLuLocalAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuLuAdminType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'pooled'), Enum(2, 'dedicated')]


class dspuLuAdminPoolClassName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class dspuLuAdminPeerPuIndex(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuLuAdminPeerLuLocalAddress(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuLuAdminRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class dspuLuOperLuLocalAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuLuOperType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'pooled'), Enum(2, 'dedicated')]


class dspuLuOperPoolClassName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class dspuLuOperPeerPuIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuLuOperPeerLuLocalAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuLuOperState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'active'), Enum(2, 'inactive')]


class dspuLuOperFsmState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'reset'), Enum(2, 'dnLuStarted'), Enum(3, 'upLuActive'), Enum(4, 'dnLuPendAct'), Enum(5, 'dnLuActUnav'), Enum(6, 'upLuPendAvail'), Enum(7, 'bothAvail'), Enum(8, 'dnLuPendInact'), Enum(9, 'upLuPendInact'), Enum(10, 'luInactivityTimeout'), Enum(11, 'dnInactivityPendInact')]


class dspuLuOperSessionState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'bound'), Enum(2, 'unbound')]


class dspuLuOperLastActivationFailureReason(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'noError'), Enum(2, 'otherError'), Enum(3, 'luNegativeResponse')]


class dspuSapAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuSapType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'upstreamSap'), Enum(2, 'dnstreamSap')]


class dspuSapDlcType(ColumnObject):
	status = 1
	access = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'undefined'), Enum(2, 'sdlc'), Enum(5, 'ethernet'), Enum(6, 'tokenRing'), Enum(8, 'rsrb'), Enum(9, 'framerelay'), Enum(10, 'fddi'), Enum(11, 'qllc')]


class dspuSapDlcUnit(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuSapDlcPort(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dspuSapOperState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'sapClosed'), Enum(2, 'sapOpening'), Enum(3, 'sapOpened'), Enum(4, 'sapClosing')]


class dspuSapRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class dspuPoolClassEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dspuPoolClassIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 2, 1, 1])
	access = 2
	columns = {'dspuPoolClassIndex': dspuPoolClassIndex, 'dspuPoolClassName': dspuPoolClassName, 'dspuPoolClassInactivityTimeout': dspuPoolClassInactivityTimeout, 'dspuPoolClassOperUpStreamLuDefs': dspuPoolClassOperUpStreamLuDefs, 'dspuPoolClassOperDnStreamLuDefs': dspuPoolClassOperDnStreamLuDefs}


class dspuPooledLuEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dspuPoolClassIndex, dspuPuOperIndex, dspuLuOperLuLocalAddress], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 3, 1, 1])
	access = 2
	columns = {'dspuPooledLuPeerPuIndex': dspuPooledLuPeerPuIndex, 'dspuPooledLuPeerLuLocalAddress': dspuPooledLuPeerLuLocalAddress}


class dspuPuAdminEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dspuPuAdminIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1])
	access = 2
	rowstatus = dspuPuAdminRowStatus
	columns = {'dspuPuAdminIndex': dspuPuAdminIndex, 'dspuPuAdminName': dspuPuAdminName, 'dspuPuAdminType': dspuPuAdminType, 'dspuPuAdminRemoteMacAddress': dspuPuAdminRemoteMacAddress, 'dspuPuAdminRemoteSapAddress': dspuPuAdminRemoteSapAddress, 'dspuPuAdminLocalSapAddress': dspuPuAdminLocalSapAddress, 'dspuPuAdminXid': dspuPuAdminXid, 'dspuPuAdminXidFmt': dspuPuAdminXidFmt, 'dspuPuAdminWindowSize': dspuPuAdminWindowSize, 'dspuPuAdminMaxIframe': dspuPuAdminMaxIframe, 'dspuPuAdminLinkRetryCount': dspuPuAdminLinkRetryCount, 'dspuPuAdminLinkRetryTimeout': dspuPuAdminLinkRetryTimeout, 'dspuPuAdminStartPu': dspuPuAdminStartPu, 'dspuPuAdminDlcType': dspuPuAdminDlcType, 'dspuPuAdminDlcUnit': dspuPuAdminDlcUnit, 'dspuPuAdminDlcPort': dspuPuAdminDlcPort, 'dspuPuAdminFocalPoint': dspuPuAdminFocalPoint, 'dspuPuAdminRowStatus': dspuPuAdminRowStatus, 'dspuPuAdminRemoteAddress': dspuPuAdminRemoteAddress}


class dspuPuOperEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dspuPuOperIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1])
	access = 2
	columns = {'dspuPuOperIndex': dspuPuOperIndex, 'dspuPuOperName': dspuPuOperName, 'dspuPuOperType': dspuPuOperType, 'dspuPuOperRemoteMacAddress': dspuPuOperRemoteMacAddress, 'dspuPuOperRemoteSapAddress': dspuPuOperRemoteSapAddress, 'dspuPuOperLocalSapAddress': dspuPuOperLocalSapAddress, 'dspuPuOperXid': dspuPuOperXid, 'dspuPuOperXidFmt': dspuPuOperXidFmt, 'dspuPuOperWindowSize': dspuPuOperWindowSize, 'dspuPuOperMaxIframe': dspuPuOperMaxIframe, 'dspuPuOperLinkRetryCount': dspuPuOperLinkRetryCount, 'dspuPuOperLinkRetryTimeout': dspuPuOperLinkRetryTimeout, 'dspuPuOperStartPu': dspuPuOperStartPu, 'dspuPuOperDlcType': dspuPuOperDlcType, 'dspuPuOperDlcUnit': dspuPuOperDlcUnit, 'dspuPuOperDlcPort': dspuPuOperDlcPort, 'dspuPuOperFocalPoint': dspuPuOperFocalPoint, 'dspuPuOperState': dspuPuOperState, 'dspuPuOperFsmState': dspuPuOperFsmState, 'dspuPuOperStartTime': dspuPuOperStartTime, 'dspuPuOperLastStateChgTime': dspuPuOperLastStateChgTime, 'dspuPuOperRemoteAddress': dspuPuOperRemoteAddress}


class dspuPuStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dspuPuOperIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1])
	access = 2
	columns = {'dspuPuStatsSentBytes': dspuPuStatsSentBytes, 'dspuPuStatsRcvdBytes': dspuPuStatsRcvdBytes, 'dspuPuStatsSentFrames': dspuPuStatsSentFrames, 'dspuPuStatsRcvdFrames': dspuPuStatsRcvdFrames, 'dspuPuStatsSentNegativeRsps': dspuPuStatsSentNegativeRsps, 'dspuPuStatsRcvdNegativeRsps': dspuPuStatsRcvdNegativeRsps, 'dspuPuStatsActiveLus': dspuPuStatsActiveLus, 'dspuPuStatsInactiveLus': dspuPuStatsInactiveLus, 'dspuPuStatsBindLus': dspuPuStatsBindLus, 'dspuPuStatsActivationFailures': dspuPuStatsActivationFailures, 'dspuPuStatsLastActivationFailureReason': dspuPuStatsLastActivationFailureReason}


class dspuLuAdminEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dspuPuAdminIndex, dspuLuAdminLuLocalAddress], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 1, 1])
	access = 2
	rowstatus = dspuLuAdminRowStatus
	columns = {'dspuLuAdminLuLocalAddress': dspuLuAdminLuLocalAddress, 'dspuLuAdminType': dspuLuAdminType, 'dspuLuAdminPoolClassName': dspuLuAdminPoolClassName, 'dspuLuAdminPeerPuIndex': dspuLuAdminPeerPuIndex, 'dspuLuAdminPeerLuLocalAddress': dspuLuAdminPeerLuLocalAddress, 'dspuLuAdminRowStatus': dspuLuAdminRowStatus}


class dspuLuOperEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dspuPuOperIndex, dspuLuOperLuLocalAddress], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1])
	access = 2
	columns = {'dspuLuOperLuLocalAddress': dspuLuOperLuLocalAddress, 'dspuLuOperType': dspuLuOperType, 'dspuLuOperPoolClassName': dspuLuOperPoolClassName, 'dspuLuOperPeerPuIndex': dspuLuOperPeerPuIndex, 'dspuLuOperPeerLuLocalAddress': dspuLuOperPeerLuLocalAddress, 'dspuLuOperState': dspuLuOperState, 'dspuLuOperFsmState': dspuLuOperFsmState, 'dspuLuOperSessionState': dspuLuOperSessionState, 'dspuLuOperLastActivationFailureReason': dspuLuOperLastActivationFailureReason}


class dspuSapEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dspuSapDlcType, dspuSapDlcUnit, dspuSapDlcPort, dspuSapAddress], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1, 1])
	access = 2
	rowstatus = dspuSapRowStatus
	columns = {'dspuSapAddress': dspuSapAddress, 'dspuSapType': dspuSapType, 'dspuSapDlcType': dspuSapDlcType, 'dspuSapDlcUnit': dspuSapDlcUnit, 'dspuSapDlcPort': dspuSapDlcPort, 'dspuSapOperState': dspuSapOperState, 'dspuSapRowStatus': dspuSapRowStatus}


# notifications (traps) 
class newdspuPuStateChangeTrap(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 4, 0, 1])

class newdspuPuActivationFailureTrap(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 4, 0, 2])

class dspuPuStateChangeTrap(NotificationObject):
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 4, 1])

class dspuPuActivationFailureTrap(NotificationObject):
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 4, 2])

class newdspuLuStateChangeTrap(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 3, 0, 1])

class dspuLuActivationFailureTrap(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 3, 0, 2])

class dspuLuStateChangeTrap(NotificationObject):
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 3, 1])

class dspuSapStateChangeTrap(NotificationObject):
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 2, 1])

# groups 
class dspuNodeGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 2, 1])
	group = [dspuNodeRsrb, dspuNodeRsrbLocalVirtualRing, dspuNodeRsrbBridgeNumber, dspuNodeRsrbTargetVirtualRing, dspuNodeRsrbVirtualMacAddress, dspuNodeDefaultPu, dspuNodeDefaultPuWindowSize, dspuNodeDefaultPuMaxIframe, dspuNodeActivationWindow, dspuNodeLastConfigChgTime]

class dspuPoolClassGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 2, 2])
	group = [dspuPoolClassName, dspuPoolClassInactivityTimeout, dspuPoolClassOperUpStreamLuDefs, dspuPoolClassOperDnStreamLuDefs]

class dspuPooledLuGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 2, 3])
	group = [dspuPooledLuPeerPuIndex, dspuPooledLuPeerLuLocalAddress]

class dspuSapGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 2, 6])
	group = [dspuSapType, dspuSapOperState, dspuSapRowStatus]

class dspuPuGroupV11R01(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 2, 7])
	group = [dspuPuAdminName, dspuPuAdminType, dspuPuAdminRemoteMacAddress, dspuPuAdminRemoteSapAddress, dspuPuAdminLocalSapAddress, dspuPuAdminXid, dspuPuAdminXidFmt, dspuPuAdminWindowSize, dspuPuAdminMaxIframe, dspuPuAdminLinkRetryCount, dspuPuAdminLinkRetryTimeout, dspuPuAdminStartPu, dspuPuAdminDlcType, dspuPuAdminDlcUnit, dspuPuAdminDlcPort, dspuPuAdminFocalPoint, dspuPuAdminRowStatus, dspuPuAdminRemoteAddress, dspuPuOperName, dspuPuOperType, dspuPuOperRemoteMacAddress, dspuPuOperRemoteSapAddress, dspuPuOperLocalSapAddress, dspuPuOperXid, dspuPuOperXidFmt, dspuPuOperWindowSize, dspuPuOperMaxIframe, dspuPuOperLinkRetryCount, dspuPuOperLinkRetryTimeout, dspuPuOperStartPu, dspuPuOperDlcType, dspuPuOperDlcUnit, dspuPuOperDlcPort, dspuPuOperFocalPoint, dspuPuOperState, dspuPuOperFsmState, dspuPuOperStartTime, dspuPuOperLastStateChgTime, dspuPuOperRemoteAddress, dspuPuStatsSentBytes, dspuPuStatsRcvdBytes, dspuPuStatsSentFrames, dspuPuStatsRcvdFrames, dspuPuStatsSentNegativeRsps, dspuPuStatsRcvdNegativeRsps, dspuPuStatsActiveLus, dspuPuStatsInactiveLus, dspuPuStatsBindLus, dspuPuStatsActivationFailures, dspuPuStatsLastActivationFailureReason]

class dspuLuGroupV11R01(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 2, 8])
	group = [dspuLuAdminType, dspuLuAdminPoolClassName, dspuLuAdminPeerPuIndex, dspuLuAdminPeerLuLocalAddress, dspuLuAdminRowStatus, dspuLuOperType, dspuLuOperPoolClassName, dspuLuOperPeerPuIndex, dspuLuOperPeerLuLocalAddress, dspuLuOperState, dspuLuOperFsmState, dspuLuOperSessionState, dspuLuOperLastActivationFailureReason]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)