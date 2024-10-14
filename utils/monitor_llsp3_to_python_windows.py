import os
import win32serviceutil
import win32service
import win32event
import servicemanager
import socket

from llsp3_utils import *

# Get the current folder of __file__
current_folder = os.path.dirname(os.path.abspath(__file__))

# Append ../src/libs to the current folder path
monitor_folder = os.path.abspath(os.path.join(current_folder, '..', 'src', 'libs'))

class LLSP3MonitorService(win32serviceutil.ServiceFramework):
    _svc_name_ = "LLSP3MonitorService"
    _svc_display_name_ = "LLSP3MonitorService"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.isrunning = False

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.isrunning = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.isrunning = True
        self.main()

    def main(self):
        log("Monitoring LLSP3 changes...")
        monitor_llsp3_changes(monitor_folder)


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(LLSP3MonitorService)