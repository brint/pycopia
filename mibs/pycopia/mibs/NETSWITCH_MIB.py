# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from RFC_1212 import OBJECT_TYPE
from HP_ICF_OID import hpSwitch
from RFC1213_MIB import DisplayString
from RFC1155_SMI import Counter

class NETSWITCH_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/NETSWITCH-MIB'
	conformance = 5
	name = 'NETSWITCH-MIB'
	language = 1

# nodes
class hpOpSystem(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1])
	name = 'hpOpSystem'

class hpBuf(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1])
	name = 'hpBuf'

class hpMsgBuf(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1])
	name = 'hpMsgBuf'

class hpPktBuf(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2])
	name = 'hpPktBuf'

class hpMem(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2])
	name = 'hpMem'

class hpLocalMem(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1])
	name = 'hpLocalMem'

class hpGlobalMem(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2])
	name = 'hpGlobalMem'


# macros
# types 
MacAddress = pycopia.SMI.Basetypes.MacAddress
# scalars 
class hpSwitchOsVersion(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class hpSwitchRomVersion(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class hpSwitchSmartCardType(ScalarObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'none'), Enum(2, 'fddi'), Enum(3, 'atm'), Enum(4, 'fddiAndATM'), Enum(5, 'other')]


class hpSwitchBaseMACAddress(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


# columns
class hpMsgBufSlotIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpMsgBufCorrupted(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpMsgBufFree(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpMsgBufInit(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpMsgBufMin(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpMsgBufMiss(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpMsgBufSize(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpPktBufSlotIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpPktBufCorrupted(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpPktBufFree(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpPktBufInit(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpPktBufMin(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpPktBufMiss(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpPktBufSize(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpLocalMemSlotIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpLocalMemSlabCnt(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpLocalMemFreeSegCnt(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpLocalMemAllocSegCnt(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpLocalMemTotalBytes(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpLocalMemFreeBytes(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpLocalMemAllocBytes(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpGlobalMemSlotIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpGlobalMemSlabCnt(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpGlobalMemFreeSegCnt(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpGlobalMemAllocSegCnt(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpGlobalMemTotalBytes(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpGlobalMemFreeBytes(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpGlobalMemAllocBytes(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# rows 
class hpMsgBufEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpMsgBufSlotIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 1, 1, 1])
	access = 2
	columns = {'hpMsgBufSlotIndex': hpMsgBufSlotIndex, 'hpMsgBufCorrupted': hpMsgBufCorrupted, 'hpMsgBufFree': hpMsgBufFree, 'hpMsgBufInit': hpMsgBufInit, 'hpMsgBufMin': hpMsgBufMin, 'hpMsgBufMiss': hpMsgBufMiss, 'hpMsgBufSize': hpMsgBufSize}


class hpPktBufEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpPktBufSlotIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 1, 2, 1, 1])
	access = 2
	columns = {'hpPktBufSlotIndex': hpPktBufSlotIndex, 'hpPktBufCorrupted': hpPktBufCorrupted, 'hpPktBufFree': hpPktBufFree, 'hpPktBufInit': hpPktBufInit, 'hpPktBufMin': hpPktBufMin, 'hpPktBufMiss': hpPktBufMiss, 'hpPktBufSize': hpPktBufSize}


class hpLocalMemEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpLocalMemSlotIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 1, 1, 1])
	access = 2
	columns = {'hpLocalMemSlotIndex': hpLocalMemSlotIndex, 'hpLocalMemSlabCnt': hpLocalMemSlabCnt, 'hpLocalMemFreeSegCnt': hpLocalMemFreeSegCnt, 'hpLocalMemAllocSegCnt': hpLocalMemAllocSegCnt, 'hpLocalMemTotalBytes': hpLocalMemTotalBytes, 'hpLocalMemFreeBytes': hpLocalMemFreeBytes, 'hpLocalMemAllocBytes': hpLocalMemAllocBytes}


class hpGlobalMemEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpGlobalMemSlotIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1, 2, 2, 1, 1])
	access = 2
	columns = {'hpGlobalMemSlotIndex': hpGlobalMemSlotIndex, 'hpGlobalMemSlabCnt': hpGlobalMemSlabCnt, 'hpGlobalMemFreeSegCnt': hpGlobalMemFreeSegCnt, 'hpGlobalMemAllocSegCnt': hpGlobalMemAllocSegCnt, 'hpGlobalMemTotalBytes': hpGlobalMemTotalBytes, 'hpGlobalMemFreeBytes': hpGlobalMemFreeBytes, 'hpGlobalMemAllocBytes': hpGlobalMemAllocBytes}


# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)