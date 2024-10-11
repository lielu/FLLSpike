import json
import os
import zipfile
import tempfile
import shutil
import sys
from llsp3_utils import *

# Import required modules for mac
import plistlib
import subprocess

monitored_libraries = ["drive.py"]

def create_launchd_plist(directory_to_monitor):
    # Define the content for the LaunchAgent plist file
    plist_content = {
        'Label': 'com.user.llsp3monitor',
        'ProgramArguments': [
            '/usr/bin/python3',
            __file__,
            'run',
            '--directory',
            directory_to_monitor
        ],
        'RunAtLoad': True,  # Run the script when the user logs in
        'KeepAlive': True,  # Keep the script running continuously
        'StandardOutPath': '/tmp/llsp3monitor.log',  # Redirect stdout to this file
        'StandardErrorPath': '/tmp/llsp3monitor_error.log'  # Redirect stderr to this file
    }
    
    # Define the path for the LaunchAgent plist file
    plist_path = os.path.expanduser('~/Library/LaunchAgents/com.user.llsp3monitor.plist')
    
    # Write the plist content to the file
    with open(plist_path, 'wb') as f:
        plistlib.dump(plist_content, f)
    
    log(f"LaunchAgent plist created at: {plist_path}")
    return plist_path

def load_launchd_service(plist_path):
    try:
        # Attempt to load the LaunchAgent service
        subprocess.run(['launchctl', 'load', plist_path], check=True)
        log("LaunchAgent service loaded successfully")
    except subprocess.CalledProcessError as e:
        # If an error occurs during loading, print the error message
        log(f"Error loading LaunchAgent service: {e}")

def unload_launchd_service(plist_path):
    try:
        # Attempt to unload the LaunchAgent service
        subprocess.run(['launchctl', 'unload', plist_path], check=True)
        log("LaunchAgent service unloaded successfully")
    except subprocess.CalledProcessError as e:
        # If an error occurs during unloading, print the error message
        log(f"Error unloading LaunchAgent service: {e}")

def remove_launchd_plist(plist_path):
    try:
        # Remove the LaunchAgent plist file
        os.remove(plist_path)
        log(f"LaunchAgent plist removed: {plist_path}")
    except OSError as e:
        # If an error occurs during removal, print the error message
        log(f"Error removing LaunchAgent plist: {e}")

def stop_and_remove_service():
    plist_path = os.path.expanduser('~/Library/LaunchAgents/com.user.llsp3monitor.plist')
    
    # Unload the service
    unload_launchd_service(plist_path)
    
    # Remove the plist file
    remove_launchd_plist(plist_path)
    
    log("Service stopped and removed successfully")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Manage LLSP3 monitor service")
    parser.add_argument("action", choices=["start", "run", "stop", "delete"], help="Action to perform")
    parser.add_argument("--directory", help="Directory to monitor (required for 'start' action)")
    args = parser.parse_args()

    plist_path = os.path.expanduser('~/Library/LaunchAgents/com.user.llsp3monitor.plist')

    if args.action == "start":
        if not args.directory:
            log("Error: --directory is required for 'start' action")
            log("Example: python3 monitor_llsp3_to_python_mac.py start --directory /path/to/monitor")
            sys.exit(1)
        
        # Create the LaunchAgent plist file
        plist_path = create_launchd_plist(args.directory)
        
        # Load the LaunchAgent service
        load_launchd_service(plist_path)
        
        log(f"Service started. Monitoring directory: {args.directory}")
    
    elif args.action == "run":
        # Actually run the script
        log("Service running")
        log("Example: python3 monitor_llsp3_to_python_mac.py run --directory /path/to/monitor")
        monitor_llsp3_changes(args.directory, monitored_libraries)

    elif args.action == "stop":
        # Unload the service
        unload_launchd_service(plist_path)
        log("Service stopped")
        log("Example: python3 monitor_llsp3_to_python_mac.py stop")
    
    elif args.action == "delete":
        # Stop and remove the service
        stop_and_remove_service()
        log("Service deleted")
        log("Example: python3 monitor_llsp3_to_python_mac.py delete")

    log("\nUsage examples:")
    log("  Start: python3 monitor_llsp3_to_python_mac.py start --directory /path/to/monitor")
    log("  Run: python3 monitor_llsp3_to_python_mac.py run --directory /path/to/monitor")
    log("  Stop:  python3 monitor_llsp3_to_python_mac.py stop")
    log("  Delete: python3 monitor_llsp3_to_python_mac.py delete")