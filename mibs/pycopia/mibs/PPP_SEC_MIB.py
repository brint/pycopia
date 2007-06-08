# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from RFC_1212 import OBJECT_TYPE
from PPP_LCP_MIB import ppp
from RFC1155_SMI import Counter

class PPP_SEC_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/PPP-SEC-MIB'
	conformance = 5
	name = 'PPP-SEC-MIB'
	language = 1

# nodes
class pppSecurity(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2])
	name = 'pppSecurity'

class pppSecurityProtocols(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2, 1])
	name = 'pppSecurityProtocols'

class pppSecurityPapProtocol(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2, 1, 1])
	name = 'pppSecurityPapProtocol'

class pppSecurityChapMD5Protocol(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2, 1, 2])
	name = 'pppSecurityChapMD5Protocol'


# macros
# types 
# scalars 
# columns
class pppSecurityConfigLink(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class pppSecurityConfigPreference(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class pppSecurityConfigProtocol(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class pppSecurityConfigStatus(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'invalid'), Enum(2, 'valid')]


class pppSecuritySecretsLink(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class pppSecuritySecretsIdIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class pppSecuritySecretsDirection(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'local-to-remote'), Enum(2, 'remote-to-local')]


class pppSecuritySecretsProtocol(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class pppSecuritySecretsIdentity(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class pppSecuritySecretsSecret(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class pppSecuritySecretsStatus(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'invalid'), Enum(2, 'valid')]


# rows 
class pppSecurityConfigEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([pppSecurityConfigLink, pppSecurityConfigPreference], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1])
	access = 2
	columns = {'pppSecurityConfigLink': pppSecurityConfigLink, 'pppSecurityConfigPreference': pppSecurityConfigPreference, 'pppSecurityConfigProtocol': pppSecurityConfigProtocol, 'pppSecurityConfigStatus': pppSecurityConfigStatus}


class pppSecuritySecretsEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([pppSecuritySecretsLink, pppSecuritySecretsIdIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1])
	access = 2
	columns = {'pppSecuritySecretsLink': pppSecuritySecretsLink, 'pppSecuritySecretsIdIndex': pppSecuritySecretsIdIndex, 'pppSecuritySecretsDirection': pppSecuritySecretsDirection, 'pppSecuritySecretsProtocol': pppSecuritySecretsProtocol, 'pppSecuritySecretsIdentity': pppSecuritySecretsIdentity, 'pppSecuritySecretsSecret': pppSecuritySecretsSecret, 'pppSecuritySecretsStatus': pppSecuritySecretsStatus}


# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)