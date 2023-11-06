set root=C:\ProgramData\Anaconda3
call %root%\Scripts\activate.bat %root%
::call conda env list
::call conda activate base
::call cd C:\Users\Administrator\app
call cd ..
::uvicorn main:app --reload --port 8000
uvicorn main:app --reload
pause
