#!/bin/bash

WEBUI="/home/onil/Documents/oobabooga_linux"
CONDA_ACTIVATE_PATH="$WEBUI/installer_files/conda/etc/profile.d/conda.sh"
ENV_PATH="$WEBUI/installer_files/env"

echo "source $CONDA_ACTIVATE_PATH"
source $CONDA_ACTIVATE_PATH

echo "conda activate $ENV_PATH"
conda activate $ENV_PATH

echo "Done"