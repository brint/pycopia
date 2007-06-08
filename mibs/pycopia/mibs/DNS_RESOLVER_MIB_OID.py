# python
# This file is generated by a program (mib2py). 

import DNS_RESOLVER_MIB

OIDMAP = {
'1.3.6.1.2.1.32.2': DNS_RESOLVER_MIB.dnsResMIB,
'1.3.6.1.2.1.32.2.1': DNS_RESOLVER_MIB.dnsResMIBObjects,
'1.3.6.1.2.1.32.2.1.1': DNS_RESOLVER_MIB.dnsResConfig,
'1.3.6.1.2.1.32.2.1.2': DNS_RESOLVER_MIB.dnsResCounter,
'1.3.6.1.2.1.32.2.1.3': DNS_RESOLVER_MIB.dnsResLameDelegation,
'1.3.6.1.2.1.32.2.1.4': DNS_RESOLVER_MIB.dnsResCache,
'1.3.6.1.2.1.32.2.1.5': DNS_RESOLVER_MIB.dnsResNCache,
'1.3.6.1.2.1.32.2.1.6': DNS_RESOLVER_MIB.dnsResOptCounter,
'1.3.6.1.2.1.32.2.2': DNS_RESOLVER_MIB.dnsResMIBGroups,
'1.3.6.1.2.1.32.2.3': DNS_RESOLVER_MIB.dnsResMIBCompliances,
'1.3.6.1.2.1.32.2.1.1.1': DNS_RESOLVER_MIB.dnsResConfigImplementIdent,
'1.3.6.1.2.1.32.2.1.1.2': DNS_RESOLVER_MIB.dnsResConfigService,
'1.3.6.1.2.1.32.2.1.1.3': DNS_RESOLVER_MIB.dnsResConfigMaxCnames,
'1.3.6.1.2.1.32.2.1.1.5': DNS_RESOLVER_MIB.dnsResConfigUpTime,
'1.3.6.1.2.1.32.2.1.1.6': DNS_RESOLVER_MIB.dnsResConfigResetTime,
'1.3.6.1.2.1.32.2.1.1.7': DNS_RESOLVER_MIB.dnsResConfigReset,
'1.3.6.1.2.1.32.2.1.2.5': DNS_RESOLVER_MIB.dnsResCounterNonAuthDataResps,
'1.3.6.1.2.1.32.2.1.2.6': DNS_RESOLVER_MIB.dnsResCounterNonAuthNoDataResps,
'1.3.6.1.2.1.32.2.1.2.7': DNS_RESOLVER_MIB.dnsResCounterMartians,
'1.3.6.1.2.1.32.2.1.2.8': DNS_RESOLVER_MIB.dnsResCounterRecdResponses,
'1.3.6.1.2.1.32.2.1.2.9': DNS_RESOLVER_MIB.dnsResCounterUnparseResps,
'1.3.6.1.2.1.32.2.1.2.10': DNS_RESOLVER_MIB.dnsResCounterFallbacks,
'1.3.6.1.2.1.32.2.1.3.1': DNS_RESOLVER_MIB.dnsResLameDelegationOverflows,
'1.3.6.1.2.1.32.2.1.4.1': DNS_RESOLVER_MIB.dnsResCacheStatus,
'1.3.6.1.2.1.32.2.1.4.2': DNS_RESOLVER_MIB.dnsResCacheMaxTTL,
'1.3.6.1.2.1.32.2.1.4.3': DNS_RESOLVER_MIB.dnsResCacheGoodCaches,
'1.3.6.1.2.1.32.2.1.4.4': DNS_RESOLVER_MIB.dnsResCacheBadCaches,
'1.3.6.1.2.1.32.2.1.5.1': DNS_RESOLVER_MIB.dnsResNCacheStatus,
'1.3.6.1.2.1.32.2.1.5.2': DNS_RESOLVER_MIB.dnsResNCacheMaxTTL,
'1.3.6.1.2.1.32.2.1.5.3': DNS_RESOLVER_MIB.dnsResNCacheGoodNCaches,
'1.3.6.1.2.1.32.2.1.5.4': DNS_RESOLVER_MIB.dnsResNCacheBadNCaches,
'1.3.6.1.2.1.32.2.1.6.1': DNS_RESOLVER_MIB.dnsResOptCounterReferals,
'1.3.6.1.2.1.32.2.1.6.2': DNS_RESOLVER_MIB.dnsResOptCounterRetrans,
'1.3.6.1.2.1.32.2.1.6.3': DNS_RESOLVER_MIB.dnsResOptCounterNoResponses,
'1.3.6.1.2.1.32.2.1.6.4': DNS_RESOLVER_MIB.dnsResOptCounterRootRetrans,
'1.3.6.1.2.1.32.2.1.6.5': DNS_RESOLVER_MIB.dnsResOptCounterInternals,
'1.3.6.1.2.1.32.2.1.6.6': DNS_RESOLVER_MIB.dnsResOptCounterInternalTimeOuts,
'1.3.6.1.2.1.32.2.1.1.4.1.1': DNS_RESOLVER_MIB.dnsResConfigSbeltAddr,
'1.3.6.1.2.1.32.2.1.1.4.1.2': DNS_RESOLVER_MIB.dnsResConfigSbeltName,
'1.3.6.1.2.1.32.2.1.1.4.1.3': DNS_RESOLVER_MIB.dnsResConfigSbeltRecursion,
'1.3.6.1.2.1.32.2.1.1.4.1.4': DNS_RESOLVER_MIB.dnsResConfigSbeltPref,
'1.3.6.1.2.1.32.2.1.1.4.1.5': DNS_RESOLVER_MIB.dnsResConfigSbeltSubTree,
'1.3.6.1.2.1.32.2.1.1.4.1.6': DNS_RESOLVER_MIB.dnsResConfigSbeltClass,
'1.3.6.1.2.1.32.2.1.1.4.1.7': DNS_RESOLVER_MIB.dnsResConfigSbeltStatus,
'1.3.6.1.2.1.32.2.1.2.3.1.1': DNS_RESOLVER_MIB.dnsResCounterByOpcodeCode,
'1.3.6.1.2.1.32.2.1.2.3.1.2': DNS_RESOLVER_MIB.dnsResCounterByOpcodeQueries,
'1.3.6.1.2.1.32.2.1.2.3.1.3': DNS_RESOLVER_MIB.dnsResCounterByOpcodeResponses,
'1.3.6.1.2.1.32.2.1.2.4.1.1': DNS_RESOLVER_MIB.dnsResCounterByRcodeCode,
'1.3.6.1.2.1.32.2.1.2.4.1.2': DNS_RESOLVER_MIB.dnsResCounterByRcodeResponses,
'1.3.6.1.2.1.32.2.1.3.2.1.1': DNS_RESOLVER_MIB.dnsResLameDelegationSource,
'1.3.6.1.2.1.32.2.1.3.2.1.2': DNS_RESOLVER_MIB.dnsResLameDelegationName,
'1.3.6.1.2.1.32.2.1.3.2.1.3': DNS_RESOLVER_MIB.dnsResLameDelegationClass,
'1.3.6.1.2.1.32.2.1.3.2.1.4': DNS_RESOLVER_MIB.dnsResLameDelegationCounts,
'1.3.6.1.2.1.32.2.1.3.2.1.5': DNS_RESOLVER_MIB.dnsResLameDelegationStatus,
'1.3.6.1.2.1.32.2.1.4.5.1.1': DNS_RESOLVER_MIB.dnsResCacheRRName,
'1.3.6.1.2.1.32.2.1.4.5.1.2': DNS_RESOLVER_MIB.dnsResCacheRRClass,
'1.3.6.1.2.1.32.2.1.4.5.1.3': DNS_RESOLVER_MIB.dnsResCacheRRType,
'1.3.6.1.2.1.32.2.1.4.5.1.4': DNS_RESOLVER_MIB.dnsResCacheRRTTL,
'1.3.6.1.2.1.32.2.1.4.5.1.5': DNS_RESOLVER_MIB.dnsResCacheRRElapsedTTL,
'1.3.6.1.2.1.32.2.1.4.5.1.6': DNS_RESOLVER_MIB.dnsResCacheRRSource,
'1.3.6.1.2.1.32.2.1.4.5.1.7': DNS_RESOLVER_MIB.dnsResCacheRRData,
'1.3.6.1.2.1.32.2.1.4.5.1.8': DNS_RESOLVER_MIB.dnsResCacheRRStatus,
'1.3.6.1.2.1.32.2.1.4.5.1.9': DNS_RESOLVER_MIB.dnsResCacheRRIndex,
'1.3.6.1.2.1.32.2.1.4.5.1.10': DNS_RESOLVER_MIB.dnsResCacheRRPrettyName,
'1.3.6.1.2.1.32.2.1.5.5.1.1': DNS_RESOLVER_MIB.dnsResNCacheErrQName,
'1.3.6.1.2.1.32.2.1.5.5.1.2': DNS_RESOLVER_MIB.dnsResNCacheErrQClass,
'1.3.6.1.2.1.32.2.1.5.5.1.3': DNS_RESOLVER_MIB.dnsResNCacheErrQType,
'1.3.6.1.2.1.32.2.1.5.5.1.4': DNS_RESOLVER_MIB.dnsResNCacheErrTTL,
'1.3.6.1.2.1.32.2.1.5.5.1.5': DNS_RESOLVER_MIB.dnsResNCacheErrElapsedTTL,
'1.3.6.1.2.1.32.2.1.5.5.1.6': DNS_RESOLVER_MIB.dnsResNCacheErrSource,
'1.3.6.1.2.1.32.2.1.5.5.1.7': DNS_RESOLVER_MIB.dnsResNCacheErrCode,
'1.3.6.1.2.1.32.2.1.5.5.1.8': DNS_RESOLVER_MIB.dnsResNCacheErrStatus,
'1.3.6.1.2.1.32.2.1.5.5.1.9': DNS_RESOLVER_MIB.dnsResNCacheErrIndex,
'1.3.6.1.2.1.32.2.1.5.5.1.10': DNS_RESOLVER_MIB.dnsResNCacheErrPrettyName,
'1.3.6.1.2.1.32.2.2.1': DNS_RESOLVER_MIB.dnsResConfigGroup,
'1.3.6.1.2.1.32.2.2.2': DNS_RESOLVER_MIB.dnsResCounterGroup,
'1.3.6.1.2.1.32.2.2.3': DNS_RESOLVER_MIB.dnsResLameDelegationGroup,
'1.3.6.1.2.1.32.2.2.4': DNS_RESOLVER_MIB.dnsResCacheGroup,
'1.3.6.1.2.1.32.2.2.5': DNS_RESOLVER_MIB.dnsResNCacheGroup,
'1.3.6.1.2.1.32.2.2.6': DNS_RESOLVER_MIB.dnsResOptCounterGroup,
}