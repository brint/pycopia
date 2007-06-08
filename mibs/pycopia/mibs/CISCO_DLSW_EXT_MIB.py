# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from IF_MIB import InterfaceIndex
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, TimeTicks
from DLSW_MIB import dlswTConnConfigEntry, dlswTConnOperEntry, dlswTConnTcpConfigEntry, dlswIfEntry, dlswCircuitEntry, dlswTConnConfigIndex, DlcType, TAddress, MacAddressNC, LFSize, dlswTConnOperState, dlswCircuitState
from CISCO_TC import SAPType
from CISCO_SMI import ciscoMgmt
from CISCO_FRAME_RELAY_MIB import DlciNumber
from SNMPv2_TC import TruthValue, TEXTUAL_CONVENTION, DisplayString

class CISCO_DLSW_EXT_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-DLSW-EXT-MIB'
	conformance = 2
	name = 'CISCO-DLSW-EXT-MIB'
	language = 2
	description = 'The MIB module for management of Cisco specific Data Link\nSwitching protocol enhancements.  DLSw is described in \nRFC 1795 and RFC 2024.\n\nDLSw+ Defined\n\nData link switching Plus (DLSw+) is a means of transporting\nSystems Network Architecture (SNA) and NetBIOS traffic over\nan IP network. The end systems can attach to the network over\nToken Ring, Ethernet, Synchronous Data Link Control\n(SDLC) protocol, or Qualified Logical Link Control (QLLC).\nDLSw+ switches between diverse media, and locally terminates\nthe data links, keeping acknowledgments, keepalives, and polling\noff of the WAN. Local termination of data links also\neliminates data link control time-outs that can occur during\ntransient network congestion or when rerouting around failed\nlinks. Finally, DLSw+ provides a mechanism for dynamically\nsearching a network for SNA or NetBIOS resources and\nincludes caching algorithms that minimize the broadcast traffic\nrequired. \n\nIn this document, DLSw+ routers are referred to as\npeers, or partners. The connection between two DLSw+\nrouters is referred to as a peer connection. A DLSw circuit is\ncomprised of the data link control connection between the\noriginating end system and the originating router, the connection\nbetween the two routers (typically a TCP connection), and\nthe data link control connection between the target router and\nthe target end system. A single peer connection can carry\nmultiple circuits.\n\nThe transport connection between DLSw+ routers can vary according\nto the needs of the network and is not tied to TCP/IP\nas the DLSw standard is. Cisco supports four different transport\nprotocols between DLSw+ routers:\n\nTCP/IP-for transport of SNA and NetBIOS traffic across WANs where\nlocal acknowledgment is required to minimize\nunnecessary traffic and prevent data-link control timeouts and\nwhere non-disruptive rerouting around link failures is\ncritical. This transport option is required when DLSw+ is\noperating in DLSw standards mode. \n\nFST/IP-for transport across WANs with an arbitrary topology and\nwith sufficient bandwidth to accommodate SNA\nand NetBIOS traffic. This solution allows for rerouting around\nlink failures, but recovery may be disruptive depending\non the time required to find an alternate path. This option does\nnot support local acknowledgment of frames. \n\nDirect-encapsulation for transport across a point-to-point or\nFrame Relay connection where the benefits of an\narbitrary topology are not important and where nondisruptive\nrerouting around link failures is not required. This option\ndoes not support local acknowledgment of frames. \n\nDLSw Lite-also known as Logical Link Control, Type2 (LLC2)\nencapsulation -for transport across a point-to-point\nconnection (currently only Frame Relay is supported) where\nlocal acknowledgment and reliable transport are\nimportant, but where nondisruptive rerouting around link\nfailures is not required. DLSw Lite uses RFC 1490\nencapsulation of LLC2.'

# nodes
class ciscoDlswExtMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74])
	name = 'ciscoDlswExtMIB'

class ciscoDlswExtMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1])
	name = 'ciscoDlswExtMIBObjects'

class cdeDomains(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 1])
	name = 'cdeDomains'

class cdeFSTDomain(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 1, 1])
	name = 'cdeFSTDomain'

class cdeDirectHdlcDomain(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 1, 2])
	name = 'cdeDirectHdlcDomain'

class cdeDirectFrameRelayDomain(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 1, 3])
	name = 'cdeDirectFrameRelayDomain'

class cdeLlc2Domain(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 1, 4])
	name = 'cdeLlc2Domain'

class cdeNode(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2])
	name = 'cdeNode'

class cdeTConn(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3])
	name = 'cdeTConn'

class cdeTConnSpecific(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3])
	name = 'cdeTConnSpecific'

class cdeTConnTcp(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 1])
	name = 'cdeTConnTcp'

class cdeTConnDirect(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2])
	name = 'cdeTConnDirect'

class cdeInterface(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 4])
	name = 'cdeInterface'

class cdeCircuit(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5])
	name = 'cdeCircuit'

class cdeFast(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6])
	name = 'cdeFast'

class cdeTrapControl(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 7])
	name = 'cdeTrapControl'

class cdeTrapsPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 2])
	name = 'cdeTrapsPrefix'

class cdeTraps(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 2, 0])
	name = 'cdeTraps'

class cdeMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 3])
	name = 'cdeMIBConformance'

class cdeMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 1])
	name = 'cdeMIBCompliances'

class cdeMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2])
	name = 'cdeMIBGroups'


# macros
# types 

class TDomainType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'tcp'), Enum(2, 'fst'), Enum(3, 'directHdlc'), Enum(4, 'directFrameRelay'), Enum(5, 'llc2')]


class Cost(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(1, 5))


class KeepaliveInterval(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 1200))


class TCPQueueMax(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(25, 2000))

# scalars 
class cdeNodeTAddr(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.TAddress


class cdeNodeGroup(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cdeNodeBorder(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 3])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cdeNodeCost(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 4])
	syntaxobject = Cost


class cdeNodeKeepaliveInterval(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 5])
	syntaxobject = KeepaliveInterval
	access = 5
	units = 'Seconds'


class cdeNodePassiveConnect(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 6])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cdeNodeBiuSegment(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 7])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cdeNodeInitPacingWindow(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'packets'


class cdeNodeMaxPacingWindow(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'packets'


class cdeNodePromiscuous(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 10])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cdeNodePromPeerDefaultsCost(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 11])
	syntaxobject = Cost


class cdeNodePromPeerDefaultsDestMac(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 12])
	syntaxobject = MacAddressNC


class cdeNodePromPeerDefaultsKeepaliveInterval(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 13])
	syntaxobject = KeepaliveInterval
	access = 5
	units = 'Seconds'


class cdeNodePromPeerDefaultsLFSize(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 14])
	syntaxobject = LFSize
	access = 5
	units = 'bytes'


class cdeNodePromPeerDefaultsTCPQueueMax(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 15])
	syntaxobject = TCPQueueMax
	access = 5
	units = 'packets'


class cdeNodePeerOnDemandDefaultsCost(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 16])
	syntaxobject = Cost


class cdeNodePeerOnDemandDefaultsFst(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 17])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cdeNodePeerOnDemandDefaultsInactivityInterval(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 18])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'Minutes'


class cdeNodePeerOnDemandDefaultsKeepaliveInterval(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 19])
	syntaxobject = KeepaliveInterval
	access = 5
	units = 'Seconds'


class cdeNodePeerOnDemandDefaultsLFSize(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 20])
	syntaxobject = LFSize


class cdeNodePeerOnDemandDefaultsPriority(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 21])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cdeNodePeerOnDemandDefaultsTCPQueueMax(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 22])
	syntaxobject = TCPQueueMax
	access = 5
	units = 'packets'


class cdeTrapCntlTConn(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 7, 1])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cdeTrapCntlCircuit(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 7, 2])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


# columns
class cdeTConnConfigTDomainType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 1])
	syntaxobject = TDomainType


class cdeTConnConfigLocalAck(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cdeTConnConfigCost(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 3])
	syntaxobject = Cost


class cdeTConnConfigLFSize(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 4])
	syntaxobject = LFSize


class cdeTConnConfigKeepaliveInterval(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 5])
	syntaxobject = KeepaliveInterval
	access = 5
	units = 'Seconds'


class cdeTConnConfigBackup(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cdeTConnConfigBackupTAddr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.TAddress


class cdeTConnConfigBackupLinger(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cdeTConnConfigBackupLingerInterval(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'Minutes'


class cdeTConnConfigPriority(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cdeTConnConfigDestMac(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 11])
	syntaxobject = MacAddressNC


class cdeTConnConfigDynamic(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cdeTConnConfigDynamicNoLlc(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'Minutes'


class cdeTConnConfigDynamicInactivityInterval(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'Minutes'


class cdeTConnOperPartnerCost(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1, 1])
	syntaxobject = Cost


class cdeTConnOperPartnerPriority(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cdeTConnOperPartnerBorderPeer(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cdeTConnOperPartnerGroupNum(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cdeTConnOperTDomainType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1, 5])
	syntaxobject = TDomainType


class cdeTConnTcpConfigQueueMax(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 1, 1, 1, 1])
	syntaxobject = TCPQueueMax
	access = 5
	units = 'packets'


class cdeTConnDirectConfigIfIndex(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2, 1, 1, 1])
	syntaxobject = InterfaceIndex


class cdeTConnDirectConfigMediaEncap(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'directHdlc'), Enum(2, 'directFrameRelay'), Enum(3, 'llc2')]


class cdeTConnDirectConfigFrameRelayDlci(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2, 1, 1, 3])
	syntaxobject = DlciNumber


class cdeIfType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 4, 1, 1, 1])
	syntaxobject = DlcType


class cdeCircuitS1Name(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cdeCircuitS2Name(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cdeCircuitS1IdBlock(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cdeCircuitS1IdNum(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cdeFastS1Mac(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 1])
	syntaxobject = MacAddressNC


class cdeFastS1Sap(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 2])
	syntaxobject = SAPType


class cdeFastS2Mac(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 3])
	syntaxobject = MacAddressNC


class cdeFastS2Sap(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 4])
	syntaxobject = SAPType


class cdeFastS1IfIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 5])
	syntaxobject = InterfaceIndex


class cdeFastS1RouteInfo(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class cdeFastS1CacheId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class cdeFastS2TDomain(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class cdeFastS2TAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.TAddress


class cdeFastS2CacheId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class cdeFastOrigin(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 's1'), Enum(2, 's2')]


class cdeFastTimeToLive(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks
	access = 4
	units = 'hundredths of a second'


# rows 
from DLSW_MIB import dlswTConnConfigIndex
class cdeTConnConfigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dlswTConnConfigIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1])
	access = 2
	columns = {'cdeTConnConfigTDomainType': cdeTConnConfigTDomainType, 'cdeTConnConfigLocalAck': cdeTConnConfigLocalAck, 'cdeTConnConfigCost': cdeTConnConfigCost, 'cdeTConnConfigLFSize': cdeTConnConfigLFSize, 'cdeTConnConfigKeepaliveInterval': cdeTConnConfigKeepaliveInterval, 'cdeTConnConfigBackup': cdeTConnConfigBackup, 'cdeTConnConfigBackupTAddr': cdeTConnConfigBackupTAddr, 'cdeTConnConfigBackupLinger': cdeTConnConfigBackupLinger, 'cdeTConnConfigBackupLingerInterval': cdeTConnConfigBackupLingerInterval, 'cdeTConnConfigPriority': cdeTConnConfigPriority, 'cdeTConnConfigDestMac': cdeTConnConfigDestMac, 'cdeTConnConfigDynamic': cdeTConnConfigDynamic, 'cdeTConnConfigDynamicNoLlc': cdeTConnConfigDynamicNoLlc, 'cdeTConnConfigDynamicInactivityInterval': cdeTConnConfigDynamicInactivityInterval}


from DLSW_MIB import dlswTConnOperTDomain
from DLSW_MIB import dlswTConnOperRemoteTAddr
class cdeTConnOperEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dlswTConnOperTDomain, dlswTConnOperRemoteTAddr], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1])
	access = 2
	columns = {'cdeTConnOperPartnerCost': cdeTConnOperPartnerCost, 'cdeTConnOperPartnerPriority': cdeTConnOperPartnerPriority, 'cdeTConnOperPartnerBorderPeer': cdeTConnOperPartnerBorderPeer, 'cdeTConnOperPartnerGroupNum': cdeTConnOperPartnerGroupNum, 'cdeTConnOperTDomainType': cdeTConnOperTDomainType}


from DLSW_MIB import dlswTConnConfigIndex
class cdeTConnTcpConfigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dlswTConnConfigIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 1, 1, 1])
	access = 2
	columns = {'cdeTConnTcpConfigQueueMax': cdeTConnTcpConfigQueueMax}


class cdeTConnDirectConfigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dlswTConnConfigIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2, 1, 1])
	access = 2
	columns = {'cdeTConnDirectConfigIfIndex': cdeTConnDirectConfigIfIndex, 'cdeTConnDirectConfigMediaEncap': cdeTConnDirectConfigMediaEncap, 'cdeTConnDirectConfigFrameRelayDlci': cdeTConnDirectConfigFrameRelayDlci}


from IF_MIB import ifIndex
class cdeIfEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 4, 1, 1])
	access = 2
	columns = {'cdeIfType': cdeIfType}


from DLSW_MIB import dlswCircuitS1Mac
from DLSW_MIB import dlswCircuitS1Sap
from DLSW_MIB import dlswCircuitS2Mac
from DLSW_MIB import dlswCircuitS2Sap
class cdeCircuitEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dlswCircuitS1Mac, dlswCircuitS1Sap, dlswCircuitS2Mac, dlswCircuitS2Sap], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1, 1])
	access = 2
	columns = {'cdeCircuitS1Name': cdeCircuitS1Name, 'cdeCircuitS2Name': cdeCircuitS2Name, 'cdeCircuitS1IdBlock': cdeCircuitS1IdBlock, 'cdeCircuitS1IdNum': cdeCircuitS1IdNum}


class cdeFastEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cdeFastS1Mac, cdeFastS1Sap, cdeFastS2Mac, cdeFastS2Sap], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1])
	access = 2
	columns = {'cdeFastS1Mac': cdeFastS1Mac, 'cdeFastS1Sap': cdeFastS1Sap, 'cdeFastS2Mac': cdeFastS2Mac, 'cdeFastS2Sap': cdeFastS2Sap, 'cdeFastS1IfIndex': cdeFastS1IfIndex, 'cdeFastS1RouteInfo': cdeFastS1RouteInfo, 'cdeFastS1CacheId': cdeFastS1CacheId, 'cdeFastS2TDomain': cdeFastS2TDomain, 'cdeFastS2TAddress': cdeFastS2TAddress, 'cdeFastS2CacheId': cdeFastS2CacheId, 'cdeFastOrigin': cdeFastOrigin, 'cdeFastTimeToLive': cdeFastTimeToLive}


# notifications (traps) 
class cdeTrapTConnUpDown(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 2, 0, 1])

class cdeTrapCircuitUpDown(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 2, 0, 2])

# groups 
class cdeMIBNodeGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 1])
	group = [cdeNodeTAddr, cdeNodeGroup, cdeNodeBorder, cdeNodeCost, cdeNodeKeepaliveInterval, cdeNodePassiveConnect, cdeNodeBiuSegment, cdeNodeInitPacingWindow, cdeNodeMaxPacingWindow, cdeNodePromiscuous, cdeNodePromPeerDefaultsCost, cdeNodePromPeerDefaultsDestMac, cdeNodePromPeerDefaultsKeepaliveInterval, cdeNodePromPeerDefaultsLFSize, cdeNodePromPeerDefaultsTCPQueueMax, cdeNodePeerOnDemandDefaultsCost, cdeNodePeerOnDemandDefaultsFst, cdeNodePeerOnDemandDefaultsInactivityInterval, cdeNodePeerOnDemandDefaultsKeepaliveInterval, cdeNodePeerOnDemandDefaultsLFSize, cdeNodePeerOnDemandDefaultsPriority, cdeNodePeerOnDemandDefaultsTCPQueueMax]

class cdeMIBTConnConfigGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 2])
	group = [cdeTConnConfigTDomainType, cdeTConnConfigLocalAck, cdeTConnConfigCost, cdeTConnConfigLFSize, cdeTConnConfigKeepaliveInterval, cdeTConnConfigBackup, cdeTConnConfigBackupTAddr, cdeTConnConfigBackupLinger, cdeTConnConfigBackupLingerInterval, cdeTConnConfigPriority, cdeTConnConfigDestMac, cdeTConnConfigDynamic, cdeTConnConfigDynamicNoLlc, cdeTConnConfigDynamicInactivityInterval]

class cdeMIBTConnOperGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 3])
	group = [cdeTConnOperPartnerCost, cdeTConnOperPartnerPriority, cdeTConnOperPartnerBorderPeer, cdeTConnOperPartnerGroupNum, cdeTConnOperTDomainType]

class cdeMIBTConnTcpConfigGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 4])
	group = [cdeTConnTcpConfigQueueMax]

class cdeMIBTConnDirectConfigGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 5])
	group = [cdeTConnDirectConfigIfIndex, cdeTConnDirectConfigMediaEncap, cdeTConnDirectConfigFrameRelayDlci]

class cdeMIBInterfaceGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 6])
	group = [cdeIfType]

class cdeMIBCircuitGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 7])
	group = [cdeCircuitS1Name, cdeCircuitS2Name, cdeCircuitS1IdBlock, cdeCircuitS1IdNum]

class cdeMIBFastGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 8])
	group = [cdeFastS1IfIndex, cdeFastS1RouteInfo, cdeFastS1CacheId, cdeFastS2TDomain, cdeFastS2TAddress, cdeFastS2CacheId, cdeFastOrigin, cdeFastTimeToLive]

class cdeTrapControlGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 9])
	group = [cdeTrapCntlTConn, cdeTrapCntlCircuit]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)