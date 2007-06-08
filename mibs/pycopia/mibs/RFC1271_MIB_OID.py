# python
# This file is generated by a program (mib2py). 

import RFC1271_MIB

OIDMAP = {
'1.3.6.1.2.1.16': RFC1271_MIB.rmon,
'1.3.6.1.2.1.16.1': RFC1271_MIB.statistics,
'1.3.6.1.2.1.16.2': RFC1271_MIB.history,
'1.3.6.1.2.1.16.3': RFC1271_MIB.alarm,
'1.3.6.1.2.1.16.4': RFC1271_MIB.hosts,
'1.3.6.1.2.1.16.5': RFC1271_MIB.hostTopN,
'1.3.6.1.2.1.16.6': RFC1271_MIB.matrix,
'1.3.6.1.2.1.16.7': RFC1271_MIB.filter,
'1.3.6.1.2.1.16.8': RFC1271_MIB.capture,
'1.3.6.1.2.1.16.9': RFC1271_MIB.event,
'1.3.6.1.2.1.16.1.1.1.1': RFC1271_MIB.etherStatsIndex,
'1.3.6.1.2.1.16.1.1.1.2': RFC1271_MIB.etherStatsDataSource,
'1.3.6.1.2.1.16.1.1.1.3': RFC1271_MIB.etherStatsDropEvents,
'1.3.6.1.2.1.16.1.1.1.4': RFC1271_MIB.etherStatsOctets,
'1.3.6.1.2.1.16.1.1.1.5': RFC1271_MIB.etherStatsPkts,
'1.3.6.1.2.1.16.1.1.1.6': RFC1271_MIB.etherStatsBroadcastPkts,
'1.3.6.1.2.1.16.1.1.1.7': RFC1271_MIB.etherStatsMulticastPkts,
'1.3.6.1.2.1.16.1.1.1.8': RFC1271_MIB.etherStatsCRCAlignErrors,
'1.3.6.1.2.1.16.1.1.1.9': RFC1271_MIB.etherStatsUndersizePkts,
'1.3.6.1.2.1.16.1.1.1.10': RFC1271_MIB.etherStatsOversizePkts,
'1.3.6.1.2.1.16.1.1.1.11': RFC1271_MIB.etherStatsFragments,
'1.3.6.1.2.1.16.1.1.1.12': RFC1271_MIB.etherStatsJabbers,
'1.3.6.1.2.1.16.1.1.1.13': RFC1271_MIB.etherStatsCollisions,
'1.3.6.1.2.1.16.1.1.1.14': RFC1271_MIB.etherStatsPkts64Octets,
'1.3.6.1.2.1.16.1.1.1.15': RFC1271_MIB.etherStatsPkts65to127Octets,
'1.3.6.1.2.1.16.1.1.1.16': RFC1271_MIB.etherStatsPkts128to255Octets,
'1.3.6.1.2.1.16.1.1.1.17': RFC1271_MIB.etherStatsPkts256to511Octets,
'1.3.6.1.2.1.16.1.1.1.18': RFC1271_MIB.etherStatsPkts512to1023Octets,
'1.3.6.1.2.1.16.1.1.1.19': RFC1271_MIB.etherStatsPkts1024to1518Octets,
'1.3.6.1.2.1.16.1.1.1.20': RFC1271_MIB.etherStatsOwner,
'1.3.6.1.2.1.16.1.1.1.21': RFC1271_MIB.etherStatsStatus,
'1.3.6.1.2.1.16.2.1.1.1': RFC1271_MIB.historyControlIndex,
'1.3.6.1.2.1.16.2.1.1.2': RFC1271_MIB.historyControlDataSource,
'1.3.6.1.2.1.16.2.1.1.3': RFC1271_MIB.historyControlBucketsRequested,
'1.3.6.1.2.1.16.2.1.1.4': RFC1271_MIB.historyControlBucketsGranted,
'1.3.6.1.2.1.16.2.1.1.5': RFC1271_MIB.historyControlInterval,
'1.3.6.1.2.1.16.2.1.1.6': RFC1271_MIB.historyControlOwner,
'1.3.6.1.2.1.16.2.1.1.7': RFC1271_MIB.historyControlStatus,
'1.3.6.1.2.1.16.2.2.1.1': RFC1271_MIB.etherHistoryIndex,
'1.3.6.1.2.1.16.2.2.1.2': RFC1271_MIB.etherHistorySampleIndex,
'1.3.6.1.2.1.16.2.2.1.3': RFC1271_MIB.etherHistoryIntervalStart,
'1.3.6.1.2.1.16.2.2.1.4': RFC1271_MIB.etherHistoryDropEvents,
'1.3.6.1.2.1.16.2.2.1.5': RFC1271_MIB.etherHistoryOctets,
'1.3.6.1.2.1.16.2.2.1.6': RFC1271_MIB.etherHistoryPkts,
'1.3.6.1.2.1.16.2.2.1.7': RFC1271_MIB.etherHistoryBroadcastPkts,
'1.3.6.1.2.1.16.2.2.1.8': RFC1271_MIB.etherHistoryMulticastPkts,
'1.3.6.1.2.1.16.2.2.1.9': RFC1271_MIB.etherHistoryCRCAlignErrors,
'1.3.6.1.2.1.16.2.2.1.10': RFC1271_MIB.etherHistoryUndersizePkts,
'1.3.6.1.2.1.16.2.2.1.11': RFC1271_MIB.etherHistoryOversizePkts,
'1.3.6.1.2.1.16.2.2.1.12': RFC1271_MIB.etherHistoryFragments,
'1.3.6.1.2.1.16.2.2.1.13': RFC1271_MIB.etherHistoryJabbers,
'1.3.6.1.2.1.16.2.2.1.14': RFC1271_MIB.etherHistoryCollisions,
'1.3.6.1.2.1.16.2.2.1.15': RFC1271_MIB.etherHistoryUtilization,
'1.3.6.1.2.1.16.3.1.1.1': RFC1271_MIB.alarmIndex,
'1.3.6.1.2.1.16.3.1.1.2': RFC1271_MIB.alarmInterval,
'1.3.6.1.2.1.16.3.1.1.3': RFC1271_MIB.alarmVariable,
'1.3.6.1.2.1.16.3.1.1.4': RFC1271_MIB.alarmSampleType,
'1.3.6.1.2.1.16.3.1.1.5': RFC1271_MIB.alarmValue,
'1.3.6.1.2.1.16.3.1.1.6': RFC1271_MIB.alarmStartupAlarm,
'1.3.6.1.2.1.16.3.1.1.7': RFC1271_MIB.alarmRisingThreshold,
'1.3.6.1.2.1.16.3.1.1.8': RFC1271_MIB.alarmFallingThreshold,
'1.3.6.1.2.1.16.3.1.1.9': RFC1271_MIB.alarmRisingEventIndex,
'1.3.6.1.2.1.16.3.1.1.10': RFC1271_MIB.alarmFallingEventIndex,
'1.3.6.1.2.1.16.3.1.1.11': RFC1271_MIB.alarmOwner,
'1.3.6.1.2.1.16.3.1.1.12': RFC1271_MIB.alarmStatus,
'1.3.6.1.2.1.16.4.1.1.1': RFC1271_MIB.hostControlIndex,
'1.3.6.1.2.1.16.4.1.1.2': RFC1271_MIB.hostControlDataSource,
'1.3.6.1.2.1.16.4.1.1.3': RFC1271_MIB.hostControlTableSize,
'1.3.6.1.2.1.16.4.1.1.4': RFC1271_MIB.hostControlLastDeleteTime,
'1.3.6.1.2.1.16.4.1.1.5': RFC1271_MIB.hostControlOwner,
'1.3.6.1.2.1.16.4.1.1.6': RFC1271_MIB.hostControlStatus,
'1.3.6.1.2.1.16.4.2.1.1': RFC1271_MIB.hostAddress,
'1.3.6.1.2.1.16.4.2.1.2': RFC1271_MIB.hostCreationOrder,
'1.3.6.1.2.1.16.4.2.1.3': RFC1271_MIB.hostIndex,
'1.3.6.1.2.1.16.4.2.1.4': RFC1271_MIB.hostInPkts,
'1.3.6.1.2.1.16.4.2.1.5': RFC1271_MIB.hostOutPkts,
'1.3.6.1.2.1.16.4.2.1.6': RFC1271_MIB.hostInOctets,
'1.3.6.1.2.1.16.4.2.1.7': RFC1271_MIB.hostOutOctets,
'1.3.6.1.2.1.16.4.2.1.8': RFC1271_MIB.hostOutErrors,
'1.3.6.1.2.1.16.4.2.1.9': RFC1271_MIB.hostOutBroadcastPkts,
'1.3.6.1.2.1.16.4.2.1.10': RFC1271_MIB.hostOutMulticastPkts,
'1.3.6.1.2.1.16.4.3.1.1': RFC1271_MIB.hostTimeAddress,
'1.3.6.1.2.1.16.4.3.1.2': RFC1271_MIB.hostTimeCreationOrder,
'1.3.6.1.2.1.16.4.3.1.3': RFC1271_MIB.hostTimeIndex,
'1.3.6.1.2.1.16.4.3.1.4': RFC1271_MIB.hostTimeInPkts,
'1.3.6.1.2.1.16.4.3.1.5': RFC1271_MIB.hostTimeOutPkts,
'1.3.6.1.2.1.16.4.3.1.6': RFC1271_MIB.hostTimeInOctets,
'1.3.6.1.2.1.16.4.3.1.7': RFC1271_MIB.hostTimeOutOctets,
'1.3.6.1.2.1.16.4.3.1.8': RFC1271_MIB.hostTimeOutErrors,
'1.3.6.1.2.1.16.4.3.1.9': RFC1271_MIB.hostTimeOutBroadcastPkts,
'1.3.6.1.2.1.16.4.3.1.10': RFC1271_MIB.hostTimeOutMulticastPkts,
'1.3.6.1.2.1.16.5.1.1.1': RFC1271_MIB.hostTopNControlIndex,
'1.3.6.1.2.1.16.5.1.1.2': RFC1271_MIB.hostTopNHostIndex,
'1.3.6.1.2.1.16.5.1.1.3': RFC1271_MIB.hostTopNRateBase,
'1.3.6.1.2.1.16.5.1.1.4': RFC1271_MIB.hostTopNTimeRemaining,
'1.3.6.1.2.1.16.5.1.1.5': RFC1271_MIB.hostTopNDuration,
'1.3.6.1.2.1.16.5.1.1.6': RFC1271_MIB.hostTopNRequestedSize,
'1.3.6.1.2.1.16.5.1.1.7': RFC1271_MIB.hostTopNGrantedSize,
'1.3.6.1.2.1.16.5.1.1.8': RFC1271_MIB.hostTopNStartTime,
'1.3.6.1.2.1.16.5.1.1.9': RFC1271_MIB.hostTopNOwner,
'1.3.6.1.2.1.16.5.1.1.10': RFC1271_MIB.hostTopNStatus,
'1.3.6.1.2.1.16.5.2.1.1': RFC1271_MIB.hostTopNReport,
'1.3.6.1.2.1.16.5.2.1.2': RFC1271_MIB.hostTopNIndex,
'1.3.6.1.2.1.16.5.2.1.3': RFC1271_MIB.hostTopNAddress,
'1.3.6.1.2.1.16.5.2.1.4': RFC1271_MIB.hostTopNRate,
'1.3.6.1.2.1.16.6.1.1.1': RFC1271_MIB.matrixControlIndex,
'1.3.6.1.2.1.16.6.1.1.2': RFC1271_MIB.matrixControlDataSource,
'1.3.6.1.2.1.16.6.1.1.3': RFC1271_MIB.matrixControlTableSize,
'1.3.6.1.2.1.16.6.1.1.4': RFC1271_MIB.matrixControlLastDeleteTime,
'1.3.6.1.2.1.16.6.1.1.5': RFC1271_MIB.matrixControlOwner,
'1.3.6.1.2.1.16.6.1.1.6': RFC1271_MIB.matrixControlStatus,
'1.3.6.1.2.1.16.6.2.1.1': RFC1271_MIB.matrixSDSourceAddress,
'1.3.6.1.2.1.16.6.2.1.2': RFC1271_MIB.matrixSDDestAddress,
'1.3.6.1.2.1.16.6.2.1.3': RFC1271_MIB.matrixSDIndex,
'1.3.6.1.2.1.16.6.2.1.4': RFC1271_MIB.matrixSDPkts,
'1.3.6.1.2.1.16.6.2.1.5': RFC1271_MIB.matrixSDOctets,
'1.3.6.1.2.1.16.6.2.1.6': RFC1271_MIB.matrixSDErrors,
'1.3.6.1.2.1.16.6.3.1.1': RFC1271_MIB.matrixDSSourceAddress,
'1.3.6.1.2.1.16.6.3.1.2': RFC1271_MIB.matrixDSDestAddress,
'1.3.6.1.2.1.16.6.3.1.3': RFC1271_MIB.matrixDSIndex,
'1.3.6.1.2.1.16.6.3.1.4': RFC1271_MIB.matrixDSPkts,
'1.3.6.1.2.1.16.6.3.1.5': RFC1271_MIB.matrixDSOctets,
'1.3.6.1.2.1.16.6.3.1.6': RFC1271_MIB.matrixDSErrors,
'1.3.6.1.2.1.16.7.1.1.1': RFC1271_MIB.filterIndex,
'1.3.6.1.2.1.16.7.1.1.2': RFC1271_MIB.filterChannelIndex,
'1.3.6.1.2.1.16.7.1.1.3': RFC1271_MIB.filterPktDataOffset,
'1.3.6.1.2.1.16.7.1.1.4': RFC1271_MIB.filterPktData,
'1.3.6.1.2.1.16.7.1.1.5': RFC1271_MIB.filterPktDataMask,
'1.3.6.1.2.1.16.7.1.1.6': RFC1271_MIB.filterPktDataNotMask,
'1.3.6.1.2.1.16.7.1.1.7': RFC1271_MIB.filterPktStatus,
'1.3.6.1.2.1.16.7.1.1.8': RFC1271_MIB.filterPktStatusMask,
'1.3.6.1.2.1.16.7.1.1.9': RFC1271_MIB.filterPktStatusNotMask,
'1.3.6.1.2.1.16.7.1.1.10': RFC1271_MIB.filterOwner,
'1.3.6.1.2.1.16.7.1.1.11': RFC1271_MIB.filterStatus,
'1.3.6.1.2.1.16.7.2.1.1': RFC1271_MIB.channelIndex,
'1.3.6.1.2.1.16.7.2.1.2': RFC1271_MIB.channelIfIndex,
'1.3.6.1.2.1.16.7.2.1.3': RFC1271_MIB.channelAcceptType,
'1.3.6.1.2.1.16.7.2.1.4': RFC1271_MIB.channelDataControl,
'1.3.6.1.2.1.16.7.2.1.5': RFC1271_MIB.channelTurnOnEventIndex,
'1.3.6.1.2.1.16.7.2.1.6': RFC1271_MIB.channelTurnOffEventIndex,
'1.3.6.1.2.1.16.7.2.1.7': RFC1271_MIB.channelEventIndex,
'1.3.6.1.2.1.16.7.2.1.8': RFC1271_MIB.channelEventStatus,
'1.3.6.1.2.1.16.7.2.1.9': RFC1271_MIB.channelMatches,
'1.3.6.1.2.1.16.7.2.1.10': RFC1271_MIB.channelDescription,
'1.3.6.1.2.1.16.7.2.1.11': RFC1271_MIB.channelOwner,
'1.3.6.1.2.1.16.7.2.1.12': RFC1271_MIB.channelStatus,
'1.3.6.1.2.1.16.8.1.1.1': RFC1271_MIB.bufferControlIndex,
'1.3.6.1.2.1.16.8.1.1.2': RFC1271_MIB.bufferControlChannelIndex,
'1.3.6.1.2.1.16.8.1.1.3': RFC1271_MIB.bufferControlFullStatus,
'1.3.6.1.2.1.16.8.1.1.4': RFC1271_MIB.bufferControlFullAction,
'1.3.6.1.2.1.16.8.1.1.5': RFC1271_MIB.bufferControlCaptureSliceSize,
'1.3.6.1.2.1.16.8.1.1.6': RFC1271_MIB.bufferControlDownloadSliceSize,
'1.3.6.1.2.1.16.8.1.1.7': RFC1271_MIB.bufferControlDownloadOffset,
'1.3.6.1.2.1.16.8.1.1.8': RFC1271_MIB.bufferControlMaxOctetsRequested,
'1.3.6.1.2.1.16.8.1.1.9': RFC1271_MIB.bufferControlMaxOctetsGranted,
'1.3.6.1.2.1.16.8.1.1.10': RFC1271_MIB.bufferControlCapturedPackets,
'1.3.6.1.2.1.16.8.1.1.11': RFC1271_MIB.bufferControlTurnOnTime,
'1.3.6.1.2.1.16.8.1.1.12': RFC1271_MIB.bufferControlOwner,
'1.3.6.1.2.1.16.8.1.1.13': RFC1271_MIB.bufferControlStatus,
'1.3.6.1.2.1.16.8.2.1.1': RFC1271_MIB.captureBufferControlIndex,
'1.3.6.1.2.1.16.8.2.1.2': RFC1271_MIB.captureBufferIndex,
'1.3.6.1.2.1.16.8.2.1.3': RFC1271_MIB.captureBufferPacketID,
'1.3.6.1.2.1.16.8.2.1.4': RFC1271_MIB.captureBufferPacketData,
'1.3.6.1.2.1.16.8.2.1.5': RFC1271_MIB.captureBufferPacketLength,
'1.3.6.1.2.1.16.8.2.1.6': RFC1271_MIB.captureBufferPacketTime,
'1.3.6.1.2.1.16.8.2.1.7': RFC1271_MIB.captureBufferPacketStatus,
'1.3.6.1.2.1.16.9.1.1.1': RFC1271_MIB.eventIndex,
'1.3.6.1.2.1.16.9.1.1.2': RFC1271_MIB.eventDescription,
'1.3.6.1.2.1.16.9.1.1.3': RFC1271_MIB.eventType,
'1.3.6.1.2.1.16.9.1.1.4': RFC1271_MIB.eventCommunity,
'1.3.6.1.2.1.16.9.1.1.5': RFC1271_MIB.eventLastTimeSent,
'1.3.6.1.2.1.16.9.1.1.6': RFC1271_MIB.eventOwner,
'1.3.6.1.2.1.16.9.1.1.7': RFC1271_MIB.eventStatus,
'1.3.6.1.2.1.16.9.2.1.1': RFC1271_MIB.logEventIndex,
'1.3.6.1.2.1.16.9.2.1.2': RFC1271_MIB.logIndex,
'1.3.6.1.2.1.16.9.2.1.3': RFC1271_MIB.logTime,
'1.3.6.1.2.1.16.9.2.1.4': RFC1271_MIB.logDescription,
}