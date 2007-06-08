# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import Integer32, Gauge32, OBJECT_TYPE, MODULE_IDENTITY
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_TC import DisplayString, RowStatus, TDomain, TAddress
from HP_ICF_OID import hpicfObjectModules, hpicfCommon

class HP_ICF_DOWNLOAD(ModuleObject):
	path = '/usr/share/snmp/mibs/site/HP-ICF-DOWNLOAD'
	conformance = 5
	name = 'HP-ICF-DOWNLOAD'
	language = 2
	description = 'This MIB module manages the network download\ncapabilities for devices in the HP Integrated\nCommunication Facility product line.'

# nodes
class hpicfDownloadMib(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4])
	name = 'hpicfDownloadMib'

class hpicfDownloadConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1])
	name = 'hpicfDownloadConformance'

class hpicfDownloadCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 1])
	name = 'hpicfDownloadCompliances'

class hpicfDownloadGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 2])
	name = 'hpicfDownloadGroups'

class hpicfDownload(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3])
	name = 'hpicfDownload'


# macros
# types 
# scalars 
class hpicfDownloadLogMaxSize(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpicfDownloadLogSize(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 3])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


# columns
class hpicfDownloadIndex(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'dlInstance')]


class hpicfDownloadOwnerAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TAddress


class hpicfDownloadOwnerDomain(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TDomain


class hpicfDownloadTAddress(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TAddress


class hpicfDownloadTDomain(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TDomain


class hpicfDownloadFilename(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class hpicfDownloadResetType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'noReset'), Enum(2, 'warmReset'), Enum(3, 'factoryReset')]


class hpicfDownloadErrorStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'fileNotFound'), Enum(2, 'accessViolation'), Enum(3, 'diskFull'), Enum(4, 'illegalOperation'), Enum(5, 'unknownTID'), Enum(6, 'fileExists'), Enum(7, 'noSuchUser'), Enum(8, 'notDefined'), Enum(9, 'corruptFile'), Enum(10, 'noServer'), Enum(11, 'tftpTimeout'), Enum(12, 'hardwareError'), Enum(13, 'success'), Enum(14, 'aborted'), Enum(15, 'inProgress'), Enum(16, 'idle'), Enum(17, 'erasingEeprom'), Enum(18, 'incompleteFirmware'), Enum(19, 'requirePowerCycle'), Enum(20, 'cannotUpgrade'), Enum(21, 'cannotDowngrade')]


class hpicfDownloadErrorText(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class hpicfDownloadStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class hpicfDownloadPassesLeft(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpicfDownloadOctetCount(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpicfDownloadDestination(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class hpicfDlLogIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpicfDlLogOwnerAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TAddress


class hpicfDlLogOwnerDomain(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TDomain


class hpicfDlLogTAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TAddress


class hpicfDlLogTDomain(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TDomain


class hpicfDlLogFilename(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class hpicfDlLogResetType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'noReset'), Enum(2, 'warmReset'), Enum(3, 'factoryReset')]


class hpicfDlLogErrorStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'fileNotFound'), Enum(2, 'accessViolation'), Enum(3, 'diskFull'), Enum(4, 'illegalOperation'), Enum(5, 'unknownTID'), Enum(6, 'fileExists'), Enum(7, 'noSuchUser'), Enum(8, 'notDefined'), Enum(9, 'corruptFile'), Enum(10, 'noServer'), Enum(11, 'tftpTimeout'), Enum(12, 'hardwareError'), Enum(13, 'success'), Enum(14, 'aborted')]


class hpicfDlLogErrorText(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


# rows 
class hpicfDownloadEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([hpicfDownloadIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1])
	access = 2
	rowstatus = hpicfDownloadStatus
	columns = {'hpicfDownloadIndex': hpicfDownloadIndex, 'hpicfDownloadOwnerAddress': hpicfDownloadOwnerAddress, 'hpicfDownloadOwnerDomain': hpicfDownloadOwnerDomain, 'hpicfDownloadTAddress': hpicfDownloadTAddress, 'hpicfDownloadTDomain': hpicfDownloadTDomain, 'hpicfDownloadFilename': hpicfDownloadFilename, 'hpicfDownloadResetType': hpicfDownloadResetType, 'hpicfDownloadErrorStatus': hpicfDownloadErrorStatus, 'hpicfDownloadErrorText': hpicfDownloadErrorText, 'hpicfDownloadStatus': hpicfDownloadStatus, 'hpicfDownloadPassesLeft': hpicfDownloadPassesLeft, 'hpicfDownloadOctetCount': hpicfDownloadOctetCount, 'hpicfDownloadDestination': hpicfDownloadDestination}


class hpicfDownloadLogEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([hpicfDlLogIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1])
	access = 2
	columns = {'hpicfDlLogIndex': hpicfDlLogIndex, 'hpicfDlLogOwnerAddress': hpicfDlLogOwnerAddress, 'hpicfDlLogOwnerDomain': hpicfDlLogOwnerDomain, 'hpicfDlLogTAddress': hpicfDlLogTAddress, 'hpicfDlLogTDomain': hpicfDlLogTDomain, 'hpicfDlLogFilename': hpicfDlLogFilename, 'hpicfDlLogResetType': hpicfDlLogResetType, 'hpicfDlLogErrorStatus': hpicfDlLogErrorStatus, 'hpicfDlLogErrorText': hpicfDlLogErrorText}


# notifications (traps) 
# groups 
class hpicfDownloadGroup(GroupObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 2, 1])
	group = [hpicfDownloadIndex, hpicfDownloadOwnerAddress, hpicfDownloadOwnerDomain, hpicfDownloadTAddress, hpicfDownloadTDomain, hpicfDownloadFilename, hpicfDownloadResetType, hpicfDownloadErrorStatus, hpicfDownloadErrorText, hpicfDownloadStatus, hpicfDownloadLogMaxSize, hpicfDownloadLogSize]

class hpicfDownloadLogGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 2, 2])
	group = [hpicfDlLogIndex, hpicfDlLogOwnerAddress, hpicfDlLogOwnerDomain, hpicfDlLogTAddress, hpicfDlLogTDomain, hpicfDlLogFilename, hpicfDlLogResetType, hpicfDlLogErrorStatus, hpicfDlLogErrorText]

class hpicfDownloadConfigGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4, 1, 2, 3])
	group = [hpicfDownloadIndex, hpicfDownloadOwnerAddress, hpicfDownloadOwnerDomain, hpicfDownloadTAddress, hpicfDownloadTDomain, hpicfDownloadFilename, hpicfDownloadResetType, hpicfDownloadErrorStatus, hpicfDownloadErrorText, hpicfDownloadStatus, hpicfDownloadPassesLeft, hpicfDownloadOctetCount, hpicfDownloadDestination, hpicfDownloadLogMaxSize, hpicfDownloadLogSize]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)