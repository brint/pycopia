# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, Counter32, Gauge32, OBJECT_TYPE, Unsigned32, experimental
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_TC import TEXTUAL_CONVENTION, TimeStamp, RowStatus, StorageType
from SNMP_FRAMEWORK_MIB import SnmpAdminString

class BLDG_HVAC_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/BLDG-HVAC-MIB'
	name = 'BLDG-HVAC-MIB'
	language = 2
	description = 'This example MIB module defines a set of management objects\nfor heating ventilation and air conditioning systems.  It\nalso includes objects that can be used to create policies\nthat are applied to rooms.  This eliminates the need to send\nper-instance configuration commands to the system.\n\nCopyright (C) The Internet Society (2003).  This version of\nthis MIB module is part of RFC 3512; see the RFC itself for\nfull legal notices.'

# nodes
class bldgHVACMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122])
	name = 'bldgHVACMIB'

class bldgHVACObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1])
	name = 'bldgHVACObjects'

class bldgConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 2])
	name = 'bldgConformance'

class bldgCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 2, 1])
	name = 'bldgCompliances'

class bldgGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 2, 2])
	name = 'bldgGroups'


# macros
# types 

class BldgHvacOperation(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'heat'), Enum(2, 'cool')]

# scalars 
# columns
class bldgHVACFloor(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class bldgHVACOffice(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class bldgHVACCfgTemplate(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class bldgHVACFanSpeed(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'revolutions per minute'


class bldgHVACCurrentTemp(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'degrees in celsius'


class bldgHVACCoolOrHeatMins(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'minutes'


class bldgHVACDiscontinuityTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class bldgHVACOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 1, 1, 8])
	syntaxobject = SnmpAdminString


class bldgHVACStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class bldgHVACStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class bldgHVACCfgTemplateInfoIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class bldgHVACCfgTemplateInfoID(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 2, 1, 2])
	syntaxobject = SnmpAdminString


class bldgHVACCfgTemplateInfoDescr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 2, 1, 3])
	syntaxobject = SnmpAdminString


class bldgHVACCfgTemplateInfoOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 2, 1, 4])
	syntaxobject = SnmpAdminString


class bldgHVACCfgTemplateInfoStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class bldgHVACCfgTemplateInfoStorType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class bldgHVACCfgTemplateIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class bldgHVACCfgTemplateDesiredTemp(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 5
	units = 'degrees in celsius'


class bldgHVACCfgTemplateCoolOrHeat(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 3, 1, 3])
	syntaxobject = BldgHvacOperation


class bldgHVACCfgTemplateInfo(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class bldgHVACCfgTemplateOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 3, 1, 5])
	syntaxobject = SnmpAdminString


class bldgHVACCfgTemplateStorage(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class bldgHVACCfgTemplateStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class bldgHVACEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([bldgHVACFloor, bldgHVACOffice], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 1, 1])
	access = 2
	rowstatus = bldgHVACStatus
	columns = {'bldgHVACFloor': bldgHVACFloor, 'bldgHVACOffice': bldgHVACOffice, 'bldgHVACCfgTemplate': bldgHVACCfgTemplate, 'bldgHVACFanSpeed': bldgHVACFanSpeed, 'bldgHVACCurrentTemp': bldgHVACCurrentTemp, 'bldgHVACCoolOrHeatMins': bldgHVACCoolOrHeatMins, 'bldgHVACDiscontinuityTime': bldgHVACDiscontinuityTime, 'bldgHVACOwner': bldgHVACOwner, 'bldgHVACStorageType': bldgHVACStorageType, 'bldgHVACStatus': bldgHVACStatus}


class bldgHVACCfgTemplateInfoEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([bldgHVACCfgTemplateInfoIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 2, 1])
	access = 2
	rowstatus = bldgHVACCfgTemplateInfoStatus
	columns = {'bldgHVACCfgTemplateInfoIndex': bldgHVACCfgTemplateInfoIndex, 'bldgHVACCfgTemplateInfoID': bldgHVACCfgTemplateInfoID, 'bldgHVACCfgTemplateInfoDescr': bldgHVACCfgTemplateInfoDescr, 'bldgHVACCfgTemplateInfoOwner': bldgHVACCfgTemplateInfoOwner, 'bldgHVACCfgTemplateInfoStatus': bldgHVACCfgTemplateInfoStatus, 'bldgHVACCfgTemplateInfoStorType': bldgHVACCfgTemplateInfoStorType}


class bldgHVACCfgTemplateEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([bldgHVACCfgTemplateIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 1, 3, 1])
	access = 2
	rowstatus = bldgHVACCfgTemplateStatus
	columns = {'bldgHVACCfgTemplateIndex': bldgHVACCfgTemplateIndex, 'bldgHVACCfgTemplateDesiredTemp': bldgHVACCfgTemplateDesiredTemp, 'bldgHVACCfgTemplateCoolOrHeat': bldgHVACCfgTemplateCoolOrHeat, 'bldgHVACCfgTemplateInfo': bldgHVACCfgTemplateInfo, 'bldgHVACCfgTemplateOwner': bldgHVACCfgTemplateOwner, 'bldgHVACCfgTemplateStorage': bldgHVACCfgTemplateStorage, 'bldgHVACCfgTemplateStatus': bldgHVACCfgTemplateStatus}


# notifications (traps) 
# groups 
class bldgHVACObjectsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 122, 2, 2, 1])
	group = [bldgHVACCfgTemplate, bldgHVACFanSpeed, bldgHVACCurrentTemp, bldgHVACCoolOrHeatMins, bldgHVACDiscontinuityTime, bldgHVACOwner, bldgHVACStatus, bldgHVACStorageType, bldgHVACCfgTemplateInfoID, bldgHVACCfgTemplateInfoDescr, bldgHVACCfgTemplateInfoOwner, bldgHVACCfgTemplateInfoStatus, bldgHVACCfgTemplateInfoStorType, bldgHVACCfgTemplateDesiredTemp, bldgHVACCfgTemplateCoolOrHeat, bldgHVACCfgTemplateInfo, bldgHVACCfgTemplateOwner, bldgHVACCfgTemplateStorage, bldgHVACCfgTemplateStatus]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)