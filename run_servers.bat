@echo off
call myvenv\Scripts\activate
call code .
cd /d "E:\My OFFICE\PROJECTS\Freelauncing Agency\LOCAL PROJECTS\Rimsha Mehtab"
start cmd /k "python manage.py runserver"
timeout /t 12
start cmd /k "ngrok http 8000"
