# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32, Gauge32
from CISCO_TC import Unsigned32
from CISCO_SMI import ciscoMgmt
from SNMPv2_TC import RowStatus, DisplayString, TimeStamp
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP

class CISCO_BULK_FILE_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-BULK-FILE-MIB'
	conformance = 3
	name = 'CISCO-BULK-FILE-MIB'
	language = 2
	description = 'The MIB module for creating and deleting bulk files of\nSNMP data for file transfer.'

# nodes
class ciscoBulkFileMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81])
	name = 'ciscoBulkFileMIB'

class ciscoBulkFileMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1])
	name = 'ciscoBulkFileMIBObjects'

class cbfDefine(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1])
	name = 'cbfDefine'

class cbfStatus(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2])
	name = 'cbfStatus'

class ciscoBulkFileMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 3])
	name = 'ciscoBulkFileMIBConformance'

class ciscoBulkFileMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 1])
	name = 'ciscoBulkFileMIBCompliances'

class ciscoBulkFileMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 2])
	name = 'ciscoBulkFileMIBGroups'


# macros
# types 
# scalars 
class cbfDefineMaxFiles(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class cbfDefineFiles(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cbfDefineHighFiles(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cbfDefineFilesRefused(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cbfDefineMaxObjects(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class cbfDefineObjects(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cbfDefineHighObjects(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cbfDefineObjectsRefused(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cbfStatusMaxFiles(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class cbfStatusFiles(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 2])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cbfStatusHighFiles(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 3])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cbfStatusFilesBumped(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# columns
class cbfDefineFileIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class cbfDefineFileName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cbfDefineFileStorage(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'ephemeral'), Enum(2, 'volatile'), Enum(3, 'permanent')]


class cbfDefineFileFormat(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'standardBER'), Enum(2, 'bulkBinary'), Enum(3, 'bulkASCII')]


class cbfDefineFileNow(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'notActive'), Enum(2, 'ready'), Enum(3, 'create'), Enum(4, 'running')]


class cbfDefineFileEntryStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class cbfDefineObjectIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class cbfDefineObjectClass(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'object'), Enum(2, 'lexicalTable'), Enum(3, 'leastCpuTable')]


class cbfDefineObjectID(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class cbfDefineObjectEntryStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class cbfStatusFileIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class cbfStatusFileState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'running'), Enum(2, 'ready'), Enum(3, 'emptied'), Enum(4, 'noSpace'), Enum(5, 'badName'), Enum(6, 'writeErr'), Enum(7, 'noMem'), Enum(8, 'buffErr'), Enum(9, 'aborted')]


class cbfStatusFileCompletionTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class cbfStatusFileEntryStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class cbfDefineFileEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cbfDefineFileIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1])
	access = 2
	rowstatus = cbfDefineFileEntryStatus
	columns = {'cbfDefineFileIndex': cbfDefineFileIndex, 'cbfDefineFileName': cbfDefineFileName, 'cbfDefineFileStorage': cbfDefineFileStorage, 'cbfDefineFileFormat': cbfDefineFileFormat, 'cbfDefineFileNow': cbfDefineFileNow, 'cbfDefineFileEntryStatus': cbfDefineFileEntryStatus}


class cbfDefineObjectEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cbfDefineFileIndex, cbfDefineObjectIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1])
	access = 2
	rowstatus = cbfDefineObjectEntryStatus
	columns = {'cbfDefineObjectIndex': cbfDefineObjectIndex, 'cbfDefineObjectClass': cbfDefineObjectClass, 'cbfDefineObjectID': cbfDefineObjectID, 'cbfDefineObjectEntryStatus': cbfDefineObjectEntryStatus}


class cbfStatusFileEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cbfDefineFileIndex, cbfStatusFileIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5, 1])
	access = 2
	rowstatus = cbfStatusFileEntryStatus
	columns = {'cbfStatusFileIndex': cbfStatusFileIndex, 'cbfStatusFileState': cbfStatusFileState, 'cbfStatusFileCompletionTime': cbfStatusFileCompletionTime, 'cbfStatusFileEntryStatus': cbfStatusFileEntryStatus}


# notifications (traps) 
# groups 
class ciscoBulkFileDefineGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 2, 1])
	group = [cbfDefineMaxFiles, cbfDefineFiles, cbfDefineHighFiles, cbfDefineFilesRefused, cbfDefineMaxObjects, cbfDefineObjects, cbfDefineHighObjects, cbfDefineObjectsRefused, cbfDefineFileName, cbfDefineFileStorage, cbfDefineFileFormat, cbfDefineFileNow, cbfDefineFileEntryStatus, cbfDefineObjectClass, cbfDefineObjectID, cbfDefineObjectEntryStatus]

class ciscoBulkFileStatusGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 2, 2])
	group = [cbfStatusMaxFiles, cbfStatusFiles, cbfStatusHighFiles, cbfStatusFilesBumped, cbfStatusFileState, cbfStatusFileCompletionTime, cbfStatusFileEntryStatus]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)