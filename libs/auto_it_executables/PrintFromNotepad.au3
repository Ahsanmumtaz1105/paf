#include <GUIListView.au3>
#include <Array.au3>
#include <MsgBoxConstants.au3>
Sleep(3000)

$file_path = $cmdLine[1]
$printer_name = $cmdLine[2]
$file_path = "notepad.exe " & $file_path

Run($file_path, "")
WinActivate("test.txt - Notepad")
Sleep(5000)
WinActivate("test.txt - Notepad")
Sleep(1000)
Send("^P")
WinActivate("test.txt - Notepad")
Send("^p")
WinWait("Print")
Local $hWnd = WinWait("Print", "", 10)
Sleep(100)
WinActivate("Print")
Sleep(100)

$index1 = ControlListView(
"Print", "", "SysListView321", "FindItem", $printer_name)
Sleep(100)
ControlListView("Print", "", "SysListView321", "Select", $index1)
Sleep(100)
ControlClick($hWnd, "", "[CLASS:Button; INSTANCE:13]")
Sleep(100)
;~ Local $hWnd = WinWait("[CLASS:#32770]", 5)
;~ Sleep(100)
;~ ControlClick($hWnd,"","[CLASS:Edit; INSTANCE:1]")
;~ Sleep(100)
;~ Send("999999")
;~ Sleep(100)
;~ ControlClick($hWnd,"","[CLASS:Button; Text:OK]")
;~ Sleep(100)
;~ ControlClick("","","[CLASS:Button; INSTANCE:1]")
;~ Run("notepad.exe")
;~ WinWaitActive("Untitled - Notepad")
;~ Send("This is some text.")
;~ Send("^P")