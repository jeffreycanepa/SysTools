"""
SysTools.py.

This is a tool for running a battery of system diagnostics from Python.  Script is from 
geeksided.com (https://geeksided.com/posts/detect-and-fix-issues-early-a-python-guide-to-system-diagnostics-01j0sbv2r9sa).

Script is meant to be run on Windows/Linux systems, but can be exectuted on OS X (Darwin) as well.
Added MacOS check for updates

Required:
    os
    platform
    psutil
    subprocess
    request
    speedtest

Jeff Canepa 8/2/2024
"""

import os

import platform

import psutil

import subprocess

import requests

def get_system_info():

    """Gather basic system information."""

    print("Gathering system information...")

    sys_info = {

        "OS": platform.system(),

        "OS Version": platform.version(),

        "Platform": platform.platform(),

        "Processor": platform.processor(),

        "Architecture": platform.architecture(),

        "Hostname": platform.node(),

    }

    for key, value in sys_info.items():

        print(f"{key}: {value}")

def get_cpu_memory_usage():

    """Monitor CPU and memory usage."""

    print("\nMonitoring CPU and memory usage...")

    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")

    print(f"Memory Usage: {psutil.virtual_memory().percent}%")

def get_disk_usage():

    """Check disk usage and health."""

    print("\nChecking disk usage and health...")

    partitions = psutil.disk_partitions()

    for partition in partitions:

        usage = psutil.disk_usage(partition.mountpoint)

        print(f"Partition: {partition.device}")

        print(f" Mountpoint: {partition.mountpoint}")

        print(f" File system type: {partition.fstype}")

        print(f" Total Size: {usage.total // (2**30)} GiB")

        print(f" Used: {usage.used // (2**30)} GiB")

        print(f" Free: {usage.free // (2**30)} GiB")

        print(f" Usage: {usage.percent}%")

def get_network_status():

    """Assess network connectivity and speed."""

    print("\nAssessing network connectivity and speed...")

    hostname = "google.com"

    response = os.system(f"ping -c 1 {hostname}")

    if response == 0:

        print(f"{hostname} is reachable")

    else:

        print(f"{hostname} is not reachable")

    try:

        import speedtest

        st = speedtest.Speedtest()

        st.download()

        st.upload()

        st.results.share()

        results = st.results.dict()

        print(f"Download Speed: {results['download'] / 1_000_000:.2f} Mbps")

        print(f"Upload Speed: {results['upload'] / 1_000_000:.2f} Mbps")

    except ImportError:

        print("Speedtest module not installed. Install it using 'pip install speedtest-cli'")

def check_security_updates():

    """Verify the presence of security updates."""

    print("\nVerifying the presence of security updates...")

    if platform.system() == "Windows":

        subprocess.run(["powershell", "Get-WindowsUpdate"])

    elif platform.system() == "Linux":

        os.system("sudo apt update && sudo apt upgrade -s")

    else:

        print("\tSecurity update check not supported for this OS.")

def scan_for_malware():

    """Scan for malware."""

    print("\nScanning for malware...")

    if platform.system() == "Windows":

        subprocess.run(["powershell", "Start-MpScan -ScanType QuickScan"])

    elif platform.system() == "Linux":

        os.system("sudo clamscan -r /")

    else:

        print("\tMalware scan not supported for this OS.")

def check_software_updates():

    """Check for updates to installed software."""

    print("\nChecking for software updates...")

    if platform.system() == "Windows":

        subprocess.run(["powershell", "Get-Package -ProviderName Programs | ForEach-Object { $_.Name; Get-Package -ProviderName Programs -Name $_.Name -IncludeWindowsInstaller -AllVersions | ForEach-Object { $_.Name, $_.Version } }"])

    elif platform.system() == "Linux":

        os.system("apt list --upgradable")

    elif platform.system() == "Darwin":

        os.system("softwareupdate -l")
    
    else:

        print("\tSoftware update check not supported for this OS.")

if __name__ == "__main__":

    get_system_info()

    get_cpu_memory_usage()

    get_disk_usage()

    get_network_status()

    check_security_updates()

    scan_for_malware()

    check_software_updates()