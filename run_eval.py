import os
def main():

    # Update me
    model_path = r"/home/onil/Documents/oobabooga_linux/text-generation-webui/models/TheBloke_Llama-2-13B-chat-GPTQ_gptq-4bit-32g-actorder_True"
    model_name = "gptq_model-4bit-32g.safetensors"
    tasks = "--tasks hellaswag --limit=2"

    script_path = r"lm-evaluation-harness/main.py"
    model_type = r"hf-causal-experimental"
    
    
    
    model_args = f"pretrained={model_path},quantized={model_name},gptq_use_triton=True"
   
    cmd = f"python {script_path} --model {model_type} --model_args {model_args} {tasks}"
    print(cmd)
    os.system(cmd)
    

if __name__ =="__main__":
    main()