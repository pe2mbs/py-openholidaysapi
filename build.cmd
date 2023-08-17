@ECHO OFF
ECHO "Building the package"
python -m build --wheel --no-isolation
IF NOT ERRORLEVEL 0 GOTO ERROR
IF NOT DEFINED WHEEL_FOLDER GOTO DONE
ECHO "Coping package distibution to %WHEEL_FOLDER%"
COPY /Y dist\*.whl %WHEEL_FOLDER%
GOTO DONE

:ERROR
ECHO "Some ERROR"

:DONE