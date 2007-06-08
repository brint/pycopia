# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Counter32, Counter64, Integer32, Gauge32
from CISCO_CHANNEL_MIB import cipCardEntryIndex, cipCardDtrBrdIndex, cipCardSubChannelIndex
from CISCO_SNA_LLC_MIB import llcPortVirtualIndex, llcSapNumber
from CISCO_SMI import ciscoMgmt
from RFC1213_MIB import ifIndex
from SNMPv2_TC import RowStatus, TEXTUAL_CONVENTION

class CISCO_CIPCSNA_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-CIPCSNA-MIB'
	conformance = 2
	name = 'CISCO-CIPCSNA-MIB'
	language = 2
	description = "This is the Management Information Base (MIB) \nmodule for objects used to manage the cisco Systems \nNetwork Architecture (SNA) support on Cisco Mainframe\nChannel Connection (CMCC) cards, also called the \nCIP-SNA feature.\n\n---------------------------------------------------\n| Acronym Definitions:                            |\n| CMCC      =  Cisco Mainframe Channel Connection |\n| CIP      =   Channel Interface Processor        |\n| CTA      =   Channel Transport Architecture     |\n| SNA      =   Systems Network Architecture       |\n| CIP-SNA  =   CNA  =  CSNA  =  SNA Support on    |\n|                               a CMCC card       |\n---------------------------------------------------\n\n\nThis mib consists of the following tables:\n1) CSNA Administration \n2) CSNA Operational\n3) CSNA Statistics\n4) Max Sessions Administration\n5) Max Sessions Operational\n8) LLC2/CSNA Connection mapping\n\nThe following is a set of IBM channel terminology:\n1) The Channel Subsystem is the way a host performs\nI/O.\n2) A Channel Path is the path to the Channel Control\nUnit.  In the Cisco CMCC environment, this is the \npath of the channel to the physical router, itself.  \nThis path is needed because the physical channel may \nbe directed (switched) through a device called \nan ESCON director.  The path defined from the \nhost to the Control Unit can be different than \nthe path from the Control Unit to the host.  \nFor an in-depth definition of how this number \nis derived, see the cipCardCsnaAdminPath object.\n3) A Sub-Channel and Device are exactly the same\nthing.  The term Sub-Channel was introduced\nfor ESCON (IBM's serial fiber optic) channel\ninterface.  Previously the term Device was used,\nand it mapped directly to hardware (in most\nsituations) via a Parallel Channel Adapter\n(PCA). Another name for PCA is Bus & Tag.  In\nthe Cisco CMCC environment, the Sub-Channel is\ncontrolled by the Channel Systems Network\nArchitecture (CSNA) feature. For an\nin-depth definition of how this number is\nderived, see the cipCardCsnaAdminDevice object.\nNOTE:  The terminology of Sub-Channel and\nSub-Channel Index are two completely different\nentities!  See below for Sub-Channel Index.\n4) An I/O Device is the entity that is addressed by\nthe combination of Sub-Channel and Device.  This\ndirectly maps to the cipCardCsnaAdminTable.\nNOTE:  The Channel Systems Network Architecture \n(CSNA) feature may have multiple  \nsub-channels/devices defined for its control.\nAlso NOTE:  That we have defined an object with\nthe name cipCardSubChannelIndex and this object\nis the two hex octet Channel Path values concatenated\nwith the second hex (the first octet is not used)\noctet Device value and then converted to an\nINTEGER (Unsigned).\nThe exact description is taken from the\nCISCO-CHANNEL-MIB\ncipCardSubChannelIndex     OBJECT-TYPE\n    SYNTAX      INTEGER\n    MAX-ACCESS  read-only\n    STATUS      current\n    DESCRIPTION\n     This indicates which subchannel is being referenced\n      for a particular daughter board on a CMCC card.\n      This value is constructed as follows:\n        path * 256 + device\n      Path and device are the values in\n      CipCardClawConfigTable.\n    ::= { cipCardSubChannelEntry 1 }\nIn this mib, the last two lines change to\n Path and device are the values in the\n  cipCardCsnaAdminTable.\n5) XCA Major Nodes.  The XCA major node binds the\nChannel Path (from the hosts perspective)/Sub-\nChannel number (i.e. I/O Device), to a CIP internal\nLAN Adapter of a specific type with a unique SAP\nNumber.  That same I/O Device can also be\nbound to the same LAN Adapter of the same\ntype with a different SAP, and/or the same I/O\nDevice can be bound to any other Adapter and\nany unique SAP on that Adapter.  The binding\nallows the I/O Device to talk to the Adapter.\nThe SAP allows multiple connections to the\nsame Adapter.\n\nThe following is an example of the hardware with\nthe above names showing there locations.\n\n      |----- Channel Path ------|\n        Eg. 150F and 190A       =================\n==========                         | Router A with |\n| HOST 1 |---     ============     | Control Unit  |\n==========   |__15| ESCON    |_____| & Virtual     |\n           ____| Director |     | I/O Devices   |\n==========   |  19============     | via the CSNA  |\n| HOST 2 |---                 -----| feature.      |\n==========                    |    =================\n                           |\n        Eg. 0100,          |\n==========  Direct Connection |\n| HOST 3 |---------------------\n==========\n\n\nThe following example configuration of a router that\nshows the entities managed by the CIPCSNA MIB.\n\n------------     ------------\n| HOST 1   |     | HOST 3   |\n| & HOST 2 |     |          |\n------------     ------------\n    ||               ||     Router A\n-----------------------------------------\n| ------------------------------------- |\n| | -----------       ---------       | |\n| | | ESCON 0 |       | PCA 1 |       | |\n| | -----------       ---------       | |\n| |                                   | |\n| | ----------------------            | |\n| | | CSNA Feature       |            | |\n| | | Control Unit F & A |            | |\n| | |   for ESCON 0      |            | |\n| | ----------------------            | |\n| |                                   | |\n| |     CMCC CARD 6                   | |\n| ------------------------------------- |\n|                                       |\n-----------------------------------------\n\nThe first table is the Cisco Mainframe Channel Connection\n(CMCC) Channel Systems Network Architecture support (CSNA) \nAdministration table.  Each entry created in this table \nwill create an I/O Device that can be attached to the \nhost (via a host VTAM XCA Major Node command).\nThe indices of the table are:\n* The CMCC Card Slot Index\n* The Daughter Board Index\n* The Sub-Channel Index\nNOTE:  In the above discussion, this value is defined\n     to be a combination of the Channel Path and\n     Device (really the address of an I/O Device).\nThe fields included in this table represent:\n* Channel Path\n* Device\nNOTE:  The two fields above are the same values as\n     the above Sub-Channel Index.\n* The configured maximum block delay time\n* The configured suggested block delay length\n* The configured maximum block length\nNOTE:  The channel uses data blocks that accumulate\n     data before it sends it to the host.\n* The row control variable\nIn the example above, three entries would be\ndefined.\nThe first entry would be:\n- CMCC Card Slot 0\n- CMCC Daughter Board 0\n- Sub-Channel Index of 0x150F00 or 1380096\n- Channel Path of 0x150F or 5391\n- Device of 00\n- rest can be defaulted\nThe second entry would be:\n- CMCC Card Slot 0\n- CMCC Daughter Board 0\n- Sub-Channel Index of 0x190A00 or 1640960\n- Channel Path of 0x190A or 6410\n- Device of 00\n- rest can be defaulted\nThe third entry would be:\n- CMCC Card Slot 0\n- CMCC Daughter Board 1\n- Sub-Channel Index of 0x010000 or 65536\n- Channel Path of 0x0100 or 256\n- Device of 00\n- rest can be defaulted\n\nThe next table is an augmented table to the first table.\nIt keeps the operational status of the first table.\nThe indices are the same as the first table.\nThe fields included in this table represent:\n* The current operational state of a this table entry\n* The current operational maximum block delay time\n* The current operational suggested block delay length\n* The current operational maximum block length\nIn the example above, three entries would be\ndefined.\nThe first entry would be:\n- CMCCC Card Slot 0\n- CMCC Daughter Board 0\n- Sub-Channel Index of 0x150F00 or 1380096\n- rest will be determined by the agent\nThe second entry would be:\n- CMCC Card Slot 0\n- CIP Daughter Board 0\n- Sub-Channel Index of 0x190A00 or 1640960\n- rest will be determined by the agent\nThe second entry would be:\n- CMCC Card Slot 0\n- CMCC Daughter Board 1\n- Sub-Channel Index of 0x010000 or 65536\n- rest will be determined by the agent\n\nThe next table is an augmented table to the first table.\nIt keeps the statistics for the Channel Systems Network\nArchitecture (CSNA) counters.\nThe indices are the same as the first table.\nThe fields included in this table represent:\n* Blocks transmitted\n* Blocks received\n* Bytes transmitted\n* Bytes received\n* Blocks transmitted by maximum block delay time\n* Blocks transmitted by the suggested block delay length\n* Blocks transmitted by maximum block length\nIn the example above, three entries would be\ndefined.\nThe first entry would be:\n- CMCC Card Slot 0\n- CMCC Daughter Board 0\n- Sub-Channel Index of 0x150F00 or 1380096\n- rest will be determined by the agent\nThe second entry would be:\n- CMCC Card Slot 0\n- CMCC Daughter Board 0\n- Sub-Channel Index of 0x190A00 or 1640960\n- rest will be determined by the agent\nThe second entry would be:\n- CMCC Card Slot 0\n- CMCC Daughter Board 1\n- Sub-Channel Index of 0x010000 or 65536\n- rest will be determined by the agent\n\nThe next table is maximum sessions Admin table.\nThe one entry in this table defines the configured\nmaximum sessions supported on the whole CMCC card.\nThe one index is:\n* The ifIndex addresses the virtual CMCC interface\nThe one field in this table represents:\n* The maximum sessions for this card\nIn the example above, the one entry would be defined.\n- ifIndex is created by the agent\n- the maximum sessions would be within the\nrange\n\nThe next table is the operational maximum sessions table.\nThis table is an augmented table to the maximum sessions\nAdmin table.  The entries in this table display the \ncurrent maximum sessions supported on the whole CMCC card. \nThe indices are the same as the maximum sessions Admin\ntable.\nThe one field in this table represents:\n* The current operational maximum sessions for\nthis card\nIn the example above, the one entry would be defined.\n- ifIndex is created by the agent\n- the maximum sessions would be within the\nrange\n\nThe next table is the statistical maximum sessions table.\nThis table is an augmented table to the maximum sessions\nAdmin table.  The entries in this table displays the \ncurrent high water maximum sessions supported on the \nwhole CMCC card and the number of allocation errors that \nhave occurred when attempting to increase the number of \nsessions. The indices are the same as the maximum sessions\nAdmin table.\nThe one field in this table represents:\n* The current operational maximum sessions for\nthis card\nIn the example above, the one entry would be defined.\n- ifIndex is created by the agent\n- the highest maximum sessions that has occurred since\nthe last re-boot.\n- the number of allocation errors when extending the\nnumber of sessions.\n\nThe last table is the SNA Connection table.  Each entry\nin this table represents a connection from an I/O Device\n(Channel Path/Device) address to a CMCC internal LAN Adapter\nfor a single SAP address. Multiple entries in this table\ncan represent the same LAN Adapter with the use\nof a different SAP.  The entries in this table are\ncreated when VTAM on a host creates an XCA Major\nNode definition.  That definition will tell the router\nwhat I/O Device address are to be bound to which\nCMCC internal LAN Adapter (of a type) and which SAP will be\nused to carry traffic.\nThe indices of the table are:\n* The ifIndex that addresses the virtual\nCMCC interface\n* The virtual interface identifying a unique\nCMCC internal MAC Adapter. This definition used is defined\nin the CISCO-SNA-LLC-MIB as llcPortVirtualIndex.\n* The SAP used by this connection.\nNOTE:  The SAP definition used is defined in\n      the CISCO-SNA-LLC-MIB.\nThe fields included in this table represent:\n* The number of currently active sessions \nover this connection\n* The slot of the CMCC card.\n* The port on the CMCC card that the Path/Device\n(subchannel is configured.\n* The Channel Path used by this connection\n* The Device used by this connection\nIn the example above, the number entries would\ndepend upon the VTAM configuration.\nEach entry would be:\n- ifIndex is created by the agent\n- one of the LAN identifiers from one of the entries\nin the CMCC internal LAN table. \n- one of the adapter identifiers from one the\nentries in the CMCC internal LAN Adapter table.\n- the SAP provided by the XCA Major Node command\n- the number of currently active sessions\n- the slot of the CMCC card.\n- the port on the CMCC card.\n- the Channel Path from one entry in the first table\n- the Device from same entry as the Channel Path\nin the first table"

# nodes
class ciscoCipCsnaMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33])
	name = 'ciscoCipCsnaMIB'

class cipCsnaObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1])
	name = 'cipCsnaObjects'

class cipCsnaChannel(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1])
	name = 'cipCsnaChannel'

class cipSession(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2])
	name = 'cipSession'

class cipCsnaConnection(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 3])
	name = 'cipCsnaConnection'

class cipCsnaNotificationPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 2])
	name = 'cipCsnaNotificationPrefix'

class cipCsnaNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 2, 0])
	name = 'cipCsnaNotifications'

class ciscoCipCsnaMibConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 3])
	name = 'ciscoCipCsnaMibConformance'

class ciscoCipCsnaMibCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 3, 1])
	name = 'ciscoCipCsnaMibCompliances'

class ciscoCipCsnaMibGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 3, 2])
	name = 'ciscoCipCsnaMibGroups'


# macros
# types 

class ChannelPath(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 2))
	format = '1x:'


class ChannelDevice(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 2))
	format = '1x:'

# scalars 
# columns
class cipCardCsnaAdminPath(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 1, 1, 1])
	syntaxobject = ChannelPath


class cipCardCsnaAdminDevice(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 1, 1, 2])
	syntaxobject = ChannelDevice


class cipCardCsnaAdminBlockDelayTime(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'milliseconds'


class cipCardCsnaAdminBlockDelayLength(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'octets'


class cipCardCsnaAdminMaxBlockLength(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'octets'


class cipCardCsnaAdminRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class cipCardCsnaOperState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(0, 'closed'), Enum(1, 'pendingOpen'), Enum(2, 'open'), Enum(3, 'pendingSetup'), Enum(4, 'setupComplete'), Enum(5, 'pendingClose')]


class cipCardCsnaOperSlowDownState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(0, 'normal'), Enum(1, 'slowDownSent'), Enum(2, 'slowDownReceived'), Enum(3, 'slowDownSentAndReceived')]


class cipCardCsnaOperBlockDelayTime(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 4
	units = 'milliseconds'


class cipCardCsnaOperBlockDelayLength(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 4
	units = 'octets'


class cipCardCsnaOperMaxBlockLength(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 4
	units = 'octets'


class cipCardCsnaStatsBlocksTxd(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipCardCsnaStatsBlocksRxd(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipCardCsnaStatsBytesTxd(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class cipCardCsnaStatsHCBytesTxd(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter64
	access = 4
	units = 'octets'


class cipCardCsnaStatsBytesRxd(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class cipCardCsnaStatsHCBytesRxd(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter64
	access = 4
	units = 'octets'


class cipCardCsnaStatsBlocksTxByBlockDelayTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipCardCsnaStatsBytesTxByBlockDelayTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipCardCsnaStatsHCBytesTxByBlockDelayTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class cipCardCsnaStatsBlocksTxByBlockDelayLength(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipCardCsnaStatsBytesTxByBlockDelayLength(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipCardCsnaStatsHCBytesTxByBlockDelayLength(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class cipCardCsnaStatsBlocksTxByMaxBlockLength(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipCardCsnaStatsBytesTxByMaxBlockLength(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipCardCsnaStatsHCBytesTxByMaxBlockLength(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class cipCardCsnaStatsSlowDownsReceived(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipCardCsnaStatsSlowDownsSent(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipCardAdminMaxLlc2Sessions(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cipCardOperMaxLlc2Sessions(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cipCardStatsHiWaterLlc2Sessions(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cipCardStatsLlc2SessionAllocationErrs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipCardCsnaConnActiveSessions(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 3, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cipCardCsnaSlot(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cipCardCsnaPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 3, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cipCardCsnaConnPath(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 3, 1, 1, 4])
	syntaxobject = ChannelPath


class cipCardCsnaConnDevice(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 3, 1, 1, 5])
	syntaxobject = ChannelDevice


# rows 
class cipCardCsnaAdminEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cipCardEntryIndex, cipCardDtrBrdIndex, cipCardSubChannelIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 1, 1])
	access = 2
	rowstatus = cipCardCsnaAdminRowStatus
	columns = {'cipCardCsnaAdminPath': cipCardCsnaAdminPath, 'cipCardCsnaAdminDevice': cipCardCsnaAdminDevice, 'cipCardCsnaAdminBlockDelayTime': cipCardCsnaAdminBlockDelayTime, 'cipCardCsnaAdminBlockDelayLength': cipCardCsnaAdminBlockDelayLength, 'cipCardCsnaAdminMaxBlockLength': cipCardCsnaAdminMaxBlockLength, 'cipCardCsnaAdminRowStatus': cipCardCsnaAdminRowStatus}


class cipCardCsnaOperEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cipCardEntryIndex, cipCardDtrBrdIndex, cipCardSubChannelIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 2, 1])
	access = 2
	columns = {'cipCardCsnaOperState': cipCardCsnaOperState, 'cipCardCsnaOperSlowDownState': cipCardCsnaOperSlowDownState, 'cipCardCsnaOperBlockDelayTime': cipCardCsnaOperBlockDelayTime, 'cipCardCsnaOperBlockDelayLength': cipCardCsnaOperBlockDelayLength, 'cipCardCsnaOperMaxBlockLength': cipCardCsnaOperMaxBlockLength}


class cipCardCsnaStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cipCardEntryIndex, cipCardDtrBrdIndex, cipCardSubChannelIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 1, 3, 1])
	access = 2
	columns = {'cipCardCsnaStatsBlocksTxd': cipCardCsnaStatsBlocksTxd, 'cipCardCsnaStatsBlocksRxd': cipCardCsnaStatsBlocksRxd, 'cipCardCsnaStatsBytesTxd': cipCardCsnaStatsBytesTxd, 'cipCardCsnaStatsHCBytesTxd': cipCardCsnaStatsHCBytesTxd, 'cipCardCsnaStatsBytesRxd': cipCardCsnaStatsBytesRxd, 'cipCardCsnaStatsHCBytesRxd': cipCardCsnaStatsHCBytesRxd, 'cipCardCsnaStatsBlocksTxByBlockDelayTime': cipCardCsnaStatsBlocksTxByBlockDelayTime, 'cipCardCsnaStatsBytesTxByBlockDelayTime': cipCardCsnaStatsBytesTxByBlockDelayTime, 'cipCardCsnaStatsHCBytesTxByBlockDelayTime': cipCardCsnaStatsHCBytesTxByBlockDelayTime, 'cipCardCsnaStatsBlocksTxByBlockDelayLength': cipCardCsnaStatsBlocksTxByBlockDelayLength, 'cipCardCsnaStatsBytesTxByBlockDelayLength': cipCardCsnaStatsBytesTxByBlockDelayLength, 'cipCardCsnaStatsHCBytesTxByBlockDelayLength': cipCardCsnaStatsHCBytesTxByBlockDelayLength, 'cipCardCsnaStatsBlocksTxByMaxBlockLength': cipCardCsnaStatsBlocksTxByMaxBlockLength, 'cipCardCsnaStatsBytesTxByMaxBlockLength': cipCardCsnaStatsBytesTxByMaxBlockLength, 'cipCardCsnaStatsHCBytesTxByMaxBlockLength': cipCardCsnaStatsHCBytesTxByMaxBlockLength, 'cipCardCsnaStatsSlowDownsReceived': cipCardCsnaStatsSlowDownsReceived, 'cipCardCsnaStatsSlowDownsSent': cipCardCsnaStatsSlowDownsSent}


class cipCardSessionsAdminEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cipCardEntryIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 1, 1])
	access = 2
	columns = {'cipCardAdminMaxLlc2Sessions': cipCardAdminMaxLlc2Sessions}


class cipCardSessionsOperEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cipCardEntryIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 2, 1])
	access = 2
	columns = {'cipCardOperMaxLlc2Sessions': cipCardOperMaxLlc2Sessions}


class cipCardSessionsStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cipCardEntryIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 2, 3, 1])
	access = 2
	columns = {'cipCardStatsHiWaterLlc2Sessions': cipCardStatsHiWaterLlc2Sessions, 'cipCardStatsLlc2SessionAllocationErrs': cipCardStatsLlc2SessionAllocationErrs}


class cipCardCsnaConnEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, llcPortVirtualIndex, llcSapNumber], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 1, 3, 1, 1])
	access = 2
	columns = {'cipCardCsnaConnActiveSessions': cipCardCsnaConnActiveSessions, 'cipCardCsnaSlot': cipCardCsnaSlot, 'cipCardCsnaPort': cipCardCsnaPort, 'cipCardCsnaConnPath': cipCardCsnaConnPath, 'cipCardCsnaConnDevice': cipCardCsnaConnDevice}


# notifications (traps) 
class cipCsnaOpenDuplicateSapFailure(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 2, 0, 1])

class cipCsnaLlc2ConnectionLimitExceeded(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 2, 0, 2])

# groups 
class ciscoCsnaGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 3, 2, 1])
	group = [cipCardCsnaAdminPath, cipCardCsnaAdminDevice, cipCardCsnaAdminBlockDelayTime, cipCardCsnaAdminBlockDelayLength, cipCardCsnaAdminMaxBlockLength, cipCardCsnaAdminRowStatus, cipCardCsnaOperState, cipCardCsnaOperSlowDownState, cipCardCsnaOperBlockDelayTime, cipCardCsnaOperBlockDelayLength, cipCardCsnaOperMaxBlockLength, cipCardCsnaStatsBlocksTxd, cipCardCsnaStatsBlocksRxd, cipCardCsnaStatsBytesTxd, cipCardCsnaStatsHCBytesTxd, cipCardCsnaStatsBytesRxd, cipCardCsnaStatsHCBytesRxd, cipCardCsnaStatsBlocksTxByBlockDelayTime, cipCardCsnaStatsBytesTxByBlockDelayTime, cipCardCsnaStatsHCBytesTxByBlockDelayTime, cipCardCsnaStatsBlocksTxByBlockDelayLength, cipCardCsnaStatsBytesTxByBlockDelayLength, cipCardCsnaStatsHCBytesTxByBlockDelayLength, cipCardCsnaStatsBlocksTxByMaxBlockLength, cipCardCsnaStatsBytesTxByMaxBlockLength, cipCardCsnaStatsHCBytesTxByMaxBlockLength, cipCardCsnaStatsSlowDownsSent, cipCardCsnaStatsSlowDownsReceived]

class ciscoMaxSessionsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 3, 2, 2])
	group = [cipCardAdminMaxLlc2Sessions, cipCardOperMaxLlc2Sessions, cipCardStatsHiWaterLlc2Sessions, cipCardStatsLlc2SessionAllocationErrs]

class ciscoCsnaConnGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 33, 3, 2, 3])
	group = [cipCardCsnaConnActiveSessions, cipCardCsnaSlot, cipCardCsnaPort, cipCardCsnaConnPath, cipCardCsnaConnDevice]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)