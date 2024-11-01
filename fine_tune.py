import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Set the path to your JSONL file
file_path = "refined_output_without_system.jsonl"

# Upload the file
with open(file_path, "rb") as file:
    file_response = client.files.create(
        file=file,
        purpose="fine-tune"
    )

# Create a fine-tuning job
job = client.fine_tuning.jobs.create(
    training_file=file_response.id,
    model="gpt-4o-mini-2024-07-18", 
    hyperparameters={
        "n_epochs": 15
    }
)

# Print the job details
print(f"Fine-tuning job created: {job.id}")

# Wait for the job to complete
while job.status != "succeeded" and job.status != "failed":
    job = client.fine_tuning.jobs.retrieve(job.id)
    print(f"Job status: {job.status}")

# Print the final status
if job.status == "succeeded":
    print(f"Fine-tuning completed successfully. New model: {job.fine_tuned_model}")
else:
    print("Fine-tuning failed.")

