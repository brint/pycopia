# python
# This file is generated by a program (mib2py). 

import Cisco90Series_MIB

OIDMAP = {
'1.3.6.1.4.1.1570': Cisco90Series_MIB.ciscoTelesend,
'1.3.6.1.4.1.1570.1': Cisco90Series_MIB.frMux,
'1.3.6.1.4.1.1570.1.1': Cisco90Series_MIB.frxSys,
'1.3.6.1.4.1.1570.1.2': Cisco90Series_MIB.frxDefault,
'1.3.6.1.4.1.1570.1.3': Cisco90Series_MIB.frxBank,
'1.3.6.1.4.1.1570.1.4': Cisco90Series_MIB.frxChUnit,
'1.3.6.1.4.1.1570.1.5': Cisco90Series_MIB.frxMgt,
'1.3.6.1.4.1.1570.1.6': Cisco90Series_MIB.frxPort,
'1.3.6.1.4.1.1570.1.1.1': Cisco90Series_MIB.frxSysDescr,
'1.3.6.1.4.1.1570.1.1.2': Cisco90Series_MIB.frxClockHour,
'1.3.6.1.4.1.1570.1.1.3': Cisco90Series_MIB.frxClockMin,
'1.3.6.1.4.1.1570.1.1.4': Cisco90Series_MIB.frxClockSec,
'1.3.6.1.4.1.1570.1.1.5': Cisco90Series_MIB.frxUpTime,
'1.3.6.1.4.1.1570.1.1.6': Cisco90Series_MIB.frxAdminContact,
'1.3.6.1.4.1.1570.1.1.7': Cisco90Series_MIB.frxSysName,
'1.3.6.1.4.1.1570.1.1.8': Cisco90Series_MIB.frxSysLoc,
'1.3.6.1.4.1.1570.1.1.9': Cisco90Series_MIB.frxSysVersion,
'1.3.6.1.4.1.1570.1.1.10': Cisco90Series_MIB.frxUPerfTrapEnable,
'1.3.6.1.4.1.1570.1.1.11': Cisco90Series_MIB.frxAgtLinkErrors,
'1.3.6.1.4.1.1570.1.1.12': Cisco90Series_MIB.frxAgtProtErrors,
'1.3.6.1.4.1.1570.1.1.13': Cisco90Series_MIB.frxAgtChInactive,
'1.3.6.1.4.1.1570.1.1.14': Cisco90Series_MIB.frxAgtChStatus,
'1.3.6.1.4.1.1570.1.2.1': Cisco90Series_MIB.frxDefaultEnable,
'1.3.6.1.4.1.1570.1.2.2': Cisco90Series_MIB.frxDefaultTrap,
'1.3.6.1.4.1.1570.1.2.3': Cisco90Series_MIB.frxDConfigSrc,
'1.3.6.1.4.1.1570.1.2.4': Cisco90Series_MIB.frxDMgtT391,
'1.3.6.1.4.1.1570.1.2.5': Cisco90Series_MIB.frxDMgtT392,
'1.3.6.1.4.1.1570.1.2.6': Cisco90Series_MIB.frxDMgtN391,
'1.3.6.1.4.1.1570.1.2.7': Cisco90Series_MIB.frxDMgtN392,
'1.3.6.1.4.1.1570.1.2.8': Cisco90Series_MIB.frxDMgtN393,
'1.3.6.1.4.1.1570.1.2.9': Cisco90Series_MIB.frxDPortSpeed,
'1.3.6.1.4.1.1570.1.2.10': Cisco90Series_MIB.frxDPortProtocol,
'1.3.6.1.4.1.1570.1.2.11': Cisco90Series_MIB.frxDCktCIR,
'1.3.6.1.4.1.1570.1.2.12': Cisco90Series_MIB.frxDCktBc,
'1.3.6.1.4.1.1570.1.2.13': Cisco90Series_MIB.frxDCktBe,
'1.3.6.1.4.1.1570.1.3.1.1.1': Cisco90Series_MIB.frxBankIndex,
'1.3.6.1.4.1.1570.1.3.1.1.2': Cisco90Series_MIB.frxBankType,
'1.3.6.1.4.1.1570.1.4.1.1.1': Cisco90Series_MIB.frxChUIndex,
'1.3.6.1.4.1.1570.1.4.1.1.2': Cisco90Series_MIB.frxChUType,
'1.3.6.1.4.1.1570.1.4.1.1.3': Cisco90Series_MIB.frxChUVersion,
'1.3.6.1.4.1.1570.1.4.1.1.4': Cisco90Series_MIB.frxSigProtocol,
'1.3.6.1.4.1.1570.1.4.1.1.5': Cisco90Series_MIB.frxConfigSrc,
'1.3.6.1.4.1.1570.1.4.1.1.6': Cisco90Series_MIB.frxDLCIAdLen,
'1.3.6.1.4.1.1570.1.4.1.1.7': Cisco90Series_MIB.frxNetInOctets,
'1.3.6.1.4.1.1570.1.4.1.1.8': Cisco90Series_MIB.frxNetOutOctets,
'1.3.6.1.4.1.1570.1.4.1.1.9': Cisco90Series_MIB.frxNetBadFrames,
'1.3.6.1.4.1.1570.1.4.1.1.10': Cisco90Series_MIB.frxNetHDLCEs,
'1.3.6.1.4.1.1570.1.4.1.1.11': Cisco90Series_MIB.frxNetCRCEs,
'1.3.6.1.4.1.1570.1.4.1.1.12': Cisco90Series_MIB.frxNetLinkEs,
'1.3.6.1.4.1.1570.1.4.1.1.13': Cisco90Series_MIB.frxNetFrShEs,
'1.3.6.1.4.1.1570.1.4.1.1.14': Cisco90Series_MIB.frxNetFrLgEs,
'1.3.6.1.4.1.1570.1.4.1.1.15': Cisco90Series_MIB.frxNetPPPEs,
'1.3.6.1.4.1.1570.1.4.1.1.16': Cisco90Series_MIB.frxNetBufEs,
'1.3.6.1.4.1.1570.1.5.1.1.1': Cisco90Series_MIB.frxPortsInSvc,
'1.3.6.1.4.1.1570.1.5.1.1.2': Cisco90Series_MIB.frxMgtT391,
'1.3.6.1.4.1.1570.1.5.1.1.3': Cisco90Series_MIB.frxMgtT392,
'1.3.6.1.4.1.1570.1.5.1.1.4': Cisco90Series_MIB.frxMgtN391,
'1.3.6.1.4.1.1570.1.5.1.1.5': Cisco90Series_MIB.frxMgtN392,
'1.3.6.1.4.1.1570.1.5.1.1.6': Cisco90Series_MIB.frxMgtN393,
'1.3.6.1.4.1.1570.1.5.1.1.7': Cisco90Series_MIB.frxNetLinkErrors,
'1.3.6.1.4.1.1570.1.5.1.1.8': Cisco90Series_MIB.frxNetProtErrors,
'1.3.6.1.4.1.1570.1.5.1.1.9': Cisco90Series_MIB.frxNetChInactive,
'1.3.6.1.4.1.1570.1.5.1.1.10': Cisco90Series_MIB.frxNetChStatus,
'1.3.6.1.4.1.1570.1.5.2.1.1': Cisco90Series_MIB.frxPortIndex,
'1.3.6.1.4.1.1570.1.5.2.1.2': Cisco90Series_MIB.frxPortLinkErrors,
'1.3.6.1.4.1.1570.1.5.2.1.3': Cisco90Series_MIB.frxPortProtErrors,
'1.3.6.1.4.1.1570.1.5.2.1.4': Cisco90Series_MIB.frxPortChInactive,
'1.3.6.1.4.1.1570.1.6.1.1.1': Cisco90Series_MIB.frxPortSpeed,
'1.3.6.1.4.1.1570.1.6.1.1.2': Cisco90Series_MIB.frxPortProtocol,
'1.3.6.1.4.1.1570.1.6.1.1.3': Cisco90Series_MIB.frxDSLStatus,
'1.3.6.1.4.1.1570.1.6.1.1.4': Cisco90Series_MIB.frxPVCAssigned,
'1.3.6.1.4.1.1570.1.6.1.1.5': Cisco90Series_MIB.frxLastChange,
'1.3.6.1.4.1.1570.1.6.1.1.6': Cisco90Series_MIB.frxBrite,
'1.3.6.1.4.1.1570.1.6.1.1.7': Cisco90Series_MIB.frxDSLInOctets,
'1.3.6.1.4.1.1570.1.6.1.1.8': Cisco90Series_MIB.frxDSLOutOctets,
'1.3.6.1.4.1.1570.1.6.1.1.9': Cisco90Series_MIB.frxT1InOctets,
'1.3.6.1.4.1.1570.1.6.1.1.10': Cisco90Series_MIB.frxT1OutOctets,
'1.3.6.1.4.1.1570.1.6.1.1.11': Cisco90Series_MIB.frxDSLBadFrames,
'1.3.6.1.4.1.1570.1.6.1.1.12': Cisco90Series_MIB.frxDSLHDLCEs,
'1.3.6.1.4.1.1570.1.6.1.1.13': Cisco90Series_MIB.frxDSLCRCEs,
'1.3.6.1.4.1.1570.1.6.1.1.14': Cisco90Series_MIB.frxDSLLinkEs,
'1.3.6.1.4.1.1570.1.6.1.1.15': Cisco90Series_MIB.frxDSLFrShEs,
'1.3.6.1.4.1.1570.1.6.1.1.16': Cisco90Series_MIB.frxDSLFrLgEs,
'1.3.6.1.4.1.1570.1.6.1.1.17': Cisco90Series_MIB.frxDSLDLCIEs,
'1.3.6.1.4.1.1570.1.6.1.1.18': Cisco90Series_MIB.frxTxBuf,
'1.3.6.1.4.1.1570.1.6.1.1.19': Cisco90Series_MIB.frxRxBuf,
'1.3.6.1.4.1.1570.1.6.1.1.20': Cisco90Series_MIB.frxPortNetEs,
'1.3.6.1.4.1.1570.1.6.2.1.1': Cisco90Series_MIB.frxPvcIndex,
'1.3.6.1.4.1.1570.1.6.2.1.2': Cisco90Series_MIB.frxCktCIR,
'1.3.6.1.4.1.1570.1.6.2.1.3': Cisco90Series_MIB.frxCktBc,
'1.3.6.1.4.1.1570.1.6.2.1.4': Cisco90Series_MIB.frxCktBe,
'1.3.6.1.4.1.1570.1.6.2.1.5': Cisco90Series_MIB.frxFarEndOpStat,
'1.3.6.1.4.1.1570.1.6.2.1.6': Cisco90Series_MIB.frxCktInOctets,
'1.3.6.1.4.1.1570.1.6.2.1.7': Cisco90Series_MIB.frxCktOutOctets,
'1.3.6.1.4.1.1570.1.6.2.1.8': Cisco90Series_MIB.frxCktInFrames,
'1.3.6.1.4.1.1570.1.6.2.1.9': Cisco90Series_MIB.frxCktOutFrames,
'1.3.6.1.4.1.1570.1.6.2.1.10': Cisco90Series_MIB.frxCktDiscards,
'1.3.6.1.4.1.1570.1.6.3.1.1': Cisco90Series_MIB.frxTestPort,
'1.3.6.1.4.1.1570.1.6.3.1.2': Cisco90Series_MIB.frxTestType,
'1.3.6.1.4.1.1570.1.6.3.1.3': Cisco90Series_MIB.frxLoopLoc,
'1.3.6.1.4.1.1570.1.6.3.1.4': Cisco90Series_MIB.frxLoopCh,
'1.3.6.1.4.1.1570.1.6.3.1.5': Cisco90Series_MIB.frxStartTest,
'1.3.6.1.4.1.1570.1.6.3.1.6': Cisco90Series_MIB.frxBertRst,
'1.3.6.1.4.1.1570.1.6.3.1.7': Cisco90Series_MIB.frxBertBE,
'1.3.6.1.4.1.1570.1.6.3.1.8': Cisco90Series_MIB.frxBertTestTime,
'1.3.6.1.4.1.1570.1.6.3.1.9': Cisco90Series_MIB.frxTestInProg,
'1.3.6.1.4.1.1570.1.6.4.1.1': Cisco90Series_MIB.frxPAddrIndex,
'1.3.6.1.4.1.1570.1.6.4.1.2': Cisco90Series_MIB.frxChEsTh,
'1.3.6.1.4.1.1570.1.6.4.1.3': Cisco90Series_MIB.frxCdEsTh,
'1.3.6.1.4.1.1570.1.6.4.1.4': Cisco90Series_MIB.frxChSesTh,
'1.3.6.1.4.1.1570.1.6.4.1.5': Cisco90Series_MIB.frxCdSesTh,
'1.3.6.1.4.1.1570.1.6.4.1.6': Cisco90Series_MIB.frxAlertMask,
'1.3.6.1.4.1.1570.1.6.4.1.7': Cisco90Series_MIB.frxThCond,
'1.3.6.1.4.1.1570.1.6.5.1.1': Cisco90Series_MIB.frxResetPM,
'1.3.6.1.4.1.1570.1.6.5.1.2': Cisco90Series_MIB.frxPMtype,
'1.3.6.1.4.1.1570.1.6.5.1.3': Cisco90Series_MIB.frxChEsTx,
'1.3.6.1.4.1.1570.1.6.5.1.4': Cisco90Series_MIB.frxChEsRx,
'1.3.6.1.4.1.1570.1.6.5.1.5': Cisco90Series_MIB.frxPhEsTx,
'1.3.6.1.4.1.1570.1.6.5.1.6': Cisco90Series_MIB.frxPhEsRx,
'1.3.6.1.4.1.1570.1.6.5.1.7': Cisco90Series_MIB.frxH2EsTx,
'1.3.6.1.4.1.1570.1.6.5.1.8': Cisco90Series_MIB.frxH2EsRx,
'1.3.6.1.4.1.1570.1.6.5.1.9': Cisco90Series_MIB.frxH3EsTx,
'1.3.6.1.4.1.1570.1.6.5.1.10': Cisco90Series_MIB.frxH3EsRx,
'1.3.6.1.4.1.1570.1.6.5.1.11': Cisco90Series_MIB.frxH4EsTx,
'1.3.6.1.4.1.1570.1.6.5.1.12': Cisco90Series_MIB.frxH4EsRx,
'1.3.6.1.4.1.1570.1.6.5.1.13': Cisco90Series_MIB.frxH5EsTx,
'1.3.6.1.4.1.1570.1.6.5.1.14': Cisco90Series_MIB.frxH5EsRx,
'1.3.6.1.4.1.1570.1.6.5.1.15': Cisco90Series_MIB.frxH6EsTx,
'1.3.6.1.4.1.1570.1.6.5.1.16': Cisco90Series_MIB.frxH6EsRx,
'1.3.6.1.4.1.1570.1.6.5.1.17': Cisco90Series_MIB.frxH7EsTx,
'1.3.6.1.4.1.1570.1.6.5.1.18': Cisco90Series_MIB.frxH7EsRx,
'1.3.6.1.4.1.1570.1.6.5.1.19': Cisco90Series_MIB.frxH8EsTx,
'1.3.6.1.4.1.1570.1.6.5.1.20': Cisco90Series_MIB.frxH8EsRx,
'1.3.6.1.4.1.1570.1.6.5.1.21': Cisco90Series_MIB.frxCdEsTx,
'1.3.6.1.4.1.1570.1.6.5.1.22': Cisco90Series_MIB.frxCdEsRx,
'1.3.6.1.4.1.1570.1.6.5.1.23': Cisco90Series_MIB.frxPdEsTx,
'1.3.6.1.4.1.1570.1.6.5.1.24': Cisco90Series_MIB.frxPdEsRx,
'1.3.6.1.4.1.1570.1.6.5.1.25': Cisco90Series_MIB.frxChSesTx,
'1.3.6.1.4.1.1570.1.6.5.1.26': Cisco90Series_MIB.frxChSesRx,
'1.3.6.1.4.1.1570.1.6.5.1.27': Cisco90Series_MIB.frxPhSesTx,
'1.3.6.1.4.1.1570.1.6.5.1.28': Cisco90Series_MIB.frxPhSesRx,
'1.3.6.1.4.1.1570.1.6.5.1.29': Cisco90Series_MIB.frxCdSesTx,
'1.3.6.1.4.1.1570.1.6.5.1.30': Cisco90Series_MIB.frxCdSesRx,
'1.3.6.1.4.1.1570.1.6.5.1.31': Cisco90Series_MIB.frxPdSesTx,
'1.3.6.1.4.1.1570.1.6.5.1.32': Cisco90Series_MIB.frxPdSesRx,
'1.3.6.1.4.1.1570.1.6.5.1.33': Cisco90Series_MIB.frxChBeTx,
'1.3.6.1.4.1.1570.1.6.5.1.34': Cisco90Series_MIB.frxChBeRx,
'1.3.6.1.4.1.1570.1.6.5.1.35': Cisco90Series_MIB.frxPhBeTx,
'1.3.6.1.4.1.1570.1.6.5.1.36': Cisco90Series_MIB.frxPhBeRx,
'1.3.6.1.4.1.1570.1.0.1': Cisco90Series_MIB.frxDownloadTrap,
'1.3.6.1.4.1.1570.1.0.2': Cisco90Series_MIB.frxUPerfTrap,
'1.3.6.1.4.1.1570.1.0.3': Cisco90Series_MIB.frxInsertChUTrap,
'1.3.6.1.4.1.1570.1.0.4': Cisco90Series_MIB.frxRemoveChUTrap,
'1.3.6.1.4.1.1570.1.0.5': Cisco90Series_MIB.frxDConfigFailed,
}