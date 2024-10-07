import json
import os
import zipfile
import tempfile
import shutil
import sys
import time
import logging

logging.basicConfig(stream=sys.stdout, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def log(message):
    logging.debug(message)
    # print(message)
    # sys.stdout.flush()

def extract_python_from_llsp3(llsp3_file_path):
    # Create a temporary directory to extract files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract the existing LLSP3 package
        with zipfile.ZipFile(llsp3_file_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        # Read projectbody.json
        project_json_path = os.path.join(temp_dir, "projectbody.json")
        with open(project_json_path, 'r') as file:
            project_json = json.load(file)
        
        # Extract the Python code from the "main" attribute
        python_code = project_json.get("main", "")
        
        # Generate the output Python file path
        output_py_path = f"{os.path.splitext(llsp3_file_path)[0]}.py"
        
        # Write the Python code to the output file
        with open(output_py_path, 'w') as file:
            file.write(python_code)
        
        log(f"Extracted Python code has been saved to '{output_py_path}'")

# # Example usage
# llsp3_file_path = "existing_project.llsp3"  # Replace with the path to your LLSP3 file
# extract_python_from_llsp3(llsp3_file_path)

def monitor_llsp3_changes(directory_path):
    log(f"Monitoring LLSP3 file changes in {directory_path}")
    last_modified_times = {}

    while True:
        for root, dirs, files in os.walk(directory_path):
            for filename in files:
                if filename.endswith('.llsp3'):
                    file_path = os.path.join(root, filename)
                    current_mtime = os.path.getmtime(file_path)

                    if file_path not in last_modified_times or current_mtime > last_modified_times[file_path]:
                        log(f"Change detected in {file_path}")
                        extract_python_from_llsp3(file_path)
                        last_modified_times[file_path] = current_mtime

        time.sleep(1)  # Check for changes every second

# # Example usage
# if __name__ == "__main__":
#     directory_to_monitor = "."  # Replace with the directory path you want to monitor
#     monitor_llsp3_changes(directory_to_monitor)