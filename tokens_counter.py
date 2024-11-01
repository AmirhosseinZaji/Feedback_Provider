import os
import json
from openai import OpenAI

# Initialize the OpenAI
client = OpenAI()

def count_tokens(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": text}],
        max_tokens=1  # We only need the token count, not a response
    )
    return response.usage.prompt_tokens

def process_files(directory):
    token_counts = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                content = data.get('content', '')
                token_count = count_tokens(content)
                token_counts.append((filename, token_count))

                print(f"{filename}: {token_count} tokens")
    return token_counts

# Process files in the Refined_Data directory
refined_data_dir = 'Refined_Data'
results = process_files(refined_data_dir)

# Print the results
for filename, count in results:
    print(f"{filename}: {count} tokens")
