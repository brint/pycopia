# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_IDENTITY, mib_2
from EtherLike_MIB import dot3

class ETHER_CHIPSET_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/ETHER-CHIPSET-MIB'
	name = 'ETHER-CHIPSET-MIB'
	language = 2
	description = 'This MIB module contains registered values for\nuse by the dot3StatsEtherChipSet object in\nthe EtherLike-MIB.  This object is used to\nidentify the MAC hardware used to communicate\non an interface.\n\nNote that the dot3StatsEtherChipSet object\nhas been deprecated.  The primary purpose of\nthis module is to capture historic assignments\nmade by the various IETF working groups that\nhave been responsible for maintaining the\nEtherLike-MIB.  Implementations which support\nthe dot3StatsEtherChipSet object for backwards\ncompatability may continue to use these values.\nFor those chipsets not represented in this\nmodule, registration is required in other\ndocumentation, e.g., assignment within that\npart of the registration tree delegated to\nindividual enterprises (see RFC 1155 and RFC\n1902).'

# nodes
class dot3ChipSets(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8])
	name = 'dot3ChipSets'

class dot3ChipSetAMD(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 1])
	name = 'dot3ChipSetAMD'

class dot3ChipSetAMD7990(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 1])
	name = 'dot3ChipSetAMD7990'

class dot3ChipSetAMD79900(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 2])
	name = 'dot3ChipSetAMD79900'

class dot3ChipSetAMD79C940(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 3])
	name = 'dot3ChipSetAMD79C940'

class dot3ChipSetAMD79C90(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 4])
	name = 'dot3ChipSetAMD79C90'

class dot3ChipSetAMD79C960(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 5])
	name = 'dot3ChipSetAMD79C960'

class dot3ChipSetAMD79C961(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 6])
	name = 'dot3ChipSetAMD79C961'

class dot3ChipSetAMD79C961A(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 7])
	name = 'dot3ChipSetAMD79C961A'

class dot3ChipSetAMD79C965(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 8])
	name = 'dot3ChipSetAMD79C965'

class dot3ChipSetAMD79C970(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 9])
	name = 'dot3ChipSetAMD79C970'

class dot3ChipSetAMD79C970A(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 10])
	name = 'dot3ChipSetAMD79C970A'

class dot3ChipSetAMD79C971(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 11])
	name = 'dot3ChipSetAMD79C971'

class dot3ChipSetAMD79C972(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 12])
	name = 'dot3ChipSetAMD79C972'

class dot3ChipSetIntel(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 2])
	name = 'dot3ChipSetIntel'

class dot3ChipSetIntel82586(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 1])
	name = 'dot3ChipSetIntel82586'

class dot3ChipSetIntel82596(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 2])
	name = 'dot3ChipSetIntel82596'

class dot3ChipSetIntel82595(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 3])
	name = 'dot3ChipSetIntel82595'

class dot3ChipSetIntel82557(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 4])
	name = 'dot3ChipSetIntel82557'

class dot3ChipSetIntel82558(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 5])
	name = 'dot3ChipSetIntel82558'

class dot3ChipSetSeeq(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 3])
	name = 'dot3ChipSetSeeq'

class dot3ChipSetSeeq8003(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 1])
	name = 'dot3ChipSetSeeq8003'

class dot3ChipSetSeeq80C03(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 2])
	name = 'dot3ChipSetSeeq80C03'

class dot3ChipSetSeeq84C30(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 3])
	name = 'dot3ChipSetSeeq84C30'

class dot3ChipSetSeeq8431(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 4])
	name = 'dot3ChipSetSeeq8431'

class dot3ChipSetSeeq80C300(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 5])
	name = 'dot3ChipSetSeeq80C300'

class dot3ChipSetSeeq84C300(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 6])
	name = 'dot3ChipSetSeeq84C300'

class dot3ChipSetSeeq84301(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 7])
	name = 'dot3ChipSetSeeq84301'

class dot3ChipSetSeeq84302(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 8])
	name = 'dot3ChipSetSeeq84302'

class dot3ChipSetSeeq8100(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 9])
	name = 'dot3ChipSetSeeq8100'

class dot3ChipSetNational(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 4])
	name = 'dot3ChipSetNational'

class dot3ChipSetNational8390(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 1])
	name = 'dot3ChipSetNational8390'

class dot3ChipSetNationalSonic(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 2])
	name = 'dot3ChipSetNationalSonic'

class dot3ChipSetNational83901(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 3])
	name = 'dot3ChipSetNational83901'

class dot3ChipSetNational83902(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 4])
	name = 'dot3ChipSetNational83902'

class dot3ChipSetNational83905(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 5])
	name = 'dot3ChipSetNational83905'

class dot3ChipSetNational83907(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 6])
	name = 'dot3ChipSetNational83907'

class dot3ChipSetNational83916(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 7])
	name = 'dot3ChipSetNational83916'

class dot3ChipSetNational83934(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 8])
	name = 'dot3ChipSetNational83934'

class dot3ChipSetNational83936(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 9])
	name = 'dot3ChipSetNational83936'

class dot3ChipSetFujitsu(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 5])
	name = 'dot3ChipSetFujitsu'

class dot3ChipSetFujitsu86950(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 1])
	name = 'dot3ChipSetFujitsu86950'

class dot3ChipSetFujitsu86960(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 2])
	name = 'dot3ChipSetFujitsu86960'

class dot3ChipSetFujitsu86964(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 3])
	name = 'dot3ChipSetFujitsu86964'

class dot3ChipSetFujitsu86965A(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 4])
	name = 'dot3ChipSetFujitsu86965A'

class dot3ChipSetFujitsu86965B(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 5])
	name = 'dot3ChipSetFujitsu86965B'

class dot3ChipSetDigital(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 6])
	name = 'dot3ChipSetDigital'

class dot3ChipSetDigitalDC21040(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 1])
	name = 'dot3ChipSetDigitalDC21040'

class dot3ChipSetDigital21041(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 2])
	name = 'dot3ChipSetDigital21041'

class dot3ChipSetDigital21140(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 3])
	name = 'dot3ChipSetDigital21140'

class dot3ChipSetDigital21143(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 4])
	name = 'dot3ChipSetDigital21143'

class dot3ChipSetDigital21340(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 5])
	name = 'dot3ChipSetDigital21340'

class dot3ChipSetDigital21440(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 6])
	name = 'dot3ChipSetDigital21440'

class dot3ChipSetDigital21540(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 6, 7])
	name = 'dot3ChipSetDigital21540'

class dot3ChipSetTI(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 7])
	name = 'dot3ChipSetTI'

class dot3ChipSetTIE100(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 7, 1])
	name = 'dot3ChipSetTIE100'

class dot3ChipSetTIE110(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 7, 2])
	name = 'dot3ChipSetTIE110'

class dot3ChipSetTIX3100(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 7, 3])
	name = 'dot3ChipSetTIX3100'

class dot3ChipSetTIX3150(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 7, 4])
	name = 'dot3ChipSetTIX3150'

class dot3ChipSetTIX3270(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 7, 5])
	name = 'dot3ChipSetTIX3270'

class dot3ChipSetToshiba(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 8])
	name = 'dot3ChipSetToshiba'

class dot3ChipSetToshibaTC35815F(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 8, 1])
	name = 'dot3ChipSetToshibaTC35815F'

class dot3ChipSetLucent(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 9])
	name = 'dot3ChipSetLucent'

class dot3ChipSetLucentATT1MX10(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 9, 1])
	name = 'dot3ChipSetLucentATT1MX10'

class dot3ChipSetLucentLUC3M08(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 9, 2])
	name = 'dot3ChipSetLucentLUC3M08'

class dot3ChipSetGalileo(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 10])
	name = 'dot3ChipSetGalileo'

class dot3ChipSetGalileoGT48001(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 1])
	name = 'dot3ChipSetGalileoGT48001'

class dot3ChipSetGalileoGT48002(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 2])
	name = 'dot3ChipSetGalileoGT48002'

class dot3ChipSetGalileoGT48004(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 3])
	name = 'dot3ChipSetGalileoGT48004'

class dot3ChipSetGalileoGT48207(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 4])
	name = 'dot3ChipSetGalileoGT48207'

class dot3ChipSetGalileoGT48208(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 5])
	name = 'dot3ChipSetGalileoGT48208'

class dot3ChipSetGalileoGT48212(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 10, 6])
	name = 'dot3ChipSetGalileoGT48212'

class dot3ChipSetJato(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 11])
	name = 'dot3ChipSetJato'

class dot3ChipSetJatoJT1001(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 11, 1])
	name = 'dot3ChipSetJatoJT1001'

class dot3ChipSetXaQti(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 12])
	name = 'dot3ChipSetXaQti'

class dot3ChipSetXaQtiXQ11800FP(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 12, 1])
	name = 'dot3ChipSetXaQtiXQ11800FP'

class dot3ChipSetXaQtiXQ18110FP(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 7, 8, 12, 2])
	name = 'dot3ChipSetXaQtiXQ18110FP'

class etherChipsetMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 70])
	name = 'etherChipsetMIB'


# macros
# types 
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