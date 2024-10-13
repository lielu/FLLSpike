import json
import os
import zipfile
import tempfile
import shutil
import sys
from llsp3_utils import *

# Windows service code
import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import argparse

monitored_libraries = ["drive.py"]

def create_windows_service(directory_to_monitor):
    # Define the Windows service
    class LLSP3MonitorService(win32serviceutil.ServiceFramework):
        _svc_name_ = "LLSP3MonitorService"
        _svc_display_name_ = "LLSP3 Monitor Service"

        def __init__(self, args):
            win32serviceutil.ServiceFramework.__init__(self, args)
            self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
            self.directory = directory_to_monitor

        def SvcStop(self):
            self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
            win32event.SetEvent(self.hWaitStop)

        def SvcDoRun(self):
            servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                                  servicemanager.PYS_SERVICE_STARTED,
                                  (self._svc_name_, ''))
            self.main()

        def main(self):
            monitor_llsp3_changes(self.directory, monitored_libraries)

    return LLSP3MonitorService

def install_windows_service(directory_to_monitor):
    service_class = create_windows_service(directory_to_monitor)
    try:
        win32serviceutil.InstallService(
            service_class._svc_name_,
            service_class._svc_display_name_,
            'Python service to monitor LLSP3 file changes'
        )
        log(f"Windows service '{service_class._svc_name_}' installed successfully")
    except Exception as e:
        log(f"Error installing Windows service: {e}")

def start_windows_service():
    try:
        win32serviceutil.StartService(LLSP3MonitorService._svc_name_)
        log(f"Windows service '{LLSP3MonitorService._svc_name_}' started successfully")
    except Exception as e:
        log(f"Error starting Windows service: {e}")

def stop_windows_service():
    try:
        win32serviceutil.StopService(LLSP3MonitorService._svc_name_)
        log(f"Windows service '{LLSP3MonitorService._svc_name_}' stopped successfully")
    except Exception as e:
        log(f"Error stopping Windows service: {e}")

def remove_windows_service():
    try:
        win32serviceutil.RemoveService(LLSP3MonitorService._svc_name_)
        log(f"Windows service '{LLSP3MonitorService._svc_name_}' removed successfully")
    except Exception as e:
        log(f"Error removing Windows service: {e}")

def run_monitor(directory):
    log("Service running")
    log(f"Example: python monitor_llsp3_to_python_windows.py run --directory {directory}")
    monitor_llsp3_changes(directory, monitored_libraries)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage LLSP3 monitor service for Windows")
    parser.add_argument("action", choices=["start", "run", "stop", "delete"], help="Action to perform")
    parser.add_argument("--directory", help="Directory to monitor (required for 'start' and 'run' actions)")
    args = parser.parse_args()

    if args.action == "start":
        if not args.directory:
            log("Error: --directory is required for 'start' action")
            log("Example: python monitor_llsp3_to_python_windows.py start --directory C:\\path\\to\\monitor")
            sys.exit(1)
        install_windows_service(args.directory)
        start_windows_service()
        log(f"Service started. Monitoring directory: {args.directory}")
    
    elif args.action == "run":
        if not args.directory:
            log("Error: --directory is required for 'run' action")
            log("Example: python monitor_llsp3_to_python_windows.py run --directory C:\\path\\to\\monitor")
            sys.exit(1)
        run_monitor(args.directory)

    elif args.action == "stop":
        stop_windows_service()
        log("Service stopped")
    
    elif args.action == "delete":
        stop_windows_service()
        remove_windows_service()
        log("Service deleted")

    log("\nUsage examples:")
    log("  Start: python monitor_llsp3_to_python_windows.py start --directory C:\\path\\to\\monitor")
    log("  Run: python monitor_llsp3_to_python_windows.py run --directory C:\\path\\to\\monitor")
    log("  Stop:  python monitor_llsp3_to_python_windows.py stop")
    log("  Delete: python monitor_llsp3_to_python_windows.py delete")

# class LLSP3MonitorService(win32serviceutil.ServiceFramework):
#     _svc_name_ = "LLSP3MonitorService"
#     _svc_display_name_ = "LLSP3 Monitor Service"

#     def __init__(self, args):
#         win32serviceutil.ServiceFramework.__init__(self, args)
#         self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
#         socket.setdefaulttimeout(60)
#         self.is_alive = True

#     def SvcStop(self):
#         # Called when the service is asked to stop
#         self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
#         win32event.SetEvent(self.hWaitStop)
#         self.is_alive = False

#     def SvcDoRun(self):
#         # Called when the service is asked to start
#         servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
#                                 servicemanager.PYS_SERVICE_STARTED,
#                                 (self._svc_name_, ''))
#         self.main()

#     def main(self):
#         while self.is_alive:
#             # Replace 'directory_to_monitor' with the actual directory path
#             monitor_llsp3_changes('directory_to_monitor')
#             # Check if service stop is requested every 5 seconds
#             rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)
#             if rc == win32event.WAIT_OBJECT_0:
#                 # Stop signal received
#                 break

# def install_windows_service():
#     """
#     Install the Windows service
#     """
#     try:
#         win32serviceutil.InstallService(
#             LLSP3MonitorService._svc_name_,
#             LLSP3MonitorService._svc_display_name_,
#             'Python service to monitor LLSP3 file changes'
#         )
#         print(f"Windows service '{LLSP3MonitorService._svc_name_}' installed successfully")
#     except Exception as e:
#         print(f"Error installing Windows service: {e}")

# def start_windows_service():
#     """
#     Start the Windows service
#     """
#     try:
#         win32serviceutil.StartService(LLSP3MonitorService._svc_name_)
#         print(f"Windows service '{LLSP3MonitorService._svc_name_}' started successfully")
#     except Exception as e:
#         print(f"Error starting Windows service: {e}")

# def stop_windows_service():
#     """
#     Stop the Windows service
#     """
#     try:
#         win32serviceutil.StopService(LLSP3MonitorService._svc_name_)
#         print(f"Windows service '{LLSP3MonitorService._svc_name_}' stopped successfully")
#     except Exception as e:
#         print(f"Error stopping Windows service: {e}")

# def delete_windows_service():
#     """
#     Delete the Windows service
#     """
#     try:
#         win32serviceutil.RemoveService(LLSP3MonitorService._svc_name_)
#         print(f"Windows service '{LLSP3MonitorService._svc_name_}' deleted successfully")
#     except Exception as e:
#         print(f"Error deleting Windows service: {e}")

# if __name__ == '__main__':
#     import argparse

#     parser = argparse.ArgumentParser(description="Manage LLSP3 monitor service for Windows")
#     parser.add_argument("action", choices=["start", "stop", "delete", "install"], help="Action to perform")
#     parser.add_argument("--directory", help="Directory to monitor (required for 'start' action)")
#     args = parser.parse_args()

#     if args.action == "install":
#         install_windows_service()
#     elif args.action == "start":
#         if not args.directory:
#             print("Error: --directory is required for 'start' action")
#             print("Example: python monitor_llsp3_to_python_windows.py start --directory C:\\path\\to\\monitor")
#             sys.exit(1)
#         start_windows_service()
#         print(f"Service started. Monitoring directory: {args.directory}")
#     elif args.action == "stop":
#         stop_windows_service()
#     elif args.action == "delete":
#         stop_windows_service()
#         delete_windows_service()
#     else:
#         win32serviceutil.HandleCommandLine(LLSP3MonitorService)

#     print("\nUsage examples:")
#     print("  Install: python monitor_llsp3_to_python_windows.py install")
#     print("  Start:   python monitor_llsp3_to_python_windows.py start --directory C:\\path\\to\\monitor")
#     print("  Stop:    python monitor_llsp3_to_python_windows.py stop")
#     print("  Delete:  python monitor_llsp3_to_python_windows.py delete")

