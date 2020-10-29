#!/usr/bin/env python3

import sys
import subprocess

def install(package):
    subprocess.check_call(["sudo", "apt-get", "-y", "install", package])

def install_all():
    install("php")
    install("unzip")
    install("gdebi-core")
    subprocess.check_call(["wget", "http://phoronix-test-suite.com/releases/repo/pts.debian/files/phoronix-test-suite_9.8.0_all.deb"])
    subprocess.check_call(["sudo", "gdebi", "phoronix-test-suite_9.8.0_all.deb"])

if __name__ == "__main__":
    install_all()
    for i in range(0, 2):
        subprocess.run(["phoronix-test-suite", "benchmark", "scimark2", "ramspeed", "fio"])

