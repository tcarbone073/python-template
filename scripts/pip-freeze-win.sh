# Python on Windows has issues with redirecting pip freeze without using parameters
# '-Xallow-non-tty' and '-Xplain'
winpty -Xallow-non-tty -Xplain python.exe -m pip freeze > requirements.txt