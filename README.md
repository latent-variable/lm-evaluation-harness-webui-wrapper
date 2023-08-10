# lm-evaluation-harness-webui-wrapper
Have you ever pondered how quantization might affect model performance, or what the trade-off is between quantized methods? Me too. Let's explore together!

This wrapper leverages both [oobabooga text-generation-webui](https://github.com/oobabooga/text-generation-webui) and [EleutherAI lm-evaluation-harness](https://raw.githubusercontent.com/EleutherAI/lm-evaluation-harness)to evaluate GPTQ version models on various benchmarks including ARC, HellaSwag, MMLU, and TruthfulQA, akin to the [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)

# Supported OS
Linux 

## Instructions 
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
6. Update the *run_eval.py* script with model path variables

```bash
chmod +x run_script.sh
./run_script.sh
```

## TODO
- Make the process more user-friendly.
- Add a file for defining variables.
- Include results from personal testing.
