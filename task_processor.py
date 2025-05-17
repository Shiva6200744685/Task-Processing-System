import json

def process_task_json(task_data):
    """
    Process a task JSON and convert it to a formatted log output.
    
    Args:
        task_data (dict): The parsed JSON task data
        
    Returns:
        str: Formatted log output
    """
    task_id = task_data.get("task_id", "Unknown")
    script = task_data.get("script", "Unknown")
    action = task_data.get("action", "Unknown")
    
    # Format the log output with consistent spacing
    log_lines = [
        f"Task Detected: {task_id}",
        f"Executing: {script}",
        f"Success: True"
    ]
    
    return "\n".join(log_lines)