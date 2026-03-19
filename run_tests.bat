@echo off

echo Starting Automation Dashboard...

cd /d %~dp0

call venv\Scripts\activate

python test_gui.py

pause