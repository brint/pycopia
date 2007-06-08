# python
# This file is generated by a program (mib2py). 

import HOST_RESOURCES_MIB

OIDMAP = {
'1.3.6.1.2.1.25': HOST_RESOURCES_MIB.host,
'1.3.6.1.2.1.25.1': HOST_RESOURCES_MIB.hrSystem,
'1.3.6.1.2.1.25.2': HOST_RESOURCES_MIB.hrStorage,
'1.3.6.1.2.1.25.2.1': HOST_RESOURCES_MIB.hrStorageTypes,
'1.3.6.1.2.1.25.3': HOST_RESOURCES_MIB.hrDevice,
'1.3.6.1.2.1.25.3.1': HOST_RESOURCES_MIB.hrDeviceTypes,
'1.3.6.1.2.1.25.3.9': HOST_RESOURCES_MIB.hrFSTypes,
'1.3.6.1.2.1.25.4': HOST_RESOURCES_MIB.hrSWRun,
'1.3.6.1.2.1.25.5': HOST_RESOURCES_MIB.hrSWRunPerf,
'1.3.6.1.2.1.25.6': HOST_RESOURCES_MIB.hrSWInstalled,
'1.3.6.1.2.1.25.7': HOST_RESOURCES_MIB.hrMIBAdminInfo,
'1.3.6.1.2.1.25.7.1': HOST_RESOURCES_MIB.hostResourcesMibModule,
'1.3.6.1.2.1.25.7.2': HOST_RESOURCES_MIB.hrMIBCompliances,
'1.3.6.1.2.1.25.7.3': HOST_RESOURCES_MIB.hrMIBGroups,
'1.3.6.1.2.1.25.1.1': HOST_RESOURCES_MIB.hrSystemUptime,
'1.3.6.1.2.1.25.1.2': HOST_RESOURCES_MIB.hrSystemDate,
'1.3.6.1.2.1.25.1.3': HOST_RESOURCES_MIB.hrSystemInitialLoadDevice,
'1.3.6.1.2.1.25.1.4': HOST_RESOURCES_MIB.hrSystemInitialLoadParameters,
'1.3.6.1.2.1.25.1.5': HOST_RESOURCES_MIB.hrSystemNumUsers,
'1.3.6.1.2.1.25.1.6': HOST_RESOURCES_MIB.hrSystemProcesses,
'1.3.6.1.2.1.25.1.7': HOST_RESOURCES_MIB.hrSystemMaxProcesses,
'1.3.6.1.2.1.25.2.2': HOST_RESOURCES_MIB.hrMemorySize,
'1.3.6.1.2.1.25.4.1': HOST_RESOURCES_MIB.hrSWOSIndex,
'1.3.6.1.2.1.25.6.1': HOST_RESOURCES_MIB.hrSWInstalledLastChange,
'1.3.6.1.2.1.25.6.2': HOST_RESOURCES_MIB.hrSWInstalledLastUpdateTime,
'1.3.6.1.2.1.25.2.3.1.1': HOST_RESOURCES_MIB.hrStorageIndex,
'1.3.6.1.2.1.25.2.3.1.2': HOST_RESOURCES_MIB.hrStorageType,
'1.3.6.1.2.1.25.2.3.1.3': HOST_RESOURCES_MIB.hrStorageDescr,
'1.3.6.1.2.1.25.2.3.1.4': HOST_RESOURCES_MIB.hrStorageAllocationUnits,
'1.3.6.1.2.1.25.2.3.1.5': HOST_RESOURCES_MIB.hrStorageSize,
'1.3.6.1.2.1.25.2.3.1.6': HOST_RESOURCES_MIB.hrStorageUsed,
'1.3.6.1.2.1.25.2.3.1.7': HOST_RESOURCES_MIB.hrStorageAllocationFailures,
'1.3.6.1.2.1.25.3.2.1.1': HOST_RESOURCES_MIB.hrDeviceIndex,
'1.3.6.1.2.1.25.3.2.1.2': HOST_RESOURCES_MIB.hrDeviceType,
'1.3.6.1.2.1.25.3.2.1.3': HOST_RESOURCES_MIB.hrDeviceDescr,
'1.3.6.1.2.1.25.3.2.1.4': HOST_RESOURCES_MIB.hrDeviceID,
'1.3.6.1.2.1.25.3.2.1.5': HOST_RESOURCES_MIB.hrDeviceStatus,
'1.3.6.1.2.1.25.3.2.1.6': HOST_RESOURCES_MIB.hrDeviceErrors,
'1.3.6.1.2.1.25.3.3.1.1': HOST_RESOURCES_MIB.hrProcessorFrwID,
'1.3.6.1.2.1.25.3.3.1.2': HOST_RESOURCES_MIB.hrProcessorLoad,
'1.3.6.1.2.1.25.3.4.1.1': HOST_RESOURCES_MIB.hrNetworkIfIndex,
'1.3.6.1.2.1.25.3.5.1.1': HOST_RESOURCES_MIB.hrPrinterStatus,
'1.3.6.1.2.1.25.3.5.1.2': HOST_RESOURCES_MIB.hrPrinterDetectedErrorState,
'1.3.6.1.2.1.25.3.6.1.1': HOST_RESOURCES_MIB.hrDiskStorageAccess,
'1.3.6.1.2.1.25.3.6.1.2': HOST_RESOURCES_MIB.hrDiskStorageMedia,
'1.3.6.1.2.1.25.3.6.1.3': HOST_RESOURCES_MIB.hrDiskStorageRemoveble,
'1.3.6.1.2.1.25.3.6.1.4': HOST_RESOURCES_MIB.hrDiskStorageCapacity,
'1.3.6.1.2.1.25.3.7.1.1': HOST_RESOURCES_MIB.hrPartitionIndex,
'1.3.6.1.2.1.25.3.7.1.2': HOST_RESOURCES_MIB.hrPartitionLabel,
'1.3.6.1.2.1.25.3.7.1.3': HOST_RESOURCES_MIB.hrPartitionID,
'1.3.6.1.2.1.25.3.7.1.4': HOST_RESOURCES_MIB.hrPartitionSize,
'1.3.6.1.2.1.25.3.7.1.5': HOST_RESOURCES_MIB.hrPartitionFSIndex,
'1.3.6.1.2.1.25.3.8.1.1': HOST_RESOURCES_MIB.hrFSIndex,
'1.3.6.1.2.1.25.3.8.1.2': HOST_RESOURCES_MIB.hrFSMountPoint,
'1.3.6.1.2.1.25.3.8.1.3': HOST_RESOURCES_MIB.hrFSRemoteMountPoint,
'1.3.6.1.2.1.25.3.8.1.4': HOST_RESOURCES_MIB.hrFSType,
'1.3.6.1.2.1.25.3.8.1.5': HOST_RESOURCES_MIB.hrFSAccess,
'1.3.6.1.2.1.25.3.8.1.6': HOST_RESOURCES_MIB.hrFSBootable,
'1.3.6.1.2.1.25.3.8.1.7': HOST_RESOURCES_MIB.hrFSStorageIndex,
'1.3.6.1.2.1.25.3.8.1.8': HOST_RESOURCES_MIB.hrFSLastFullBackupDate,
'1.3.6.1.2.1.25.3.8.1.9': HOST_RESOURCES_MIB.hrFSLastPartialBackupDate,
'1.3.6.1.2.1.25.4.2.1.1': HOST_RESOURCES_MIB.hrSWRunIndex,
'1.3.6.1.2.1.25.4.2.1.2': HOST_RESOURCES_MIB.hrSWRunName,
'1.3.6.1.2.1.25.4.2.1.3': HOST_RESOURCES_MIB.hrSWRunID,
'1.3.6.1.2.1.25.4.2.1.4': HOST_RESOURCES_MIB.hrSWRunPath,
'1.3.6.1.2.1.25.4.2.1.5': HOST_RESOURCES_MIB.hrSWRunParameters,
'1.3.6.1.2.1.25.4.2.1.6': HOST_RESOURCES_MIB.hrSWRunType,
'1.3.6.1.2.1.25.4.2.1.7': HOST_RESOURCES_MIB.hrSWRunStatus,
'1.3.6.1.2.1.25.5.1.1.1': HOST_RESOURCES_MIB.hrSWRunPerfCPU,
'1.3.6.1.2.1.25.5.1.1.2': HOST_RESOURCES_MIB.hrSWRunPerfMem,
'1.3.6.1.2.1.25.6.3.1.1': HOST_RESOURCES_MIB.hrSWInstalledIndex,
'1.3.6.1.2.1.25.6.3.1.2': HOST_RESOURCES_MIB.hrSWInstalledName,
'1.3.6.1.2.1.25.6.3.1.3': HOST_RESOURCES_MIB.hrSWInstalledID,
'1.3.6.1.2.1.25.6.3.1.4': HOST_RESOURCES_MIB.hrSWInstalledType,
'1.3.6.1.2.1.25.6.3.1.5': HOST_RESOURCES_MIB.hrSWInstalledDate,
'1.3.6.1.2.1.25.7.3.1': HOST_RESOURCES_MIB.hrSystemGroup,
'1.3.6.1.2.1.25.7.3.2': HOST_RESOURCES_MIB.hrStorageGroup,
'1.3.6.1.2.1.25.7.3.3': HOST_RESOURCES_MIB.hrDeviceGroup,
'1.3.6.1.2.1.25.7.3.4': HOST_RESOURCES_MIB.hrSWRunGroup,
'1.3.6.1.2.1.25.7.3.5': HOST_RESOURCES_MIB.hrSWRunPerfGroup,
'1.3.6.1.2.1.25.7.3.6': HOST_RESOURCES_MIB.hrSWInstalledGroup,
}