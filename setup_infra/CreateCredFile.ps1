# Create a encrypted credential file to authenticate to Vsphere Server
Connect-VIServer -Server 10.x.x.x
New-VICredentialStoreItem -Host 10.x.x.x -User username -Password XYZ -File C:\git-repo\ivt_framework\AutomationPOC\setup_infra\In_creds
