#!/bin/bash 

# Check for updates and install packages
sudo apt-get install -y
sudo apt-get update -y

# Install benchmarks
sudo apt-get install -y sysbench
sudo apt-get install -y hdparm
sudo apt-get install -y dbench

# Start running benchmarks
echo 'Running benchmarks for memory and disk...'

# Run each benchmark 5 times
for i in {1..5}
do {

echo $i

# 1.1  Memory Benchmark Sysbench
echo Running sysbench benchmark
echo Sysbench iteration $i >> memory-tests.txt

# Test sequential read 100G and block size 1M
sudo sysbench memory --memory-block-size=1M run >> memory-tests.txt

# Test random read 100G
sudo sysbench memory --memory-access-mode=rnd run >> memory-tests.txt

# Use variety of block sizes to test read and write
sudo sysbench memory --memory-block-size=1K --memory-oper=read run >> memory-tests.txt
sudo sysbench memory --memory-block-size=1K --memory-oper=write run >> memory-tests.txt


# 2.1 Disk Benchmark : hdparm
echo Running benchmark for hdparm...
echo Hdparm iteration $i >> disk-tests.txt

# Test throughput
sudo hdparm -Tt /dev/root >> disk-tests.txt

# Test direct read from disk
sudo hdparm -Tt --direct /dev/root >> disk-tests.txt

# Test read with an offset of 50G
sudo hdparm -Tt -offset 50 /dev/root >> disk-tests.txt

# 2.1 Disk Benchmark
echo Running benchmark for dbench...
echo dbench iteration $i >> disk-tests.txt
dbench 120 -t 10 >> disk-tests.txt
}
done