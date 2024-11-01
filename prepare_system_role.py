import re

def clean_for_json(text):
    # Replace line breaks with spaces
    text = re.sub(r'\s+', ' ', text)
    # Escape double quotes
    text = text.replace('"', '\\"')
    # Remove any remaining control characters
    text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)
    return text

def prepare_system_role():
    input_file = "system_role.txt"
    output_file = "system_role_json_friendly.txt"

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
            cleaned_content = clean_for_json(content)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)

        print(f"Processing complete. JSON-friendly content saved in {output_file}")
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Prepare system role content
prepare_system_role()
