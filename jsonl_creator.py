import os
import json

# Directory containing the refined data files
refined_data_dir = 'Refined_Data'

# Read the system role content from the file
with open('system_role_json_friendly.txt', 'r') as system_file:
    system_content = system_file.read().strip()

# List all files in the directory
files = os.listdir(refined_data_dir)

# Filter out the prompt and completion files
prompt_files = sorted([f for f in files if f.endswith('o.json')])
completion_files = sorted([f for f in files if f.endswith('f.json')])

# Open a new JSONL file to write the output
with open('refined_output_without_system.jsonl', 'w') as jsonl_file:
    # Iterate over the prompt and completion files
    for prompt_file, completion_file in zip(prompt_files, completion_files):
        # Read the prompt content
        with open(os.path.join(refined_data_dir, prompt_file), 'r') as pf:
            prompt_data = json.load(pf)
            prompt_content = prompt_data.get('content', '').strip()
        
        # Read the completion content
        with open(os.path.join(refined_data_dir, completion_file), 'r') as cf:
            completion_data = json.load(cf)
            completion_content = completion_data.get('content', '').strip()
        
        # Create a JSON object
        json_object = {
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": prompt_content},
                {"role": "assistant", "content": completion_content}
            ]
        }
        
        # Write the JSON object to the JSONL file
        jsonl_file.write(json.dumps(json_object) + '\n')

        print(f"Processed {prompt_file} and {completion_file}")
