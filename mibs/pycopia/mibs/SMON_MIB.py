# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from IF_MIB import InterfaceIndex
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32, Integer32, Counter64
from RMON2_MIB import LastCreateTime, DataSource, rmonConformance, probeConfig
from RMON_MIB import rmon, OwnerString
from SNMPv2_TC import RowStatus, TEXTUAL_CONVENTION

class SMON_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/SMON-MIB'
	conformance = 3
	name = 'SMON-MIB'
	language = 2
	description = 'The MIB module for managing remote monitoring device\nimplementations for Switched Networks'

# nodes
class smonMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 20, 3])
	name = 'smonMIBCompliances'

class smonMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 20, 4])
	name = 'smonMIBGroups'

class switchRMON(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22])
	name = 'switchRMON'

class smonMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1])
	name = 'smonMIBObjects'

class dataSourceCaps(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 1])
	name = 'dataSourceCaps'

class smonStats(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2])
	name = 'smonStats'

class portCopyConfig(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 3])
	name = 'portCopyConfig'

class smonRegistrationPoints(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 4])
	name = 'smonRegistrationPoints'

class smonVlanDataSource(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 4, 1])
	name = 'smonVlanDataSource'


# macros
# types 

class SmonDataSource(pycopia.SMI.Basetypes.ObjectIdentifier):
	status = 1

# scalars 
class smonCapabilities(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 19, 15])
	syntaxobject = pycopia.SMI.Basetypes.BITS


# columns
class dataSourceCapsObject(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1, 1, 1])
	syntaxobject = SmonDataSource


class dataSourceRmonCaps(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class dataSourceCopyCaps(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class dataSourceCapsIfIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1, 1, 4])
	syntaxobject = InterfaceIndex


class smonVlanStatsControlIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class smonVlanStatsControlDataSource(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1, 2])
	syntaxobject = DataSource


class smonVlanStatsControlCreateTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1, 3])
	syntaxobject = LastCreateTime


class smonVlanStatsControlOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1, 4])
	syntaxobject = OwnerString


class smonVlanStatsControlStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class smonVlanIdStatsId(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class smonVlanIdStatsTotalPkts(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class smonVlanIdStatsTotalOverflowPkts(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class smonVlanIdStatsTotalHCPkts(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter64
	access = 4
	units = 'packets'


class smonVlanIdStatsTotalOctets(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class smonVlanIdStatsTotalOverflowOctets(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class smonVlanIdStatsTotalHCOctets(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter64
	access = 4
	units = 'octets'


class smonVlanIdStatsNUcastPkts(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class smonVlanIdStatsNUcastOverflowPkts(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class smonVlanIdStatsNUcastHCPkts(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter64
	access = 4
	units = 'packets'


class smonVlanIdStatsNUcastOctets(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class smonVlanIdStatsNUcastOverflowOctets(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class smonVlanIdStatsNUcastHCOctets(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter64
	access = 4
	units = 'octets'


class smonVlanIdStatsCreateTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 14])
	syntaxobject = LastCreateTime


class smonPrioStatsControlIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class smonPrioStatsControlDataSource(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1, 2])
	syntaxobject = DataSource


class smonPrioStatsControlCreateTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1, 3])
	syntaxobject = LastCreateTime


class smonPrioStatsControlOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1, 4])
	syntaxobject = OwnerString


class smonPrioStatsControlStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class smonPrioStatsId(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class smonPrioStatsPkts(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class smonPrioStatsOverflowPkts(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class smonPrioStatsHCPkts(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter64
	access = 4
	units = 'packets'


class smonPrioStatsOctets(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class smonPrioStatsOverflowOctets(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class smonPrioStatsHCOctets(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter64
	access = 4
	units = 'octets'


class portCopySource(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1, 1])
	syntaxobject = InterfaceIndex


class portCopyDest(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1, 2])
	syntaxobject = InterfaceIndex


class portCopyDestDropEvents(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'events'


class portCopyDirection(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'copyRxOnly'), Enum(2, 'copyTxOnly'), Enum(3, 'copyBoth')]


class portCopyStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class dataSourceCapsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dataSourceCapsObject], True)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1, 1])
	access = 2
	columns = {'dataSourceCapsObject': dataSourceCapsObject, 'dataSourceRmonCaps': dataSourceRmonCaps, 'dataSourceCopyCaps': dataSourceCopyCaps, 'dataSourceCapsIfIndex': dataSourceCapsIfIndex}


class smonVlanStatsControlEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([smonVlanStatsControlIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1])
	access = 2
	rowstatus = smonVlanStatsControlStatus
	columns = {'smonVlanStatsControlIndex': smonVlanStatsControlIndex, 'smonVlanStatsControlDataSource': smonVlanStatsControlDataSource, 'smonVlanStatsControlCreateTime': smonVlanStatsControlCreateTime, 'smonVlanStatsControlOwner': smonVlanStatsControlOwner, 'smonVlanStatsControlStatus': smonVlanStatsControlStatus}


class smonVlanIdStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([smonVlanStatsControlIndex, smonVlanIdStatsId], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1])
	access = 2
	columns = {'smonVlanIdStatsId': smonVlanIdStatsId, 'smonVlanIdStatsTotalPkts': smonVlanIdStatsTotalPkts, 'smonVlanIdStatsTotalOverflowPkts': smonVlanIdStatsTotalOverflowPkts, 'smonVlanIdStatsTotalHCPkts': smonVlanIdStatsTotalHCPkts, 'smonVlanIdStatsTotalOctets': smonVlanIdStatsTotalOctets, 'smonVlanIdStatsTotalOverflowOctets': smonVlanIdStatsTotalOverflowOctets, 'smonVlanIdStatsTotalHCOctets': smonVlanIdStatsTotalHCOctets, 'smonVlanIdStatsNUcastPkts': smonVlanIdStatsNUcastPkts, 'smonVlanIdStatsNUcastOverflowPkts': smonVlanIdStatsNUcastOverflowPkts, 'smonVlanIdStatsNUcastHCPkts': smonVlanIdStatsNUcastHCPkts, 'smonVlanIdStatsNUcastOctets': smonVlanIdStatsNUcastOctets, 'smonVlanIdStatsNUcastOverflowOctets': smonVlanIdStatsNUcastOverflowOctets, 'smonVlanIdStatsNUcastHCOctets': smonVlanIdStatsNUcastHCOctets, 'smonVlanIdStatsCreateTime': smonVlanIdStatsCreateTime}


class smonPrioStatsControlEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([smonPrioStatsControlIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1])
	access = 2
	rowstatus = smonPrioStatsControlStatus
	columns = {'smonPrioStatsControlIndex': smonPrioStatsControlIndex, 'smonPrioStatsControlDataSource': smonPrioStatsControlDataSource, 'smonPrioStatsControlCreateTime': smonPrioStatsControlCreateTime, 'smonPrioStatsControlOwner': smonPrioStatsControlOwner, 'smonPrioStatsControlStatus': smonPrioStatsControlStatus}


class smonPrioStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([smonPrioStatsControlIndex, smonPrioStatsId], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1])
	access = 2
	columns = {'smonPrioStatsId': smonPrioStatsId, 'smonPrioStatsPkts': smonPrioStatsPkts, 'smonPrioStatsOverflowPkts': smonPrioStatsOverflowPkts, 'smonPrioStatsHCPkts': smonPrioStatsHCPkts, 'smonPrioStatsOctets': smonPrioStatsOctets, 'smonPrioStatsOverflowOctets': smonPrioStatsOverflowOctets, 'smonPrioStatsHCOctets': smonPrioStatsHCOctets}


class portCopyEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([portCopySource, portCopyDest], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1])
	access = 2
	rowstatus = portCopyStatus
	columns = {'portCopySource': portCopySource, 'portCopyDest': portCopyDest, 'portCopyDestDropEvents': portCopyDestDropEvents, 'portCopyDirection': portCopyDirection, 'portCopyStatus': portCopyStatus}


# notifications (traps) 
# groups 
class dataSourceCapsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 20, 4, 1])
	group = [dataSourceRmonCaps, dataSourceCopyCaps, dataSourceCapsIfIndex]

class smonVlanStatsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 20, 4, 2])
	group = [smonVlanStatsControlDataSource, smonVlanStatsControlCreateTime, smonVlanStatsControlOwner, smonVlanStatsControlStatus, smonVlanIdStatsTotalPkts, smonVlanIdStatsTotalOctets, smonVlanIdStatsNUcastPkts, smonVlanIdStatsCreateTime]

class smonPrioStatsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 20, 4, 3])
	group = [smonPrioStatsControlDataSource, smonPrioStatsControlCreateTime, smonPrioStatsControlOwner, smonPrioStatsControlStatus, smonPrioStatsPkts, smonPrioStatsOctets]

class smonHcTo100mbGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 20, 4, 4])
	group = [smonVlanIdStatsTotalOverflowOctets, smonVlanIdStatsTotalHCOctets, smonPrioStatsOverflowOctets, smonPrioStatsHCOctets]

class smonHc100mbPlusGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 20, 4, 5])
	group = [smonVlanIdStatsTotalOverflowPkts, smonVlanIdStatsTotalHCPkts, smonVlanIdStatsTotalOverflowOctets, smonVlanIdStatsTotalHCOctets, smonVlanIdStatsNUcastOverflowPkts, smonVlanIdStatsNUcastHCPkts, smonPrioStatsOverflowPkts, smonPrioStatsHCPkts, smonPrioStatsOverflowOctets, smonPrioStatsHCOctets]

class hcVlanTo100mbGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 20, 4, 6])
	group = [smonVlanIdStatsTotalOverflowOctets, smonVlanIdStatsTotalHCOctets]

class hcVlan100mbPlusGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 20, 4, 7])
	group = [smonVlanIdStatsTotalOverflowPkts, smonVlanIdStatsTotalHCPkts, smonVlanIdStatsTotalOverflowOctets, smonVlanIdStatsTotalHCOctets, smonVlanIdStatsNUcastOverflowPkts, smonVlanIdStatsNUcastHCPkts]

class hcPrioTo100mbGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 20, 4, 8])
	group = [smonPrioStatsOverflowOctets, smonPrioStatsHCOctets]

class hcPrio100mbPlusGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 20, 4, 9])
	group = [smonPrioStatsOverflowPkts, smonPrioStatsHCPkts, smonPrioStatsOverflowOctets, smonPrioStatsHCOctets]

class smonVlanStatsExtGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 20, 4, 10])
	group = [smonVlanIdStatsNUcastOctets, smonVlanIdStatsNUcastOverflowOctets, smonVlanIdStatsNUcastHCOctets]

class smonInformationGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 20, 4, 11])
	group = [smonCapabilities]

class portCopyConfigGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 20, 4, 12])
	group = [portCopyDestDropEvents, portCopyDirection, portCopyStatus]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)