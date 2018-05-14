#include <GUIListView.au3>
#include <Array.au3>

$user_id = $cmdLine[1]
$password = $cmdLine[2]
$rename_doc_name = $cmdLine[3]

Sleep(2000)
WinActivate("Equitrac")
Local $hwnd = WinWait("Equitrac")
Sleep(2000)
ControlClick($hwnd ,"","[CLASS:Edit; INSTANCE:1]")
Send("^a")
Send("{DEL}")
Send($user_id)
Sleep(2000)
Send("{TAB}")
ControlClick($hwnd ,"","[CLASS:Edit; INSTANCE:2]")
Send("^a")
Send("{DEL}")
Send($password)
Sleep(2000)
ControlClick($hwnd ,"OK","[CLASS:Button; INSTANCE:2]")
Sleep(2000)
Local $hwnd = WinWait("Equitrac")
Sleep(2000)
ControlClick($hwnd ,"","[CLASS:Edit; INSTANCE:1]")
Sleep(2000)
Send("^a")
Send("{DEL}")
Send($rename_doc_name)
ControlClick("Equitrac" ,"OK","[CLASS:Button;INSTANCE:1]")
Sleep(2000)
Local $hwnd = WinWait("Cost preview")
WinActivate("Cost preview")
Sleep(2000)
ControlClick("Cost preview" ,"&Accept","[CLASS:Button;INSTANCE:5]")
