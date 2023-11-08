@ECHO OFF
set PYTHONPATH=%CD%
ECHO "%PYTHONPATH%"
call .venv/Scripts/activate.bat
python tabor_api/server/app.py
@ECHO ON