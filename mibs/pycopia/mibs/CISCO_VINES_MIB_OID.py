# python
# This file is generated by a program (mib2py). 

import CISCO_VINES_MIB

OIDMAP = {
'1.3.6.1.4.1.9.9.17': CISCO_VINES_MIB.ciscoVinesMIB,
'1.3.6.1.4.1.9.9.17.1': CISCO_VINES_MIB.ciscoVinesMIBObjects,
'1.3.6.1.4.1.9.9.17.1.1': CISCO_VINES_MIB.cvBasic,
'1.3.6.1.4.1.9.9.17.1.2': CISCO_VINES_MIB.cvForwarding,
'1.3.6.1.4.1.9.9.17.1.3': CISCO_VINES_MIB.cvTotal,
'1.3.6.1.4.1.9.9.17.1.4': CISCO_VINES_MIB.cvInterface,
'1.3.6.1.4.1.9.9.17.3': CISCO_VINES_MIB.ciscoVinesMIBConformance,
'1.3.6.1.4.1.9.9.17.3.1': CISCO_VINES_MIB.ciscoVinesMIBCompliances,
'1.3.6.1.4.1.9.9.17.3.2': CISCO_VINES_MIB.ciscoVinesMIBGroups,
'1.3.6.1.4.1.9.9.17.1.1.1': CISCO_VINES_MIB.cvBasicNetwork,
'1.3.6.1.4.1.9.9.17.1.1.2': CISCO_VINES_MIB.cvBasicHost,
'1.3.6.1.4.1.9.9.17.1.1.3': CISCO_VINES_MIB.cvBasicNextClient,
'1.3.6.1.4.1.9.9.17.1.2.1': CISCO_VINES_MIB.cvForwNeighborNeighborCount,
'1.3.6.1.4.1.9.9.17.1.2.2': CISCO_VINES_MIB.cvForwNeighborPathCount,
'1.3.6.1.4.1.9.9.17.1.2.3': CISCO_VINES_MIB.cvForwNeighborVersion,
'1.3.6.1.4.1.9.9.17.1.2.5': CISCO_VINES_MIB.cvForwRouteRouterCount,
'1.3.6.1.4.1.9.9.17.1.2.6': CISCO_VINES_MIB.cvForwRouteRouteCount,
'1.3.6.1.4.1.9.9.17.1.2.7': CISCO_VINES_MIB.cvForwRouteVersion,
'1.3.6.1.4.1.9.9.17.1.2.8': CISCO_VINES_MIB.cvForwRouteUpdateCountdown,
'1.3.6.1.4.1.9.9.17.1.3.1': CISCO_VINES_MIB.cvTotalInputPackets,
'1.3.6.1.4.1.9.9.17.1.3.2': CISCO_VINES_MIB.cvTotalOutputPackets,
'1.3.6.1.4.1.9.9.17.1.3.3': CISCO_VINES_MIB.cvTotalLocalDestPackets,
'1.3.6.1.4.1.9.9.17.1.3.4': CISCO_VINES_MIB.cvTotalForwardedPackets,
'1.3.6.1.4.1.9.9.17.1.3.5': CISCO_VINES_MIB.cvTotalBroadcastInPackets,
'1.3.6.1.4.1.9.9.17.1.3.6': CISCO_VINES_MIB.cvTotalBroadcastOutPackets,
'1.3.6.1.4.1.9.9.17.1.3.7': CISCO_VINES_MIB.cvTotalBroadcastForwardPackets,
'1.3.6.1.4.1.9.9.17.1.3.8': CISCO_VINES_MIB.cvTotalLanOnlyPackets,
'1.3.6.1.4.1.9.9.17.1.3.9': CISCO_VINES_MIB.cvTotalNotOver4800Packets,
'1.3.6.1.4.1.9.9.17.1.3.10': CISCO_VINES_MIB.cvTotalNoChargesPackets,
'1.3.6.1.4.1.9.9.17.1.3.11': CISCO_VINES_MIB.cvTotalFormatErrors,
'1.3.6.1.4.1.9.9.17.1.3.12': CISCO_VINES_MIB.cvTotalChecksumErrors,
'1.3.6.1.4.1.9.9.17.1.3.13': CISCO_VINES_MIB.cvTotalHopCountsExceeded,
'1.3.6.1.4.1.9.9.17.1.3.14': CISCO_VINES_MIB.cvTotalNoRouteDrops,
'1.3.6.1.4.1.9.9.17.1.3.15': CISCO_VINES_MIB.cvTotalEncapsFailedDrops,
'1.3.6.1.4.1.9.9.17.1.3.16': CISCO_VINES_MIB.cvTotalUnknownPackets,
'1.3.6.1.4.1.9.9.17.1.3.17': CISCO_VINES_MIB.cvTotalIcpInPackets,
'1.3.6.1.4.1.9.9.17.1.3.18': CISCO_VINES_MIB.cvTotalIcpOutPackets,
'1.3.6.1.4.1.9.9.17.1.3.19': CISCO_VINES_MIB.cvTotalMetricOutPackets,
'1.3.6.1.4.1.9.9.17.1.3.20': CISCO_VINES_MIB.cvTotalMacEchoInPackets,
'1.3.6.1.4.1.9.9.17.1.3.21': CISCO_VINES_MIB.cvTotalMacEchoOutPackets,
'1.3.6.1.4.1.9.9.17.1.3.22': CISCO_VINES_MIB.cvTotalEchoInPackets,
'1.3.6.1.4.1.9.9.17.1.3.23': CISCO_VINES_MIB.cvTotalEchoOutPackets,
'1.3.6.1.4.1.9.9.17.1.3.24': CISCO_VINES_MIB.cvTotalProxyOutPackets,
'1.3.6.1.4.1.9.9.17.1.3.25': CISCO_VINES_MIB.cvTotalProxyReplyOutPackets,
'1.3.6.1.4.1.9.9.17.1.2.4.1.1': CISCO_VINES_MIB.cvForwNeighborNetwork,
'1.3.6.1.4.1.9.9.17.1.2.4.1.2': CISCO_VINES_MIB.cvForwNeighborHost,
'1.3.6.1.4.1.9.9.17.1.2.4.1.3': CISCO_VINES_MIB.cvForwNeighborPhysAddress,
'1.3.6.1.4.1.9.9.17.1.2.4.1.4': CISCO_VINES_MIB.cvForwNeighborSource,
'1.3.6.1.4.1.9.9.17.1.2.4.1.5': CISCO_VINES_MIB.cvForwNeighborRtpVersion,
'1.3.6.1.4.1.9.9.17.1.2.4.1.6': CISCO_VINES_MIB.cvForwNeighborUsageType,
'1.3.6.1.4.1.9.9.17.1.2.4.1.7': CISCO_VINES_MIB.cvForwNeighborAge,
'1.3.6.1.4.1.9.9.17.1.2.4.1.8': CISCO_VINES_MIB.cvForwNeighborMetric,
'1.3.6.1.4.1.9.9.17.1.2.4.1.9': CISCO_VINES_MIB.cvForwNeighborUses,
'1.3.6.1.4.1.9.9.17.1.2.9.1.1': CISCO_VINES_MIB.cvForwRouteNetworkNumber,
'1.3.6.1.4.1.9.9.17.1.2.9.1.2': CISCO_VINES_MIB.cvForwRouteNeighborNetwork,
'1.3.6.1.4.1.9.9.17.1.2.9.1.3': CISCO_VINES_MIB.cvForwRouteSource,
'1.3.6.1.4.1.9.9.17.1.2.9.1.4': CISCO_VINES_MIB.cvForwRouteRtpVersion,
'1.3.6.1.4.1.9.9.17.1.2.9.1.5': CISCO_VINES_MIB.cvForwRouteUseNext,
'1.3.6.1.4.1.9.9.17.1.2.9.1.6': CISCO_VINES_MIB.cvForwRouteForwardBroadcast,
'1.3.6.1.4.1.9.9.17.1.2.9.1.7': CISCO_VINES_MIB.cvForwRouteSuppress,
'1.3.6.1.4.1.9.9.17.1.2.9.1.8': CISCO_VINES_MIB.cvForwRouteLoadShareEligible,
'1.3.6.1.4.1.9.9.17.1.2.9.1.9': CISCO_VINES_MIB.cvForwRouteAge,
'1.3.6.1.4.1.9.9.17.1.2.9.1.10': CISCO_VINES_MIB.cvForwRouteMetric,
'1.3.6.1.4.1.9.9.17.1.2.9.1.11': CISCO_VINES_MIB.cvForwRouteUses,
'1.3.6.1.4.1.9.9.17.1.4.1.1.1': CISCO_VINES_MIB.cvIfConfigMetric,
'1.3.6.1.4.1.9.9.17.1.4.1.1.2': CISCO_VINES_MIB.cvIfConfigEncapsulation,
'1.3.6.1.4.1.9.9.17.1.4.1.1.3': CISCO_VINES_MIB.cvIfConfigAccesslist,
'1.3.6.1.4.1.9.9.17.1.4.1.1.4': CISCO_VINES_MIB.cvIfConfigPropagate,
'1.3.6.1.4.1.9.9.17.1.4.1.1.5': CISCO_VINES_MIB.cvIfConfigArpEnabled,
'1.3.6.1.4.1.9.9.17.1.4.1.1.6': CISCO_VINES_MIB.cvIfConfigServerless,
'1.3.6.1.4.1.9.9.17.1.4.1.1.7': CISCO_VINES_MIB.cvIfConfigRedirectInterval,
'1.3.6.1.4.1.9.9.17.1.4.1.1.8': CISCO_VINES_MIB.cvIfConfigSplitDisabled,
'1.3.6.1.4.1.9.9.17.1.4.1.1.9': CISCO_VINES_MIB.cvIfConfigLineup,
'1.3.6.1.4.1.9.9.17.1.4.1.1.10': CISCO_VINES_MIB.cvIfConfigFastokay,
'1.3.6.1.4.1.9.9.17.1.4.1.1.11': CISCO_VINES_MIB.cvIfConfigRouteCache,
'1.3.6.1.4.1.9.9.17.1.4.1.1.12': CISCO_VINES_MIB.cvIfConfigInputRouterFilter,
'1.3.6.1.4.1.9.9.17.1.4.1.1.13': CISCO_VINES_MIB.cvIfConfigInputNetworkFilter,
'1.3.6.1.4.1.9.9.17.1.4.1.1.14': CISCO_VINES_MIB.cvIfConfigOutputNetworkFilter,
'1.3.6.1.4.1.9.9.17.1.4.2.1.1': CISCO_VINES_MIB.cvIfCountInNotEnabledDrops,
'1.3.6.1.4.1.9.9.17.1.4.2.1.2': CISCO_VINES_MIB.cvIfCountInFormatErrors,
'1.3.6.1.4.1.9.9.17.1.4.2.1.3': CISCO_VINES_MIB.cvIfCountInLocalDestPackets,
'1.3.6.1.4.1.9.9.17.1.4.2.1.4': CISCO_VINES_MIB.cvIfCountInBroadcastPackets,
'1.3.6.1.4.1.9.9.17.1.4.2.1.5': CISCO_VINES_MIB.cvIfCountInForwardedPackets,
'1.3.6.1.4.1.9.9.17.1.4.2.1.6': CISCO_VINES_MIB.cvIfCountInNoRouteDrops,
'1.3.6.1.4.1.9.9.17.1.4.2.1.7': CISCO_VINES_MIB.cvIfCountInZeroHopCountDrops,
'1.3.6.1.4.1.9.9.17.1.4.2.1.8': CISCO_VINES_MIB.cvIfCountInChecksumErrors,
'1.3.6.1.4.1.9.9.17.1.4.2.1.9': CISCO_VINES_MIB.cvIfCountInArpQueryRequests,
'1.3.6.1.4.1.9.9.17.1.4.2.1.10': CISCO_VINES_MIB.cvIfCountInArpQueryResponses,
'1.3.6.1.4.1.9.9.17.1.4.2.1.11': CISCO_VINES_MIB.cvIfCountInArpAssignmentRequests,
'1.3.6.1.4.1.9.9.17.1.4.2.1.12': CISCO_VINES_MIB.cvIfCountInArpAssignmentResponses,
'1.3.6.1.4.1.9.9.17.1.4.2.1.13': CISCO_VINES_MIB.cvIfCountInArpIllegalMessages,
'1.3.6.1.4.1.9.9.17.1.4.2.1.14': CISCO_VINES_MIB.cvIfCountInIcpErrorMessages,
'1.3.6.1.4.1.9.9.17.1.4.2.1.15': CISCO_VINES_MIB.cvIfCountInIcpMetricMessages,
'1.3.6.1.4.1.9.9.17.1.4.2.1.16': CISCO_VINES_MIB.cvIfCountInIcpIllegalMessages,
'1.3.6.1.4.1.9.9.17.1.4.2.1.17': CISCO_VINES_MIB.cvIfCountInIpcMessages,
'1.3.6.1.4.1.9.9.17.1.4.2.1.18': CISCO_VINES_MIB.cvIfCountInRtp0Messages,
'1.3.6.1.4.1.9.9.17.1.4.2.1.19': CISCO_VINES_MIB.cvIfCountInRtp1Messages,
'1.3.6.1.4.1.9.9.17.1.4.2.1.20': CISCO_VINES_MIB.cvIfCountInRtp2Messages,
'1.3.6.1.4.1.9.9.17.1.4.2.1.21': CISCO_VINES_MIB.cvIfCountInRtp3Messages,
'1.3.6.1.4.1.9.9.17.1.4.2.1.22': CISCO_VINES_MIB.cvIfCountInRtpUpdateMessages,
'1.3.6.1.4.1.9.9.17.1.4.2.1.23': CISCO_VINES_MIB.cvIfCountInRtpResponseMessages,
'1.3.6.1.4.1.9.9.17.1.4.2.1.24': CISCO_VINES_MIB.cvIfCountInRtpRedirectMessages,
'1.3.6.1.4.1.9.9.17.1.4.2.1.25': CISCO_VINES_MIB.cvIfCountInRtpIllegalMessages,
'1.3.6.1.4.1.9.9.17.1.4.2.1.26': CISCO_VINES_MIB.cvIfCountInSppMessages,
'1.3.6.1.4.1.9.9.17.1.4.2.1.27': CISCO_VINES_MIB.cvIfCountInIpUnknownProtocols,
'1.3.6.1.4.1.9.9.17.1.4.2.1.28': CISCO_VINES_MIB.cvIfCountInIpcUnknownPorts,
'1.3.6.1.4.1.9.9.17.1.4.2.1.29': CISCO_VINES_MIB.cvIfCountInBroadcastsHelpered,
'1.3.6.1.4.1.9.9.17.1.4.2.1.30': CISCO_VINES_MIB.cvIfCountInBroadcastsForwarded,
'1.3.6.1.4.1.9.9.17.1.4.2.1.31': CISCO_VINES_MIB.cvIfCountInBroadcastDuplicates,
'1.3.6.1.4.1.9.9.17.1.4.2.1.32': CISCO_VINES_MIB.cvIfCountInEchoPackets,
'1.3.6.1.4.1.9.9.17.1.4.2.1.33': CISCO_VINES_MIB.cvIfCountInMacEchoPackets,
'1.3.6.1.4.1.9.9.17.1.4.2.1.34': CISCO_VINES_MIB.cvIfCountInProxyReplyPackets,
'1.3.6.1.4.1.9.9.17.1.4.3.1.1': CISCO_VINES_MIB.cvIfCountOutUnicastPackets,
'1.3.6.1.4.1.9.9.17.1.4.3.1.2': CISCO_VINES_MIB.cvIfCountOutBroadcastPackets,
'1.3.6.1.4.1.9.9.17.1.4.3.1.3': CISCO_VINES_MIB.cvIfCountOutForwardedPackets,
'1.3.6.1.4.1.9.9.17.1.4.3.1.4': CISCO_VINES_MIB.cvIfCountOutEncapsulationFailures,
'1.3.6.1.4.1.9.9.17.1.4.3.1.5': CISCO_VINES_MIB.cvIfCountOutAccessFailures,
'1.3.6.1.4.1.9.9.17.1.4.3.1.6': CISCO_VINES_MIB.cvIfCountOutDownFailures,
'1.3.6.1.4.1.9.9.17.1.4.3.1.7': CISCO_VINES_MIB.cvIfCountOutPacketsNotBroadcastToSource,
'1.3.6.1.4.1.9.9.17.1.4.3.1.8': CISCO_VINES_MIB.cvIfCountOutPacketsNotBroadcastLanOnly,
'1.3.6.1.4.1.9.9.17.1.4.3.1.9': CISCO_VINES_MIB.cvIfCountOutPacketsNotBroadcastNotOver4800,
'1.3.6.1.4.1.9.9.17.1.4.3.1.10': CISCO_VINES_MIB.cvIfCountOutPacketsNotBroadcastNoCharge,
'1.3.6.1.4.1.9.9.17.1.4.3.1.11': CISCO_VINES_MIB.cvIfCountOutBroadcastsForwarded,
'1.3.6.1.4.1.9.9.17.1.4.3.1.12': CISCO_VINES_MIB.cvIfCountOutBroadcastsHelpered,
'1.3.6.1.4.1.9.9.17.1.4.3.1.13': CISCO_VINES_MIB.cvIfCountOutArpQueryRequests,
'1.3.6.1.4.1.9.9.17.1.4.3.1.14': CISCO_VINES_MIB.cvIfCountOutArpQueryResponses,
'1.3.6.1.4.1.9.9.17.1.4.3.1.15': CISCO_VINES_MIB.cvIfCountOutArpAssignmentRequests,
'1.3.6.1.4.1.9.9.17.1.4.3.1.16': CISCO_VINES_MIB.cvIfCountOutArpAssignmentResponses,
'1.3.6.1.4.1.9.9.17.1.4.3.1.17': CISCO_VINES_MIB.cvIfCountOutIcpErrorMessages,
'1.3.6.1.4.1.9.9.17.1.4.3.1.18': CISCO_VINES_MIB.cvIfCountOutIcpMetricMessages,
'1.3.6.1.4.1.9.9.17.1.4.3.1.19': CISCO_VINES_MIB.cvIfCountOutIpcMessages,
'1.3.6.1.4.1.9.9.17.1.4.3.1.20': CISCO_VINES_MIB.cvIfCountOutRtp0Messages,
'1.3.6.1.4.1.9.9.17.1.4.3.1.21': CISCO_VINES_MIB.cvIfCountOutRtpRequestMessages,
'1.3.6.1.4.1.9.9.17.1.4.3.1.22': CISCO_VINES_MIB.cvIfCountOutRtp2Messages,
'1.3.6.1.4.1.9.9.17.1.4.3.1.23': CISCO_VINES_MIB.cvIfCountOutRtp3Messages,
'1.3.6.1.4.1.9.9.17.1.4.3.1.24': CISCO_VINES_MIB.cvIfCountOutRtpUpdateMessages,
'1.3.6.1.4.1.9.9.17.1.4.3.1.25': CISCO_VINES_MIB.cvIfCountOutRtpResponseMessages,
'1.3.6.1.4.1.9.9.17.1.4.3.1.26': CISCO_VINES_MIB.cvIfCountOutRtpRedirectMessages,
'1.3.6.1.4.1.9.9.17.1.4.3.1.27': CISCO_VINES_MIB.cvIfCountOutSppMessages,
'1.3.6.1.4.1.9.9.17.1.4.3.1.28': CISCO_VINES_MIB.cvIfCountOutEchoPackets,
'1.3.6.1.4.1.9.9.17.1.4.3.1.29': CISCO_VINES_MIB.cvIfCountOutMacEchoPackets,
'1.3.6.1.4.1.9.9.17.1.4.3.1.30': CISCO_VINES_MIB.cvIfCountOutProxyPackets,
'1.3.6.1.4.1.9.9.17.3.2.1': CISCO_VINES_MIB.ciscoVinesMIBGroup,
}