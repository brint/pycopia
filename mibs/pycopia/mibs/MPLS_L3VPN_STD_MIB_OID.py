# python
# This file is generated by a program (mib2py). 

import MPLS_L3VPN_STD_MIB

OIDMAP = {
'1.3.6.1.2.1.10.166.11': MPLS_L3VPN_STD_MIB.mplsL3VpnMIB,
'1.3.6.1.2.1.10.166.11.0': MPLS_L3VPN_STD_MIB.mplsL3VpnNotifications,
'1.3.6.1.2.1.10.166.11.1': MPLS_L3VPN_STD_MIB.mplsL3VpnObjects,
'1.3.6.1.2.1.10.166.11.1.1': MPLS_L3VPN_STD_MIB.mplsL3VpnScalars,
'1.3.6.1.2.1.10.166.11.1.2': MPLS_L3VPN_STD_MIB.mplsL3VpnConf,
'1.3.6.1.2.1.10.166.11.1.3': MPLS_L3VPN_STD_MIB.mplsL3VpnPerf,
'1.3.6.1.2.1.10.166.11.1.4': MPLS_L3VPN_STD_MIB.mplsL3VpnRoute,
'1.3.6.1.2.1.10.166.11.2': MPLS_L3VPN_STD_MIB.mplsL3VpnConformance,
'1.3.6.1.2.1.10.166.11.2.1': MPLS_L3VPN_STD_MIB.mplsL3VpnGroups,
'1.3.6.1.2.1.10.166.11.2.2': MPLS_L3VPN_STD_MIB.mplsL3VpnCompliances,
'1.3.6.1.2.1.10.166.11.1.1.1': MPLS_L3VPN_STD_MIB.mplsL3VpnConfiguredVrfs,
'1.3.6.1.2.1.10.166.11.1.1.2': MPLS_L3VPN_STD_MIB.mplsL3VpnActiveVrfs,
'1.3.6.1.2.1.10.166.11.1.1.3': MPLS_L3VPN_STD_MIB.mplsL3VpnConnectedInterfaces,
'1.3.6.1.2.1.10.166.11.1.1.4': MPLS_L3VPN_STD_MIB.mplsL3VpnNotificationEnable,
'1.3.6.1.2.1.10.166.11.1.1.5': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfConfMaxPossRts,
'1.3.6.1.2.1.10.166.11.1.1.6': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfConfRteMxThrshTime,
'1.3.6.1.2.1.10.166.11.1.1.7': MPLS_L3VPN_STD_MIB.mplsL3VpnIllLblRcvThrsh,
'1.3.6.1.2.1.10.166.11.1.2.1.1.1': MPLS_L3VPN_STD_MIB.mplsL3VpnIfConfIndex,
'1.3.6.1.2.1.10.166.11.1.2.1.1.2': MPLS_L3VPN_STD_MIB.mplsL3VpnIfVpnClassification,
'1.3.6.1.2.1.10.166.11.1.2.1.1.3': MPLS_L3VPN_STD_MIB.mplsL3VpnIfVpnRouteDistProtocol,
'1.3.6.1.2.1.10.166.11.1.2.1.1.4': MPLS_L3VPN_STD_MIB.mplsL3VpnIfConfStorageType,
'1.3.6.1.2.1.10.166.11.1.2.1.1.5': MPLS_L3VPN_STD_MIB.mplsL3VpnIfConfRowStatus,
'1.3.6.1.2.1.10.166.11.1.2.2.1.1': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfName,
'1.3.6.1.2.1.10.166.11.1.2.2.1.2': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfVpnId,
'1.3.6.1.2.1.10.166.11.1.2.2.1.3': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfDescription,
'1.3.6.1.2.1.10.166.11.1.2.2.1.4': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRD,
'1.3.6.1.2.1.10.166.11.1.2.2.1.5': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfCreationTime,
'1.3.6.1.2.1.10.166.11.1.2.2.1.6': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfOperStatus,
'1.3.6.1.2.1.10.166.11.1.2.2.1.7': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfActiveInterfaces,
'1.3.6.1.2.1.10.166.11.1.2.2.1.8': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfAssociatedInterfaces,
'1.3.6.1.2.1.10.166.11.1.2.2.1.9': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfConfMidRteThresh,
'1.3.6.1.2.1.10.166.11.1.2.2.1.10': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfConfHighRteThresh,
'1.3.6.1.2.1.10.166.11.1.2.2.1.11': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfConfMaxRoutes,
'1.3.6.1.2.1.10.166.11.1.2.2.1.12': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfConfLastChanged,
'1.3.6.1.2.1.10.166.11.1.2.2.1.13': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfConfRowStatus,
'1.3.6.1.2.1.10.166.11.1.2.2.1.14': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfConfAdminStatus,
'1.3.6.1.2.1.10.166.11.1.2.2.1.15': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfConfStorageType,
'1.3.6.1.2.1.10.166.11.1.2.3.1.2': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRTIndex,
'1.3.6.1.2.1.10.166.11.1.2.3.1.3': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRTType,
'1.3.6.1.2.1.10.166.11.1.2.3.1.4': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRT,
'1.3.6.1.2.1.10.166.11.1.2.3.1.5': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRTDescr,
'1.3.6.1.2.1.10.166.11.1.2.3.1.6': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRTRowStatus,
'1.3.6.1.2.1.10.166.11.1.2.3.1.7': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRTStorageType,
'1.3.6.1.2.1.10.166.11.1.2.6.1.1': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfSecIllegalLblVltns,
'1.3.6.1.2.1.10.166.11.1.2.6.1.2': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfSecDiscontinuityTime,
'1.3.6.1.2.1.10.166.11.1.3.1.1.1': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfPerfRoutesAdded,
'1.3.6.1.2.1.10.166.11.1.3.1.1.2': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfPerfRoutesDeleted,
'1.3.6.1.2.1.10.166.11.1.3.1.1.3': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfPerfCurrNumRoutes,
'1.3.6.1.2.1.10.166.11.1.3.1.1.4': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfPerfRoutesDropped,
'1.3.6.1.2.1.10.166.11.1.3.1.1.5': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfPerfDiscTime,
'1.3.6.1.2.1.10.166.11.1.4.1.1.1': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrDestType,
'1.3.6.1.2.1.10.166.11.1.4.1.1.2': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrDest,
'1.3.6.1.2.1.10.166.11.1.4.1.1.3': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrPfxLen,
'1.3.6.1.2.1.10.166.11.1.4.1.1.4': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrPolicy,
'1.3.6.1.2.1.10.166.11.1.4.1.1.5': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrNHopType,
'1.3.6.1.2.1.10.166.11.1.4.1.1.6': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrNextHop,
'1.3.6.1.2.1.10.166.11.1.4.1.1.7': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrIfIndex,
'1.3.6.1.2.1.10.166.11.1.4.1.1.8': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrType,
'1.3.6.1.2.1.10.166.11.1.4.1.1.9': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrProto,
'1.3.6.1.2.1.10.166.11.1.4.1.1.10': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrAge,
'1.3.6.1.2.1.10.166.11.1.4.1.1.11': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrNextHopAS,
'1.3.6.1.2.1.10.166.11.1.4.1.1.12': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrMetric1,
'1.3.6.1.2.1.10.166.11.1.4.1.1.13': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrMetric2,
'1.3.6.1.2.1.10.166.11.1.4.1.1.14': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrMetric3,
'1.3.6.1.2.1.10.166.11.1.4.1.1.15': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrMetric4,
'1.3.6.1.2.1.10.166.11.1.4.1.1.16': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrMetric5,
'1.3.6.1.2.1.10.166.11.1.4.1.1.17': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteXCPointer,
'1.3.6.1.2.1.10.166.11.1.4.1.1.18': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteInetCidrStatus,
'1.3.6.1.2.1.10.166.11.0.1': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfUp,
'1.3.6.1.2.1.10.166.11.0.2': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfDown,
'1.3.6.1.2.1.10.166.11.0.3': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRouteMidThreshExceeded,
'1.3.6.1.2.1.10.166.11.0.4': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfNumVrfRouteMaxThreshExceeded,
'1.3.6.1.2.1.10.166.11.0.5': MPLS_L3VPN_STD_MIB.mplsL3VpnNumVrfSecIllglLblThrshExcd,
'1.3.6.1.2.1.10.166.11.0.6': MPLS_L3VPN_STD_MIB.mplsL3VpnNumVrfRouteMaxThreshCleared,
'1.3.6.1.2.1.10.166.11.2.1.1': MPLS_L3VPN_STD_MIB.mplsL3VpnScalarGroup,
'1.3.6.1.2.1.10.166.11.2.1.2': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfGroup,
'1.3.6.1.2.1.10.166.11.2.1.3': MPLS_L3VPN_STD_MIB.mplsL3VpnIfGroup,
'1.3.6.1.2.1.10.166.11.2.1.4': MPLS_L3VPN_STD_MIB.mplsL3VpnPerfGroup,
'1.3.6.1.2.1.10.166.11.2.1.5': MPLS_L3VPN_STD_MIB.mplsL3VpnPerfRouteGroup,
'1.3.6.1.2.1.10.166.11.2.1.7': MPLS_L3VPN_STD_MIB.mplsL3VpnSecGroup,
'1.3.6.1.2.1.10.166.11.2.1.8': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRteGroup,
'1.3.6.1.2.1.10.166.11.2.1.9': MPLS_L3VPN_STD_MIB.mplsL3VpnVrfRTGroup,
'1.3.6.1.2.1.10.166.11.2.1.10': MPLS_L3VPN_STD_MIB.mplsL3VpnNotificationGroup,
}