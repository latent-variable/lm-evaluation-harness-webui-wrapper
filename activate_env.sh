#!/bin/bash

WEBUI="/home/onil/Documents/oobabooga_linux"


CONDA_ACTIVATE_PATH="$WEBUI/installer_files/conda/etc/profile.d/conda.sh"
CONDA_PATH="$WEBUI/installer_files/conda/bin/conda"
ENV_PATH="$WEBUI/installer_files/env"


echo "$CONDA_ACTIVATE_PATH"
source $CONDA_ACTIVATE_PATH 

source $CONDA_PATH
echo "conda activate $ENV_PATH"
source activate $ENV_PATH 
echo "Done"
