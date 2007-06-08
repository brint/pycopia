# python
# This file is generated by a program (mib2py). 

import HP_SN_IPX_MIB

OIDMAP = {
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1': HP_SN_IPX_MIB.snIpxGen,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.2': HP_SN_IPX_MIB.snIpxCache,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.3': HP_SN_IPX_MIB.snIpxRoute,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.4': HP_SN_IPX_MIB.snIpxServer,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.5': HP_SN_IPX_MIB.snIpxFwdFilter,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.6': HP_SN_IPX_MIB.snIpxRipFilter,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.7': HP_SN_IPX_MIB.snIpxSapFilter,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.8': HP_SN_IPX_MIB.snIpxIfFwdAccess,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.9': HP_SN_IPX_MIB.snIpxIfRipAccess,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.10': HP_SN_IPX_MIB.snIpxIfSapAccess,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.11': HP_SN_IPX_MIB.snIpxPortAddr,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.12': HP_SN_IPX_MIB.snIpxPortCounters,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1.1': HP_SN_IPX_MIB.snIpxRoutingMode,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1.2': HP_SN_IPX_MIB.snIpxNetBiosFilterMode,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1.3': HP_SN_IPX_MIB.snIpxClearCache,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1.4': HP_SN_IPX_MIB.snIpxClearRoute,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1.5': HP_SN_IPX_MIB.snIpxClearTrafficCnts,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1.6': HP_SN_IPX_MIB.snIpxRcvPktsCnt,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1.7': HP_SN_IPX_MIB.snIpxTxPktsCnt,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1.8': HP_SN_IPX_MIB.snIpxFwdPktsCnt,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1.9': HP_SN_IPX_MIB.snIpxRcvDropPktsCnt,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1.10': HP_SN_IPX_MIB.snIpxRcvFiltPktsCnt,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1.11': HP_SN_IPX_MIB.snIpxRipGblFiltList,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1.12': HP_SN_IPX_MIB.snIpxRipFiltOnAllPort,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1.13': HP_SN_IPX_MIB.snIpxSapGblFiltList,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1.14': HP_SN_IPX_MIB.snIpxSapFiltOnAllPort,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1.15': HP_SN_IPX_MIB.snIpxTxDropPktsCnt,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.1.16': HP_SN_IPX_MIB.snIpxTxFiltPktsCnt,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.2.1.1.1': HP_SN_IPX_MIB.snIpxCacheIndex,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.2.1.1.2': HP_SN_IPX_MIB.snIpxCacheNetNum,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.2.1.1.3': HP_SN_IPX_MIB.snIpxCacheNode,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.2.1.1.4': HP_SN_IPX_MIB.snIpxCacheOutFilter,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.2.1.1.5': HP_SN_IPX_MIB.snIpxCacheEncap,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.2.1.1.6': HP_SN_IPX_MIB.snIpxCachePort,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.3.1.1.1': HP_SN_IPX_MIB.snIpxRouteIndex,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.3.1.1.2': HP_SN_IPX_MIB.snIpxDestNetNum,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.3.1.1.3': HP_SN_IPX_MIB.snIpxFwdRouterNode,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.3.1.1.4': HP_SN_IPX_MIB.snIpxDestHopCnts,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.3.1.1.5': HP_SN_IPX_MIB.snIpxRouteMetric,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.3.1.1.6': HP_SN_IPX_MIB.snIpxDestPort,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.4.1.1.1': HP_SN_IPX_MIB.snIpxServerIndex,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.4.1.1.2': HP_SN_IPX_MIB.snIpxServerType,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.4.1.1.3': HP_SN_IPX_MIB.snIpxServerNetNum,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.4.1.1.4': HP_SN_IPX_MIB.snIpxServerNode,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.4.1.1.5': HP_SN_IPX_MIB.snIpxServerSocket,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.4.1.1.6': HP_SN_IPX_MIB.snIpxServerHopCnts,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.4.1.1.7': HP_SN_IPX_MIB.snIpxServerName,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.5.1.1.1': HP_SN_IPX_MIB.snIpxFwdFilterId,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.5.1.1.2': HP_SN_IPX_MIB.snIpxFwdFilterAction,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.5.1.1.3': HP_SN_IPX_MIB.snIpxFwdFilterSocket,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.5.1.1.4': HP_SN_IPX_MIB.snIpxFwdFilterSrcNet,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.5.1.1.5': HP_SN_IPX_MIB.snIpxFwdFilterSrcNode,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.5.1.1.6': HP_SN_IPX_MIB.snIpxFwdFilterDestNet,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.5.1.1.7': HP_SN_IPX_MIB.snIpxFwdFilterDestNode,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.5.1.1.8': HP_SN_IPX_MIB.snIpxFwdFilterRowStatus,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.6.1.1.1': HP_SN_IPX_MIB.snIpxRipFilterId,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.6.1.1.2': HP_SN_IPX_MIB.snIpxRipFilterAction,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.6.1.1.3': HP_SN_IPX_MIB.snIpxRipFilterNet,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.6.1.1.4': HP_SN_IPX_MIB.snIpxRipFilterMask,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.6.1.1.5': HP_SN_IPX_MIB.snIpxRipFilterRowStatus,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.7.1.1.1': HP_SN_IPX_MIB.snIpxSapFilterId,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.7.1.1.2': HP_SN_IPX_MIB.snIpxSapFilterAction,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.7.1.1.3': HP_SN_IPX_MIB.snIpxSapFilterType,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.7.1.1.4': HP_SN_IPX_MIB.snIpxSapFilterName,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.7.1.1.5': HP_SN_IPX_MIB.snIpxSapFilterRowStatus,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.8.1.1.1': HP_SN_IPX_MIB.snIpxIfFwdAccessPort,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.8.1.1.2': HP_SN_IPX_MIB.snIpxIfFwdAccessDir,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.8.1.1.3': HP_SN_IPX_MIB.snIpxIfFwdAccessFilterList,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.8.1.1.4': HP_SN_IPX_MIB.snIpxIfFwdAccessRowStatus,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.9.1.1.1': HP_SN_IPX_MIB.snIpxIfRipAccessPort,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.9.1.1.2': HP_SN_IPX_MIB.snIpxIfRipAccessDir,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.9.1.1.3': HP_SN_IPX_MIB.snIpxIfRipAccessFilterList,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.9.1.1.4': HP_SN_IPX_MIB.snIpxIfRipAccessRowStatus,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.10.1.1.1': HP_SN_IPX_MIB.snIpxIfSapAccessPort,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.10.1.1.2': HP_SN_IPX_MIB.snIpxIfSapAccessDir,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.10.1.1.3': HP_SN_IPX_MIB.snIpxIfSapAccessFilterList,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.10.1.1.4': HP_SN_IPX_MIB.snIpxIfSapAccessRowStatus,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.11.1.1.1': HP_SN_IPX_MIB.snIpxPortAddrPort,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.11.1.1.2': HP_SN_IPX_MIB.snIpxPortAddrEncap,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.11.1.1.3': HP_SN_IPX_MIB.snIpxPortAddrNetNum,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.11.1.1.4': HP_SN_IPX_MIB.snIpxPortAddrRowStatus,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.11.1.1.5': HP_SN_IPX_MIB.snIpxPortAddrNetBiosFilterMode,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.12.1.1.1': HP_SN_IPX_MIB.snIpxPortCountersPort,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.12.1.1.2': HP_SN_IPX_MIB.snIpxPortCountersRcvPktsCnt,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.12.1.1.3': HP_SN_IPX_MIB.snIpxPortCountersTxPktsCnt,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.12.1.1.4': HP_SN_IPX_MIB.snIpxPortCountersFwdPktsCnt,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.12.1.1.5': HP_SN_IPX_MIB.snIpxPortCountersRcvDropPktsCnt,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.12.1.1.6': HP_SN_IPX_MIB.snIpxPortCountersTxDropPktsCnt,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.12.1.1.7': HP_SN_IPX_MIB.snIpxPortCountersRcvFiltPktsCnt,
'1.3.6.1.4.1.11.2.3.7.11.12.2.1.12.1.1.8': HP_SN_IPX_MIB.snIpxPortCountersTxFiltPktsCnt,
}