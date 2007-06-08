# python
# This file is generated by a program (mib2py). 

import ATM_MIB

OIDMAP = {
'1.3.6.1.2.1.37': ATM_MIB.atmMIB,
'1.3.6.1.2.1.37.1': ATM_MIB.atmMIBObjects,
'1.3.6.1.2.1.37.2': ATM_MIB.atmMIBConformance,
'1.3.6.1.2.1.37.2.1': ATM_MIB.atmMIBGroups,
'1.3.6.1.2.1.37.2.2': ATM_MIB.atmMIBCompliances,
'1.3.6.1.2.1.37.1.8': ATM_MIB.atmVpCrossConnectIndexNext,
'1.3.6.1.2.1.37.1.10': ATM_MIB.atmVcCrossConnectIndexNext,
'1.3.6.1.2.1.37.1.13': ATM_MIB.atmTrafficDescrParamIndexNext,
'1.3.6.1.2.1.37.1.2.1.1': ATM_MIB.atmInterfaceMaxVpcs,
'1.3.6.1.2.1.37.1.2.1.2': ATM_MIB.atmInterfaceMaxVccs,
'1.3.6.1.2.1.37.1.2.1.3': ATM_MIB.atmInterfaceConfVpcs,
'1.3.6.1.2.1.37.1.2.1.4': ATM_MIB.atmInterfaceConfVccs,
'1.3.6.1.2.1.37.1.2.1.5': ATM_MIB.atmInterfaceMaxActiveVpiBits,
'1.3.6.1.2.1.37.1.2.1.6': ATM_MIB.atmInterfaceMaxActiveVciBits,
'1.3.6.1.2.1.37.1.2.1.7': ATM_MIB.atmInterfaceIlmiVpi,
'1.3.6.1.2.1.37.1.2.1.8': ATM_MIB.atmInterfaceIlmiVci,
'1.3.6.1.2.1.37.1.2.1.9': ATM_MIB.atmInterfaceAddressType,
'1.3.6.1.2.1.37.1.2.1.10': ATM_MIB.atmInterfaceAdminAddress,
'1.3.6.1.2.1.37.1.2.1.11': ATM_MIB.atmInterfaceMyNeighborIpAddress,
'1.3.6.1.2.1.37.1.2.1.12': ATM_MIB.atmInterfaceMyNeighborIfName,
'1.3.6.1.2.1.37.1.2.1.13': ATM_MIB.atmInterfaceCurrentMaxVpiBits,
'1.3.6.1.2.1.37.1.2.1.14': ATM_MIB.atmInterfaceCurrentMaxVciBits,
'1.3.6.1.2.1.37.1.2.1.15': ATM_MIB.atmInterfaceSubscrAddress,
'1.3.6.1.2.1.37.1.3.1.1': ATM_MIB.atmInterfaceDs3PlcpSEFSs,
'1.3.6.1.2.1.37.1.3.1.2': ATM_MIB.atmInterfaceDs3PlcpAlarmState,
'1.3.6.1.2.1.37.1.3.1.3': ATM_MIB.atmInterfaceDs3PlcpUASs,
'1.3.6.1.2.1.37.1.4.1.1': ATM_MIB.atmInterfaceOCDEvents,
'1.3.6.1.2.1.37.1.4.1.2': ATM_MIB.atmInterfaceTCAlarmState,
'1.3.6.1.2.1.37.1.5.1.1': ATM_MIB.atmTrafficDescrParamIndex,
'1.3.6.1.2.1.37.1.5.1.2': ATM_MIB.atmTrafficDescrType,
'1.3.6.1.2.1.37.1.5.1.3': ATM_MIB.atmTrafficDescrParam1,
'1.3.6.1.2.1.37.1.5.1.4': ATM_MIB.atmTrafficDescrParam2,
'1.3.6.1.2.1.37.1.5.1.5': ATM_MIB.atmTrafficDescrParam3,
'1.3.6.1.2.1.37.1.5.1.6': ATM_MIB.atmTrafficDescrParam4,
'1.3.6.1.2.1.37.1.5.1.7': ATM_MIB.atmTrafficDescrParam5,
'1.3.6.1.2.1.37.1.5.1.8': ATM_MIB.atmTrafficQoSClass,
'1.3.6.1.2.1.37.1.5.1.9': ATM_MIB.atmTrafficDescrRowStatus,
'1.3.6.1.2.1.37.1.5.1.10': ATM_MIB.atmServiceCategory,
'1.3.6.1.2.1.37.1.5.1.11': ATM_MIB.atmTrafficFrameDiscard,
'1.3.6.1.2.1.37.1.6.1.1': ATM_MIB.atmVplVpi,
'1.3.6.1.2.1.37.1.6.1.2': ATM_MIB.atmVplAdminStatus,
'1.3.6.1.2.1.37.1.6.1.3': ATM_MIB.atmVplOperStatus,
'1.3.6.1.2.1.37.1.6.1.4': ATM_MIB.atmVplLastChange,
'1.3.6.1.2.1.37.1.6.1.5': ATM_MIB.atmVplReceiveTrafficDescrIndex,
'1.3.6.1.2.1.37.1.6.1.6': ATM_MIB.atmVplTransmitTrafficDescrIndex,
'1.3.6.1.2.1.37.1.6.1.7': ATM_MIB.atmVplCrossConnectIdentifier,
'1.3.6.1.2.1.37.1.6.1.8': ATM_MIB.atmVplRowStatus,
'1.3.6.1.2.1.37.1.6.1.9': ATM_MIB.atmVplCastType,
'1.3.6.1.2.1.37.1.6.1.10': ATM_MIB.atmVplConnKind,
'1.3.6.1.2.1.37.1.7.1.1': ATM_MIB.atmVclVpi,
'1.3.6.1.2.1.37.1.7.1.2': ATM_MIB.atmVclVci,
'1.3.6.1.2.1.37.1.7.1.3': ATM_MIB.atmVclAdminStatus,
'1.3.6.1.2.1.37.1.7.1.4': ATM_MIB.atmVclOperStatus,
'1.3.6.1.2.1.37.1.7.1.5': ATM_MIB.atmVclLastChange,
'1.3.6.1.2.1.37.1.7.1.6': ATM_MIB.atmVclReceiveTrafficDescrIndex,
'1.3.6.1.2.1.37.1.7.1.7': ATM_MIB.atmVclTransmitTrafficDescrIndex,
'1.3.6.1.2.1.37.1.7.1.8': ATM_MIB.atmVccAalType,
'1.3.6.1.2.1.37.1.7.1.9': ATM_MIB.atmVccAal5CpcsTransmitSduSize,
'1.3.6.1.2.1.37.1.7.1.10': ATM_MIB.atmVccAal5CpcsReceiveSduSize,
'1.3.6.1.2.1.37.1.7.1.11': ATM_MIB.atmVccAal5EncapsType,
'1.3.6.1.2.1.37.1.7.1.12': ATM_MIB.atmVclCrossConnectIdentifier,
'1.3.6.1.2.1.37.1.7.1.13': ATM_MIB.atmVclRowStatus,
'1.3.6.1.2.1.37.1.7.1.14': ATM_MIB.atmVclCastType,
'1.3.6.1.2.1.37.1.7.1.15': ATM_MIB.atmVclConnKind,
'1.3.6.1.2.1.37.1.9.1.1': ATM_MIB.atmVpCrossConnectIndex,
'1.3.6.1.2.1.37.1.9.1.2': ATM_MIB.atmVpCrossConnectLowIfIndex,
'1.3.6.1.2.1.37.1.9.1.3': ATM_MIB.atmVpCrossConnectLowVpi,
'1.3.6.1.2.1.37.1.9.1.4': ATM_MIB.atmVpCrossConnectHighIfIndex,
'1.3.6.1.2.1.37.1.9.1.5': ATM_MIB.atmVpCrossConnectHighVpi,
'1.3.6.1.2.1.37.1.9.1.6': ATM_MIB.atmVpCrossConnectAdminStatus,
'1.3.6.1.2.1.37.1.9.1.7': ATM_MIB.atmVpCrossConnectL2HOperStatus,
'1.3.6.1.2.1.37.1.9.1.8': ATM_MIB.atmVpCrossConnectH2LOperStatus,
'1.3.6.1.2.1.37.1.9.1.9': ATM_MIB.atmVpCrossConnectL2HLastChange,
'1.3.6.1.2.1.37.1.9.1.10': ATM_MIB.atmVpCrossConnectH2LLastChange,
'1.3.6.1.2.1.37.1.9.1.11': ATM_MIB.atmVpCrossConnectRowStatus,
'1.3.6.1.2.1.37.1.11.1.1': ATM_MIB.atmVcCrossConnectIndex,
'1.3.6.1.2.1.37.1.11.1.2': ATM_MIB.atmVcCrossConnectLowIfIndex,
'1.3.6.1.2.1.37.1.11.1.3': ATM_MIB.atmVcCrossConnectLowVpi,
'1.3.6.1.2.1.37.1.11.1.4': ATM_MIB.atmVcCrossConnectLowVci,
'1.3.6.1.2.1.37.1.11.1.5': ATM_MIB.atmVcCrossConnectHighIfIndex,
'1.3.6.1.2.1.37.1.11.1.6': ATM_MIB.atmVcCrossConnectHighVpi,
'1.3.6.1.2.1.37.1.11.1.7': ATM_MIB.atmVcCrossConnectHighVci,
'1.3.6.1.2.1.37.1.11.1.8': ATM_MIB.atmVcCrossConnectAdminStatus,
'1.3.6.1.2.1.37.1.11.1.9': ATM_MIB.atmVcCrossConnectL2HOperStatus,
'1.3.6.1.2.1.37.1.11.1.10': ATM_MIB.atmVcCrossConnectH2LOperStatus,
'1.3.6.1.2.1.37.1.11.1.11': ATM_MIB.atmVcCrossConnectL2HLastChange,
'1.3.6.1.2.1.37.1.11.1.12': ATM_MIB.atmVcCrossConnectH2LLastChange,
'1.3.6.1.2.1.37.1.11.1.13': ATM_MIB.atmVcCrossConnectRowStatus,
'1.3.6.1.2.1.37.1.12.1.1': ATM_MIB.aal5VccVpi,
'1.3.6.1.2.1.37.1.12.1.2': ATM_MIB.aal5VccVci,
'1.3.6.1.2.1.37.1.12.1.3': ATM_MIB.aal5VccCrcErrors,
'1.3.6.1.2.1.37.1.12.1.4': ATM_MIB.aal5VccSarTimeOuts,
'1.3.6.1.2.1.37.1.12.1.5': ATM_MIB.aal5VccOverSizedSDUs,
'1.3.6.1.2.1.37.2.1.1': ATM_MIB.atmInterfaceConfGroup,
'1.3.6.1.2.1.37.2.1.2': ATM_MIB.atmTrafficDescrGroup,
'1.3.6.1.2.1.37.2.1.3': ATM_MIB.atmInterfaceDs3PlcpGroup,
'1.3.6.1.2.1.37.2.1.4': ATM_MIB.atmInterfaceTCGroup,
'1.3.6.1.2.1.37.2.1.5': ATM_MIB.atmVpcTerminationGroup,
'1.3.6.1.2.1.37.2.1.6': ATM_MIB.atmVccTerminationGroup,
'1.3.6.1.2.1.37.2.1.7': ATM_MIB.atmVpCrossConnectGroup,
'1.3.6.1.2.1.37.2.1.8': ATM_MIB.atmVcCrossConnectGroup,
'1.3.6.1.2.1.37.2.1.9': ATM_MIB.aal5VccGroup,
'1.3.6.1.2.1.37.2.1.10': ATM_MIB.atmInterfaceConfGroup2,
'1.3.6.1.2.1.37.2.1.11': ATM_MIB.atmTrafficDescrGroup2,
'1.3.6.1.2.1.37.2.1.12': ATM_MIB.atmVpcTerminationGroup2,
'1.3.6.1.2.1.37.2.1.13': ATM_MIB.atmVccTerminationGroup2,
'1.3.6.1.2.1.37.2.1.14': ATM_MIB.atmVplCrossConnectGroup,
'1.3.6.1.2.1.37.2.1.15': ATM_MIB.atmVpPvcCrossConnectGroup,
'1.3.6.1.2.1.37.2.1.16': ATM_MIB.atmVclCrossConnectGroup,
'1.3.6.1.2.1.37.2.1.17': ATM_MIB.atmVcPvcCrossConnectGroup,
}