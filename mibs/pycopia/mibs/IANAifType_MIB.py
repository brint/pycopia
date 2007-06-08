# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, mib_2
from SNMPv2_TC import TEXTUAL_CONVENTION

class IANAifType_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/iana/IANAifType-MIB'
	conformance = 4
	name = 'IANAifType-MIB'
	language = 2
	description = "This MIB module defines the IANAifType Textual\nConvention, and thus the enumerated values of\nthe ifType object defined in MIB-II's ifTable."

# nodes
class ianaifType(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 30])
	name = 'ianaifType'


# macros
# types 

class IANAifType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'other'), Enum(2, 'regular1822'), Enum(3, 'hdh1822'), Enum(4, 'ddnX25'), Enum(5, 'rfc877x25'), Enum(6, 'ethernetCsmacd'), Enum(7, 'iso88023Csmacd'), Enum(8, 'iso88024TokenBus'), Enum(9, 'iso88025TokenRing'), Enum(10, 'iso88026Man'), Enum(11, 'starLan'), Enum(12, 'proteon10Mbit'), Enum(13, 'proteon80Mbit'), Enum(14, 'hyperchannel'), Enum(15, 'fddi'), Enum(16, 'lapb'), Enum(17, 'sdlc'), Enum(18, 'ds1'), Enum(19, 'e1'), Enum(20, 'basicISDN'), Enum(21, 'primaryISDN'), Enum(22, 'propPointToPointSerial'), Enum(23, 'ppp'), Enum(24, 'softwareLoopback'), Enum(25, 'eon'), Enum(26, 'ethernet3Mbit'), Enum(27, 'nsip'), Enum(28, 'slip'), Enum(29, 'ultra'), Enum(30, 'ds3'), Enum(31, 'sip'), Enum(32, 'frameRelay'), Enum(33, 'rs232'), Enum(34, 'para'), Enum(35, 'arcnet'), Enum(36, 'arcnetPlus'), Enum(37, 'atm'), Enum(38, 'miox25'), Enum(39, 'sonet'), Enum(40, 'x25ple'), Enum(41, 'iso88022llc'), Enum(42, 'localTalk'), Enum(43, 'smdsDxi'), Enum(44, 'frameRelayService'), Enum(45, 'v35'), Enum(46, 'hssi'), Enum(47, 'hippi'), Enum(48, 'modem'), Enum(49, 'aal5'), Enum(50, 'sonetPath'), Enum(51, 'sonetVT'), Enum(52, 'smdsIcip'), Enum(53, 'propVirtual'), Enum(54, 'propMultiplexor'), Enum(55, 'ieee80212'), Enum(56, 'fibreChannel'), Enum(57, 'hippiInterface'), Enum(58, 'frameRelayInterconnect'), Enum(59, 'aflane8023'), Enum(60, 'aflane8025'), Enum(61, 'cctEmul'), Enum(62, 'fastEther'), Enum(63, 'isdn'), Enum(64, 'v11'), Enum(65, 'v36'), Enum(66, 'g703at64k'), Enum(67, 'g703at2mb'), Enum(68, 'qllc'), Enum(69, 'fastEtherFX'), Enum(70, 'channel'), Enum(71, 'ieee80211'), Enum(72, 'ibm370parChan'), Enum(73, 'escon'), Enum(74, 'dlsw'), Enum(75, 'isdns'), Enum(76, 'isdnu'), Enum(77, 'lapd'), Enum(78, 'ipSwitch'), Enum(79, 'rsrb'), Enum(80, 'atmLogical'), Enum(81, 'ds0'), Enum(82, 'ds0Bundle'), Enum(83, 'bsc'), Enum(84, 'async'), Enum(85, 'cnr'), Enum(86, 'iso88025Dtr'), Enum(87, 'eplrs'), Enum(88, 'arap'), Enum(89, 'propCnls'), Enum(90, 'hostPad'), Enum(91, 'termPad'), Enum(92, 'frameRelayMPI'), Enum(93, 'x213'), Enum(94, 'adsl'), Enum(95, 'radsl'), Enum(96, 'sdsl'), Enum(97, 'vdsl'), Enum(98, 'iso88025CRFPInt'), Enum(99, 'myrinet'), Enum(100, 'voiceEM'), Enum(101, 'voiceFXO'), Enum(102, 'voiceFXS'), Enum(103, 'voiceEncap'), Enum(104, 'voiceOverIp'), Enum(105, 'atmDxi'), Enum(106, 'atmFuni'), Enum(107, 'atmIma'), Enum(108, 'pppMultilinkBundle'), Enum(109, 'ipOverCdlc'), Enum(110, 'ipOverClaw'), Enum(111, 'stackToStack'), Enum(112, 'virtualIpAddress'), Enum(113, 'mpc'), Enum(114, 'ipOverAtm'), Enum(115, 'iso88025Fiber'), Enum(116, 'tdlc'), Enum(117, 'gigabitEthernet'), Enum(118, 'hdlc'), Enum(119, 'lapf'), Enum(120, 'v37'), Enum(121, 'x25mlp'), Enum(122, 'x25huntGroup'), Enum(123, 'trasnpHdlc'), Enum(124, 'interleave'), Enum(125, 'fast'), Enum(126, 'ip'), Enum(127, 'docsCableMaclayer'), Enum(128, 'docsCableDownstream'), Enum(129, 'docsCableUpstream'), Enum(130, 'a12MppSwitch'), Enum(131, 'tunnel'), Enum(132, 'coffee'), Enum(133, 'ces'), Enum(134, 'atmSubInterface'), Enum(135, 'l2vlan'), Enum(136, 'l3ipvlan'), Enum(137, 'l3ipxvlan'), Enum(138, 'digitalPowerline'), Enum(139, 'mediaMailOverIp'), Enum(140, 'dtm'), Enum(141, 'dcn'), Enum(142, 'ipForward'), Enum(143, 'msdsl'), Enum(144, 'ieee1394'), Enum(145, 'if-gsn'), Enum(146, 'dvbRccMacLayer'), Enum(147, 'dvbRccDownstream'), Enum(148, 'dvbRccUpstream'), Enum(149, 'atmVirtual'), Enum(150, 'mplsTunnel'), Enum(151, 'srp'), Enum(152, 'voiceOverAtm'), Enum(153, 'voiceOverFrameRelay'), Enum(154, 'idsl'), Enum(155, 'compositeLink'), Enum(156, 'ss7SigLink'), Enum(157, 'propWirelessP2P'), Enum(158, 'frForward'), Enum(159, 'rfc1483'), Enum(160, 'usb'), Enum(161, 'ieee8023adLag'), Enum(162, 'bgppolicyaccounting'), Enum(163, 'frf16MfrBundle'), Enum(164, 'h323Gatekeeper'), Enum(165, 'h323Proxy'), Enum(166, 'mpls'), Enum(167, 'mfSigLink'), Enum(168, 'hdsl2'), Enum(169, 'shdsl'), Enum(170, 'ds1FDL'), Enum(171, 'pos'), Enum(172, 'dvbAsiIn'), Enum(173, 'dvbAsiOut'), Enum(174, 'plc'), Enum(175, 'nfas'), Enum(176, 'tr008'), Enum(177, 'gr303RDT'), Enum(178, 'gr303IDT'), Enum(179, 'isup'), Enum(180, 'propDocsWirelessMaclayer'), Enum(181, 'propDocsWirelessDownstream'), Enum(182, 'propDocsWirelessUpstream'), Enum(183, 'hiperlan2'), Enum(184, 'propBWAp2Mp'), Enum(185, 'sonetOverheadChannel'), Enum(186, 'digitalWrapperOverheadChannel'), Enum(187, 'aal2'), Enum(188, 'radioMAC'), Enum(189, 'atmRadio'), Enum(190, 'imt'), Enum(191, 'mvl'), Enum(192, 'reachDSL'), Enum(193, 'frDlciEndPt'), Enum(194, 'atmVciEndPt'), Enum(195, 'opticalChannel'), Enum(196, 'opticalTransport'), Enum(197, 'propAtm'), Enum(198, 'voiceOverCable'), Enum(199, 'infiniband'), Enum(200, 'teLink'), Enum(201, 'q2931'), Enum(202, 'virtualTg'), Enum(203, 'sipTg'), Enum(204, 'sipSig'), Enum(205, 'docsCableUpstreamChannel'), Enum(206, 'econet'), Enum(207, 'pon155'), Enum(208, 'pon622'), Enum(209, 'bridge'), Enum(210, 'linegroup'), Enum(211, 'voiceEMFGD'), Enum(212, 'voiceFGDEANA'), Enum(213, 'voiceDID'), Enum(214, 'mpegTransport'), Enum(215, 'sixToFour'), Enum(216, 'gtp'), Enum(217, 'pdnEtherLoop1'), Enum(218, 'pdnEtherLoop2'), Enum(219, 'opticalChannelGroup'), Enum(220, 'homepna'), Enum(221, 'gfp'), Enum(222, 'ciscoISLvlan'), Enum(223, 'actelisMetaLOOP'), Enum(224, 'fcipLink'), Enum(225, 'rpr'), Enum(226, 'qam'), Enum(227, 'lmp'), Enum(228, 'cblVectaStar'), Enum(229, 'docsCableMCmtsDownstream'), Enum(230, 'adsl2'), Enum(231, 'macSecControlledIF'), Enum(232, 'macSecUncontrolledIF'), Enum(233, 'aviciOpticalEther'), Enum(234, 'atmbond'), Enum(235, 'voiceFGDOS'), Enum(236, 'mocaVersion1'), Enum(237, 'ieee80216WMAN'), Enum(238, 'adsl2plus'), Enum(239, 'dvbRcsMacLayer'), Enum(240, 'dvbTdm'), Enum(241, 'dvbRcsTdma')]


class IANAtunnelType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'other'), Enum(2, 'direct'), Enum(3, 'gre'), Enum(4, 'minimal'), Enum(5, 'l2tp'), Enum(6, 'pptp'), Enum(7, 'l2f'), Enum(8, 'udp'), Enum(9, 'atmp'), Enum(10, 'msdp'), Enum(11, 'sixToFour'), Enum(12, 'sixOverFour'), Enum(13, 'isatap'), Enum(14, 'teredo')]

# scalars 
# columns
# rows 
# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)