#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; runs soundforge
!8::
Run, C:\Program Files (x86)\Sony\Sound Forge Pro 11.0\Forge110.exe, , max

WinActivate Sound Forge Pro 11.0
Sleep, 5000
Send ^o
Sleep, 2000
Send ^v
Sleep, 1000
Send {Enter}
Sleep, 20000
Send !{F2}
Sleep, 3000
Send {Enter}
Sleep, 120000
Send {Tab}
Sleep, 500
Send {Enter}

return
