import os
def main():

    # Update me
    model_path = r"/home/onil/Documents/oobabooga_linux/text-generation-webui/models/TheBloke_Llama-2-13B-chat-GPTQ_gptq-4bit-32g-actorder_True"
    model_name = "gptq_model-4bit-32g.safetensors"
    tasks = "--tasks hellaswag --limit=2"
    output_path = "--output_path output"


    model_args = f"--model_args pretrained={model_path},quantized={model_name},gptq_use_triton=True"
    script_path = r"lm-evaluation-harness/main.py"
    model_type = r"--model  hf-causal-experimental"

   
    cmd = f"python {script_path} {model_type}  {model_args} {tasks} {output_path}"
    print(cmd)
    os.system(cmd)
    

if __name__ =="__main__":
    main()