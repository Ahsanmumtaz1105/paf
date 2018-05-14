$basedir = "\\ROBO-REPO\testreports\"

$today   = (Get-Date).ToString('ddMMyyyy')

$targetdir = $basedir+$today 

if(!(Test-Path -Path $targetdir))
{
    New-Item -Path $basedir -Type Directory -Name $today
}

Set-Location -Path "E:\git-repo\ivt_framework\AutomationPOC\tests"

pybot  -d $targetdir -T -l demo_log.html -r demo_result.html -A ..\test_runner\test_suite.txt
