# AI-Powered Teaching Assistant for Faculty

## Overview
This tool helps faculty members generate consistent, personalized feedback on student assignments using OpenAI's GPT models. It follows a specific professor-style feedback template that includes:
- An engaging, topic-relevant opening joke
- Positive reinforcement of strong points
- Constructive suggestions for improvement
- Consistent tone and format

## Project Structure
project/
├── Data/ # Student assignments (raw text)
├── Refined_Data/ # Generated feedback (JSON format)
├── fine_tune.py # Fine-tuning script
├── jsonl_creator.py # JSONL creation script
├── system_role.txt # Feedback style rules
├── .env # Environment variables
└── README.md # This file


## Prerequisites
You'll need:
1. A computer with internet access
2. Python installed (Download from [python.org](https://python.org))
3. An OpenAI API key
4. Basic comfort with:
   - Creating/saving text files
   - Running simple commands
   - Managing folders

## Step-by-Step Setup Guide

### 1. Get Your OpenAI API Key (5-10 minutes)
1. Go to [OpenAI's website](https://openai.com)
2. Click "Sign Up" (top right)
3. Create an account
4. Go to "API Keys" section
5. Click "Create New Key"
6. Copy and save the key securely

### 2. Install Required Software (10-15 minutes)
1. Download Python from [python.org](https://python.org)
2. During installation:
   - Check "Add Python to PATH"
   - Click "Install Now"

### 3. Set Up the Project (15-20 minutes)

#### Install Required Packages:
Open Terminal (Mac) or Command Prompt (Windows):

bash
pip install openai python-dotenv


#### Configure API Key:
1. Create a file named `.env` in the project folder
2. Add your OpenAI key:

OPENAI_API_KEY=your_key_here

### 4. Prepare Student Assignments (5-10 minutes per batch)

1. Create a folder named `Data` (if not exists)
2. Save student assignments as text files:
   - One assignment per file
   - Use consistent naming (e.g., "student1.txt")
   - Plain text format (.txt)

### 5. Configure Feedback Style (Optional)

The `system_role.txt` file contains the feedback style rules. You can customize:
- Joke style and tone
- Feedback structure
- Language preferences

Example from current system:

Professor's Feedback Style Rules:
Start with a topic-related joke
Highlight good areas (concise, encouraging)
Address weak areas (directive, straightforward)
Keep overall tone conversational and playful

### 6. Generate Feedback

1. Create JSONL file:

bash
python jsonl_creator.py

2. Fine-tune the model:

bash
python fine_tune.py


### 7. Review Generated Feedback
- Find feedback files in `Refined_Data` folder
- Each file includes:
  - Opening joke
  - Positive highlights
  - Improvement suggestions
  - Overall assessment

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
For technical issues:
- Check OpenAI documentation
- Review error logs
- Contact system administrator

## Updates & Maintenance
- Check for updates monthly
- Backup custom templates
- Update API key as needed

Remember: This tool is designed to assist, not replace, your expertise. Always review and adjust the generated feedback before sending to students.