# python
# This file is generated by a program (mib2py). 

import RADIUS_DYNAUTH_CLIENT_MIB

OIDMAP = {
'1.3.6.1.2.1.145': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientMIB,
'1.3.6.1.2.1.145.1': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientMIBObjects,
'1.3.6.1.2.1.145.1.1': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientScalars,
'1.3.6.1.2.1.145.2': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientMIBConformance,
'1.3.6.1.2.1.145.2.1': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientMIBCompliances,
'1.3.6.1.2.1.145.2.2': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientMIBGroups,
'1.3.6.1.2.1.145.1.1.1': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientDisconInvalidServerAddresses,
'1.3.6.1.2.1.145.1.1.2': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientCoAInvalidServerAddresses,
'1.3.6.1.2.1.145.1.2.1.1': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthServerIndex,
'1.3.6.1.2.1.145.1.2.1.2': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthServerAddressType,
'1.3.6.1.2.1.145.1.2.1.3': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthServerAddress,
'1.3.6.1.2.1.145.1.2.1.4': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthServerClientPortNumber,
'1.3.6.1.2.1.145.1.2.1.5': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthServerID,
'1.3.6.1.2.1.145.1.2.1.6': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientRoundTripTime,
'1.3.6.1.2.1.145.1.2.1.7': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientDisconRequests,
'1.3.6.1.2.1.145.1.2.1.8': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientDisconAuthOnlyRequests,
'1.3.6.1.2.1.145.1.2.1.9': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientDisconRetransmissions,
'1.3.6.1.2.1.145.1.2.1.10': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientDisconAcks,
'1.3.6.1.2.1.145.1.2.1.11': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientDisconNaks,
'1.3.6.1.2.1.145.1.2.1.12': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientDisconNakAuthOnlyRequest,
'1.3.6.1.2.1.145.1.2.1.13': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientDisconNakSessNoContext,
'1.3.6.1.2.1.145.1.2.1.14': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientMalformedDisconResponses,
'1.3.6.1.2.1.145.1.2.1.15': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientDisconBadAuthenticators,
'1.3.6.1.2.1.145.1.2.1.16': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientDisconPendingRequests,
'1.3.6.1.2.1.145.1.2.1.17': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientDisconTimeouts,
'1.3.6.1.2.1.145.1.2.1.18': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientDisconPacketsDropped,
'1.3.6.1.2.1.145.1.2.1.19': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientCoARequests,
'1.3.6.1.2.1.145.1.2.1.20': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientCoAAuthOnlyRequest,
'1.3.6.1.2.1.145.1.2.1.21': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientCoARetransmissions,
'1.3.6.1.2.1.145.1.2.1.22': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientCoAAcks,
'1.3.6.1.2.1.145.1.2.1.23': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientCoANaks,
'1.3.6.1.2.1.145.1.2.1.24': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientCoANakAuthOnlyRequest,
'1.3.6.1.2.1.145.1.2.1.25': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientCoANakSessNoContext,
'1.3.6.1.2.1.145.1.2.1.26': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientMalformedCoAResponses,
'1.3.6.1.2.1.145.1.2.1.27': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientCoABadAuthenticators,
'1.3.6.1.2.1.145.1.2.1.28': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientCoAPendingRequests,
'1.3.6.1.2.1.145.1.2.1.29': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientCoATimeouts,
'1.3.6.1.2.1.145.1.2.1.30': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientCoAPacketsDropped,
'1.3.6.1.2.1.145.1.2.1.31': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientUnknownTypes,
'1.3.6.1.2.1.145.1.2.1.32': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientCounterDiscontinuity,
'1.3.6.1.2.1.145.2.2.1': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientMIBGroup,
'1.3.6.1.2.1.145.2.2.2': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientAuthOnlyGroup,
'1.3.6.1.2.1.145.2.2.3': RADIUS_DYNAUTH_CLIENT_MIB.radiusDynAuthClientNoSessGroup,
}