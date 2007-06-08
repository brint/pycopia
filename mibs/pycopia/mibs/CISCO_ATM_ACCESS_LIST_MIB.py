# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoMgmt
from SNMPv2_TC import TEXTUAL_CONVENTION, DisplayString, RowStatus
from IF_MIB import ifIndex

class CISCO_ATM_ACCESS_LIST_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-ATM-ACCESS-LIST-MIB'
	conformance = 3
	name = 'CISCO-ATM-ACCESS-LIST-MIB'
	language = 2
	description = 'A cisco ATM access list mib module.'

# nodes
class ciscoAtmAccessListMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67])
	name = 'ciscoAtmAccessListMIB'

class ciscoAtmAccessListMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1])
	name = 'ciscoAtmAccessListMIBObjects'

class ciscoAtmAddressTemplate(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 1])
	name = 'ciscoAtmAddressTemplate'

class ciscoAtmAddressFilter(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2])
	name = 'ciscoAtmAddressFilter'

class ciscoAtmAccessGroup(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 3])
	name = 'ciscoAtmAccessGroup'

class ciscoAtmAccessListMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 3])
	name = 'ciscoAtmAccessListMIBConformance'

class ciscoAtmAccessListMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 3, 1])
	name = 'ciscoAtmAccessListMIBCompliances'

class ciscoAtmAccessListMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 3, 2])
	name = 'ciscoAtmAccessListMIBGroups'


# macros
# types 

class CiscoAtmAddressTemplate(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(1, 70))

# scalars 
# columns
class atmAddressAliasName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class atmAddressTemplate(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 1, 1, 1, 2])
	syntaxobject = CiscoAtmAddressTemplate


class atmAddressTemplateRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class atmAddressFilterSetName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class atmAddressFilterSetIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAddressFilterSetType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'addressFilter'), Enum(2, 'timeOfDayFilter')]


class atmAddressFilterSetTemplate(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class atmAddressFilterSetStartHour(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAddressFilterSetStartMinute(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAddressFilterSetEndHour(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAddressFilterSetEndMinute(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAddressFilterSetPermission(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'permit'), Enum(2, 'deny')]


class atmAddressFilterSetRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class atmAddressFilterExpressionName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class atmAddressFilterExpressionQualifier1(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'source'), Enum(2, 'destination'), Enum(3, 'none')]


class atmAddressFilterExpressionTerm1(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class atmAddressFilterExpressionQualifier2(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'source'), Enum(2, 'destination'), Enum(3, 'none')]


class atmAddressFilterExpressionTerm2(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class atmAddressFilterExpressionOperator(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'and'), Enum(2, 'or'), Enum(3, 'xor'), Enum(4, 'not'), Enum(5, 'none')]


class atmAddressFilterExpressionRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class atmInboundAccessGroupName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 3, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class atmOutboundAccessGroupName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


# rows 
class ciscoAtmAddressTemplateEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([atmAddressAliasName], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 1, 1, 1])
	access = 2
	rowstatus = atmAddressTemplateRowStatus
	columns = {'atmAddressAliasName': atmAddressAliasName, 'atmAddressTemplate': atmAddressTemplate, 'atmAddressTemplateRowStatus': atmAddressTemplateRowStatus}


class ciscoAtmAddressFilterSetEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([atmAddressFilterSetName, atmAddressFilterSetIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 1, 1])
	access = 2
	rowstatus = atmAddressFilterSetRowStatus
	columns = {'atmAddressFilterSetName': atmAddressFilterSetName, 'atmAddressFilterSetIndex': atmAddressFilterSetIndex, 'atmAddressFilterSetType': atmAddressFilterSetType, 'atmAddressFilterSetTemplate': atmAddressFilterSetTemplate, 'atmAddressFilterSetStartHour': atmAddressFilterSetStartHour, 'atmAddressFilterSetStartMinute': atmAddressFilterSetStartMinute, 'atmAddressFilterSetEndHour': atmAddressFilterSetEndHour, 'atmAddressFilterSetEndMinute': atmAddressFilterSetEndMinute, 'atmAddressFilterSetPermission': atmAddressFilterSetPermission, 'atmAddressFilterSetRowStatus': atmAddressFilterSetRowStatus}


class ciscoAtmAddressFilterExpressionEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([atmAddressFilterExpressionName], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 2, 2, 1])
	access = 2
	rowstatus = atmAddressFilterExpressionRowStatus
	columns = {'atmAddressFilterExpressionName': atmAddressFilterExpressionName, 'atmAddressFilterExpressionQualifier1': atmAddressFilterExpressionQualifier1, 'atmAddressFilterExpressionTerm1': atmAddressFilterExpressionTerm1, 'atmAddressFilterExpressionQualifier2': atmAddressFilterExpressionQualifier2, 'atmAddressFilterExpressionTerm2': atmAddressFilterExpressionTerm2, 'atmAddressFilterExpressionOperator': atmAddressFilterExpressionOperator, 'atmAddressFilterExpressionRowStatus': atmAddressFilterExpressionRowStatus}


class ciscoAtmAccessGroupEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 1, 3, 1, 1])
	access = 2
	columns = {'atmInboundAccessGroupName': atmInboundAccessGroupName, 'atmOutboundAccessGroupName': atmOutboundAccessGroupName}


# notifications (traps) 
# groups 
class ciscoAtmAccessListMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 67, 3, 2, 1])
	group = [atmAddressTemplate, atmAddressTemplateRowStatus, atmAddressFilterSetType, atmAddressFilterSetTemplate, atmAddressFilterSetStartHour, atmAddressFilterSetStartMinute, atmAddressFilterSetEndHour, atmAddressFilterSetEndMinute, atmAddressFilterSetPermission, atmAddressFilterSetRowStatus, atmAddressFilterExpressionQualifier1, atmAddressFilterExpressionTerm1, atmAddressFilterExpressionQualifier2, atmAddressFilterExpressionTerm2, atmAddressFilterExpressionOperator, atmAddressFilterExpressionRowStatus, atmInboundAccessGroupName, atmOutboundAccessGroupName]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)