import os
import time
import json
import platform

from metrics import get_metrics


with open('model.json', 'r') as file:
  parameters = json.load(file)

model_path = os.path.dirname(parameters['model_path'])
model_name = os.path.basename(parameters['model_path'])
mname = os.path.basename(model_path)
# Leave me
script_path = r"lm-evaluation-harness/main.py"

if platform.system() == 'Windows':
    print('Windows')
    model_type = r"--model hf"
    model_spec = r'gptq'
    use_triton = "False"
elif platform.system() == 'Linux':
    print(' Linux')
    model_type = r"--model hf-causal-experimental"
    model_spec = r'quantized'
    use_triton = "True"
else:
    print('Unknown OS')
    exit(-1)

limit = ""
# limit = "--limit=2"

def run_harness(task_name, tasks, few_shot):

    
    output_path = f"--output_path output/{mname}-{task_name}.json"

    model_args = f"--model_args pretrained={model_path},{model_spec}={model_name},gptq_use_triton={use_triton}"
    
    print(f'Executing task {task_name}, with few_shot {few_shot}')

    cmd = f"python {script_path} {model_type}  {model_args} {tasks} {few_shot} {output_path} {limit}"
    
    print(cmd)
    os.system(cmd)
    


def run_arc_challenge():
    task_name = 'arc_challenge'
    tasks = f"--tasks {task_name}" 
    few_shot = "--num_fewshot 25"
    run_harness(task_name, tasks, few_shot)


def run_hellaswag():
    task_name = 'hellaswag'
    tasks = f"--tasks {task_name}"
    few_shot = "--num_fewshot 10"
    run_harness(task_name, tasks, few_shot)


def run_truthfulqa():
    task_name = 'truthfulqa_mc'
    tasks = f"--tasks {task_name}"
    few_shot = "--num_fewshot 0"
    run_harness(task_name, tasks, few_shot)


def run_mmlu():
    task_name = 'MMLU'
    task_list = ','.join([
                     'hendrycksTest-abstract_algebra',
                     'hendrycksTest-anatomy',
                     'hendrycksTest-astronomy',
                     'hendrycksTest-business_ethics',
                     'hendrycksTest-clinical_knowledge',
                     'hendrycksTest-college_biology',
                     'hendrycksTest-college_chemistry',
                     'hendrycksTest-college_computer_science',
                     'hendrycksTest-college_mathematics',
                     'hendrycksTest-college_medicine',
                     'hendrycksTest-college_physics',
                     'hendrycksTest-computer_security',
                     'hendrycksTest-conceptual_physics',
                     'hendrycksTest-econometrics',
                     'hendrycksTest-electrical_engineering',
                     'hendrycksTest-elementary_mathematics',
                     'hendrycksTest-formal_logic',
                     'hendrycksTest-global_facts',
                     'hendrycksTest-high_school_biology',
                     'hendrycksTest-high_school_chemistry',
                     'hendrycksTest-high_school_computer_science',
                     'hendrycksTest-high_school_european_history',
                     'hendrycksTest-high_school_geography',
                     'hendrycksTest-high_school_government_and_politics',
                     'hendrycksTest-high_school_macroeconomics',
                     'hendrycksTest-high_school_mathematics',
                     'hendrycksTest-high_school_microeconomics',
                     'hendrycksTest-high_school_physics',
                     'hendrycksTest-high_school_psychology',
                     'hendrycksTest-high_school_statistics',
                     'hendrycksTest-high_school_us_history',
                     'hendrycksTest-high_school_world_history',
                     'hendrycksTest-human_aging',
                     'hendrycksTest-human_sexuality',
                     'hendrycksTest-international_law',
                     'hendrycksTest-jurisprudence',
                     'hendrycksTest-logical_fallacies',
                     'hendrycksTest-machine_learning',
                     'hendrycksTest-management',
                     'hendrycksTest-marketing',
                     'hendrycksTest-medical_genetics',
                     'hendrycksTest-miscellaneous',
                     'hendrycksTest-moral_disputes',
                     'hendrycksTest-moral_scenarios',
                     'hendrycksTest-nutrition',
                     'hendrycksTest-philosophy',
                     'hendrycksTest-prehistory',
                     'hendrycksTest-professional_accounting',
                     'hendrycksTest-professional_law',
                     'hendrycksTest-professional_medicine',
                     'hendrycksTest-professional_psychology',
                     'hendrycksTest-public_relations',
                     'hendrycksTest-security_studies',
                     'hendrycksTest-sociology',
                     'hendrycksTest-us_foreign_policy',
                     'hendrycksTest-virology',
                     'hendrycksTest-world_religions'
                    ])

    
    tasks = f"--tasks {task_list} "
    few_shot = "--num_fewshot 5"
    run_harness(task_name, tasks, few_shot)


def main():
    tik = time.time()

    #run each benchmark
    
    run_arc_challenge()
    # run_mmlu()
    # run_hellaswag()
    # run_truthfulqa()
    

    # Get final results 
    get_metrics(mname)
    
    elapsed_time_seconds = time.time() - tik
    elapsed_time_struct = time.gmtime(elapsed_time_seconds)
    formatted_time = time.strftime('%H:%M:%S', elapsed_time_struct)
    print('Completed in:', formatted_time)
    
   
    

if __name__ =="__main__":
    main()
