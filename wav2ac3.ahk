#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; runs soundforge
!8::
Run, C:\Program Files (x86)\Sony\Sound Forge Pro 11.0\Forge110.exe, , max
IfWinActive, Sound Forge Pro 11.0
{

Send ^o

return

}
