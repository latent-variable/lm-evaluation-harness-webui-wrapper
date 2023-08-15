# lm-evaluation-harness-webui-wrapper
Have you ever pondered how quantization might affect model performance, or what the trade-off is between quantized methods? Me too. Let's explore together!

This wrapper leverages both [oobabooga text-generation-webui](https://github.com/oobabooga/text-generation-webui) and [EleutherAI lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) to evaluate GPTQ version models on various benchmarks including ARC, HellaSwag, MMLU, and TruthfulQA, akin to the [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)

# Test Results 
[Original Model](https://huggingface.co/Open-Orca/OpenOrca-Platypus2-13B) [Quantized Model](https://huggingface.co/TheBloke/OpenOrca-Platypus2-13B-GPTQ) ARC: 25-shot, arc-challenge (acc_norm) matching EleutherAI lm-evaluation-harness

| Model Name              | Bits    |     GS    | ARC         | Act Order |
|-------------------------|---------|-----------|-------------|-----------|
| OpenOrca Platypus2 13B  | 16-bit  |     NA    | 62.88%      |    NA     |
| OpenOrca Platypus2 13B  | 8-bit   |   None    | 62.88%      |   Yes     |
| OpenOrca Platypus2 13B  | 4-bit   |     32    | 62.28%      |   Yes     |
| OpenOrca Platypus2 13B  | 4-bit   |    128    | 62.62%      |    No     |

Note the 4bit 32GS model reports lower acc_norm then the 4bit 128GS but higher acc of 58.02% vs 57.59%

# Supported OS
Linux & Windows

## Linux Instructions 
1. Follow the installation procedure for [oobabooga text-generation-webui](https://github.com/oobabooga text-generation-webui).
2. Download a model and run it in the webui to ensure it is working. Then, shutdown the webui.
3. Update `activate_env.sh` with the path to the webui.
4. Open a terminal in this directory and run:
```bash
chmod +x activate_env.sh
source activate_env.sh
```
5. Proceed with the installation of lm-evaluation-harness 
```bash
git clone https://github.com/EleutherAI/lm-evaluation-harness
cd lm-evaluation-harness
pip install -e .
```
6. Update the *model.json* file model path

```bash
chmod +x run_script.sh
./run_script.sh
```

## Windows Instructions 
1. Follow the installation procedure for [oobabooga text-generation-webui](https://github.com/oobabooga text-generation-webui).
2. Download a model and run it in the webui to ensure it is working. Then, shutdown the webui.
3. Update `activate_env.bat` with the path to the webui.
4. Run the 'activate_env.bat'
5. Proceed with the installation of lm-evaluation-harness big refactor branch
```bash
git clone https://github.com/EleutherAI/lm-evaluation-harness
cd lm-evaluation-harness
git checkout big-refactor
pip install -e .
```
6. Update the *model.json* file model path

```bash
./run_script.bat
```


## TODO
- Make the process more user-friendly.
- Add a file for defining variables.
- Add results with 3bit models
