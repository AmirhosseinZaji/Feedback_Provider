import os
import json
import re

def clean_for_json(text):
    # Replace line breaks with \n
    text = text.replace('\n', '\\n')
    # Escape double quotes
    text = text.replace('"', '\\"')
    # Remove any remaining control characters
    text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)
    return text

def process_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".txt") or filename.endswith(".json"):
            with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                cleaned_content = clean_for_json(content)
                
                output_data = {
                    "filename": filename,
                    "content": cleaned_content
                }
                
                output_filename = os.path.splitext(filename)[0] + ".json"
                with open(os.path.join(output_dir, output_filename), "w", encoding='utf-8') as outfile:
                    json.dump(output_data, outfile, ensure_ascii=False, indent=2)

    print("Processing complete. Refined data saved in the Refined_Data folder.")

# Process files
process_files("Data", "Refined_Data")
