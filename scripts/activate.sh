echo "INFO: Make sure to use 'source' and not 'sh' to activate the environment."
winpty python.exe -m venv .venv
source .venv/Scripts/activate
winpty python.exe -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
