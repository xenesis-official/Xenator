@echo off
echo "######################## XENETOR Voice Code Genrator ########################"
echo "########################### copyright@XENETOR-VCG ###########################"

echo "Starting XENETOR Voice Code Genrator "

@echo off
setlocal EnableDelayedExpansion

rem Count the number of files in this dir (just as an example)
set n=0
for %%f in (*.*) do set /A n+=1

rem Fill "bar" variable with 70 characters
set "bar="
for /L %%i in (1,1,70) do set "bar=!bar!X"

rem Fill "space" variable with filler spaces
set "space="
for /L %%i in (1,1,110) do set "space=!space!_"

rem "Process" the files and show the progress bar in the title
set i=0
echo Processing files:
for %%f in (*.*) do (
   set /A i+=1, percent=i*100/n, barLen=70*percent/100
   for %%a in (!barLen!) do title !percent!%%  !bar:~0,%%a!%space%
   echo !i!- %%f
   ping -n 1 localhost > NUL
)

title Xenetor Command Prompt
cls
echo "######################## XENETOR Voice Code Genrator ########################"
echo "########################### copyright@XENETOR-VCG ###########################"
python speech.py
cls
echo "######################## XENETOR Voice Code Genrator ########################"
echo "########################### copyright@XENETOR-VCG ###########################"
echo "CREATING Code Base"

v_output.txt

