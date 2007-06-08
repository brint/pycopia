# python
# This file is generated by a program (mib2py). 

import DS3_MIB

OIDMAP = {
'1.3.6.1.2.1.10.30': DS3_MIB.ds3,
'1.3.6.1.2.1.10.30.14': DS3_MIB.ds3Conformance,
'1.3.6.1.2.1.10.30.14.1': DS3_MIB.ds3Groups,
'1.3.6.1.2.1.10.30.14.2': DS3_MIB.ds3Compliances,
'1.3.6.1.2.1.10.30.15': DS3_MIB.ds3Traps,
'1.3.6.1.2.1.10.30.5.1.1': DS3_MIB.dsx3LineIndex,
'1.3.6.1.2.1.10.30.5.1.2': DS3_MIB.dsx3IfIndex,
'1.3.6.1.2.1.10.30.5.1.3': DS3_MIB.dsx3TimeElapsed,
'1.3.6.1.2.1.10.30.5.1.4': DS3_MIB.dsx3ValidIntervals,
'1.3.6.1.2.1.10.30.5.1.5': DS3_MIB.dsx3LineType,
'1.3.6.1.2.1.10.30.5.1.6': DS3_MIB.dsx3LineCoding,
'1.3.6.1.2.1.10.30.5.1.7': DS3_MIB.dsx3SendCode,
'1.3.6.1.2.1.10.30.5.1.8': DS3_MIB.dsx3CircuitIdentifier,
'1.3.6.1.2.1.10.30.5.1.9': DS3_MIB.dsx3LoopbackConfig,
'1.3.6.1.2.1.10.30.5.1.10': DS3_MIB.dsx3LineStatus,
'1.3.6.1.2.1.10.30.5.1.11': DS3_MIB.dsx3TransmitClockSource,
'1.3.6.1.2.1.10.30.5.1.12': DS3_MIB.dsx3InvalidIntervals,
'1.3.6.1.2.1.10.30.5.1.13': DS3_MIB.dsx3LineLength,
'1.3.6.1.2.1.10.30.5.1.14': DS3_MIB.dsx3LineStatusLastChange,
'1.3.6.1.2.1.10.30.5.1.15': DS3_MIB.dsx3LineStatusChangeTrapEnable,
'1.3.6.1.2.1.10.30.5.1.16': DS3_MIB.dsx3LoopbackStatus,
'1.3.6.1.2.1.10.30.5.1.17': DS3_MIB.dsx3Channelization,
'1.3.6.1.2.1.10.30.5.1.18': DS3_MIB.dsx3Ds1ForRemoteLoop,
'1.3.6.1.2.1.10.30.6.1.1': DS3_MIB.dsx3CurrentIndex,
'1.3.6.1.2.1.10.30.6.1.2': DS3_MIB.dsx3CurrentPESs,
'1.3.6.1.2.1.10.30.6.1.3': DS3_MIB.dsx3CurrentPSESs,
'1.3.6.1.2.1.10.30.6.1.4': DS3_MIB.dsx3CurrentSEFSs,
'1.3.6.1.2.1.10.30.6.1.5': DS3_MIB.dsx3CurrentUASs,
'1.3.6.1.2.1.10.30.6.1.6': DS3_MIB.dsx3CurrentLCVs,
'1.3.6.1.2.1.10.30.6.1.7': DS3_MIB.dsx3CurrentPCVs,
'1.3.6.1.2.1.10.30.6.1.8': DS3_MIB.dsx3CurrentLESs,
'1.3.6.1.2.1.10.30.6.1.9': DS3_MIB.dsx3CurrentCCVs,
'1.3.6.1.2.1.10.30.6.1.10': DS3_MIB.dsx3CurrentCESs,
'1.3.6.1.2.1.10.30.6.1.11': DS3_MIB.dsx3CurrentCSESs,
'1.3.6.1.2.1.10.30.7.1.1': DS3_MIB.dsx3IntervalIndex,
'1.3.6.1.2.1.10.30.7.1.2': DS3_MIB.dsx3IntervalNumber,
'1.3.6.1.2.1.10.30.7.1.3': DS3_MIB.dsx3IntervalPESs,
'1.3.6.1.2.1.10.30.7.1.4': DS3_MIB.dsx3IntervalPSESs,
'1.3.6.1.2.1.10.30.7.1.5': DS3_MIB.dsx3IntervalSEFSs,
'1.3.6.1.2.1.10.30.7.1.6': DS3_MIB.dsx3IntervalUASs,
'1.3.6.1.2.1.10.30.7.1.7': DS3_MIB.dsx3IntervalLCVs,
'1.3.6.1.2.1.10.30.7.1.8': DS3_MIB.dsx3IntervalPCVs,
'1.3.6.1.2.1.10.30.7.1.9': DS3_MIB.dsx3IntervalLESs,
'1.3.6.1.2.1.10.30.7.1.10': DS3_MIB.dsx3IntervalCCVs,
'1.3.6.1.2.1.10.30.7.1.11': DS3_MIB.dsx3IntervalCESs,
'1.3.6.1.2.1.10.30.7.1.12': DS3_MIB.dsx3IntervalCSESs,
'1.3.6.1.2.1.10.30.7.1.13': DS3_MIB.dsx3IntervalValidData,
'1.3.6.1.2.1.10.30.8.1.1': DS3_MIB.dsx3TotalIndex,
'1.3.6.1.2.1.10.30.8.1.2': DS3_MIB.dsx3TotalPESs,
'1.3.6.1.2.1.10.30.8.1.3': DS3_MIB.dsx3TotalPSESs,
'1.3.6.1.2.1.10.30.8.1.4': DS3_MIB.dsx3TotalSEFSs,
'1.3.6.1.2.1.10.30.8.1.5': DS3_MIB.dsx3TotalUASs,
'1.3.6.1.2.1.10.30.8.1.6': DS3_MIB.dsx3TotalLCVs,
'1.3.6.1.2.1.10.30.8.1.7': DS3_MIB.dsx3TotalPCVs,
'1.3.6.1.2.1.10.30.8.1.8': DS3_MIB.dsx3TotalLESs,
'1.3.6.1.2.1.10.30.8.1.9': DS3_MIB.dsx3TotalCCVs,
'1.3.6.1.2.1.10.30.8.1.10': DS3_MIB.dsx3TotalCESs,
'1.3.6.1.2.1.10.30.8.1.11': DS3_MIB.dsx3TotalCSESs,
'1.3.6.1.2.1.10.30.9.1.1': DS3_MIB.dsx3FarEndLineIndex,
'1.3.6.1.2.1.10.30.9.1.2': DS3_MIB.dsx3FarEndEquipCode,
'1.3.6.1.2.1.10.30.9.1.3': DS3_MIB.dsx3FarEndLocationIDCode,
'1.3.6.1.2.1.10.30.9.1.4': DS3_MIB.dsx3FarEndFrameIDCode,
'1.3.6.1.2.1.10.30.9.1.5': DS3_MIB.dsx3FarEndUnitCode,
'1.3.6.1.2.1.10.30.9.1.6': DS3_MIB.dsx3FarEndFacilityIDCode,
'1.3.6.1.2.1.10.30.10.1.1': DS3_MIB.dsx3FarEndCurrentIndex,
'1.3.6.1.2.1.10.30.10.1.2': DS3_MIB.dsx3FarEndTimeElapsed,
'1.3.6.1.2.1.10.30.10.1.3': DS3_MIB.dsx3FarEndValidIntervals,
'1.3.6.1.2.1.10.30.10.1.4': DS3_MIB.dsx3FarEndCurrentCESs,
'1.3.6.1.2.1.10.30.10.1.5': DS3_MIB.dsx3FarEndCurrentCSESs,
'1.3.6.1.2.1.10.30.10.1.6': DS3_MIB.dsx3FarEndCurrentCCVs,
'1.3.6.1.2.1.10.30.10.1.7': DS3_MIB.dsx3FarEndCurrentUASs,
'1.3.6.1.2.1.10.30.10.1.8': DS3_MIB.dsx3FarEndInvalidIntervals,
'1.3.6.1.2.1.10.30.11.1.1': DS3_MIB.dsx3FarEndIntervalIndex,
'1.3.6.1.2.1.10.30.11.1.2': DS3_MIB.dsx3FarEndIntervalNumber,
'1.3.6.1.2.1.10.30.11.1.3': DS3_MIB.dsx3FarEndIntervalCESs,
'1.3.6.1.2.1.10.30.11.1.4': DS3_MIB.dsx3FarEndIntervalCSESs,
'1.3.6.1.2.1.10.30.11.1.5': DS3_MIB.dsx3FarEndIntervalCCVs,
'1.3.6.1.2.1.10.30.11.1.6': DS3_MIB.dsx3FarEndIntervalUASs,
'1.3.6.1.2.1.10.30.11.1.7': DS3_MIB.dsx3FarEndIntervalValidData,
'1.3.6.1.2.1.10.30.12.1.1': DS3_MIB.dsx3FarEndTotalIndex,
'1.3.6.1.2.1.10.30.12.1.2': DS3_MIB.dsx3FarEndTotalCESs,
'1.3.6.1.2.1.10.30.12.1.3': DS3_MIB.dsx3FarEndTotalCSESs,
'1.3.6.1.2.1.10.30.12.1.4': DS3_MIB.dsx3FarEndTotalCCVs,
'1.3.6.1.2.1.10.30.12.1.5': DS3_MIB.dsx3FarEndTotalUASs,
'1.3.6.1.2.1.10.30.13.1.1': DS3_MIB.dsx3FracIndex,
'1.3.6.1.2.1.10.30.13.1.2': DS3_MIB.dsx3FracNumber,
'1.3.6.1.2.1.10.30.13.1.3': DS3_MIB.dsx3FracIfIndex,
'1.3.6.1.2.1.10.30.15.0.1': DS3_MIB.dsx3LineStatusChange,
'1.3.6.1.2.1.10.30.14.1.1': DS3_MIB.ds3NearEndConfigGroup,
'1.3.6.1.2.1.10.30.14.1.2': DS3_MIB.ds3NearEndStatisticsGroup,
'1.3.6.1.2.1.10.30.14.1.3': DS3_MIB.ds3FarEndGroup,
'1.3.6.1.2.1.10.30.14.1.4': DS3_MIB.ds3DeprecatedGroup,
'1.3.6.1.2.1.10.30.14.1.5': DS3_MIB.ds3NearEndOptionalConfigGroup,
'1.3.6.1.2.1.10.30.14.1.6': DS3_MIB.ds3NearEndOptionalTrapGroup,
}