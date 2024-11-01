# AI-Powered Teaching Assistant for Faculty

## Overview
This tool helps faculty members generate consistent, personalized feedback on student assignments using OpenAI's GPT models. It follows a specific professor-style feedback template that includes an engaging, topic-relevant opening joke, positive reinforcement of strong points, constructive suggestions for improvement, and a consistent tone and format.

## Project Structure
The project is organized as follows:
- `Data/`: Contains student assignments in raw text format.
- `Refined_Data/`: Stores generated feedback in JSON format.
- `fine_tune.py`: Script for fine-tuning the model.
- `jsonl_creator.py`: Script for creating JSONL files.
- `system_role.txt`: Contains feedback style rules.
- `.env`: Stores environment variables.
- `README.md`: This documentation file.

## Prerequisites
To use this tool, you will need a computer with internet access, Python installed (which can be downloaded from [python.org](https://python.org)), an OpenAI API key, and basic comfort with creating and saving text files, running simple commands, and managing folders.

## Step-by-Step Setup Guide

### 1. Get Your OpenAI API Key (5-10 minutes)

An API key is essential because it authenticates your requests to OpenAI's servers, tracks your usage and billing, ensures secure access to the GPT models, and enables rate limiting and quota management.

- Go to [OpenAI's website](https://openai.com)
- Click "Sign Up" (top right)
- Create an account
- Go to "API Keys" section
- Click "Create New Key"
- Copy and save the key securely

⚠️ Important Security Notes:
Keep your API key private, never commit it to public repositories, rotate keys periodically for security, and monitor usage to prevent unauthorized access.

### 2. Install Required Software (10-15 minutes)

Installing Python is necessary because it is the primary programming language for the tool, providing access to OpenAI's API library, handling text processing and file operations, and managing environment variables securely.

- Download Python from [python.org](https://python.org)
- During installation:
  - Check "Add Python to PATH"
  - Click "Install Now"

⚠️ Installation Notes:
Requires admin privileges, may need to restart computer, verify installation with `python --version`, and check PATH environment if commands fail.

### 3. Set Up the Project (15-20 minutes)

Setting up the project is crucial for organizing code and data, managing dependencies, securing sensitive information, and ensuring consistent operation.

#### Install Required Packages:
Open Terminal (Mac) or Command Prompt (Windows):
```bash
pip install openai python-dotenv
```

#### Configure API Key:
- Create a file named `.env` in the project folder
- Add your OpenAI key:
  ```
  OPENAI_API_KEY=your_key_here
  ```

### 4. Prepare Student Assignments (5-10 minutes per batch)

Proper preparation ensures consistent processing, accurate feedback generation, efficient batch handling, and error prevention.

- Create a folder named `Data` (if not exists)
- Save student assignments as text files:
  - One assignment per file
  - Use consistent naming (e.g., "student1.txt")
  - Plain text format (.txt)

### 5. Configure Feedback Style (Optional)

Configuring the feedback style allows for a personalized feedback approach, consistent tone and format, customized learning experience, and brand alignment.

The `system_role.txt` file contains:
```
Professor's Feedback Style Rules:
- Start with a topic-related joke
- Highlight good areas (concise, encouraging)
- Address weak areas (directive, straightforward)
- Keep overall tone conversational and playful
```

### 6. Generate Feedback

This process involves converting raw data to a structured format, training the model on your style, and generating consistent feedback.

- Create JSONL file:
  ```bash
  python jsonl_creator.py
  ```
- Fine-tune the model:
  ```bash
  python fine_tune.py
  ```

### 7. Review Generated Feedback

Reviewing the generated feedback is critical for quality assurance, adding a personal touch, catching errors, and ensuring continuous improvement.

- Find feedback files in `Refined_Data` folder
- Each file includes:
  - Opening joke
  - Positive highlights
  - Improvement suggestions
  - Overall assessment

⚠️ Review Guidelines:
Check for accuracy, ensure appropriate tone, verify completeness, and add personal insights.

## Best Practices

1. **Review Before Sending**
   - Always review generated feedback
   - Make necessary adjustments
   - Ensure personal touch remains

2. **Maintain Consistency**
   - Use consistent file naming
   - Keep feedback style rules updated
   - Regular backup of custom templates

3. **Privacy & Security**
   - Never share your API key
   - Keep student data confidential
   - Regular cleanup of processed files

## Troubleshooting

Common issues and solutions:

1. **API Key Error**
   - Check `.env` file exists
   - Verify API key is valid
   - Ensure proper file permissions

2. **File Processing Issues**
   - Verify file formats (.txt)
   - Check file naming consistency
   - Ensure proper folder structure

## Support
For technical issues, consult OpenAI documentation, review error logs, or contact your system administrator.

## Updates & Maintenance
Check for updates monthly, backup custom templates, and update the API key as needed. Remember, this tool is designed to assist, not replace, your expertise. Always review and adjust the generated feedback before sending it to students.