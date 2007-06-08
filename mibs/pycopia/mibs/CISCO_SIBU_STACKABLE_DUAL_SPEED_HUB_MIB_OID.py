# python
# This file is generated by a program (mib2py). 

import CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB

OIDMAP = {
'1.3.6.1.4.1.9.10.44': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.ciscoSibuStackableDualSpeedHubMIB,
'1.3.6.1.4.1.9.10.44.1': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.ciscoSibuStackableDualSpeedHubMIBObjects,
'1.3.6.1.4.1.9.10.44.1.1': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssSystem,
'1.3.6.1.4.1.9.10.44.1.2': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssGroup,
'1.3.6.1.4.1.9.10.44.1.3': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssRepeaterPort,
'1.3.6.1.4.1.9.10.44.1.4': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssSwitchPort,
'1.3.6.1.4.1.9.10.44.2': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.ciscoSibuStackableDualSpeedHubNotifications,
'1.3.6.1.4.1.9.10.44.2.0': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.ciscoSibuStackableDualSpeedHubNotificationsPrefix,
'1.3.6.1.4.1.9.10.44.3': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.ciscoSibuStackableDualSpeedHubMIBComformance,
'1.3.6.1.4.1.9.10.44.3.1': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.ciscoSibuStackableDualSpeedHubMIBCompliances,
'1.3.6.1.4.1.9.10.44.3.2': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.ciscoSibuStackableDualSpeedHubMIBGroups,
'1.3.6.1.4.1.9.10.44.1.1.1': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssSystemLinkTraps,
'1.3.6.1.4.1.9.10.44.1.2.1.1.1': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssGroupID,
'1.3.6.1.4.1.9.10.44.1.2.1.1.2': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssGroupType,
'1.3.6.1.4.1.9.10.44.1.2.1.1.4': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssGroupSerialNo,
'1.3.6.1.4.1.9.10.44.1.2.1.1.5': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssGroupBoardRevision,
'1.3.6.1.4.1.9.10.44.1.2.1.1.6': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssGroupAgentBootVersion,
'1.3.6.1.4.1.9.10.44.1.2.1.1.7': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssGroupAgentFirmwareVersion,
'1.3.6.1.4.1.9.10.44.1.2.1.1.8': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssGroupAgentStatus,
'1.3.6.1.4.1.9.10.44.1.2.1.1.9': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssGroupAgentPhysAddress,
'1.3.6.1.4.1.9.10.44.1.2.1.1.12': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssGroupInternalPowerState,
'1.3.6.1.4.1.9.10.44.1.2.1.1.13': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssGroupRedundantPowerState,
'1.3.6.1.4.1.9.10.44.1.2.1.1.14': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssGroupReset,
'1.3.6.1.4.1.9.10.44.1.2.1.1.15': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssGroupConfigDefaultReset,
'1.3.6.1.4.1.9.10.44.1.2.1.1.16': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssGroupIsolatedState,
'1.3.6.1.4.1.9.10.44.1.3.1.1.1': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssRepeaterPortName,
'1.3.6.1.4.1.9.10.44.1.3.1.1.2': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssRepeaterPortControllerRevision,
'1.3.6.1.4.1.9.10.44.1.3.1.1.3': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssRepeaterPortSpeedAdmin,
'1.3.6.1.4.1.9.10.44.1.3.1.1.4': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssRepeaterPortSpeedStatus,
'1.3.6.1.4.1.9.10.44.1.3.1.1.5': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssRepeaterPortLinkStatus,
'1.3.6.1.4.1.9.10.44.1.4.1.1.1': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssSwitchPortModuleID,
'1.3.6.1.4.1.9.10.44.1.4.1.1.2': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssSwitchPortPortID,
'1.3.6.1.4.1.9.10.44.1.4.1.1.3': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssSwitchPortName,
'1.3.6.1.4.1.9.10.44.1.4.1.1.4': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssSwitchPortType,
'1.3.6.1.4.1.9.10.44.1.4.1.1.5': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssSwitchPortControllerRevision,
'1.3.6.1.4.1.9.10.44.1.4.1.1.6': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssSwitchPortState,
'1.3.6.1.4.1.9.10.44.1.4.1.1.7': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssSwitchPortDuplexAdmin,
'1.3.6.1.4.1.9.10.44.1.4.1.1.8': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssSwitchPortDuplexStatus,
'1.3.6.1.4.1.9.10.44.1.4.1.1.9': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssSwitchPortSpeedAdmin,
'1.3.6.1.4.1.9.10.44.1.4.1.1.10': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssSwitchPortSpeedStatus,
'1.3.6.1.4.1.9.10.44.1.4.1.1.11': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.cssSwitchPortLinkStatus,
'1.3.6.1.4.1.9.10.44.2.0.1': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.ciscoSibuStackableDualSpeedHubRptrPortLinkChange,
'1.3.6.1.4.1.9.10.44.2.0.2': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.ciscoSibuStackableDualSpeedHubSwitchPortLinkChange,
'1.3.6.1.4.1.9.10.44.3.2.1': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.ciscoSibuStackableDualSpeedHubGroup,
'1.3.6.1.4.1.9.10.44.3.2.2': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.ciscoSibuStackableDualSpeedHubRepeaterPortGroup,
'1.3.6.1.4.1.9.10.44.3.2.3': CISCO_SIBU_STACKABLE_DUAL_SPEED_HUB_MIB.ciscoSibuStackableDualSpeedHubSwitchPortGroup,
}