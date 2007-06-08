# python
# This file is generated by a program (mib2py). 

import HP_ICF_OID

OIDMAP = {
'1.3.6.1.4.1.11': HP_ICF_OID.hp,
'1.3.6.1.4.1.11.2': HP_ICF_OID.nm,
'1.3.6.1.4.1.11.2.3': HP_ICF_OID.hpSystem,
'1.3.6.1.4.1.11.2.3.7': HP_ICF_OID.netElement,
'1.3.6.1.4.1.11.2.3.7.1': HP_ICF_OID.bridge,
'1.3.6.1.4.1.11.2.3.7.1.1': HP_ICF_OID.bridge1010,
'1.3.6.1.4.1.11.2.3.7.1.2': HP_ICF_OID.bridgeRemote,
'1.3.6.1.4.1.11.2.3.7.1.3': HP_ICF_OID.eswitch,
'1.3.6.1.4.1.11.2.3.7.1.8': HP_ICF_OID.eswitch2,
'1.3.6.1.4.1.11.2.3.7.1.9': HP_ICF_OID.netSwitch100,
'1.3.6.1.4.1.11.2.3.7.1.10': HP_ICF_OID.netSwitch200,
'1.3.6.1.4.1.11.2.3.7.2': HP_ICF_OID.router,
'1.3.6.1.4.1.11.2.3.7.2.1': HP_ICF_OID.icfRouterER,
'1.3.6.1.4.1.11.2.3.7.2.2': HP_ICF_OID.icfRouterTR,
'1.3.6.1.4.1.11.2.3.7.2.3': HP_ICF_OID.icfRouterSR,
'1.3.6.1.4.1.11.2.3.7.2.4': HP_ICF_OID.icfRouterFR,
'1.3.6.1.4.1.11.2.3.7.2.5': HP_ICF_OID.icfRouterLR,
'1.3.6.1.4.1.11.2.3.7.2.6': HP_ICF_OID.icfRouterBR,
'1.3.6.1.4.1.11.2.3.7.2.7': HP_ICF_OID.icfRouterPR,
'1.3.6.1.4.1.11.2.3.7.2.8': HP_ICF_OID.icfRouter650,
'1.3.6.1.4.1.11.2.3.7.2.8.2': HP_ICF_OID.icfRouter650Engine,
'1.3.6.1.4.1.11.2.3.7.2.8.3': HP_ICF_OID.icfRouter650Port4E,
'1.3.6.1.4.1.11.2.3.7.2.8.4': HP_ICF_OID.icfRouter650Port4S,
'1.3.6.1.4.1.11.2.3.7.2.8.5': HP_ICF_OID.icfRouter650Port4T,
'1.3.6.1.4.1.11.2.3.7.2.8.6': HP_ICF_OID.icfRouter650PortFDDI,
'1.3.6.1.4.1.11.2.3.7.2.8.7': HP_ICF_OID.icfRouter650Port100VG,
'1.3.6.1.4.1.11.2.3.7.2.9': HP_ICF_OID.icfRouter230,
'1.3.6.1.4.1.11.2.3.7.2.10': HP_ICF_OID.icfRouter250,
'1.3.6.1.4.1.11.2.3.7.2.11': HP_ICF_OID.icfRouter255,
'1.3.6.1.4.1.11.2.3.7.2.12': HP_ICF_OID.icfRouter210,
'1.3.6.1.4.1.11.2.3.7.5': HP_ICF_OID.hub,
'1.3.6.1.4.1.11.2.3.7.5.1': HP_ICF_OID.etherTwist12,
'1.3.6.1.4.1.11.2.3.7.5.3': HP_ICF_OID.fiberOptic,
'1.3.6.1.4.1.11.2.3.7.5.4': HP_ICF_OID.etherTwist48,
'1.3.6.1.4.1.11.2.3.7.5.5': HP_ICF_OID.thinLAN,
'1.3.6.1.4.1.11.2.3.7.5.6': HP_ICF_OID.etherTwist24S,
'1.3.6.1.4.1.11.2.3.7.5.7': HP_ICF_OID.advStack12,
'1.3.6.1.4.1.11.2.3.7.5.8': HP_ICF_OID.advStack24,
'1.3.6.1.4.1.11.2.3.7.5.9': HP_ICF_OID.advStack48,
'1.3.6.1.4.1.11.2.3.7.5.10': HP_ICF_OID.advStackVg15,
'1.3.6.1.4.1.11.2.3.7.5.11': HP_ICF_OID.advStackU8,
'1.3.6.1.4.1.11.2.3.7.5.12': HP_ICF_OID.advStackU16,
'1.3.6.1.4.1.11.2.3.7.5.13': HP_ICF_OID.advStackVg6,
'1.3.6.1.4.1.11.2.3.7.5.14': HP_ICF_OID.advStackVg12,
'1.3.6.1.4.1.11.2.3.7.5.15': HP_ICF_OID.hpAdvStkEnetSH12R,
'1.3.6.1.4.1.11.2.3.7.5.16': HP_ICF_OID.hpAdvStkEnetSH24R,
'1.3.6.1.4.1.11.2.3.7.5.17': HP_ICF_OID.hpAdvStkEnetSH24T,
'1.3.6.1.4.1.11.2.3.7.5.18': HP_ICF_OID.hpAdvStk100Tx12TM,
'1.3.6.1.4.1.11.2.3.7.5.19': HP_ICF_OID.hp10THub16M,
'1.3.6.1.4.1.11.2.3.7.5.20': HP_ICF_OID.hp10BaseTHub12M,
'1.3.6.1.4.1.11.2.3.7.5.21': HP_ICF_OID.hp10BaseTHub24M,
'1.3.6.1.4.1.11.2.3.7.5.22': HP_ICF_OID.hpProCurve10T100THub12M,
'1.3.6.1.4.1.11.2.3.7.5.23': HP_ICF_OID.hpProCurve10T100THub24M,
'1.3.6.1.4.1.11.2.3.7.8': HP_ICF_OID.chassis,
'1.3.6.1.4.1.11.2.3.7.8.1': HP_ICF_OID.repeaterAgent,
'1.3.6.1.4.1.11.2.3.7.8.2': HP_ICF_OID.chassisAgents,
'1.3.6.1.4.1.11.2.3.7.8.2.1': HP_ICF_OID.icfVgAgent,
'1.3.6.1.4.1.11.2.3.7.8.2.3': HP_ICF_OID.icfVgAgent2,
'1.3.6.1.4.1.11.2.3.7.8.2.4': HP_ICF_OID.hpicfEnetSMM,
'1.3.6.1.4.1.11.2.3.7.8.2.5': HP_ICF_OID.hpAdvStkEnetSHAgent,
'1.3.6.1.4.1.11.2.3.7.8.2.6': HP_ICF_OID.hpAdvStkSwStackTopMgmt,
'1.3.6.1.4.1.11.2.3.7.8.2.7': HP_ICF_OID.hpSwitch8000CpuCard,
'1.3.6.1.4.1.11.2.3.7.8.3': HP_ICF_OID.icfSensors,
'1.3.6.1.4.1.11.2.3.7.8.3.1': HP_ICF_OID.icfPowerSupplySensor,
'1.3.6.1.4.1.11.2.3.7.8.3.2': HP_ICF_OID.icfFanSensor,
'1.3.6.1.4.1.11.2.3.7.8.3.3': HP_ICF_OID.icfTemperatureSensor,
'1.3.6.1.4.1.11.2.3.7.8.3.4': HP_ICF_OID.icfFutureSlotSensor,
'1.3.6.1.4.1.11.2.3.7.8.4': HP_ICF_OID.icfCards,
'1.3.6.1.4.1.11.2.3.7.8.4.1': HP_ICF_OID.icfUnidentifiedCard,
'1.3.6.1.4.1.11.2.3.7.8.4.2': HP_ICF_OID.hpAdvStkEnetSHSwitch,
'1.3.6.1.4.1.11.2.3.7.8.4.3': HP_ICF_OID.hpAdvStkSwStackExpander,
'1.3.6.1.4.1.11.2.3.7.8.5': HP_ICF_OID.hpicfStacks,
'1.3.6.1.4.1.11.2.3.7.8.5.1': HP_ICF_OID.hpAdvStkEnetSHStack,
'1.3.6.1.4.1.11.2.3.7.8.6': HP_ICF_OID.hpicfBackplanes,
'1.3.6.1.4.1.11.2.3.7.8.6.1': HP_ICF_OID.hpAdvStkEnetSHExtSeg,
'1.3.6.1.4.1.11.2.3.7.8.6.2': HP_ICF_OID.hpAdvStkEnetSHIntSeg,
'1.3.6.1.4.1.11.2.3.7.8.6.3': HP_ICF_OID.hp10BaseTHubSeg,
'1.3.6.1.4.1.11.2.3.7.8.6.4': HP_ICF_OID.hpSwitchBackplane,
'1.3.6.1.4.1.11.2.3.7.8.6.5': HP_ICF_OID.hp100BaseTHubSeg,
'1.3.6.1.4.1.11.2.3.7.8.7': HP_ICF_OID.hpicfSlots,
'1.3.6.1.4.1.11.2.3.7.8.7.1': HP_ICF_OID.hpAdvStkEnetSHAgentSlot,
'1.3.6.1.4.1.11.2.3.7.8.7.2': HP_ICF_OID.hpAdvStkEnetSHIOSlot,
'1.3.6.1.4.1.11.2.3.7.8.7.3': HP_ICF_OID.hpAdvStkSwStackMgmtSlot,
'1.3.6.1.4.1.11.2.3.7.8.7.4': HP_ICF_OID.hpAdvStkSwStackExpSlot,
'1.3.6.1.4.1.11.2.3.7.8.7.5': HP_ICF_OID.hpSwitch8000PowerSupplyBay,
'1.3.6.1.4.1.11.2.3.7.8.7.6': HP_ICF_OID.hpSwitch8000CpuSlot,
'1.3.6.1.4.1.11.2.3.7.8.7.7': HP_ICF_OID.hpSwitch8000PortSlot,
'1.3.6.1.4.1.11.2.3.7.8.7.8': HP_ICF_OID.hpSwitch2524PortSlot,
'1.3.6.1.4.1.11.2.3.7.8.7.9': HP_ICF_OID.hpSwitch5308PowerSupplyBay,
'1.3.6.1.4.1.11.2.3.7.8.7.10': HP_ICF_OID.hpSwitch5308PortSlot,
'1.3.6.1.4.1.11.2.3.7.8.7.11': HP_ICF_OID.hpSwitch4865PowerSupplyBay,
'1.3.6.1.4.1.11.2.3.7.8.7.12': HP_ICF_OID.hpSwitch4865PortSlot,
'1.3.6.1.4.1.11.2.3.7.8.7.13': HP_ICF_OID.hpSwitch2650PortSlot,
'1.3.6.1.4.1.11.2.3.7.8.7.14': HP_ICF_OID.hpSwitch6108PortSlot,
'1.3.6.1.4.1.11.2.3.7.8.7.15': HP_ICF_OID.hpSwitch2824PortSlot,
'1.3.6.1.4.1.11.2.3.7.8.7.16': HP_ICF_OID.hpSwitch2626PortSlot,
'1.3.6.1.4.1.11.2.3.7.8.7.17': HP_ICF_OID.hpSwitch2650PPortSlot,
'1.3.6.1.4.1.11.2.3.7.8.7.18': HP_ICF_OID.hpSwitch2626PPortSlot,
'1.3.6.1.4.1.11.2.3.7.8.8': HP_ICF_OID.hpicfHubPorts,
'1.3.6.1.4.1.11.2.3.7.8.8.1': HP_ICF_OID.hpAdvStkEnetSHExtPort,
'1.3.6.1.4.1.11.2.3.7.8.8.2': HP_ICF_OID.hpAdvStkEnetSHIntPort,
'1.3.6.1.4.1.11.2.3.7.8.8.3': HP_ICF_OID.hpAdvStkEnetSHAgentPort,
'1.3.6.1.4.1.11.2.3.7.8.8.4': HP_ICF_OID.hp10BaseTHubPort,
'1.3.6.1.4.1.11.2.3.7.8.8.5': HP_ICF_OID.hp10BaseTHubAgentPort,
'1.3.6.1.4.1.11.2.3.7.8.8.6': HP_ICF_OID.hp10T100THubPort,
'1.3.6.1.4.1.11.2.3.7.8.8.7': HP_ICF_OID.hp100BaseTHubAgentPort,
'1.3.6.1.4.1.11.2.3.7.8.9': HP_ICF_OID.hpicfEnetChipSets,
'1.3.6.1.4.1.11.2.3.7.8.9.1': HP_ICF_OID.hpicfEnetChipSetHydra,
'1.3.6.1.4.1.11.2.3.7.8.9.2': HP_ICF_OID.hpicfEnetChipSetGT48001,
'1.3.6.1.4.1.11.2.3.7.8.9.3': HP_ICF_OID.hpicfEnetChipSetPentagon,
'1.3.6.1.4.1.11.2.3.7.8.10': HP_ICF_OID.hpicfSwitchPorts,
'1.3.6.1.4.1.11.2.3.7.8.10.1': HP_ICF_OID.hpicfSwitchPort10T100TX,
'1.3.6.1.4.1.11.2.3.7.8.10.2': HP_ICF_OID.hpicfSwitchPort100FX,
'1.3.6.1.4.1.11.2.3.7.8.10.3': HP_ICF_OID.hpicfSwitchPort10FL,
'1.3.6.1.4.1.11.2.3.7.8.10.4': HP_ICF_OID.hpicfSwitchPort1000SX,
'1.3.6.1.4.1.11.2.3.7.8.10.5': HP_ICF_OID.hpicfSwitchPort10T,
'1.3.6.1.4.1.11.2.3.7.8.10.6': HP_ICF_OID.hpicfSwitchPort1000LX,
'1.3.6.1.4.1.11.2.3.7.8.10.7': HP_ICF_OID.hpicfSwitchPort1000T,
'1.3.6.1.4.1.11.2.3.7.8.10.8': HP_ICF_OID.hpicfSwitchPort1000Stk,
'1.3.6.1.4.1.11.2.3.7.8.10.9': HP_ICF_OID.hpicfSwitchPort1000LH,
'1.3.6.1.4.1.11.2.3.7.8.11': HP_ICF_OID.hpicfMAUTypes,
'1.3.6.1.4.1.11.2.3.7.8.11.1': HP_ICF_OID.hpicfMauType1000BaseSXHD,
'1.3.6.1.4.1.11.2.3.7.8.11.2': HP_ICF_OID.hpicfMauType1000BaseSXFD,
'1.3.6.1.4.1.11.2.3.7.8.11.3': HP_ICF_OID.hpicfMauType1000BaseLXHD,
'1.3.6.1.4.1.11.2.3.7.8.11.4': HP_ICF_OID.hpicfMauType1000BaseLXFD,
'1.3.6.1.4.1.11.2.3.7.8.11.5': HP_ICF_OID.hpicfMauType1000BaseTHD,
'1.3.6.1.4.1.11.2.3.7.8.11.6': HP_ICF_OID.hpicfMauType1000BaseTFD,
'1.3.6.1.4.1.11.2.3.7.8.11.7': HP_ICF_OID.hpicfMauType1000BaseStkHD,
'1.3.6.1.4.1.11.2.3.7.8.11.8': HP_ICF_OID.hpicfMauType1000BaseStkFD,
'1.3.6.1.4.1.11.2.3.7.8.11.9': HP_ICF_OID.hpicfMauType1000BaseLHFD,
'1.3.6.1.4.1.11.2.3.7.11': HP_ICF_OID.hpEtherSwitch,
'1.3.6.1.4.1.11.2.3.7.11.1': HP_ICF_OID.hpAdvSwitch2000,
'1.3.6.1.4.1.11.2.3.7.11.1.1': HP_ICF_OID.hpSwitchPortModuleET4,
'1.3.6.1.4.1.11.2.3.7.11.1.2': HP_ICF_OID.hpSwitchPortModuleVG2,
'1.3.6.1.4.1.11.2.3.7.11.1.3': HP_ICF_OID.hpSwitchPortModule10FL,
'1.3.6.1.4.1.11.2.3.7.11.1.4': HP_ICF_OID.hpSwitchPortModuleFDDI,
'1.3.6.1.4.1.11.2.3.7.11.1.5': HP_ICF_OID.hpSwitchPortModuleTX2,
'1.3.6.1.4.1.11.2.3.7.11.1.6': HP_ICF_OID.hpSwitchPortModuleATM,
'1.3.6.1.4.1.11.2.3.7.11.2': HP_ICF_OID.hpAdvSwitch2000B,
'1.3.6.1.4.1.11.2.3.7.11.3': HP_ICF_OID.hpAdvSwitch800T,
'1.3.6.1.4.1.11.2.3.7.11.4': HP_ICF_OID.hpAdvSwitch200,
'1.3.6.1.4.1.11.2.3.7.11.4.1': HP_ICF_OID.hpAdvSwitch208T,
'1.3.6.1.4.1.11.2.3.7.11.4.2': HP_ICF_OID.hpAdvSwitch208VG,
'1.3.6.1.4.1.11.2.3.7.11.4.3': HP_ICF_OID.hpAdvSwitch224T,
'1.3.6.1.4.1.11.2.3.7.11.4.4': HP_ICF_OID.hpAdvSwitch224VG,
'1.3.6.1.4.1.11.2.3.7.11.5': HP_ICF_OID.hpSwitch212M,
'1.3.6.1.4.1.11.2.3.7.11.6': HP_ICF_OID.hpSwitch224M,
'1.3.6.1.4.1.11.2.3.7.11.7': HP_ICF_OID.hpSwitch8000,
'1.3.6.1.4.1.11.2.3.7.11.7.1': HP_ICF_OID.hpSwitchPortModule100TX8,
'1.3.6.1.4.1.11.2.3.7.11.7.2': HP_ICF_OID.hpSwitchPortModule100FX4,
'1.3.6.1.4.1.11.2.3.7.11.7.3': HP_ICF_OID.hpSwitchPortModule10FL4,
'1.3.6.1.4.1.11.2.3.7.11.7.4': HP_ICF_OID.hpSwitchPortModuleGigSX,
'1.3.6.1.4.1.11.2.3.7.11.7.5': HP_ICF_OID.hpSwitchPortModuleGigLX,
'1.3.6.1.4.1.11.2.3.7.11.7.6': HP_ICF_OID.hpSwitchPortModuleTwoGig,
'1.3.6.1.4.1.11.2.3.7.11.7.7': HP_ICF_OID.hpSwitchPortModuleGigStk,
'1.3.6.1.4.1.11.2.3.7.11.7.8': HP_ICF_OID.hpSwitchPortModuleGigT,
'1.3.6.1.4.1.11.2.3.7.11.8': HP_ICF_OID.hpSwitch1600,
'1.3.6.1.4.1.11.2.3.7.11.9': HP_ICF_OID.hpSwitch4000,
'1.3.6.1.4.1.11.2.3.7.11.10': HP_ICF_OID.hpSwitch2400,
'1.3.6.1.4.1.11.2.3.7.11.11': HP_ICF_OID.hpSwitch2424,
'1.3.6.1.4.1.11.2.3.7.11.13': HP_ICF_OID.hpSwitch9308,
'1.3.6.1.4.1.11.2.3.7.11.14': HP_ICF_OID.hpSwitch9304,
'1.3.6.1.4.1.11.2.3.7.11.15': HP_ICF_OID.hpSwitch6308,
'1.3.6.1.4.1.11.2.3.7.11.16': HP_ICF_OID.hpSwitch6208,
'1.3.6.1.4.1.11.2.3.7.11.17': HP_ICF_OID.hpSwitchJ4819A,
'1.3.6.1.4.1.11.2.3.7.11.17.1': HP_ICF_OID.hpSwitchPortModuleJ4820A,
'1.3.6.1.4.1.11.2.3.7.11.17.2': HP_ICF_OID.hpSwitchPortModuleJ4821A,
'1.3.6.1.4.1.11.2.3.7.11.17.3': HP_ICF_OID.hpSwitchPortModuleJ4878A,
'1.3.6.1.4.1.11.2.3.7.11.17.4': HP_ICF_OID.hpSwitchModuleJ4852A,
'1.3.6.1.4.1.11.2.3.7.11.18': HP_ICF_OID.hpSwitchJ4812A,
'1.3.6.1.4.1.11.2.3.7.11.18.1': HP_ICF_OID.hpSwitchModuleJ4812A,
'1.3.6.1.4.1.11.2.3.7.11.19': HP_ICF_OID.hpSwitchJ4813A,
'1.3.6.1.4.1.11.2.3.7.11.19.1': HP_ICF_OID.hpSwitchModuleJ4813A,
'1.3.6.1.4.1.11.2.3.7.11.20': HP_ICF_OID.hpSwitchJ4850A,
'1.3.6.1.4.1.11.2.3.7.11.21': HP_ICF_OID.hpSwitchJ4815A,
'1.3.6.1.4.1.11.2.3.7.11.22': HP_ICF_OID.hpSwitchJ4851A,
'1.3.6.1.4.1.11.2.3.7.11.23': HP_ICF_OID.hpSwitchJ4865A,
'1.3.6.1.4.1.11.2.3.7.11.23.1': HP_ICF_OID.hpSwitchModuleJ4862A,
'1.3.6.1.4.1.11.2.3.7.11.23.2': HP_ICF_OID.hpSwitchModuleJ4863A,
'1.3.6.1.4.1.11.2.3.7.11.23.3': HP_ICF_OID.hpSwitchModuleJ4864A,
'1.3.6.1.4.1.11.2.3.7.11.23.4': HP_ICF_OID.hpSwitchModuleJ4862B,
'1.3.6.1.4.1.11.2.3.7.11.23.5': HP_ICF_OID.hpSwitchModuleJ4893A,
'1.3.6.1.4.1.11.2.3.7.11.23.6': HP_ICF_OID.hpSwitchModuleJ4892A,
'1.3.6.1.4.1.11.2.3.7.11.23.7': HP_ICF_OID.hpSwitchModuleJ4908A,
'1.3.6.1.4.1.11.2.3.7.11.24': HP_ICF_OID.hpSwitchA6713A,
'1.3.6.1.4.1.11.2.3.7.11.25': HP_ICF_OID.hpSwitchA6716A,
'1.3.6.1.4.1.11.2.3.7.11.26': HP_ICF_OID.hpSwitchA6717A,
'1.3.6.1.4.1.11.2.3.7.11.27': HP_ICF_OID.hpSwitchJ4887A,
'1.3.6.1.4.1.11.2.3.7.11.28': HP_ICF_OID.hpSwitchJ4874A,
'1.3.6.1.4.1.11.2.3.7.11.29': HP_ICF_OID.hpSwitchJ4899A,
'1.3.6.1.4.1.11.2.3.7.11.30': HP_ICF_OID.hpSwitchJ4902A,
'1.3.6.1.4.1.11.2.3.7.11.31': HP_ICF_OID.hpSwitchJ4903A,
'1.3.6.1.4.1.11.2.3.7.11.31.1': HP_ICF_OID.hpSwitchModuleJ4903A,
'1.3.6.1.4.1.11.2.3.7.11.31.2': HP_ICF_OID.hpSwitchModuleJxxx2A,
'1.3.6.1.4.1.11.2.3.7.11.31.3': HP_ICF_OID.hpSwitchModuleJxxx2B,
'1.3.6.1.4.1.11.2.3.7.11.32': HP_ICF_OID.hpSwitchJ490xA,
'1.3.6.1.4.1.11.2.3.7.11.32.1': HP_ICF_OID.hpSwitchModuleJxxx3A,
'1.3.6.1.4.1.11.2.3.7.11.33': HP_ICF_OID.hpSwitchProliant,
'1.3.6.1.4.1.11.2.3.7.11.34': HP_ICF_OID.hpSwitchJ4900A,
'1.3.6.1.4.1.11.2.3.7.11.35': HP_ICF_OID.hpSwitchJ8165A,
'1.3.6.1.4.1.11.2.3.7.11.36': HP_ICF_OID.hpSwitchJ8164A,
'1.3.6.1.4.1.11.2.3.7.11.37': HP_ICF_OID.hpSwitchJ8130A,
'1.3.6.1.4.1.11.2.3.7.11.38': HP_ICF_OID.hpSwitchJ8133A,
'1.3.6.1.4.1.11.2.3.7.11.39': HP_ICF_OID.hpSwitchJ8153A,
'1.3.6.1.4.1.11.2.3.7.11.40': HP_ICF_OID.hpSwitchJ8154A,
'1.3.6.1.4.1.11.2.3.7.11.41': HP_ICF_OID.hpSwitchJ8155A,
'1.3.6.1.4.1.11.2.3.7.11.99': HP_ICF_OID.hpEtherSwitchPortType,
'1.3.6.1.4.1.11.2.3.7.11.99.1': HP_ICF_OID.hpEtherSwitchPort10T,
'1.3.6.1.4.1.11.2.3.7.11.99.2': HP_ICF_OID.hpEtherSwitchPort100T,
'1.3.6.1.4.1.11.2.3.7.11.99.3': HP_ICF_OID.hpEtherSwitchPort100VG,
'1.3.6.1.4.1.11.2.3.7.11.99.4': HP_ICF_OID.hpEtherSwitchPort100F,
'1.3.6.1.4.1.11.2.14': HP_ICF_OID.icf,
'1.3.6.1.4.1.11.2.14.1': HP_ICF_OID.icfCommon,
'1.3.6.1.4.1.11.2.14.2': HP_ICF_OID.icfHub,
'1.3.6.1.4.1.11.2.14.3': HP_ICF_OID.icfBridge,
'1.3.6.1.4.1.11.2.14.4': HP_ICF_OID.icfSecurity,
'1.3.6.1.4.1.11.2.14.5': HP_ICF_OID.icfConfig,
'1.3.6.1.4.1.11.2.14.6': HP_ICF_OID.icfEsSwitch,
'1.3.6.1.4.1.11.2.14.6.1': HP_ICF_OID.hpEs,
'1.3.6.1.4.1.11.2.14.6.2': HP_ICF_OID.hpEs2,
'1.3.6.1.4.1.11.2.14.6.3': HP_ICF_OID.hpNetSwitch,
'1.3.6.1.4.1.11.2.14.7': HP_ICF_OID.icfRouter,
'1.3.6.1.4.1.11.2.14.8': HP_ICF_OID.icfDot12Draft,
'1.3.6.1.4.1.11.2.14.8.1': HP_ICF_OID.icfVgRepeater,
'1.3.6.1.4.1.11.2.14.8.2': HP_ICF_OID.icfVgInterface,
'1.3.6.1.4.1.11.2.14.9': HP_ICF_OID.hpEntityMIB,
'1.3.6.1.4.1.11.2.14.10': HP_ICF_OID.hpicfAdmin,
'1.3.6.1.4.1.11.2.14.10.1': HP_ICF_OID.hpicfDomains,
'1.3.6.1.4.1.11.2.14.10.1.1': HP_ICF_OID.hpicfLLCDomain,
'1.3.6.1.4.1.11.2.14.10.2': HP_ICF_OID.hpicfObjectModules,
'1.3.6.1.4.1.11.2.14.10.2.1': HP_ICF_OID.icfSecurityMib,
'1.3.6.1.4.1.11.2.14.10.2.2': HP_ICF_OID.hpicfChainMib,
'1.3.6.1.4.1.11.2.14.10.2.3': HP_ICF_OID.hpicfChassisMib,
'1.3.6.1.4.1.11.2.14.10.2.4': HP_ICF_OID.hpicfDownloadMib,
'1.3.6.1.4.1.11.2.14.10.2.5': HP_ICF_OID.hpicfBasicMib,
'1.3.6.1.4.1.11.2.14.10.2.6': HP_ICF_OID.hpicfStackMib,
'1.3.6.1.4.1.11.2.14.10.2.7': HP_ICF_OID.hpicfLinkTestMib,
'1.3.6.1.4.1.11.2.14.10.2.8': HP_ICF_OID.hpicfGenRptrMib,
'1.3.6.1.4.1.11.2.14.10.2.9': HP_ICF_OID.hpicf8023RptrMib,
'1.3.6.1.4.1.11.2.14.10.2.10': HP_ICF_OID.icfVgRepeaterMib,
'1.3.6.1.4.1.11.2.14.10.2.11': HP_ICF_OID.hpicfVgRptrMib,
'1.3.6.1.4.1.11.2.14.10.2.12': HP_ICF_OID.hpicfFaultFinderMib,
'1.3.6.1.4.1.11.2.14.10.3': HP_ICF_OID.hpicfAgentModules,
'1.3.6.1.4.1.11.2.14.10.3.1': HP_ICF_OID.hpicfETwistHubAgentsMib,
'1.3.6.1.4.1.11.2.14.10.3.2': HP_ICF_OID.hpicfETwistBridgeAgentsMib,
'1.3.6.1.4.1.11.2.14.10.3.3': HP_ICF_OID.hpicfAdvStk8023AgentsMib,
'1.3.6.1.4.1.11.2.14.10.3.4': HP_ICF_OID.hpicfAdvStkVGAgentsMib,
'1.3.6.1.4.1.11.2.14.10.4': HP_ICF_OID.hpicfTextualConventions,
'1.3.6.1.4.1.11.2.14.11': HP_ICF_OID.hpicfObjects,
'1.3.6.1.4.1.11.2.14.11.1': HP_ICF_OID.hpicfCommon,
'1.3.6.1.4.1.11.2.14.11.1.1': HP_ICF_OID.hpicfChain,
'1.3.6.1.4.1.11.2.14.11.1.2': HP_ICF_OID.hpicfChassis,
'1.3.6.1.4.1.11.2.14.11.1.3': HP_ICF_OID.hpicfDownload,
'1.3.6.1.4.1.11.2.14.11.1.4': HP_ICF_OID.hpicfBasic,
'1.3.6.1.4.1.11.2.14.11.1.5': HP_ICF_OID.hpicfStack,
'1.3.6.1.4.1.11.2.14.11.1.6': HP_ICF_OID.hpicfLinktest,
'1.3.6.1.4.1.11.2.14.11.1.7': HP_ICF_OID.hpicfFaultFinder,
'1.3.6.1.4.1.11.2.14.11.2': HP_ICF_OID.hpicfRepeater,
'1.3.6.1.4.1.11.2.14.11.3': HP_ICF_OID.hpicfVg,
'1.3.6.1.4.1.11.2.14.11.4': HP_ICF_OID.hpicfGenericRepeater,
'1.3.6.1.4.1.11.2.14.11.5': HP_ICF_OID.hpicfSwitch,
'1.3.6.1.4.1.11.2.14.11.5.1': HP_ICF_OID.hpSwitch,
'1.3.6.1.4.1.11.2.14.11.5.1.1': HP_ICF_OID.hpOpSystem,
'1.3.6.1.4.1.11.2.14.11.5.1.2': HP_ICF_OID.hpHwSystem,
'1.3.6.1.4.1.11.2.14.11.5.1.3': HP_ICF_OID.hpVLAN,
'1.3.6.1.4.1.11.2.14.11.5.1.7': HP_ICF_OID.hpConfig,
'1.3.6.1.4.1.11.2.14.11.5.1.9': HP_ICF_OID.hpSwitchStatistics,
'1.3.6.1.4.1.11.2.14.11.5.1.10': HP_ICF_OID.hpSwitchVirtualStackMib,
'1.3.6.1.4.1.11.2.14.11.5.1.11': HP_ICF_OID.hpicfDhcpRelay,
'1.3.6.1.4.1.11.2.14.11.5.1.12': HP_ICF_OID.hpicfBridge,
'1.3.6.1.4.1.11.2.14.11.5.1.13': HP_ICF_OID.hpicfRip,
'1.3.6.1.4.1.11.2.14.11.5.1.14': HP_ICF_OID.hpicfOspf,
'1.3.6.1.4.1.11.2.14.11.5.1.15': HP_ICF_OID.hpicfIpRouting,
'1.3.6.1.4.1.11.2.14.11.6': HP_ICF_OID.hpicfAccess,
'1.3.6.1.4.1.11.2.14.12': HP_ICF_OID.hpicfNotifications,
'1.3.6.1.4.1.11.2.14.12.1': HP_ICF_OID.hpicfCommonTraps,
'1.3.6.1.4.1.11.2.14.12.1.0': HP_ICF_OID.hpicfCommonTrapsPrefix,
'1.3.6.1.4.1.11.2.14.12.2': HP_ICF_OID.hpicf8023RptrTraps,
'1.3.6.1.4.1.11.2.14.12.2.0': HP_ICF_OID.hpicf8023RptrTrapsPrefix,
'1.3.6.1.4.1.11.2.14.12.3': HP_ICF_OID.hpicfVgRptrTraps,
'1.3.6.1.4.1.11.2.14.12.3.0': HP_ICF_OID.hpicfVgRptrTrapsPrefix,
'1.3.6.1.4.1.11.2.14.12.4': HP_ICF_OID.hpicfGenRptrTraps,
'1.3.6.1.4.1.11.2.14.12.4.0': HP_ICF_OID.hpicfGenRptrTrapsPrefix,
'1.3.6.1.4.1.11.2.14.13': HP_ICF_OID.hpicfOEMs,
'1.3.6.1.4.1.11.2.14.13.1': HP_ICF_OID.hpicfFEHub,
}