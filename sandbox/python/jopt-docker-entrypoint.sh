#!/bin/sh
set -eu

echo "Trying to download Python-REST-Client-Examples"

folder="/home/coder/project/python.rest.examples/"
url="https://github.com/DNA-Evolutions/Python-REST-Client-Examples.git"

# Clone the repository if the folder does not exist
if [ ! -d "${folder}" ]; then
    echo "Cloning repository from ${url} to ${folder}"
    git clone "${url}" "${folder}"
else
    echo "Clone skipped as the folder ${folder} already exists. If you want a 'fresh' clone, choose another volume or rename the existing folder."
fi

# Ensure project directory is in the Python path
export PYTHONPATH=${PYTHONPATH:-""}:${folder}

# Activate the virtual environment
. /opt/venv/bin/activate

# Check if installation is needed and install if necessary
if [ -d "${folder}" ]; then
    cd "${folder}"
    if [ ! -f ".installed" ]; then
        echo "Running pip install -e . in ${folder}"
        if pip install -e .; then
            echo "Installation completed successfully."
            touch .installed
        else
            echo "Installation failed."
        fi
    else
        echo "Installation skipped as it appears to be already done."
    fi
else
    echo "Folder ${folder} does not exist. Skipping installation."
fi

# Ensure .vscode directory exists within the project folder
mkdir -p ${folder}.vscode

# Ensure VS Code uses the virtual environment's interpreter
echo "{
    \"python.pythonPath\": \"/opt/venv/bin/python\"
}" > ${folder}.vscode/settings.json

exec /usr/bin/entrypoint.sh "$@"
