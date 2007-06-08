# python
# This file is generated by a program (mib2py). 

import CISCO_POP_MGMT_MIB

OIDMAP = {
'1.3.6.1.4.1.9.10.19': CISCO_POP_MGMT_MIB.ciscoPopMgmtMIB,
'1.3.6.1.4.1.9.10.19.1': CISCO_POP_MGMT_MIB.ciscoPopMgmtMIBObjects,
'1.3.6.1.4.1.9.10.19.1.1': CISCO_POP_MGMT_MIB.cpmDS0Usage,
'1.3.6.1.4.1.9.10.19.1.2': CISCO_POP_MGMT_MIB.cpmCallFailure,
'1.3.6.1.4.1.9.10.19.1.3': CISCO_POP_MGMT_MIB.cpmActiveCallSummary,
'1.3.6.1.4.1.9.10.19.1.4': CISCO_POP_MGMT_MIB.cpmCallHistorySummary,
'1.3.6.1.4.1.9.10.19.3': CISCO_POP_MGMT_MIB.ciscoPopMgmtMIBConformance,
'1.3.6.1.4.1.9.10.19.3.1': CISCO_POP_MGMT_MIB.ciscoPopMgmtMIBCompliances,
'1.3.6.1.4.1.9.10.19.3.2': CISCO_POP_MGMT_MIB.ciscoPopMgmtMIBGroups,
'1.3.6.1.4.1.9.10.19.1.1.2': CISCO_POP_MGMT_MIB.cpmISDNCfgBChanInUseForAnalog,
'1.3.6.1.4.1.9.10.19.1.1.3': CISCO_POP_MGMT_MIB.cpmISDNCfgBChannelsInUse,
'1.3.6.1.4.1.9.10.19.1.1.4': CISCO_POP_MGMT_MIB.cpmActiveDS0s,
'1.3.6.1.4.1.9.10.19.1.1.5': CISCO_POP_MGMT_MIB.cpmPPPCalls,
'1.3.6.1.4.1.9.10.19.1.1.6': CISCO_POP_MGMT_MIB.cpmV120Calls,
'1.3.6.1.4.1.9.10.19.1.1.7': CISCO_POP_MGMT_MIB.cpmV110Calls,
'1.3.6.1.4.1.9.10.19.1.1.8': CISCO_POP_MGMT_MIB.cpmActiveDS0sHighWaterMark,
'1.3.6.1.4.1.9.10.19.1.1.10': CISCO_POP_MGMT_MIB.cpmSW56CfgBChannelsInUse,
'1.3.6.1.4.1.9.10.19.1.2.1': CISCO_POP_MGMT_MIB.cpmISDNCallsRejected,
'1.3.6.1.4.1.9.10.19.1.2.2': CISCO_POP_MGMT_MIB.cpmModemCallsRejected,
'1.3.6.1.4.1.9.10.19.1.2.3': CISCO_POP_MGMT_MIB.cpmISDNCallsClearedAbnormally,
'1.3.6.1.4.1.9.10.19.1.2.4': CISCO_POP_MGMT_MIB.cpmModemCallsClearedAbnormally,
'1.3.6.1.4.1.9.10.19.1.2.5': CISCO_POP_MGMT_MIB.cpmISDNNoResource,
'1.3.6.1.4.1.9.10.19.1.2.6': CISCO_POP_MGMT_MIB.cpmModemNoResource,
'1.3.6.1.4.1.9.10.19.1.4.1': CISCO_POP_MGMT_MIB.cpmCallHistorySummaryTableMaxLength,
'1.3.6.1.4.1.9.10.19.1.4.2': CISCO_POP_MGMT_MIB.cpmCallHistorySummaryRetainTimer,
'1.3.6.1.4.1.9.10.19.1.1.1.1.1': CISCO_POP_MGMT_MIB.cpmDS1SlotIndex,
'1.3.6.1.4.1.9.10.19.1.1.1.1.2': CISCO_POP_MGMT_MIB.cpmDS1PortIndex,
'1.3.6.1.4.1.9.10.19.1.1.1.1.3': CISCO_POP_MGMT_MIB.cpmChannelIndex,
'1.3.6.1.4.1.9.10.19.1.1.1.1.4': CISCO_POP_MGMT_MIB.cpmConfiguredType,
'1.3.6.1.4.1.9.10.19.1.1.1.1.5': CISCO_POP_MGMT_MIB.cpmDS0CallType,
'1.3.6.1.4.1.9.10.19.1.1.1.1.6': CISCO_POP_MGMT_MIB.cpmL2Encapsulation,
'1.3.6.1.4.1.9.10.19.1.1.1.1.7': CISCO_POP_MGMT_MIB.cpmCallCount,
'1.3.6.1.4.1.9.10.19.1.1.1.1.8': CISCO_POP_MGMT_MIB.cpmTimeInUse,
'1.3.6.1.4.1.9.10.19.1.1.1.1.9': CISCO_POP_MGMT_MIB.cpmInOctets,
'1.3.6.1.4.1.9.10.19.1.1.1.1.10': CISCO_POP_MGMT_MIB.cpmOutOctets,
'1.3.6.1.4.1.9.10.19.1.1.1.1.11': CISCO_POP_MGMT_MIB.cpmInPackets,
'1.3.6.1.4.1.9.10.19.1.1.1.1.12': CISCO_POP_MGMT_MIB.cpmOutPackets,
'1.3.6.1.4.1.9.10.19.1.1.1.1.13': CISCO_POP_MGMT_MIB.cpmAssociatedInterface,
'1.3.6.1.4.1.9.10.19.1.1.9.1.1': CISCO_POP_MGMT_MIB.cpmDS1UsageSlotIndex,
'1.3.6.1.4.1.9.10.19.1.1.9.1.2': CISCO_POP_MGMT_MIB.cpmDS1UsagePortIndex,
'1.3.6.1.4.1.9.10.19.1.1.9.1.3': CISCO_POP_MGMT_MIB.cpmDS1ActiveDS0s,
'1.3.6.1.4.1.9.10.19.1.1.9.1.4': CISCO_POP_MGMT_MIB.cpmDS1ActiveDS0sHighWaterMark,
'1.3.6.1.4.1.9.10.19.1.3.1.1.1': CISCO_POP_MGMT_MIB.cpmActiveCallStartTimeIndex,
'1.3.6.1.4.1.9.10.19.1.3.1.1.2': CISCO_POP_MGMT_MIB.cpmActiveCallSummaryIndex,
'1.3.6.1.4.1.9.10.19.1.3.1.1.3': CISCO_POP_MGMT_MIB.cpmActiveUserID,
'1.3.6.1.4.1.9.10.19.1.3.1.1.4': CISCO_POP_MGMT_MIB.cpmActiveUserIpAddr,
'1.3.6.1.4.1.9.10.19.1.3.1.1.5': CISCO_POP_MGMT_MIB.cpmActiveCallType,
'1.3.6.1.4.1.9.10.19.1.3.1.1.6': CISCO_POP_MGMT_MIB.cpmActiveModemSlot,
'1.3.6.1.4.1.9.10.19.1.3.1.1.7': CISCO_POP_MGMT_MIB.cpmActiveModemPort,
'1.3.6.1.4.1.9.10.19.1.3.1.1.8': CISCO_POP_MGMT_MIB.cpmActiveCallDuration,
'1.3.6.1.4.1.9.10.19.1.3.1.1.9': CISCO_POP_MGMT_MIB.cpmActiveEntrySlot,
'1.3.6.1.4.1.9.10.19.1.3.1.1.10': CISCO_POP_MGMT_MIB.cpmActiveEntryPort,
'1.3.6.1.4.1.9.10.19.1.3.1.1.11': CISCO_POP_MGMT_MIB.cpmActiveEntryChannel,
'1.3.6.1.4.1.9.10.19.1.3.1.1.12': CISCO_POP_MGMT_MIB.cpmActiveRemotePhoneNumber,
'1.3.6.1.4.1.9.10.19.1.3.1.1.13': CISCO_POP_MGMT_MIB.cpmActiveLocalPhoneNumber,
'1.3.6.1.4.1.9.10.19.1.3.1.1.14': CISCO_POP_MGMT_MIB.cpmActiveTTYNumber,
'1.3.6.1.4.1.9.10.19.1.4.3.1.1': CISCO_POP_MGMT_MIB.cpmCallDisconnectTimeIndex,
'1.3.6.1.4.1.9.10.19.1.4.3.1.2': CISCO_POP_MGMT_MIB.cpmCallStartTimeIndex,
'1.3.6.1.4.1.9.10.19.1.4.3.1.3': CISCO_POP_MGMT_MIB.cpmCallHistorySummaryIndex,
'1.3.6.1.4.1.9.10.19.1.4.3.1.4': CISCO_POP_MGMT_MIB.cpmUserID,
'1.3.6.1.4.1.9.10.19.1.4.3.1.5': CISCO_POP_MGMT_MIB.cpmUserIpAddr,
'1.3.6.1.4.1.9.10.19.1.4.3.1.6': CISCO_POP_MGMT_MIB.cpmCallType,
'1.3.6.1.4.1.9.10.19.1.4.3.1.7': CISCO_POP_MGMT_MIB.cpmModemSlot,
'1.3.6.1.4.1.9.10.19.1.4.3.1.8': CISCO_POP_MGMT_MIB.cpmModemPort,
'1.3.6.1.4.1.9.10.19.1.4.3.1.9': CISCO_POP_MGMT_MIB.cpmCallDuration,
'1.3.6.1.4.1.9.10.19.1.4.3.1.10': CISCO_POP_MGMT_MIB.cpmEntrySlot,
'1.3.6.1.4.1.9.10.19.1.4.3.1.11': CISCO_POP_MGMT_MIB.cpmEntryPort,
'1.3.6.1.4.1.9.10.19.1.4.3.1.12': CISCO_POP_MGMT_MIB.cpmEntryChannel,
'1.3.6.1.4.1.9.10.19.1.4.3.1.13': CISCO_POP_MGMT_MIB.cpmRemotePhoneNumber,
'1.3.6.1.4.1.9.10.19.1.4.3.1.14': CISCO_POP_MGMT_MIB.cpmLocalPhoneNumber,
'1.3.6.1.4.1.9.10.19.1.4.3.1.15': CISCO_POP_MGMT_MIB.cpmTTYNumber,
'1.3.6.1.4.1.9.10.19.3.2.2': CISCO_POP_MGMT_MIB.cpmCallFailureGroup,
'1.3.6.1.4.1.9.10.19.3.2.3': CISCO_POP_MGMT_MIB.cpmActiveCallSummaryGroup,
'1.3.6.1.4.1.9.10.19.3.2.4': CISCO_POP_MGMT_MIB.cpmCallHistorySummaryGroup,
'1.3.6.1.4.1.9.10.19.3.2.5': CISCO_POP_MGMT_MIB.cpmDS0UsageGroupRev1,
}