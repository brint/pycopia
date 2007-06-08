# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from RFC_1212 import OBJECT_TYPE
from HP_SN_ROOT_MIB import snPOS
from RFC1155_SMI import Counter, Gauge

class HP_SN_POS_GROUP_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/HP-SN-POS-GROUP-MIB'
	conformance = 2
	name = 'HP-SN-POS-GROUP-MIB'
	language = 1

# nodes
class snPOSInfo(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1])
	name = 'snPOSInfo'


# macros
# types 

class POSStatus(pycopia.SMI.Basetypes.Enumeration):
	enumerations = [Enum(0, 'disabled'), Enum(1, 'enabled')]

DisplayString = pycopia.SMI.Basetypes.DisplayString
# scalars 
# columns
class snPOSInfoPortNum(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snPOSIfIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snPOSDescr(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class snPOSName(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class snPOSInfoSpeed(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 's155000'), Enum(2, 's622000'), Enum(3, 'other')]


class snPOSInfoAdminStatus(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'up'), Enum(2, 'down'), Enum(3, 'testing')]


class snPOSInfoLinkStatus(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'up'), Enum(2, 'down'), Enum(3, 'testing')]


class snPOSInfoClock(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'internal'), Enum(2, 'line')]


class snPOSInfoLoopBack(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'line'), Enum(2, 'internal'), Enum(3, 'none')]


class snPOSInfoScambleATM(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 10])
	syntaxobject = POSStatus


class snPOSInfoFraming(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'sonet'), Enum(2, 'sdh')]


class snPOSInfoCRC(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'crc32bits'), Enum(2, 'crc16bits')]


class snPOSInfoKeepAlive(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snPOSInfoFlagC2(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snPOSInfoFlagJ0(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snPOSInfoFlagH1(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snPOSStatsInFrames(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snPOSStatsOutFrames(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snPOSStatsAlignErrors(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snPOSStatsFCSErrors(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snPOSStatsFrameTooLongs(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 21])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snPOSStatsFrameTooShorts(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 22])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snPOSStatsInDiscard(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 23])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snPOSStatsOutDiscard(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 24])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snPOSInOctets(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 25])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class snPOSOutOctets(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 26])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class snPOSStatsInBitsPerSec(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 27])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class snPOSStatsOutBitsPerSec(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 28])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class snPOSStatsInPktsPerSec(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 29])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class snPOSStatsOutPktsPerSec(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 30])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class snPOSStatsInUtilization(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 31])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snPOSStatsOutUtilization(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 32])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# rows 
class snPOSInfoEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([snPOSInfoPortNum], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1])
	access = 2
	columns = {'snPOSInfoPortNum': snPOSInfoPortNum, 'snPOSIfIndex': snPOSIfIndex, 'snPOSDescr': snPOSDescr, 'snPOSName': snPOSName, 'snPOSInfoSpeed': snPOSInfoSpeed, 'snPOSInfoAdminStatus': snPOSInfoAdminStatus, 'snPOSInfoLinkStatus': snPOSInfoLinkStatus, 'snPOSInfoClock': snPOSInfoClock, 'snPOSInfoLoopBack': snPOSInfoLoopBack, 'snPOSInfoScambleATM': snPOSInfoScambleATM, 'snPOSInfoFraming': snPOSInfoFraming, 'snPOSInfoCRC': snPOSInfoCRC, 'snPOSInfoKeepAlive': snPOSInfoKeepAlive, 'snPOSInfoFlagC2': snPOSInfoFlagC2, 'snPOSInfoFlagJ0': snPOSInfoFlagJ0, 'snPOSInfoFlagH1': snPOSInfoFlagH1, 'snPOSStatsInFrames': snPOSStatsInFrames, 'snPOSStatsOutFrames': snPOSStatsOutFrames, 'snPOSStatsAlignErrors': snPOSStatsAlignErrors, 'snPOSStatsFCSErrors': snPOSStatsFCSErrors, 'snPOSStatsFrameTooLongs': snPOSStatsFrameTooLongs, 'snPOSStatsFrameTooShorts': snPOSStatsFrameTooShorts, 'snPOSStatsInDiscard': snPOSStatsInDiscard, 'snPOSStatsOutDiscard': snPOSStatsOutDiscard, 'snPOSInOctets': snPOSInOctets, 'snPOSOutOctets': snPOSOutOctets, 'snPOSStatsInBitsPerSec': snPOSStatsInBitsPerSec, 'snPOSStatsOutBitsPerSec': snPOSStatsOutBitsPerSec, 'snPOSStatsInPktsPerSec': snPOSStatsInPktsPerSec, 'snPOSStatsOutPktsPerSec': snPOSStatsOutPktsPerSec, 'snPOSStatsInUtilization': snPOSStatsInUtilization, 'snPOSStatsOutUtilization': snPOSStatsOutUtilization}


# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)