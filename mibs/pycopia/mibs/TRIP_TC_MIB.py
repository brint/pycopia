# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, Unsigned32, Integer32, mib_2
from SNMPv2_TC import TEXTUAL_CONVENTION

class TRIP_TC_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/TRIP-TC-MIB'
	conformance = 5
	name = 'TRIP-TC-MIB'
	language = 2
	description = 'Initial version of TRIP (Telephony Routing Over IP)\nMIB Textual Conventions module used by other\n\n\n\nTRIP-related MIB Modules.\n\nCopyright (C) The Internet Society (2004). This version of\nthis MIB module is part of RFC 3872, see the RFC itself\nfor full legal notices.'

# nodes
class tripTC(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 115])
	name = 'tripTC'


# macros
# types 

class TripItad(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(0, -1))


class TripId(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(0, -1))


class TripAddressFamily(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'decimal'), Enum(2, 'pentadecimal'), Enum(3, 'e164'), Enum(255, 'other')]


class TripAppProtocol(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'sip'), Enum(2, 'q931'), Enum(3, 'ras'), Enum(4, 'annexG'), Enum(255, 'other')]


class TripCommunityId(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(0, -1))


class TripProtocolVersion(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(1, 255))


class TripSendReceiveMode(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'sendReceive'), Enum(2, 'sendOnly'), Enum(3, 'receiveOnly')]

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