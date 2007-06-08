# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, enterprises, Integer32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_TC import TEXTUAL_CONVENTION

class Job_Monitoring_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/Job-Monitoring-MIB'
	conformance = 5
	name = 'Job-Monitoring-MIB'
	language = 2
	description = 'The MIB module for monitoring job in servers, printers, and\nother devices.\n\nVersion: 1.0'

# nodes
class jobmonMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1])
	name = 'jobmonMIB'

class jobmonMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1])
	name = 'jobmonMIBObjects'

class jmGeneral(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1])
	name = 'jmGeneral'

class jmJobID(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2])
	name = 'jmJobID'

class jmJob(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3])
	name = 'jmJob'

class jmAttribute(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4])
	name = 'jmAttribute'

class jobmonMIBNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 2])
	name = 'jobmonMIBNotifications'

class jmMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 3])
	name = 'jmMIBConformance'

class jmMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2])
	name = 'jmMIBGroups'


# macros
# types 

class JmUTF8StringTC(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 63))
	format = '255a'


class JmJobStringTC(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 63))


class JmNaturalLanguageTagTC(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 63))


class JmTimeStampTC(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 2147483647))


class JmJobSourcePlatformTypeTC(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'other'), Enum(2, 'unknown'), Enum(3, 'sptUNIX'), Enum(4, 'sptOS2'), Enum(5, 'sptPCDOS'), Enum(6, 'sptNT'), Enum(7, 'sptMVS'), Enum(8, 'sptVM'), Enum(9, 'sptOS400'), Enum(10, 'sptVMS'), Enum(11, 'sptWindows'), Enum(12, 'sptNetWare')]


class JmFinishingTC(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'other'), Enum(2, 'unknown'), Enum(3, 'none'), Enum(4, 'staple'), Enum(5, 'punch'), Enum(6, 'cover'), Enum(7, 'bind')]


class JmPrintQualityTC(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'other'), Enum(2, 'unknown'), Enum(3, 'draft'), Enum(4, 'normal'), Enum(5, 'high')]


class JmPrinterResolutionTC(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(9, 9))


class JmTonerEconomyTC(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(2, 'unknown'), Enum(3, 'off'), Enum(4, 'on')]


class JmBooleanTC(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(2, 'unknown'), Enum(3, 'false'), Enum(4, 'true')]


class JmMediumTypeTC(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'other'), Enum(2, 'unknown'), Enum(3, 'stationery'), Enum(4, 'transparency'), Enum(5, 'envelope'), Enum(6, 'envelopePlain'), Enum(7, 'envelopeWindow'), Enum(8, 'continuousLong'), Enum(9, 'continuousShort'), Enum(10, 'tabStock'), Enum(11, 'multiPartForm'), Enum(12, 'labels'), Enum(13, 'multiLayer')]


class JmJobCollationTypeTC(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'other'), Enum(2, 'unknown'), Enum(3, 'uncollatedSheets'), Enum(4, 'collatedDocuments'), Enum(5, 'uncollatedDocuments')]


class JmJobSubmissionIDTypeTC(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(1, 1))


class JmJobStateTC(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(2, 'unknown'), Enum(3, 'pending'), Enum(4, 'pendingHeld'), Enum(5, 'processing'), Enum(6, 'processingStopped'), Enum(7, 'canceled'), Enum(8, 'aborted'), Enum(9, 'completed')]


class JmAttributeTypeTC(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'other'), Enum(3, 'jobStateReasons2'), Enum(4, 'jobStateReasons3'), Enum(5, 'jobStateReasons4'), Enum(6, 'processingMessage'), Enum(7, 'processingMessageNaturalLangTag'), Enum(8, 'jobCodedCharSet'), Enum(9, 'jobNaturalLanguageTag'), Enum(20, 'jobURI'), Enum(21, 'jobAccountName'), Enum(22, 'serverAssignedJobName'), Enum(23, 'jobName'), Enum(24, 'jobServiceTypes'), Enum(25, 'jobSourceChannelIndex'), Enum(26, 'jobSourcePlatformType'), Enum(27, 'submittingServerName'), Enum(28, 'submittingApplicationName'), Enum(29, 'jobOriginatingHost'), Enum(30, 'deviceNameRequested'), Enum(31, 'queueNameRequested'), Enum(32, 'physicalDevice'), Enum(33, 'numberOfDocuments'), Enum(34, 'fileName'), Enum(35, 'documentName'), Enum(36, 'jobComment'), Enum(37, 'documentFormatIndex'), Enum(38, 'documentFormat'), Enum(50, 'jobPriority'), Enum(51, 'jobProcessAfterDateAndTime'), Enum(52, 'jobHold'), Enum(53, 'jobHoldUntil'), Enum(54, 'outputBin'), Enum(55, 'sides'), Enum(56, 'finishing'), Enum(70, 'printQualityRequested'), Enum(71, 'printQualityUsed'), Enum(72, 'printerResolutionRequested'), Enum(73, 'printerResolutionUsed'), Enum(74, 'tonerEcomonyRequested'), Enum(75, 'tonerEcomonyUsed'), Enum(76, 'tonerDensityRequested'), Enum(77, 'tonerDensityUsed'), Enum(90, 'jobCopiesRequested'), Enum(91, 'jobCopiesCompleted'), Enum(92, 'documentCopiesRequested'), Enum(93, 'documentCopiesCompleted'), Enum(94, 'jobKOctetsTransferred'), Enum(95, 'sheetCompletedCopyNumber'), Enum(96, 'sheetCompletedDocumentNumber'), Enum(97, 'jobCollationType'), Enum(110, 'impressionsSpooled'), Enum(111, 'impressionsSentToDevice'), Enum(112, 'impressionsInterpreted'), Enum(113, 'impressionsCompletedCurrentCopy'), Enum(114, 'fullColorImpressionsCompleted'), Enum(115, 'highlightColorImpressionsCompleted'), Enum(130, 'pagesRequested'), Enum(131, 'pagesCompleted'), Enum(132, 'pagesCompletedCurrentCopy'), Enum(150, 'sheetsRequested'), Enum(151, 'sheetsCompleted'), Enum(152, 'sheetsCompletedCurrentCopy'), Enum(170, 'mediumRequested'), Enum(171, 'mediumConsumed'), Enum(172, 'colorantRequested'), Enum(173, 'colorantConsumed'), Enum(174, 'mediumTypeConsumed'), Enum(175, 'mediumSizeConsumed'), Enum(190, 'jobSubmissionToServerTime'), Enum(191, 'jobSubmissionTime'), Enum(192, 'jobStartedBeingHeldTime'), Enum(193, 'jobStartedProcessingTime'), Enum(194, 'jobCompletionTime'), Enum(195, 'jobProcessingCPUTime')]


class JmJobServiceTypesTC(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 2147483647))


class JmJobStateReasons1TC(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 2147483647))


class JmJobStateReasons2TC(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 2147483647))


class JmJobStateReasons3TC(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 2147483647))


class JmJobStateReasons4TC(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 2147483647))

# scalars 
# columns
class jmGeneralJobSetIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class jmGeneralNumberOfActiveJobs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class jmGeneralOldestActiveJobIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class jmGeneralNewestActiveJobIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class jmGeneralJobPersistence(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 4
	units = 'seconds'


class jmGeneralAttributePersistence(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 4
	units = 'seconds'


class jmGeneralJobSetName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 7])
	syntaxobject = JmUTF8StringTC


class jmJobSubmissionID(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class jmJobIDJobSetIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class jmJobIDJobIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class jmJobIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class jmJobState(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 2])
	syntaxobject = JmJobStateTC


class jmJobStateReasons1(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 3])
	syntaxobject = JmJobStateReasons1TC


class jmNumberOfInterveningJobs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class jmJobKOctetsPerCopyRequested(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class jmJobKOctetsProcessed(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class jmJobImpressionsPerCopyRequested(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class jmJobImpressionsCompleted(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class jmJobOwner(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 9])
	syntaxobject = JmJobStringTC


class jmAttributeTypeIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1, 1])
	syntaxobject = JmAttributeTypeTC


class jmAttributeInstanceIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class jmAttributeValueAsInteger(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class jmAttributeValueAsOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


# rows 
class jmGeneralEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([jmGeneralJobSetIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1])
	access = 2
	columns = {'jmGeneralJobSetIndex': jmGeneralJobSetIndex, 'jmGeneralNumberOfActiveJobs': jmGeneralNumberOfActiveJobs, 'jmGeneralOldestActiveJobIndex': jmGeneralOldestActiveJobIndex, 'jmGeneralNewestActiveJobIndex': jmGeneralNewestActiveJobIndex, 'jmGeneralJobPersistence': jmGeneralJobPersistence, 'jmGeneralAttributePersistence': jmGeneralAttributePersistence, 'jmGeneralJobSetName': jmGeneralJobSetName}


class jmJobIDEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([jmJobSubmissionID], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1, 1])
	access = 2
	columns = {'jmJobSubmissionID': jmJobSubmissionID, 'jmJobIDJobSetIndex': jmJobIDJobSetIndex, 'jmJobIDJobIndex': jmJobIDJobIndex}


class jmJobEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([jmGeneralJobSetIndex, jmJobIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1])
	access = 2
	columns = {'jmJobIndex': jmJobIndex, 'jmJobState': jmJobState, 'jmJobStateReasons1': jmJobStateReasons1, 'jmNumberOfInterveningJobs': jmNumberOfInterveningJobs, 'jmJobKOctetsPerCopyRequested': jmJobKOctetsPerCopyRequested, 'jmJobKOctetsProcessed': jmJobKOctetsProcessed, 'jmJobImpressionsPerCopyRequested': jmJobImpressionsPerCopyRequested, 'jmJobImpressionsCompleted': jmJobImpressionsCompleted, 'jmJobOwner': jmJobOwner}


class jmAttributeEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([jmGeneralJobSetIndex, jmJobIndex, jmAttributeTypeIndex, jmAttributeInstanceIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1])
	access = 2
	columns = {'jmAttributeTypeIndex': jmAttributeTypeIndex, 'jmAttributeInstanceIndex': jmAttributeInstanceIndex, 'jmAttributeValueAsInteger': jmAttributeValueAsInteger, 'jmAttributeValueAsOctets': jmAttributeValueAsOctets}


# notifications (traps) 
# groups 
class jmGeneralGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2, 1])
	group = [jmGeneralNumberOfActiveJobs, jmGeneralOldestActiveJobIndex, jmGeneralNewestActiveJobIndex, jmGeneralJobPersistence, jmGeneralAttributePersistence, jmGeneralJobSetName]

class jmJobIDGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2, 2])
	group = [jmJobIDJobSetIndex, jmJobIDJobIndex]

class jmJobGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2, 3])
	group = [jmJobState, jmJobStateReasons1, jmNumberOfInterveningJobs, jmJobKOctetsPerCopyRequested, jmJobKOctetsProcessed, jmJobImpressionsPerCopyRequested, jmJobImpressionsCompleted, jmJobOwner]

class jmAttributeGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2, 4])
	group = [jmAttributeValueAsInteger, jmAttributeValueAsOctets]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)