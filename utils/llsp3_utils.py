import os
import shutil
import sys
import json
import zipfile
import tempfile
import time
import logging

from logging.handlers import RotatingFileHandler

def setup_logger(logger_name, log_file, level=logging.ERROR):
    log_formatter = logging.Formatter('%(asctime)s %(process)d:%(thread)d %(name)s %(message)s')
    my_handler = RotatingFileHandler(log_file, maxBytes=100 * 1024 * 1024, backupCount=5)
    my_handler.setFormatter(log_formatter)
    my_handler.setLevel(level)
    l = logging.getLogger(logger_name)
    l.handlers[:] = []
    l.addHandler(my_handler)

log_file=os.path.splitext(__file__)[0]+".log"
setup_logger('debug', log_file)
logger = logging.getLogger('debug')

def log(message):
    logger.error(message)
    # logging.info(message)
    # print(message)
    # sys.stdout.flush()

monitored_libraries = ["drive.py", "run_red.py", "run_blue.py", "run_green.py", "run_yellow.py", "run_black.py"]
empty_llsp3 = "empty.llsp3"

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

def monitor_llsp3_changes(llsp3_directory_path, monitored_libraries = monitored_libraries):
    log(f"Monitoring LLSP3 file changes in {llsp3_directory_path} and Python file changes for {monitored_libraries}")
    last_modified_times = {}

    while True:
        for root, dirs, files in os.walk(llsp3_directory_path):
            for filename in files:
                if filename.endswith('.llsp3'):
                    file_path = os.path.join(root, filename)
                    current_mtime = os.path.getmtime(file_path)

                    if file_path not in last_modified_times or current_mtime > last_modified_times[file_path]:
                        log(f"Change detected in {file_path}")
                        extract_python_from_llsp3(file_path)
                        last_modified_times[file_path] = current_mtime

        for filename in monitored_libraries:
            file_path = os.path.join(llsp3_directory_path, filename)
            if os.path.exists(file_path) and file_path.endswith('.py') and not file_path.endswith('_lib.py'):
                current_mtime = os.path.getmtime(file_path)

                if file_path not in last_modified_times or current_mtime > last_modified_times[file_path]:
                    log(f"Change detected in {file_path}")
                    created_file = create_lib_file(file_path)
                    # Update the corresponding LLSP3 file
                    llsp3_file = os.path.splitext(created_file)[0] + '.llsp3'
                    log(f"LLSP3 file: {llsp3_file}")
                    if os.path.exists(llsp3_file):
                        log(f"Updating LLSP3 file: {llsp3_file}")
                    else:
                        log(f"Creating new LLSP3 file for {created_file}")
                        copy_empty_llsp3(llsp3_file, os.path.basename(created_file))
                    update_llsp3(llsp3_file, created_file, llsp3_file)
                    last_modified_times[file_path] = current_mtime

        time.sleep(1)  # Check for changes every second

def copy_empty_llsp3(destination_file, project_name):
    empty_llsp3_template = os.path.join(os.path.dirname(destination_file), empty_llsp3)
    if not os.path.exists(empty_llsp3_template):
        raise FileNotFoundError(f"Empty LLSP3 template not found: {empty_llsp3_template}")
    
    shutil.copy(empty_llsp3_template, destination_file)
    
    # Update the project name in the copied file
    with zipfile.ZipFile(destination_file, 'a') as zf:
        with zf.open('manifest.json') as f:
            manifest = json.load(f)
        
        manifest['name'] = project_name
        
        with zf.open('manifest.json', 'w') as f:
            f.write(json.dumps(manifest, indent=2).encode('utf-8'))
    
    log(f"Created empty LLSP3 file: {destination_file}")

def update_llsp3(llsp3_file_path, new_python_file_path, output_llsp3_path):
    # Create a temporary directory to extract files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract the existing LLSP3 package
        with zipfile.ZipFile(llsp3_file_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        # Read the new Python file
        with open(new_python_file_path, 'r') as file:
            new_python_code = file.read()
        
        # Update project.json
        project_json_path = os.path.join(temp_dir, "projectbody.json")
        with open(project_json_path, 'r') as file:
            project_json = json.load(file)
        
        # Replace the "main" attribute with the new Python code
        project_json["main"] = new_python_code
        
        # Write the updated project.json
        with open(project_json_path, 'w') as file:
            json.dump(project_json, file, indent=2)
        
        # Create the updated LLSP3 package
        with zipfile.ZipFile(output_llsp3_path, 'w') as zf:
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, temp_dir)
                    zf.write(file_path, arcname)

def monitor_python_changes(directory_path, filenames):
    log(f"Monitoring Python file changes in {directory_path} for {filenames}")
    last_modified_times = {}

    while True:
        for filename in filenames:
            file_path = os.path.join(directory_path, filename)
            if os.path.exists(file_path) and file_path.endswith('.py') and not file_path.endswith('_lib.py'):
                current_mtime = os.path.getmtime(file_path)

                if file_path not in last_modified_times or current_mtime > last_modified_times[file_path]:
                    log(f"Change detected in {file_path}")
                    created_file = create_lib_file(file_path)
                    # Update the corresponding LLSP3 file
                    llsp3_file = os.path.splitext(created_file)[0] + '.llsp3'
                    log(f"LLSP3 file: {llsp3_file}")
                    if os.path.exists(llsp3_file):
                        log(f"Updating LLSP3 file: {llsp3_file}")
                        update_llsp3(llsp3_file, created_file, llsp3_file)
                    else:
                        log(f"Corresponding LLSP3 file not found for {created_file}")
                    last_modified_times[file_path] = current_mtime

        time.sleep(1)  # Check for changes every second

def create_lib_file(source_file):
    log(f"Creating lib file for {source_file}")
    # Generate the new file name with "_lib" added
    base_name = os.path.basename(os.path.splitext(source_file)[0])
    lib_file = os.path.join(os.path.dirname(os.path.dirname(source_file)), "runtime", f"{base_name}_lib.py")

    # Read the content of the source file
    with open(source_file, 'r') as file:
        source_code = file.read()

    # Create the template with the source code embedded
    template = f'''
# Generated code
export_code: str = """
{source_code}
"""

def exportProgram():  # Function to export the library code string
    import os
    global export_code
    os.chdir('/flash')  # change directory to root
    try:
        os.remove('{base_name}.py')  # remove any existing library file of the same name
    except:
        pass
    f = open('{base_name}.py', 'w+')  # Create a new file drive.py in the SPIKE hub root
    f.write(export_code)  # Write out the library code string to the drive.py file
    f.close()

if __name__ == "__main__":
    import sys
    exportProgram()  # Runs the export function    
    sys.exit(0)
'''

    log(f"Writing template to {lib_file}")
    # Write the template to the new lib file
    with open(lib_file, 'w+') as file:
        file.write(template)

    log(f"Created library file: {lib_file}")
    return lib_file  # Return the created file path

import datetime
import uuid

def create_empty_llsp3(file_path, project_name):
    log(f"Creating empty LLSP3 file at {file_path}")
    
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create an empty projectbody.json
        project_json = {
            "main": "from hub import port, motion_sensor\nimport motor #imports a ability to control a single motor\nimport motor_pair #imports a pair of motors moving like one\nimport runloop\n"
        }
        
        project_json_path = os.path.join(temp_dir, "projectbody.json")
        with open(project_json_path, 'w') as file:
            json.dump(project_json, file, indent=2)
        
        # Create manifest.json
        manifest_json = {
            "type": "python",
            "appType": "llsp3",
            "autoDelete": False,
            "created": datetime.datetime.utcnow().isoformat() + "Z",
            "id": str(uuid.uuid4())[:12],
            "lastsaved": datetime.datetime.utcnow().isoformat() + "Z",
            "size": 0,
            "name": project_name,
            "slotIndex": 0,
            "workspaceX": -155,
            "workspaceY": 0,
            "zoomLevel": 1.2750000000000006,
            # "hardware": {
            #     "python": {
            #         "id": str(uuid.uuid4()).upper(),
            #         "description": "",
            #         "connection": "bluetooth-lowenergy",
            #         "name": "MiniBot",
            #         "type": "flipper",
            #         "connectionState": 2,
            #         "hubState": {"programRunning": False},
            #         "lastConnectedHubId": str(uuid.uuid4()).upper()
            #     }
            # },
            "state": {
                "canvasDrawerOpen": True,
                "knowledgeBaseSection": "lls-help-python-gs-hello",
                "hasMonitors": True,
                "playMode": "download",
                "canvasDrawerTab": "knowledgeBaseTab"
            },
            "extraFiles": [],
            "lastConnectedHubType": "flipper"
        }
        
        manifest_json_path = os.path.join(temp_dir, "manifest.json")
        with open(manifest_json_path, 'w') as file:
            json.dump(manifest_json, file, indent=2)
        
        # Create monitors.json
        monitors_json = {
            "programStopTime": int(datetime.datetime.now().timestamp() * 1000),
            "display": {
                "visible": False,
                "viewMode": "In window",
                "type": "image",
                "content": "",
                "hideImage": False,
                "includedImages": [11],
                "showImageSelector": False
            },
            "linegraph": {
                "visible": False,
                "viewMode": "In window",
                "lineVariant": 0,
                "data": [],
                "splitMode": 0,
                "yAxisMode": 0
            },
            "bargraph": {
                "visible": False,
                "viewMode": "In window",
                "data": {"1": 0, "3": 0, "4": 0, "6": 0, "7": 0, "9": 0}
            }
        }
        
        monitors_json_path = os.path.join(temp_dir, "monitors.json")
        with open(monitors_json_path, 'w') as file:
            json.dump(monitors_json, file, indent=2)
        
        # Create icon.svg
        icon_svg_content = '''<svg width="60" height="60" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd"><g fill="#D8D8D8" fill-rule="nonzero"><path d="M34.613 7.325H15.79a3.775 3.775 0 00-3.776 3.776v37.575a3.775 3.775 0 003.776 3.776h28.274a3.775 3.775 0 003.776-3.776V20.714a.8.8 0 00-.231-.561L35.183 7.563a.8.8 0 00-.57-.238zm-.334 1.6l11.96 12.118v27.633a2.175 2.175 0 01-2.176 2.176H15.789a2.175 2.175 0 01-2.176-2.176V11.1c0-1.202.973-2.176 2.176-2.176h18.49z"/><path d="M35.413 8.214v11.7h11.7v1.6h-13.3v-13.3z"/></g><path fill="#0290F5" d="M23.291 27h13.5v2.744h-13.5z"/><path fill="#D8D8D8" d="M38.428 27h4.32v2.744h-4.32zM17 27h2.7v2.7H17zM17 31.86h2.7v2.744H17zM28.151 31.861h11.34v2.7h-11.34zM17 36.72h2.7v2.7H17zM34.665 36.723h8.1v2.7h-8.1z"/><path fill="#0290F5" d="M28.168 36.723h4.86v2.7h-4.86z"/></g></svg>'''
        
        icon_svg_path = os.path.join(temp_dir, "icon.svg")
        with open(icon_svg_path, 'w') as file:
            file.write(icon_svg_content)
        
        # Create the LLSP3 file (which is essentially a zip file)
        with zipfile.ZipFile(file_path, 'w') as zf:
            zf.write(project_json_path, arcname="projectbody.json")
            zf.write(manifest_json_path, arcname="manifest.json")
            zf.write(monitors_json_path, arcname="monitors.json")
            zf.write(icon_svg_path, arcname="icon.svg")
    
    log(f"Empty LLSP3 file created at {file_path}")
    return file_path

# Example usage
if __name__ == "__main__":
    # directory_to_monitor = "."  # Replace with the directory path you want to monitor
    monitor_llsp3_changes("/Users/lielu/projects/WeLostAPiece/FLLSpike/src/libs", ["run_red.py"])
    
    # monitor_python_changes("/Users/lielu/projects/WeLostAPiece/FLLSpike/src/libs", ["drive.py"])

    # create_empty_llsp3("empty.llsp3", "Empty LLSP3")
