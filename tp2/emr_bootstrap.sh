#!/bin/bash

# Install dependencies
sudo yum -y install git
sudo python3 -m pip install boto3 findspark pandas

# Fetch scripts
git clone https://github.com/JigsawCorp/log8415e.git