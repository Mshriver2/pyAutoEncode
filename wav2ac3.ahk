#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; runs soundforge
!8::

;opens soundforge
Run, C:\Program Files (x86)\Sony\Sound Forge Pro 11.0\Forge110.exe, , max

WinActivate Sound Forge Pro 11.0
Sleep, 5000

;opens the file open dialog
Send ^o
Sleep, 2000

;paste's in the wav name from python script
Send ^v
Sleep, 1000
Send {Enter}

;waits for file to load then does a save as
Sleep, 20000
Send !{F2}
Sleep, 3000
Send {Enter}

;waits for audio to finish saving then closes popup message
Sleep, 120000
Send {Tab}
Sleep, 500
Send {Enter}

return
