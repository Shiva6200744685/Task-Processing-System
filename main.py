import os
import json
from task_processor import process_task_json

def read_json(path):
    """Read and parse a JSON file."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_file(output_path, content):
    """Write content to a file, creating directories if needed."""
    dir_name = os.path.dirname(output_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_task_file(input_path, output_path):
    """Process a task file and generate a log file."""
    # Read and parse the input file
    task_data = read_json(input_path)
    
    # Process the task data to log format
    log_content = process_task_json(task_data)
    
    # Write to output file
    write_file(output_path, log_content)
    
    return output_path

if __name__ == "__main__":
    input_file = "task.json"
    output_file = "log.txt"
    
    result_path = process_task_file(input_file, output_file)
    print(f"✅ Log file created at: {result_path}")