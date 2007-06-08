# python
# This file is generated by a program (mib2py). 

import SNA_NAU_MIB

OIDMAP = {
'1.3.6.1.2.1.34': SNA_NAU_MIB.snanauMIB,
'1.3.6.1.2.1.34.1': SNA_NAU_MIB.snanauObjects,
'1.3.6.1.2.1.34.1.1': SNA_NAU_MIB.snaNode,
'1.3.6.1.2.1.34.1.1.10': SNA_NAU_MIB.snaNodeTraps,
'1.3.6.1.2.1.34.1.2': SNA_NAU_MIB.snaLu,
'1.3.6.1.2.1.34.1.2.5': SNA_NAU_MIB.snaLuTraps,
'1.3.6.1.2.1.34.1.3': SNA_NAU_MIB.snaMgtTools,
'1.3.6.1.2.1.34.2': SNA_NAU_MIB.snanauConformance,
'1.3.6.1.2.1.34.2.1': SNA_NAU_MIB.snanauCompliances,
'1.3.6.1.2.1.34.2.2': SNA_NAU_MIB.snanauGroups,
'1.3.6.1.2.1.34.1.1.2': SNA_NAU_MIB.snaNodeAdminTableLastChange,
'1.3.6.1.2.1.34.1.1.4': SNA_NAU_MIB.snaNodeOperTableLastChange,
'1.3.6.1.2.1.34.1.1.7': SNA_NAU_MIB.snaNodeLinkAdminTableLastChange,
'1.3.6.1.2.1.34.1.1.9': SNA_NAU_MIB.snaNodeLinkOperTableLastChange,
'1.3.6.1.2.1.34.1.1.1.1.1': SNA_NAU_MIB.snaNodeAdminIndex,
'1.3.6.1.2.1.34.1.1.1.1.2': SNA_NAU_MIB.snaNodeAdminName,
'1.3.6.1.2.1.34.1.1.1.1.3': SNA_NAU_MIB.snaNodeAdminType,
'1.3.6.1.2.1.34.1.1.1.1.4': SNA_NAU_MIB.snaNodeAdminXidFormat,
'1.3.6.1.2.1.34.1.1.1.1.5': SNA_NAU_MIB.snaNodeAdminBlockNum,
'1.3.6.1.2.1.34.1.1.1.1.6': SNA_NAU_MIB.snaNodeAdminIdNum,
'1.3.6.1.2.1.34.1.1.1.1.7': SNA_NAU_MIB.snaNodeAdminEnablingMethod,
'1.3.6.1.2.1.34.1.1.1.1.8': SNA_NAU_MIB.snaNodeAdminLuTermDefault,
'1.3.6.1.2.1.34.1.1.1.1.9': SNA_NAU_MIB.snaNodeAdminMaxLu,
'1.3.6.1.2.1.34.1.1.1.1.10': SNA_NAU_MIB.snaNodeAdminHostDescription,
'1.3.6.1.2.1.34.1.1.1.1.11': SNA_NAU_MIB.snaNodeAdminStopMethod,
'1.3.6.1.2.1.34.1.1.1.1.12': SNA_NAU_MIB.snaNodeAdminState,
'1.3.6.1.2.1.34.1.1.1.1.13': SNA_NAU_MIB.snaNodeAdminRowStatus,
'1.3.6.1.2.1.34.1.1.3.1.1': SNA_NAU_MIB.snaNodeOperName,
'1.3.6.1.2.1.34.1.1.3.1.2': SNA_NAU_MIB.snaNodeOperType,
'1.3.6.1.2.1.34.1.1.3.1.3': SNA_NAU_MIB.snaNodeOperXidFormat,
'1.3.6.1.2.1.34.1.1.3.1.4': SNA_NAU_MIB.snaNodeOperBlockNum,
'1.3.6.1.2.1.34.1.1.3.1.5': SNA_NAU_MIB.snaNodeOperIdNum,
'1.3.6.1.2.1.34.1.1.3.1.6': SNA_NAU_MIB.snaNodeOperEnablingMethod,
'1.3.6.1.2.1.34.1.1.3.1.7': SNA_NAU_MIB.snaNodeOperLuTermDefault,
'1.3.6.1.2.1.34.1.1.3.1.8': SNA_NAU_MIB.snaNodeOperMaxLu,
'1.3.6.1.2.1.34.1.1.3.1.9': SNA_NAU_MIB.snaNodeOperHostDescription,
'1.3.6.1.2.1.34.1.1.3.1.10': SNA_NAU_MIB.snaNodeOperStopMethod,
'1.3.6.1.2.1.34.1.1.3.1.11': SNA_NAU_MIB.snaNodeOperState,
'1.3.6.1.2.1.34.1.1.3.1.12': SNA_NAU_MIB.snaNodeOperHostSscpId,
'1.3.6.1.2.1.34.1.1.3.1.13': SNA_NAU_MIB.snaNodeOperStartTime,
'1.3.6.1.2.1.34.1.1.3.1.14': SNA_NAU_MIB.snaNodeOperLastStateChange,
'1.3.6.1.2.1.34.1.1.3.1.15': SNA_NAU_MIB.snaNodeOperActFailures,
'1.3.6.1.2.1.34.1.1.3.1.16': SNA_NAU_MIB.snaNodeOperActFailureReason,
'1.3.6.1.2.1.34.1.1.5.1.1': SNA_NAU_MIB.snaPu20StatsSentBytes,
'1.3.6.1.2.1.34.1.1.5.1.2': SNA_NAU_MIB.snaPu20StatsReceivedBytes,
'1.3.6.1.2.1.34.1.1.5.1.3': SNA_NAU_MIB.snaPu20StatsSentPius,
'1.3.6.1.2.1.34.1.1.5.1.4': SNA_NAU_MIB.snaPu20StatsReceivedPius,
'1.3.6.1.2.1.34.1.1.5.1.5': SNA_NAU_MIB.snaPu20StatsSentNegativeResps,
'1.3.6.1.2.1.34.1.1.5.1.6': SNA_NAU_MIB.snaPu20StatsReceivedNegativeResps,
'1.3.6.1.2.1.34.1.1.5.1.7': SNA_NAU_MIB.snaPu20StatsActLus,
'1.3.6.1.2.1.34.1.1.5.1.8': SNA_NAU_MIB.snaPu20StatsInActLus,
'1.3.6.1.2.1.34.1.1.5.1.9': SNA_NAU_MIB.snaPu20StatsBindLus,
'1.3.6.1.2.1.34.1.1.6.1.1': SNA_NAU_MIB.snaNodeLinkAdminIndex,
'1.3.6.1.2.1.34.1.1.6.1.2': SNA_NAU_MIB.snaNodeLinkAdminSpecific,
'1.3.6.1.2.1.34.1.1.6.1.3': SNA_NAU_MIB.snaNodeLinkAdminMaxPiu,
'1.3.6.1.2.1.34.1.1.6.1.4': SNA_NAU_MIB.snaNodeLinkAdminRowStatus,
'1.3.6.1.2.1.34.1.1.8.1.1': SNA_NAU_MIB.snaNodeLinkOperSpecific,
'1.3.6.1.2.1.34.1.1.8.1.2': SNA_NAU_MIB.snaNodeLinkOperMaxPiu,
'1.3.6.1.2.1.34.1.2.1.1.1': SNA_NAU_MIB.snaLuAdminLuIndex,
'1.3.6.1.2.1.34.1.2.1.1.2': SNA_NAU_MIB.snaLuAdminName,
'1.3.6.1.2.1.34.1.2.1.1.3': SNA_NAU_MIB.snaLuAdminSnaName,
'1.3.6.1.2.1.34.1.2.1.1.4': SNA_NAU_MIB.snaLuAdminType,
'1.3.6.1.2.1.34.1.2.1.1.5': SNA_NAU_MIB.snaLuAdminDepType,
'1.3.6.1.2.1.34.1.2.1.1.6': SNA_NAU_MIB.snaLuAdminLocalAddress,
'1.3.6.1.2.1.34.1.2.1.1.7': SNA_NAU_MIB.snaLuAdminDisplayModel,
'1.3.6.1.2.1.34.1.2.1.1.8': SNA_NAU_MIB.snaLuAdminTerm,
'1.3.6.1.2.1.34.1.2.1.1.9': SNA_NAU_MIB.snaLuAdminRowStatus,
'1.3.6.1.2.1.34.1.2.2.1.1': SNA_NAU_MIB.snaLuOperName,
'1.3.6.1.2.1.34.1.2.2.1.2': SNA_NAU_MIB.snaLuOperSnaName,
'1.3.6.1.2.1.34.1.2.2.1.3': SNA_NAU_MIB.snaLuOperType,
'1.3.6.1.2.1.34.1.2.2.1.4': SNA_NAU_MIB.snaLuOperDepType,
'1.3.6.1.2.1.34.1.2.2.1.5': SNA_NAU_MIB.snaLuOperLocalAddress,
'1.3.6.1.2.1.34.1.2.2.1.6': SNA_NAU_MIB.snaLuOperDisplayModel,
'1.3.6.1.2.1.34.1.2.2.1.7': SNA_NAU_MIB.snaLuOperTerm,
'1.3.6.1.2.1.34.1.2.2.1.8': SNA_NAU_MIB.snaLuOperState,
'1.3.6.1.2.1.34.1.2.2.1.9': SNA_NAU_MIB.snaLuOperSessnCount,
'1.3.6.1.2.1.34.1.2.3.1.1': SNA_NAU_MIB.snaLuSessnRluIndex,
'1.3.6.1.2.1.34.1.2.3.1.2': SNA_NAU_MIB.snaLuSessnIndex,
'1.3.6.1.2.1.34.1.2.3.1.3': SNA_NAU_MIB.snaLuSessnLocalApplName,
'1.3.6.1.2.1.34.1.2.3.1.4': SNA_NAU_MIB.snaLuSessnRemoteLuName,
'1.3.6.1.2.1.34.1.2.3.1.5': SNA_NAU_MIB.snaLuSessnMaxSndRuSize,
'1.3.6.1.2.1.34.1.2.3.1.6': SNA_NAU_MIB.snaLuSessnMaxRcvRuSize,
'1.3.6.1.2.1.34.1.2.3.1.7': SNA_NAU_MIB.snaLuSessnSndPacingSize,
'1.3.6.1.2.1.34.1.2.3.1.8': SNA_NAU_MIB.snaLuSessnRcvPacingSize,
'1.3.6.1.2.1.34.1.2.3.1.9': SNA_NAU_MIB.snaLuSessnActiveTime,
'1.3.6.1.2.1.34.1.2.3.1.10': SNA_NAU_MIB.snaLuSessnAdminState,
'1.3.6.1.2.1.34.1.2.3.1.11': SNA_NAU_MIB.snaLuSessnOperState,
'1.3.6.1.2.1.34.1.2.3.1.12': SNA_NAU_MIB.snaLuSessnSenseData,
'1.3.6.1.2.1.34.1.2.3.1.13': SNA_NAU_MIB.snaLuSessnTerminationRu,
'1.3.6.1.2.1.34.1.2.3.1.14': SNA_NAU_MIB.snaLuSessnUnbindType,
'1.3.6.1.2.1.34.1.2.3.1.15': SNA_NAU_MIB.snaLuSessnLinkIndex,
'1.3.6.1.2.1.34.1.2.4.1.1': SNA_NAU_MIB.snaLuSessnStatsSentBytes,
'1.3.6.1.2.1.34.1.2.4.1.2': SNA_NAU_MIB.snaLuSessnStatsReceivedBytes,
'1.3.6.1.2.1.34.1.2.4.1.3': SNA_NAU_MIB.snaLuSessnStatsSentRus,
'1.3.6.1.2.1.34.1.2.4.1.4': SNA_NAU_MIB.snaLuSessnStatsReceivedRus,
'1.3.6.1.2.1.34.1.2.4.1.5': SNA_NAU_MIB.snaLuSessnStatsSentNegativeResps,
'1.3.6.1.2.1.34.1.2.4.1.6': SNA_NAU_MIB.snaLuSessnStatsReceivedNegativeResps,
'1.3.6.1.2.1.34.1.3.1.1.1': SNA_NAU_MIB.snaLuRtmPuIndex,
'1.3.6.1.2.1.34.1.3.1.1.2': SNA_NAU_MIB.snaLuRtmLuIndex,
'1.3.6.1.2.1.34.1.3.1.1.3': SNA_NAU_MIB.snaLuRtmState,
'1.3.6.1.2.1.34.1.3.1.1.4': SNA_NAU_MIB.snaLuRtmStateTime,
'1.3.6.1.2.1.34.1.3.1.1.5': SNA_NAU_MIB.snaLuRtmDef,
'1.3.6.1.2.1.34.1.3.1.1.6': SNA_NAU_MIB.snaLuRtmBoundary1,
'1.3.6.1.2.1.34.1.3.1.1.7': SNA_NAU_MIB.snaLuRtmBoundary2,
'1.3.6.1.2.1.34.1.3.1.1.8': SNA_NAU_MIB.snaLuRtmBoundary3,
'1.3.6.1.2.1.34.1.3.1.1.9': SNA_NAU_MIB.snaLuRtmBoundary4,
'1.3.6.1.2.1.34.1.3.1.1.10': SNA_NAU_MIB.snaLuRtmCounter1,
'1.3.6.1.2.1.34.1.3.1.1.11': SNA_NAU_MIB.snaLuRtmCounter2,
'1.3.6.1.2.1.34.1.3.1.1.12': SNA_NAU_MIB.snaLuRtmCounter3,
'1.3.6.1.2.1.34.1.3.1.1.13': SNA_NAU_MIB.snaLuRtmCounter4,
'1.3.6.1.2.1.34.1.3.1.1.14': SNA_NAU_MIB.snaLuRtmOverFlows,
'1.3.6.1.2.1.34.1.3.1.1.15': SNA_NAU_MIB.snaLuRtmObjPercent,
'1.3.6.1.2.1.34.1.3.1.1.16': SNA_NAU_MIB.snaLuRtmObjRange,
'1.3.6.1.2.1.34.1.3.1.1.17': SNA_NAU_MIB.snaLuRtmNumTrans,
'1.3.6.1.2.1.34.1.3.1.1.18': SNA_NAU_MIB.snaLuRtmLastRspTime,
'1.3.6.1.2.1.34.1.3.1.1.19': SNA_NAU_MIB.snaLuRtmAvgRspTime,
'1.3.6.1.2.1.34.1.1.10.1': SNA_NAU_MIB.snaNodeStateChangeTrap,
'1.3.6.1.2.1.34.1.1.10.2': SNA_NAU_MIB.snaNodeActFailTrap,
'1.3.6.1.2.1.34.1.2.5.1': SNA_NAU_MIB.snaLuStateChangeTrap,
'1.3.6.1.2.1.34.1.2.5.2': SNA_NAU_MIB.snaLuSessnBindFailTrap,
'1.3.6.1.2.1.34.2.2.1': SNA_NAU_MIB.snaNodeGroup,
'1.3.6.1.2.1.34.2.2.2': SNA_NAU_MIB.snaLuGroup,
'1.3.6.1.2.1.34.2.2.3': SNA_NAU_MIB.snaSessionGroup,
'1.3.6.1.2.1.34.2.2.4': SNA_NAU_MIB.snaPu20Group,
'1.3.6.1.2.1.34.2.2.5': SNA_NAU_MIB.snaMgtToolsRtmGroup,
}