# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY
from MPLS_TC_STD_MIB import mplsStdMIB
from SNMPv2_TC import TEXTUAL_CONVENTION

class GMPLS_TC_STD_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/GMPLS-TC-STD-MIB'
	conformance = 4
	name = 'GMPLS-TC-STD-MIB'
	language = 2
	description = 'Copyright (C) The IETF Trust (2007).  This version of\nthis MIB module is part of RFC 4801; see the RFC itself for\nfull legal notices.\n\nThis MIB module defines TEXTUAL-CONVENTIONs for concepts used in\nGeneralized Multiprotocol Label Switching (GMPLS) networks.'

# nodes
class gmplsTCStdMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 12])
	name = 'gmplsTCStdMIB'


# macros
# types 

class GmplsFreeformLabelTC(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 64))


class GmplsLabelTypeTC(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'gmplsMplsLabel'), Enum(2, 'gmplsPortWavelengthLabel'), Enum(3, 'gmplsFreeformGeneralizedLabel'), Enum(4, 'gmplsSonetLabel'), Enum(5, 'gmplsSdhLabel'), Enum(6, 'gmplsWavebandLabel')]


class GmplsSegmentDirectionTC(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'forward'), Enum(2, 'reverse')]

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