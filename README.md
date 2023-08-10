# lm-evaluation-harness-webui-wrapper
Wrapper utilizing the [oobabooga text-generation-webui](https://github.com/oobabooga/text-generation-webui) and [EleutherAI lm-evaluation-harness](https://raw.githubusercontent.com/EleutherAI/lm-evaluation-harness) to evaluate GPTQ version of models

# Supported OS
Linux 

## Instructions 
1. Follow the installation procedure for [oobabooga text-generation-webui](https://github.com/oobabooga/text-generation-webui)
2. Download a model and run it in the webui to ensure it is working. Shutdown the webui
3. Update the activate_env.sh with the path to the webui
4. Open a terminal in this directory and run 
```bash
chmod +x activate_env.sh
source activate_env.sh
```
5. Run the installation of the lm-evaluation-harness
```bash
git clone https://github.com/EleutherAI/lm-evaluation-harness
cd lm-evaluation-harness
pip install -e .
```
6. Update the *run_eval.py* script with model path variables

```bash
chmod +x run_script.sh
./run_script.sh
```

## TODO
1. Make process easier 
2. Add a file defining the variables
3. Add results from my own testing
