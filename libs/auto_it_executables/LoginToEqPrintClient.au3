#include <GUIListView.au3>
#include <Array.au3>

$user_id = $cmdLine[1]
$password = $cmdLine[2]
$renamed_doc_name = $cmdLine[3]

ControlClick("Shell_TrayWnd" , "", "[CLASS:Button; INSTANCE:2]")
WinActivate("Equitrac - Messages")
WinActivate("Equitrac")
Local $hwnd = WinWait("Equitrac")
Sleep(2000)
ControlClick($hwnd , "", "[CLASS:Edit; INSTANCE:1]")
Send("^a")
Send("{DEL}")
Send($user_id)
Sleep(2000)
ControlClick($hwnd , "", "[CLASS:Edit; INSTANCE:2]")
Send("^a")
Send("{DEL}")
Send($password)
Sleep(1000)
ControlClick($hwnd , "", "[CLASS:Button; INSTANCE:2]")
Local $hwnd = WinWait("Equitrac")
Sleep(2000)
ControlClick($hwnd , "", "[CLASS:Edit; INSTANCE:1]")
Send("^a")
Send("{DEL}")
Send($renamed_doc_name)
ControlClick("Equitrac", "OK", "[CLASS:Button;INSTANCE:1]")
Sleep(2000)
Local $hwnd = WinWait("Cost preview")
WinActivate("Cost preview")
Sleep(2000)
ControlClick("Cost preview", "&Accept", "[CLASS:Button;INSTANCE:5]")