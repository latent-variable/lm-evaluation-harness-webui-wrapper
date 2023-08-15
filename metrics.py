
import json
import os

# Load the JSON file
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data

def get_avg_score(data, metric='acc'):
    # Extract the "results" section
    results_data = data.get("results", {})

    # Extract all the "acc" values from the results and calculate the average
    acc_values_from_results = [item[metric] for item in results_data.values()]
    avg_acc_from_results = sum(acc_values_from_results) / len(acc_values_from_results)
    
    return avg_acc_from_results


def extract_mmlu_score(file_path):
    data = load_data(file_path)
    score = get_avg_score(data, metric='acc')
    print(f'MMLU acc score: {score}')

def extract_arc_challenge_score(file_path):
    data = load_data(file_path)
    score = get_avg_score(data, metric='acc')
    print(f'ARC challenge acc score: {score}')

def extract_hellaswag_score(file_path):
    data = load_data(file_path)
    score = get_avg_score(data, metric='acc')
    print(f'Hellaswag acc score: {score}')

def extract_truthfulqa_score(file_path):
    data = load_data(file_path)
    score = get_avg_score(data, metric='mc2')
    print(f'truthfulqa mc2 score: {score}')

def get_metrics(mname='TheBloke_OpenOrca-Platypus2-13B-GPTQ_gptq-4bit-32g-actorder_True'):


    

    acc_file_path = f'output/{mname}-arc_challenge.json'
    extract_arc_challenge_score(acc_file_path)

    # mmlu_file_path = f'output/{mname}-MMLU.json'
    # extract_mmlu_score(mmlu_file_path)


    # hellaswag_file_path = f'output/{mname}-hellaswag.json'
    # extract_hellaswag_score(hellaswag_file_path)


    # truthfulqa_mc_file_path = f'output/{mname}-truthfulqa_mc.json'
    # extract_truthfulqa_score(truthfulqa_mc_file_path)

if __name__=="__main__":

    get_metrics()