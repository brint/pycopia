# python
# This file is generated by a program (mib2py). 

import NETSWITCH_DRIVERS_MIB

OIDMAP = {
'1.3.6.1.4.1.11': NETSWITCH_DRIVERS_MIB.hp,
'1.3.6.1.4.1.11.2': NETSWITCH_DRIVERS_MIB.nm,
'1.3.6.1.4.1.11.2.14': NETSWITCH_DRIVERS_MIB.icf,
'1.3.6.1.4.1.11.2.14.11': NETSWITCH_DRIVERS_MIB.hpicfObjects,
'1.3.6.1.4.1.11.2.14.11.5': NETSWITCH_DRIVERS_MIB.hpicfSwitch,
'1.3.6.1.4.1.11.2.14.11.5.1': NETSWITCH_DRIVERS_MIB.hpSwitch,
'1.3.6.1.4.1.11.2.14.11.5.1.1': NETSWITCH_DRIVERS_MIB.hpOpSystem,
'1.3.6.1.4.1.11.2.14.11.5.1.2': NETSWITCH_DRIVERS_MIB.hpHwSystem,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3': NETSWITCH_DRIVERS_MIB.hpDriverStats,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.1.1.1': NETSWITCH_DRIVERS_MIB.hpDriverStatsIndex,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.1.1.2': NETSWITCH_DRIVERS_MIB.hpDriverStatsType,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.1.1.3': NETSWITCH_DRIVERS_MIB.hpDriverStatsOctetsRxOk,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.1.1.4': NETSWITCH_DRIVERS_MIB.hpDriverStatsFrameRxOk,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.1.1.5': NETSWITCH_DRIVERS_MIB.hpDriverStatsTotalRxError,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.1.1.6': NETSWITCH_DRIVERS_MIB.hpDriverStatsOctetTxOk,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.1.1.7': NETSWITCH_DRIVERS_MIB.hpDriverStatsFrameTxOk,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.1.1.8': NETSWITCH_DRIVERS_MIB.hpDriverStatsTotalTxError,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.1.1.9': NETSWITCH_DRIVERS_MIB.hpDriverStatsOctetsRxPerSec,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.1.1.10': NETSWITCH_DRIVERS_MIB.hpDriverStatsPeakOctetsRx,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.1.1.11': NETSWITCH_DRIVERS_MIB.hpDriverStatsFramesRxPerSec,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.1.1.12': NETSWITCH_DRIVERS_MIB.hpDriverStatsPeakFramesRx,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.1.1.13': NETSWITCH_DRIVERS_MIB.hpDriverStatsOctetsTxPerSec,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.1.1.14': NETSWITCH_DRIVERS_MIB.hpDriverStatsPeakOctetsTx,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.1.1.15': NETSWITCH_DRIVERS_MIB.hpDriverStatsFramesTxPerSec,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.1.1.16': NETSWITCH_DRIVERS_MIB.hpDriverStatsPeakFramesTx,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.1': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsIndex,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.2': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsSMTOctetsRxOk,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.3': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsSMTFrameRxOk,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.4': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsSMTOctetsTxOk,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.5': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsSMTFrameTxOk,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.6': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsErrRxCRC,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.7': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsErrRxOverrun,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.8': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsErrRxParity,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.9': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsErrRxMACStatus,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.10': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsErrTxAbort,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.11': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsErrTxUnderrun,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.12': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsErrTxParity,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.13': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsErrGsrLlcTxRer,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.14': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsErrGsrLlcRxRer,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.15': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsErrGsrSMTTxRer,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.16': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsErrGsrSMTRxRer,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.17': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsErrGsrPortOp,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.18': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsErrGsrLlcRxRov,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.19': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsErrGsrSMTRxRov,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.20': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsErrGsrInternalOp,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.21': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsIoeMov,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.22': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsErrGsrHost,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.23': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsTxCongestion,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.24': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsMissedCmd,
'1.3.6.1.4.1.11.2.14.11.5.1.2.3.2.1.25': NETSWITCH_DRIVERS_MIB.hpFddiDriverStatsMissedCRF,
}