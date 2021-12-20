@ECHO OFF
REM BFCPEOPTIONSTART
REM Advanced BAT to EXE Converter www.BatToExeConverter.com
REM BFCPEEXE= Forms Auto Compiler by @OnyyTheBest
REM BFCPEICON=
REM BFCPEICONINDEX=-1
REM BFCPEEMBEDDISPLAY=0
REM BFCPEEMBEDDELETE=1
REM BFCPEADMINEXE=0
REM BFCPEINVISEXE=0
REM BFCPEVERINCLUDE=0
REM BFCPEVERVERSION=1.0.0.0
REM BFCPEVERPRODUCT= Forms AutoCompiler
REM BFCPEVERDESC= Dev @OnyyTheBest
REM BFCPEVERCOMPANY= MoonNetwork
REM BFCPEVERCOPYRIGHT= Copyright MoonNetwork 2020-2021
REM BFCPEOPTIONEND
@ECHO ON
title Forms Auto Compiler BY @OnyyTheBest
@ECHO ON
color a
@echo installing the dependencies  
pip install -r "C:\Users\Utente\Desktop\Google_forms_auto-compiler\main_sourcecode\requirements.txt"
echo off & color a & cls 
@echo Done
@echo starting test file
   echo off
py "C:\Users\Utente\Desktop\Google_forms_auto-compiler\main_sourcecode\main.py"
   echo off & color a & cls 

:init
 setlocal DisableDelayedExpansion
 set cmdInvoke=1
 set winSysFolder=System32
 set "batchPath=%~0"
 for %%k in (%0) do set batchName=%%~nk
 set "vbsGetPrivileges=%temp%\OEgetPriv_%batchName%.vbs"
 setlocal EnableDelayedExpansion
 goto :start

:start 
mode 70,20
cls
echo.
echo.
echo.
echo.
echo.                      
echo.                      
echo.                      
echo                      --------------------------
echo                        [Forms Auto Compiler]
echo                      --------------------------
echo               Do you want to activate the loop version?
echo                       [1] Yes
echo                       [2] No  
echo                       [3] YouTube
echo                       [4] Discord
echo                      ---------------------------
echo                     https://bit.ly/NovoInizioOnyy
echo                      ---------------------------
echo.
echo.
echo.            
echo.                                                                v1
choice /c:1234 /n
if %errorlevel% equ 1 goto :form
if %errorlevel% equ 2 goto :exit
if %errorlevel% equ 3 goto :yt
if %errorlevel% equ 4 goto :ds
                                                         v1

:form
py "C:\Users\Utente\Desktop\Google_forms_auto-compiler\main_sourcecode\onlyform.py"

:thanks
echo.
echo.
echo.
echo.
echo.                      
echo.                      
echo.                      
echo                      --------------------------
echo                             [Thank You]
echo                      --------------------------
echo                      Thank you for using my tool
echo                      ---------------------------
echo                     https://bit.ly/NovoInizioOnyy
echo                      ---------------------------
echo.
echo.
echo.            
echo. 
      
:close
exit

:yt
start https://bit.ly/NovoInizioOnyy
goto :thanks

:ds
start https://discord.gg/MNsJu4AjxJ