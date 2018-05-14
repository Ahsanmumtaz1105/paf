# Create a encrypted credential file to authenticate to Vsphere Server
Connect-VIServer -Server 10.17.6.250
New-VICredentialStoreItem -Host 10.17.6.250 -User NDI\ahsan_mumtaz -Password XYZ -File C:\git-repo\ivt_framework\AutomationPOC\setup_infra\In_creds