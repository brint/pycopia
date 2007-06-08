# python
# This file is generated by a program (mib2py). 

import RFC1213_MIB

OIDMAP = {
'1.3.6.1.2.1': RFC1213_MIB.mib_2,
'1.3.6.1.2.1.1': RFC1213_MIB.system,
'1.3.6.1.2.1.2': RFC1213_MIB.interfaces,
'1.3.6.1.2.1.3': RFC1213_MIB.at,
'1.3.6.1.2.1.4': RFC1213_MIB.ip,
'1.3.6.1.2.1.5': RFC1213_MIB.icmp,
'1.3.6.1.2.1.6': RFC1213_MIB.tcp,
'1.3.6.1.2.1.7': RFC1213_MIB.udp,
'1.3.6.1.2.1.8': RFC1213_MIB.egp,
'1.3.6.1.2.1.10': RFC1213_MIB.transmission,
'1.3.6.1.2.1.11': RFC1213_MIB.snmp,
'1.3.6.1.2.1.1.1': RFC1213_MIB.sysDescr,
'1.3.6.1.2.1.1.2': RFC1213_MIB.sysObjectID,
'1.3.6.1.2.1.1.3': RFC1213_MIB.sysUpTime,
'1.3.6.1.2.1.1.4': RFC1213_MIB.sysContact,
'1.3.6.1.2.1.1.5': RFC1213_MIB.sysName,
'1.3.6.1.2.1.1.6': RFC1213_MIB.sysLocation,
'1.3.6.1.2.1.1.7': RFC1213_MIB.sysServices,
'1.3.6.1.2.1.2.1': RFC1213_MIB.ifNumber,
'1.3.6.1.2.1.4.1': RFC1213_MIB.ipForwarding,
'1.3.6.1.2.1.4.2': RFC1213_MIB.ipDefaultTTL,
'1.3.6.1.2.1.4.3': RFC1213_MIB.ipInReceives,
'1.3.6.1.2.1.4.4': RFC1213_MIB.ipInHdrErrors,
'1.3.6.1.2.1.4.5': RFC1213_MIB.ipInAddrErrors,
'1.3.6.1.2.1.4.6': RFC1213_MIB.ipForwDatagrams,
'1.3.6.1.2.1.4.7': RFC1213_MIB.ipInUnknownProtos,
'1.3.6.1.2.1.4.8': RFC1213_MIB.ipInDiscards,
'1.3.6.1.2.1.4.9': RFC1213_MIB.ipInDelivers,
'1.3.6.1.2.1.4.10': RFC1213_MIB.ipOutRequests,
'1.3.6.1.2.1.4.11': RFC1213_MIB.ipOutDiscards,
'1.3.6.1.2.1.4.12': RFC1213_MIB.ipOutNoRoutes,
'1.3.6.1.2.1.4.13': RFC1213_MIB.ipReasmTimeout,
'1.3.6.1.2.1.4.14': RFC1213_MIB.ipReasmReqds,
'1.3.6.1.2.1.4.15': RFC1213_MIB.ipReasmOKs,
'1.3.6.1.2.1.4.16': RFC1213_MIB.ipReasmFails,
'1.3.6.1.2.1.4.17': RFC1213_MIB.ipFragOKs,
'1.3.6.1.2.1.4.18': RFC1213_MIB.ipFragFails,
'1.3.6.1.2.1.4.19': RFC1213_MIB.ipFragCreates,
'1.3.6.1.2.1.4.23': RFC1213_MIB.ipRoutingDiscards,
'1.3.6.1.2.1.5.1': RFC1213_MIB.icmpInMsgs,
'1.3.6.1.2.1.5.2': RFC1213_MIB.icmpInErrors,
'1.3.6.1.2.1.5.3': RFC1213_MIB.icmpInDestUnreachs,
'1.3.6.1.2.1.5.4': RFC1213_MIB.icmpInTimeExcds,
'1.3.6.1.2.1.5.5': RFC1213_MIB.icmpInParmProbs,
'1.3.6.1.2.1.5.6': RFC1213_MIB.icmpInSrcQuenchs,
'1.3.6.1.2.1.5.7': RFC1213_MIB.icmpInRedirects,
'1.3.6.1.2.1.5.8': RFC1213_MIB.icmpInEchos,
'1.3.6.1.2.1.5.9': RFC1213_MIB.icmpInEchoReps,
'1.3.6.1.2.1.5.10': RFC1213_MIB.icmpInTimestamps,
'1.3.6.1.2.1.5.11': RFC1213_MIB.icmpInTimestampReps,
'1.3.6.1.2.1.5.12': RFC1213_MIB.icmpInAddrMasks,
'1.3.6.1.2.1.5.13': RFC1213_MIB.icmpInAddrMaskReps,
'1.3.6.1.2.1.5.14': RFC1213_MIB.icmpOutMsgs,
'1.3.6.1.2.1.5.15': RFC1213_MIB.icmpOutErrors,
'1.3.6.1.2.1.5.16': RFC1213_MIB.icmpOutDestUnreachs,
'1.3.6.1.2.1.5.17': RFC1213_MIB.icmpOutTimeExcds,
'1.3.6.1.2.1.5.18': RFC1213_MIB.icmpOutParmProbs,
'1.3.6.1.2.1.5.19': RFC1213_MIB.icmpOutSrcQuenchs,
'1.3.6.1.2.1.5.20': RFC1213_MIB.icmpOutRedirects,
'1.3.6.1.2.1.5.21': RFC1213_MIB.icmpOutEchos,
'1.3.6.1.2.1.5.22': RFC1213_MIB.icmpOutEchoReps,
'1.3.6.1.2.1.5.23': RFC1213_MIB.icmpOutTimestamps,
'1.3.6.1.2.1.5.24': RFC1213_MIB.icmpOutTimestampReps,
'1.3.6.1.2.1.5.25': RFC1213_MIB.icmpOutAddrMasks,
'1.3.6.1.2.1.5.26': RFC1213_MIB.icmpOutAddrMaskReps,
'1.3.6.1.2.1.6.1': RFC1213_MIB.tcpRtoAlgorithm,
'1.3.6.1.2.1.6.2': RFC1213_MIB.tcpRtoMin,
'1.3.6.1.2.1.6.3': RFC1213_MIB.tcpRtoMax,
'1.3.6.1.2.1.6.4': RFC1213_MIB.tcpMaxConn,
'1.3.6.1.2.1.6.5': RFC1213_MIB.tcpActiveOpens,
'1.3.6.1.2.1.6.6': RFC1213_MIB.tcpPassiveOpens,
'1.3.6.1.2.1.6.7': RFC1213_MIB.tcpAttemptFails,
'1.3.6.1.2.1.6.8': RFC1213_MIB.tcpEstabResets,
'1.3.6.1.2.1.6.9': RFC1213_MIB.tcpCurrEstab,
'1.3.6.1.2.1.6.10': RFC1213_MIB.tcpInSegs,
'1.3.6.1.2.1.6.11': RFC1213_MIB.tcpOutSegs,
'1.3.6.1.2.1.6.12': RFC1213_MIB.tcpRetransSegs,
'1.3.6.1.2.1.6.14': RFC1213_MIB.tcpInErrs,
'1.3.6.1.2.1.6.15': RFC1213_MIB.tcpOutRsts,
'1.3.6.1.2.1.7.1': RFC1213_MIB.udpInDatagrams,
'1.3.6.1.2.1.7.2': RFC1213_MIB.udpNoPorts,
'1.3.6.1.2.1.7.3': RFC1213_MIB.udpInErrors,
'1.3.6.1.2.1.7.4': RFC1213_MIB.udpOutDatagrams,
'1.3.6.1.2.1.8.1': RFC1213_MIB.egpInMsgs,
'1.3.6.1.2.1.8.2': RFC1213_MIB.egpInErrors,
'1.3.6.1.2.1.8.3': RFC1213_MIB.egpOutMsgs,
'1.3.6.1.2.1.8.4': RFC1213_MIB.egpOutErrors,
'1.3.6.1.2.1.8.6': RFC1213_MIB.egpAs,
'1.3.6.1.2.1.11.1': RFC1213_MIB.snmpInPkts,
'1.3.6.1.2.1.11.2': RFC1213_MIB.snmpOutPkts,
'1.3.6.1.2.1.11.3': RFC1213_MIB.snmpInBadVersions,
'1.3.6.1.2.1.11.4': RFC1213_MIB.snmpInBadCommunityNames,
'1.3.6.1.2.1.11.5': RFC1213_MIB.snmpInBadCommunityUses,
'1.3.6.1.2.1.11.6': RFC1213_MIB.snmpInASNParseErrs,
'1.3.6.1.2.1.11.8': RFC1213_MIB.snmpInTooBigs,
'1.3.6.1.2.1.11.9': RFC1213_MIB.snmpInNoSuchNames,
'1.3.6.1.2.1.11.10': RFC1213_MIB.snmpInBadValues,
'1.3.6.1.2.1.11.11': RFC1213_MIB.snmpInReadOnlys,
'1.3.6.1.2.1.11.12': RFC1213_MIB.snmpInGenErrs,
'1.3.6.1.2.1.11.13': RFC1213_MIB.snmpInTotalReqVars,
'1.3.6.1.2.1.11.14': RFC1213_MIB.snmpInTotalSetVars,
'1.3.6.1.2.1.11.15': RFC1213_MIB.snmpInGetRequests,
'1.3.6.1.2.1.11.16': RFC1213_MIB.snmpInGetNexts,
'1.3.6.1.2.1.11.17': RFC1213_MIB.snmpInSetRequests,
'1.3.6.1.2.1.11.18': RFC1213_MIB.snmpInGetResponses,
'1.3.6.1.2.1.11.19': RFC1213_MIB.snmpInTraps,
'1.3.6.1.2.1.11.20': RFC1213_MIB.snmpOutTooBigs,
'1.3.6.1.2.1.11.21': RFC1213_MIB.snmpOutNoSuchNames,
'1.3.6.1.2.1.11.22': RFC1213_MIB.snmpOutBadValues,
'1.3.6.1.2.1.11.24': RFC1213_MIB.snmpOutGenErrs,
'1.3.6.1.2.1.11.25': RFC1213_MIB.snmpOutGetRequests,
'1.3.6.1.2.1.11.26': RFC1213_MIB.snmpOutGetNexts,
'1.3.6.1.2.1.11.27': RFC1213_MIB.snmpOutSetRequests,
'1.3.6.1.2.1.11.28': RFC1213_MIB.snmpOutGetResponses,
'1.3.6.1.2.1.11.29': RFC1213_MIB.snmpOutTraps,
'1.3.6.1.2.1.11.30': RFC1213_MIB.snmpEnableAuthenTraps,
'1.3.6.1.2.1.2.2.1.1': RFC1213_MIB.ifIndex,
'1.3.6.1.2.1.2.2.1.2': RFC1213_MIB.ifDescr,
'1.3.6.1.2.1.2.2.1.3': RFC1213_MIB.ifType,
'1.3.6.1.2.1.2.2.1.4': RFC1213_MIB.ifMtu,
'1.3.6.1.2.1.2.2.1.5': RFC1213_MIB.ifSpeed,
'1.3.6.1.2.1.2.2.1.6': RFC1213_MIB.ifPhysAddress,
'1.3.6.1.2.1.2.2.1.7': RFC1213_MIB.ifAdminStatus,
'1.3.6.1.2.1.2.2.1.8': RFC1213_MIB.ifOperStatus,
'1.3.6.1.2.1.2.2.1.9': RFC1213_MIB.ifLastChange,
'1.3.6.1.2.1.2.2.1.10': RFC1213_MIB.ifInOctets,
'1.3.6.1.2.1.2.2.1.11': RFC1213_MIB.ifInUcastPkts,
'1.3.6.1.2.1.2.2.1.12': RFC1213_MIB.ifInNUcastPkts,
'1.3.6.1.2.1.2.2.1.13': RFC1213_MIB.ifInDiscards,
'1.3.6.1.2.1.2.2.1.14': RFC1213_MIB.ifInErrors,
'1.3.6.1.2.1.2.2.1.15': RFC1213_MIB.ifInUnknownProtos,
'1.3.6.1.2.1.2.2.1.16': RFC1213_MIB.ifOutOctets,
'1.3.6.1.2.1.2.2.1.17': RFC1213_MIB.ifOutUcastPkts,
'1.3.6.1.2.1.2.2.1.18': RFC1213_MIB.ifOutNUcastPkts,
'1.3.6.1.2.1.2.2.1.19': RFC1213_MIB.ifOutDiscards,
'1.3.6.1.2.1.2.2.1.20': RFC1213_MIB.ifOutErrors,
'1.3.6.1.2.1.2.2.1.21': RFC1213_MIB.ifOutQLen,
'1.3.6.1.2.1.2.2.1.22': RFC1213_MIB.ifSpecific,
'1.3.6.1.2.1.3.1.1.1': RFC1213_MIB.atIfIndex,
'1.3.6.1.2.1.3.1.1.2': RFC1213_MIB.atPhysAddress,
'1.3.6.1.2.1.3.1.1.3': RFC1213_MIB.atNetAddress,
'1.3.6.1.2.1.4.20.1.1': RFC1213_MIB.ipAdEntAddr,
'1.3.6.1.2.1.4.20.1.2': RFC1213_MIB.ipAdEntIfIndex,
'1.3.6.1.2.1.4.20.1.3': RFC1213_MIB.ipAdEntNetMask,
'1.3.6.1.2.1.4.20.1.4': RFC1213_MIB.ipAdEntBcastAddr,
'1.3.6.1.2.1.4.20.1.5': RFC1213_MIB.ipAdEntReasmMaxSize,
'1.3.6.1.2.1.4.21.1.1': RFC1213_MIB.ipRouteDest,
'1.3.6.1.2.1.4.21.1.2': RFC1213_MIB.ipRouteIfIndex,
'1.3.6.1.2.1.4.21.1.3': RFC1213_MIB.ipRouteMetric1,
'1.3.6.1.2.1.4.21.1.4': RFC1213_MIB.ipRouteMetric2,
'1.3.6.1.2.1.4.21.1.5': RFC1213_MIB.ipRouteMetric3,
'1.3.6.1.2.1.4.21.1.6': RFC1213_MIB.ipRouteMetric4,
'1.3.6.1.2.1.4.21.1.7': RFC1213_MIB.ipRouteNextHop,
'1.3.6.1.2.1.4.21.1.8': RFC1213_MIB.ipRouteType,
'1.3.6.1.2.1.4.21.1.9': RFC1213_MIB.ipRouteProto,
'1.3.6.1.2.1.4.21.1.10': RFC1213_MIB.ipRouteAge,
'1.3.6.1.2.1.4.21.1.11': RFC1213_MIB.ipRouteMask,
'1.3.6.1.2.1.4.21.1.12': RFC1213_MIB.ipRouteMetric5,
'1.3.6.1.2.1.4.21.1.13': RFC1213_MIB.ipRouteInfo,
'1.3.6.1.2.1.4.22.1.1': RFC1213_MIB.ipNetToMediaIfIndex,
'1.3.6.1.2.1.4.22.1.2': RFC1213_MIB.ipNetToMediaPhysAddress,
'1.3.6.1.2.1.4.22.1.3': RFC1213_MIB.ipNetToMediaNetAddress,
'1.3.6.1.2.1.4.22.1.4': RFC1213_MIB.ipNetToMediaType,
'1.3.6.1.2.1.6.13.1.1': RFC1213_MIB.tcpConnState,
'1.3.6.1.2.1.6.13.1.2': RFC1213_MIB.tcpConnLocalAddress,
'1.3.6.1.2.1.6.13.1.3': RFC1213_MIB.tcpConnLocalPort,
'1.3.6.1.2.1.6.13.1.4': RFC1213_MIB.tcpConnRemAddress,
'1.3.6.1.2.1.6.13.1.5': RFC1213_MIB.tcpConnRemPort,
'1.3.6.1.2.1.7.5.1.1': RFC1213_MIB.udpLocalAddress,
'1.3.6.1.2.1.7.5.1.2': RFC1213_MIB.udpLocalPort,
'1.3.6.1.2.1.8.5.1.1': RFC1213_MIB.egpNeighState,
'1.3.6.1.2.1.8.5.1.2': RFC1213_MIB.egpNeighAddr,
'1.3.6.1.2.1.8.5.1.3': RFC1213_MIB.egpNeighAs,
'1.3.6.1.2.1.8.5.1.4': RFC1213_MIB.egpNeighInMsgs,
'1.3.6.1.2.1.8.5.1.5': RFC1213_MIB.egpNeighInErrs,
'1.3.6.1.2.1.8.5.1.6': RFC1213_MIB.egpNeighOutMsgs,
'1.3.6.1.2.1.8.5.1.7': RFC1213_MIB.egpNeighOutErrs,
'1.3.6.1.2.1.8.5.1.8': RFC1213_MIB.egpNeighInErrMsgs,
'1.3.6.1.2.1.8.5.1.9': RFC1213_MIB.egpNeighOutErrMsgs,
'1.3.6.1.2.1.8.5.1.10': RFC1213_MIB.egpNeighStateUps,
'1.3.6.1.2.1.8.5.1.11': RFC1213_MIB.egpNeighStateDowns,
'1.3.6.1.2.1.8.5.1.12': RFC1213_MIB.egpNeighIntervalHello,
'1.3.6.1.2.1.8.5.1.13': RFC1213_MIB.egpNeighIntervalPoll,
'1.3.6.1.2.1.8.5.1.14': RFC1213_MIB.egpNeighMode,
'1.3.6.1.2.1.8.5.1.15': RFC1213_MIB.egpNeighEventTrigger,
}