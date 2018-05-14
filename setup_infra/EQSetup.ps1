param([string]$cred_file_path, $folder_name, $VMName, $VMHost_name, $datastore_name, $template_name, $logs_path, $domain_name, $domain_admin_user, $domain_admin_pwd, $VM_user_name, $VM_user_pwd, $domain_user, $domain_pwd, $is_control_suite, $is_eq, $eq_build_version, $cs_path, $eq_path, $os_cus_spec )

#Stop an error from occurring when a transcript is already stopped
$ErrorActionPreference="SilentlyContinue"

#Reset the error level before starting the transcript
$ErrorActionPreference="Continue"

#Add the VMWare Snap-in
#Add-PSSnapin -Name VMWare.VimAutomation.Core
Get-Module –ListAvailable VM* | Import-Module

#Get the Credentials
$creds = Get-VICredentialStoreItem -file  $cred_file_path

#Connect to the server using the credentials file
Connect-VIServer -Server $creds.host -User $creds.User -Password $creds.Password

$VMHost = Get-VMHost $VMHost_name 
$Datastore = Get-Datastore $datastore_name
$myTemplate = Get-Template -Name $template_name

$OSCusSpec = Get-OSCustomizationSpec -Name $os_cus_spec

$vm = New-VM -Name $VMName -Location $folder_name -Template $myTemplate -VMHost $VMHost -Datastore $Datastore -OSCustomizationSpec $OSCusSpec
 
 Wait-Tools -VM $VMName
Start-VM -VM $VMName -Confirm:$false

Wait-Tools -VM $VMName

function GetHostname {
try
{
$vm = Get-VM -name $VMName
while($vm -eq $null)
{
Start-Sleep -s 120
GetHostname }
$hostname = $vm.ExtensionData.Guest.Hostname
return $hostname.ToLower()
}
catch { GetHostname }
}

$vmhostname = $null
$dns = $VMName + "." + $domain_name

while($dns.ToLower() -ne $vmhostname){
$vmhostname = GetHostname }

Wait-Tools -VM $VMName
# User Add in SQL Server
Invoke-VMScript -vm $VMName -GuestUser $VM_user_name -GuestPassword $VM_user_pwd -ScriptText { C:\scripts\createUser.bat -Verb runAs -wait } -ScriptType Powershell

if($is_control_suite –eq "TRUE") {

#Copy ControlSuite Build from shared repo
$copyCSBuild = @'
$src_dir = '$src_path'
$dst_dir = "C:\Installers\CS\"
Copy-Item -Path $src_dir -Destination $dst_dir
'@
$copyCSBuild = $copyCSBuild.Replace('$src_path', $cs_path)
Wait-Tools -VM $VMName
Invoke-VMScript -vm $VMName -GuestUser $domain_admin_user -GuestPassword $domain_admin_pwd -ScriptText $copyCSBuild -ScriptType Powershell

# Install ControlSuite
Invoke-VMScript -vm $VMName -GuestUser $domain_admin_user -GuestPassword $domain_admin_pwd -scriptText {C:\scripts\install_cs.bat $PACKAGES="""AAService, SSDService, LicenseServer, DDBService""" -Verb runAs -wait}-ScriptType PowerShell}

if(($is_eq –eq "TRUE") -and ($is_control_suite –eq "TRUE")) {

#Copy EQ build
$copyEQBuild = @'
$src_dir = '$src_path'
$dst_dir = "C:\Installers\EQ\"
Copy-Item -Path $src_dir -Destination $dst_dir
'@
$copyEQBuild = $copyEQBuild.Replace('$src_path', $eq_path)
Wait-Tools -VM $VMName
Invoke-VMScript -vm $VMName -GuestUser $domain_admin_user -GuestPassword $domain_admin_pwd -ScriptText $copyEQBuild -ScriptType Powershell

# Install Equitrac
Invoke-VMScript  -vm $VMName -GuestUser $VM_user_name -GuestPassword $VM_user_pwd -ScriptText {C:\scripts\install_eq.bat $ADDLOCAL="""AdministrativeApplications,AuxApplications,CAS,Common,DCS,DCE,DME,DRE,DWS,DeviceMonitoringConsole,F.EQXLPD,ReportManager,SPE,ScanClient,ServerComponents,SystemManager,UserDashboard,WebClient,WebSystemManager""" -Verb runAs -wait } -ScriptType Powershell}

#Clean Up
Disconnect-VIServer -Force -Confirm:$false