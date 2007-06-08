# python
# This file is generated by a program (mib2py). 

import MOBILEIPV6_MIB

OIDMAP = {
'1.3.6.1.2.1.133': MOBILEIPV6_MIB.mip6MIB,
'1.3.6.1.2.1.133.0': MOBILEIPV6_MIB.mip6Notifications,
'1.3.6.1.2.1.133.1': MOBILEIPV6_MIB.mip6Objects,
'1.3.6.1.2.1.133.1.1': MOBILEIPV6_MIB.mip6Core,
'1.3.6.1.2.1.133.1.1.1': MOBILEIPV6_MIB.mip6System,
'1.3.6.1.2.1.133.1.1.2': MOBILEIPV6_MIB.mip6Bindings,
'1.3.6.1.2.1.133.1.1.3': MOBILEIPV6_MIB.mip6Stats,
'1.3.6.1.2.1.133.1.1.3.1': MOBILEIPV6_MIB.mip6TotalTraffic,
'1.3.6.1.2.1.133.1.2': MOBILEIPV6_MIB.mip6Mn,
'1.3.6.1.2.1.133.1.2.1': MOBILEIPV6_MIB.mip6MnSystem,
'1.3.6.1.2.1.133.1.2.2': MOBILEIPV6_MIB.mip6MnConf,
'1.3.6.1.2.1.133.1.2.3': MOBILEIPV6_MIB.mip6MnRegistration,
'1.3.6.1.2.1.133.1.2.3.2': MOBILEIPV6_MIB.mip6MnRegnCounters,
'1.3.6.1.2.1.133.1.3': MOBILEIPV6_MIB.mip6Cn,
'1.3.6.1.2.1.133.1.3.1': MOBILEIPV6_MIB.mip6CnSystem,
'1.3.6.1.2.1.133.1.3.2': MOBILEIPV6_MIB.mip6CnStats,
'1.3.6.1.2.1.133.1.3.2.1': MOBILEIPV6_MIB.mip6CnGlobalStats,
'1.3.6.1.2.1.133.1.4': MOBILEIPV6_MIB.mip6Ha,
'1.3.6.1.2.1.133.1.4.1': MOBILEIPV6_MIB.mip6HaAdvertisement,
'1.3.6.1.2.1.133.1.4.2': MOBILEIPV6_MIB.mip6HaStats,
'1.3.6.1.2.1.133.1.4.2.1': MOBILEIPV6_MIB.mip6HaGlobalStats,
'1.3.6.1.2.1.133.2': MOBILEIPV6_MIB.mip6Conformance,
'1.3.6.1.2.1.133.2.1': MOBILEIPV6_MIB.mip6Groups,
'1.3.6.1.2.1.133.2.2': MOBILEIPV6_MIB.mip6Compliances,
'1.3.6.1.2.1.133.1.1.1.1': MOBILEIPV6_MIB.mip6Capabilities,
'1.3.6.1.2.1.133.1.1.1.2': MOBILEIPV6_MIB.mip6Status,
'1.3.6.1.2.1.133.1.1.3.1.1': MOBILEIPV6_MIB.mip6InOctets,
'1.3.6.1.2.1.133.1.1.3.1.2': MOBILEIPV6_MIB.mip6HCInOctets,
'1.3.6.1.2.1.133.1.1.3.1.3': MOBILEIPV6_MIB.mip6InPkts,
'1.3.6.1.2.1.133.1.1.3.1.4': MOBILEIPV6_MIB.mip6HCInPkts,
'1.3.6.1.2.1.133.1.1.3.1.5': MOBILEIPV6_MIB.mip6OutOctets,
'1.3.6.1.2.1.133.1.1.3.1.6': MOBILEIPV6_MIB.mip6HCOutOctets,
'1.3.6.1.2.1.133.1.1.3.1.7': MOBILEIPV6_MIB.mip6OutPkts,
'1.3.6.1.2.1.133.1.1.3.1.8': MOBILEIPV6_MIB.mip6HCOutPkts,
'1.3.6.1.2.1.133.1.1.3.1.9': MOBILEIPV6_MIB.mip6CounterDiscontinuityTime,
'1.3.6.1.2.1.133.1.2.2.1': MOBILEIPV6_MIB.mip6MnDiscoveryRequests,
'1.3.6.1.2.1.133.1.2.2.2': MOBILEIPV6_MIB.mip6MnDiscoveryReplies,
'1.3.6.1.2.1.133.1.2.2.3': MOBILEIPV6_MIB.mip6MnDiscoveryTimeouts,
'1.3.6.1.2.1.133.1.2.2.4': MOBILEIPV6_MIB.mip6MnPrefixSolicitationsSent,
'1.3.6.1.2.1.133.1.2.2.5': MOBILEIPV6_MIB.mip6MnPrefixAdvsRecd,
'1.3.6.1.2.1.133.1.2.2.6': MOBILEIPV6_MIB.mip6MnPrefixAdvsIgnored,
'1.3.6.1.2.1.133.1.2.2.7': MOBILEIPV6_MIB.mip6MnMovedToFN,
'1.3.6.1.2.1.133.1.2.2.8': MOBILEIPV6_MIB.mip6MnMovedToHN,
'1.3.6.1.2.1.133.1.2.3.2.1': MOBILEIPV6_MIB.mip6MnMobilityMessagesSent,
'1.3.6.1.2.1.133.1.2.3.2.2': MOBILEIPV6_MIB.mip6MnMobilityMessagesRecd,
'1.3.6.1.2.1.133.1.2.3.2.3': MOBILEIPV6_MIB.mip6MnBUsToHA,
'1.3.6.1.2.1.133.1.2.3.2.4': MOBILEIPV6_MIB.mip6MnBUAcksFromHA,
'1.3.6.1.2.1.133.1.2.3.2.5': MOBILEIPV6_MIB.mip6MnBUsToCN,
'1.3.6.1.2.1.133.1.2.3.2.6': MOBILEIPV6_MIB.mip6MnBUAcksFromCN,
'1.3.6.1.2.1.133.1.2.3.2.7': MOBILEIPV6_MIB.mip6MnBindingErrorsFromCN,
'1.3.6.1.2.1.133.1.2.3.2.8': MOBILEIPV6_MIB.mip6MnICMPErrorsRecd,
'1.3.6.1.2.1.133.1.2.3.2.9': MOBILEIPV6_MIB.mip6MnBRRequestsRecd,
'1.3.6.1.2.1.133.1.3.2.1.1': MOBILEIPV6_MIB.mip6CnHomeTestInitsRecd,
'1.3.6.1.2.1.133.1.3.2.1.2': MOBILEIPV6_MIB.mip6CnHomeTestsSent,
'1.3.6.1.2.1.133.1.3.2.1.3': MOBILEIPV6_MIB.mip6CnCareOfTestInitsRecd,
'1.3.6.1.2.1.133.1.3.2.1.4': MOBILEIPV6_MIB.mip6CnCareOfTestsSent,
'1.3.6.1.2.1.133.1.3.2.1.5': MOBILEIPV6_MIB.mip6CnBUsRecd,
'1.3.6.1.2.1.133.1.3.2.1.6': MOBILEIPV6_MIB.mip6CnBUAcksSent,
'1.3.6.1.2.1.133.1.3.2.1.7': MOBILEIPV6_MIB.mip6CnBRsSent,
'1.3.6.1.2.1.133.1.3.2.1.8': MOBILEIPV6_MIB.mip6CnBindingErrors,
'1.3.6.1.2.1.133.1.3.2.1.9': MOBILEIPV6_MIB.mip6CnBUsAccepted,
'1.3.6.1.2.1.133.1.3.2.1.10': MOBILEIPV6_MIB.mip6CnBUsRejected,
'1.3.6.1.2.1.133.1.3.2.1.11': MOBILEIPV6_MIB.mip6CnReasonUnspecified,
'1.3.6.1.2.1.133.1.3.2.1.12': MOBILEIPV6_MIB.mip6CnInsufficientResource,
'1.3.6.1.2.1.133.1.3.2.1.13': MOBILEIPV6_MIB.mip6CnHomeRegnNotSupported,
'1.3.6.1.2.1.133.1.3.2.1.14': MOBILEIPV6_MIB.mip6CnSeqNumberOutOfWindow,
'1.3.6.1.2.1.133.1.3.2.1.15': MOBILEIPV6_MIB.mip6CnExpiredHomeNonceIndex,
'1.3.6.1.2.1.133.1.3.2.1.16': MOBILEIPV6_MIB.mip6CnExpiredCareOfNonceIndex,
'1.3.6.1.2.1.133.1.3.2.1.17': MOBILEIPV6_MIB.mip6CnExpiredNonce,
'1.3.6.1.2.1.133.1.3.2.1.18': MOBILEIPV6_MIB.mip6CnRegTypeChangeDisallowed,
'1.3.6.1.2.1.133.1.4.1.1': MOBILEIPV6_MIB.mip6HaAdvsRecd,
'1.3.6.1.2.1.133.1.4.1.2': MOBILEIPV6_MIB.mip6HaAdvsSent,
'1.3.6.1.2.1.133.1.4.2.1.1': MOBILEIPV6_MIB.mip6HaHomeTestInitsRecd,
'1.3.6.1.2.1.133.1.4.2.1.2': MOBILEIPV6_MIB.mip6HaHomeTestsSent,
'1.3.6.1.2.1.133.1.4.2.1.3': MOBILEIPV6_MIB.mip6HaBUsRecd,
'1.3.6.1.2.1.133.1.4.2.1.4': MOBILEIPV6_MIB.mip6HaBUAcksSent,
'1.3.6.1.2.1.133.1.4.2.1.5': MOBILEIPV6_MIB.mip6HaBRAdviceSent,
'1.3.6.1.2.1.133.1.4.2.1.6': MOBILEIPV6_MIB.mip6HaBUsAccepted,
'1.3.6.1.2.1.133.1.4.2.1.7': MOBILEIPV6_MIB.mip6HaPrefDiscoverReqd,
'1.3.6.1.2.1.133.1.4.2.1.8': MOBILEIPV6_MIB.mip6HaReasonUnspecified,
'1.3.6.1.2.1.133.1.4.2.1.9': MOBILEIPV6_MIB.mip6HaAdmProhibited,
'1.3.6.1.2.1.133.1.4.2.1.10': MOBILEIPV6_MIB.mip6HaInsufficientResource,
'1.3.6.1.2.1.133.1.4.2.1.11': MOBILEIPV6_MIB.mip6HaHomeRegnNotSupported,
'1.3.6.1.2.1.133.1.4.2.1.12': MOBILEIPV6_MIB.mip6HaNotHomeSubnet,
'1.3.6.1.2.1.133.1.4.2.1.13': MOBILEIPV6_MIB.mip6HaNotHomeAgentForThisMN,
'1.3.6.1.2.1.133.1.4.2.1.14': MOBILEIPV6_MIB.mip6HaDupAddrDetectionFailed,
'1.3.6.1.2.1.133.1.4.2.1.15': MOBILEIPV6_MIB.mip6HaSeqNumberOutOfWindow,
'1.3.6.1.2.1.133.1.4.2.1.16': MOBILEIPV6_MIB.mip6HaExpiredHomeNonceIndex,
'1.3.6.1.2.1.133.1.4.2.1.17': MOBILEIPV6_MIB.mip6HaRegTypeChangeDisallowed,
'1.3.6.1.2.1.133.1.1.2.1.1.1': MOBILEIPV6_MIB.mip6BindingHomeAddressType,
'1.3.6.1.2.1.133.1.1.2.1.1.2': MOBILEIPV6_MIB.mip6BindingHomeAddress,
'1.3.6.1.2.1.133.1.1.2.1.1.3': MOBILEIPV6_MIB.mip6BindingCOAType,
'1.3.6.1.2.1.133.1.1.2.1.1.4': MOBILEIPV6_MIB.mip6BindingCOA,
'1.3.6.1.2.1.133.1.1.2.1.1.5': MOBILEIPV6_MIB.mip6BindingTimeRegistered,
'1.3.6.1.2.1.133.1.1.2.1.1.6': MOBILEIPV6_MIB.mip6BindingTimeGranted,
'1.3.6.1.2.1.133.1.1.2.1.1.7': MOBILEIPV6_MIB.mip6BindingTimeRemaining,
'1.3.6.1.2.1.133.1.1.2.1.1.8': MOBILEIPV6_MIB.mip6BindingHomeRegn,
'1.3.6.1.2.1.133.1.1.2.1.1.9': MOBILEIPV6_MIB.mip6BindingMaxSeq,
'1.3.6.1.2.1.133.1.1.2.1.1.10': MOBILEIPV6_MIB.mip6BindingUsageTS,
'1.3.6.1.2.1.133.1.1.2.1.1.11': MOBILEIPV6_MIB.mip6BindingUsageCount,
'1.3.6.1.2.1.133.1.1.2.1.1.12': MOBILEIPV6_MIB.mip6BindingAdminStatus,
'1.3.6.1.2.1.133.1.1.2.2.1.1': MOBILEIPV6_MIB.mip6BindingHstHomeAddressType,
'1.3.6.1.2.1.133.1.1.2.2.1.2': MOBILEIPV6_MIB.mip6BindingHstHomeAddress,
'1.3.6.1.2.1.133.1.1.2.2.1.3': MOBILEIPV6_MIB.mip6BindingHstIndex,
'1.3.6.1.2.1.133.1.1.2.2.1.4': MOBILEIPV6_MIB.mip6BindingHstCOAType,
'1.3.6.1.2.1.133.1.1.2.2.1.5': MOBILEIPV6_MIB.mip6BindingHstCOA,
'1.3.6.1.2.1.133.1.1.2.2.1.6': MOBILEIPV6_MIB.mip6BindingHstTimeRegistered,
'1.3.6.1.2.1.133.1.1.2.2.1.7': MOBILEIPV6_MIB.mip6BindingHstTimeExpired,
'1.3.6.1.2.1.133.1.1.2.2.1.8': MOBILEIPV6_MIB.mip6BindingHstHomeRegn,
'1.3.6.1.2.1.133.1.1.2.2.1.9': MOBILEIPV6_MIB.mip6BindingHstUsageTS,
'1.3.6.1.2.1.133.1.1.2.2.1.10': MOBILEIPV6_MIB.mip6BindingHstUsageCount,
'1.3.6.1.2.1.133.1.1.3.2.1.1': MOBILEIPV6_MIB.mip6NodeInOctets,
'1.3.6.1.2.1.133.1.1.3.2.1.2': MOBILEIPV6_MIB.mip6HCNodeInOctets,
'1.3.6.1.2.1.133.1.1.3.2.1.3': MOBILEIPV6_MIB.mip6NodeInPkts,
'1.3.6.1.2.1.133.1.1.3.2.1.4': MOBILEIPV6_MIB.mip6HCNodeInPkts,
'1.3.6.1.2.1.133.1.1.3.2.1.5': MOBILEIPV6_MIB.mip6NodeOutOctets,
'1.3.6.1.2.1.133.1.1.3.2.1.6': MOBILEIPV6_MIB.mip6HCNodeOutOctets,
'1.3.6.1.2.1.133.1.1.3.2.1.7': MOBILEIPV6_MIB.mip6NodeOutPkts,
'1.3.6.1.2.1.133.1.1.3.2.1.8': MOBILEIPV6_MIB.mip6HCNodeOutPkts,
'1.3.6.1.2.1.133.1.1.3.2.1.9': MOBILEIPV6_MIB.mip6NodeCtrDiscontinuityTime,
'1.3.6.1.2.1.133.1.2.1.1.1.1': MOBILEIPV6_MIB.mip6MnHomeAddressType,
'1.3.6.1.2.1.133.1.2.1.1.1.2': MOBILEIPV6_MIB.mip6MnHomeAddress,
'1.3.6.1.2.1.133.1.2.1.1.1.3': MOBILEIPV6_MIB.mip6MnHomeAddressState,
'1.3.6.1.2.1.133.1.2.3.1.1.1': MOBILEIPV6_MIB.mip6MnBLNodeAddressType,
'1.3.6.1.2.1.133.1.2.3.1.1.2': MOBILEIPV6_MIB.mip6MnBLNodeAddress,
'1.3.6.1.2.1.133.1.2.3.1.1.3': MOBILEIPV6_MIB.mip6MnBLCOAType,
'1.3.6.1.2.1.133.1.2.3.1.1.4': MOBILEIPV6_MIB.mip6MnBLCOA,
'1.3.6.1.2.1.133.1.2.3.1.1.5': MOBILEIPV6_MIB.mip6MnBLLifeTimeRequested,
'1.3.6.1.2.1.133.1.2.3.1.1.6': MOBILEIPV6_MIB.mip6MnBLLifeTimeGranted,
'1.3.6.1.2.1.133.1.2.3.1.1.7': MOBILEIPV6_MIB.mip6MnBLMaxSeq,
'1.3.6.1.2.1.133.1.2.3.1.1.8': MOBILEIPV6_MIB.mip6MnBLTimeSent,
'1.3.6.1.2.1.133.1.2.3.1.1.9': MOBILEIPV6_MIB.mip6MnBLAccepted,
'1.3.6.1.2.1.133.1.2.3.1.1.10': MOBILEIPV6_MIB.mip6MnBLAcceptedTime,
'1.3.6.1.2.1.133.1.2.3.1.1.11': MOBILEIPV6_MIB.mip6MnBLRetransmissions,
'1.3.6.1.2.1.133.1.2.3.1.1.12': MOBILEIPV6_MIB.mip6MnBLDontSendBUFlag,
'1.3.6.1.2.1.133.1.3.2.2.1.1': MOBILEIPV6_MIB.mip6CnBURequestsAccepted,
'1.3.6.1.2.1.133.1.3.2.2.1.2': MOBILEIPV6_MIB.mip6CnBURequestsRejected,
'1.3.6.1.2.1.133.1.3.2.2.1.3': MOBILEIPV6_MIB.mip6CnBCEntryCreationTime,
'1.3.6.1.2.1.133.1.3.2.2.1.4': MOBILEIPV6_MIB.mip6CnBUAcceptedTime,
'1.3.6.1.2.1.133.1.3.2.2.1.5': MOBILEIPV6_MIB.mip6CnBURejectionTime,
'1.3.6.1.2.1.133.1.3.2.2.1.6': MOBILEIPV6_MIB.mip6CnBURejectionCode,
'1.3.6.1.2.1.133.1.3.2.2.1.7': MOBILEIPV6_MIB.mip6CnCtrDiscontinuityTime,
'1.3.6.1.2.1.133.1.4.1.3.1.1': MOBILEIPV6_MIB.mip6HaAdvPreference,
'1.3.6.1.2.1.133.1.4.1.3.1.2': MOBILEIPV6_MIB.mip6HaAdvLifetime,
'1.3.6.1.2.1.133.1.4.1.3.1.3': MOBILEIPV6_MIB.mip6HaPrefixAdv,
'1.3.6.1.2.1.133.1.4.1.3.1.4': MOBILEIPV6_MIB.mip6HaPrefixSolicitation,
'1.3.6.1.2.1.133.1.4.1.3.1.5': MOBILEIPV6_MIB.mip6HaMCastCtlMsgSupport,
'1.3.6.1.2.1.133.1.4.1.4.1.1': MOBILEIPV6_MIB.mip6HaLinkLocalAddressType,
'1.3.6.1.2.1.133.1.4.1.4.1.2': MOBILEIPV6_MIB.mip6HaLinkLocalAddress,
'1.3.6.1.2.1.133.1.4.1.4.1.3': MOBILEIPV6_MIB.mip6HaPreference,
'1.3.6.1.2.1.133.1.4.1.4.1.4': MOBILEIPV6_MIB.mip6HaRecvLifeTime,
'1.3.6.1.2.1.133.1.4.1.4.1.5': MOBILEIPV6_MIB.mip6HaRecvTimeStamp,
'1.3.6.1.2.1.133.1.4.1.5.1.1': MOBILEIPV6_MIB.mip6HaGaAddrSeqNo,
'1.3.6.1.2.1.133.1.4.1.5.1.2': MOBILEIPV6_MIB.mip6HaGaGlobalAddressType,
'1.3.6.1.2.1.133.1.4.1.5.1.3': MOBILEIPV6_MIB.mip6HaGaGlobalAddress,
'1.3.6.1.2.1.133.1.4.2.2.1.1': MOBILEIPV6_MIB.mip6HaBURequestsAccepted,
'1.3.6.1.2.1.133.1.4.2.2.1.2': MOBILEIPV6_MIB.mip6HaBURequestsDenied,
'1.3.6.1.2.1.133.1.4.2.2.1.3': MOBILEIPV6_MIB.mip6HaBCEntryCreationTime,
'1.3.6.1.2.1.133.1.4.2.2.1.4': MOBILEIPV6_MIB.mip6HaBUAcceptedTime,
'1.3.6.1.2.1.133.1.4.2.2.1.5': MOBILEIPV6_MIB.mip6HaBURejectionTime,
'1.3.6.1.2.1.133.1.4.2.2.1.6': MOBILEIPV6_MIB.mip6HaRecentBURejectionCode,
'1.3.6.1.2.1.133.1.4.2.2.1.7': MOBILEIPV6_MIB.mip6HaCtrDiscontinuityTime,
'1.3.6.1.2.1.133.0.1': MOBILEIPV6_MIB.mip6MnRegistered,
'1.3.6.1.2.1.133.0.2': MOBILEIPV6_MIB.mip6MnDeRegistered,
'1.3.6.1.2.1.133.0.3': MOBILEIPV6_MIB.mip6MnCOAChanged,
'1.3.6.1.2.1.133.0.4': MOBILEIPV6_MIB.mip6MnBindingExpiredAtHA,
'1.3.6.1.2.1.133.0.5': MOBILEIPV6_MIB.mip6MnBindingExpiredAtCN,
'1.3.6.1.2.1.133.2.1.1': MOBILEIPV6_MIB.mip6SystemGroup,
'1.3.6.1.2.1.133.2.1.2': MOBILEIPV6_MIB.mip6BindingCacheGroup,
'1.3.6.1.2.1.133.2.1.3': MOBILEIPV6_MIB.mip6BindingHstGroup,
'1.3.6.1.2.1.133.2.1.4': MOBILEIPV6_MIB.mip6TotalTrafficGroup,
'1.3.6.1.2.1.133.2.1.5': MOBILEIPV6_MIB.mip6NodeTrafficGroup,
'1.3.6.1.2.1.133.2.1.6': MOBILEIPV6_MIB.mip6MnSystemGroup,
'1.3.6.1.2.1.133.2.1.7': MOBILEIPV6_MIB.mip6MnConfGroup,
'1.3.6.1.2.1.133.2.1.8': MOBILEIPV6_MIB.mip6MnRegistrationGroup,
'1.3.6.1.2.1.133.2.1.9': MOBILEIPV6_MIB.mip6CnStatsGroup,
'1.3.6.1.2.1.133.2.1.10': MOBILEIPV6_MIB.mip6HaSystemGroup,
'1.3.6.1.2.1.133.2.1.11': MOBILEIPV6_MIB.mip6HaListGroup,
'1.3.6.1.2.1.133.2.1.12': MOBILEIPV6_MIB.mip6HaStatsGroup,
'1.3.6.1.2.1.133.2.1.13': MOBILEIPV6_MIB.mip6CnGlobalStatsGroup,
'1.3.6.1.2.1.133.2.1.14': MOBILEIPV6_MIB.mip6HaGlobalStatsGroup,
'1.3.6.1.2.1.133.2.1.15': MOBILEIPV6_MIB.mip6BindingCacheCtlGroup,
'1.3.6.1.2.1.133.2.1.16': MOBILEIPV6_MIB.mip6NotificationGroup,
}