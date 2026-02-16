@echo off
start "" "%~dp0FreePieOpenVR1.2.3\FreePIE.exe"

set "SCRIPT_PATH=%~dp0VRcompanionHogwartsLegacy.py"
echo %SCRIPT_PATH%| clip

echo set shell = CreateObject("WScript.Shell") > "%temp%\run_freepie.vbs"
echo WScript.Sleep 1000 >> "%temp%\run_freepie.vbs"
echo shell.SendKeys "^o" >> "%temp%\run_freepie.vbs"
echo WScript.Sleep 1000 >> "%temp%\run_freepie.vbs"
echo shell.SendKeys "^v" >> "%temp%\run_freepie.vbs"
echo WScript.Sleep 500 >> "%temp%\run_freepie.vbs"
echo shell.SendKeys "{ENTER}" >> "%temp%\run_freepie.vbs"
echo WScript.Sleep 1000 >> "%temp%\run_freepie.vbs"
echo shell.SendKeys "{F5}" >> "%temp%\run_freepie.vbs"
echo WScript.Sleep 2500 >> "%temp%\run_freepie.vbs"

cscript //nologo "%temp%\run_freepie.vbs"
del "%temp%\run_freepie.vbs"