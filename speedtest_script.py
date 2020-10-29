#!/usr/bin/env python3

import subprocess
import sys

if __name__ == "__main__":
    subprocess.check_call(["sudo", "apt", "update", "-y"])
    subprocess.check_call(["sudo", "apt", "install", "python3-pip", "-y"])
    subprocess.check_call(["sudo", "apt", "install", "speedtest-cli", "-y"])
    
    with open("speedtest_results.txt", "w") as f:
        for i in range(0, 5):
            subprocess.run(["speedtest-cli"], stdout=f)