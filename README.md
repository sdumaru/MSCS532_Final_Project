# MSCS532_Final_Project
Final Project for MSCS 532

## Memory Management Optimization in High-Performance Computing (HPC)
This repository contains a Python implementation demonstrating memory management optimization techniques for improving performance in high-performance computing (HPC) environments. The project compares two array reversal methods:
- In-Place Reversal (Optimized): A memory-efficient approach that minimizes memory allocation and improves cache utilization.
- New Array Reversal (Less Efficient): A less efficient method that involves creating a new array, leading to higher memory usage and potential cache misses.

## Files
- 'HPC_Optimization.py' : The main Python script containing the implementation of both algorithms.

## How to Run
1. Clone the repository using the command: git clone https://github.com/sdumaru/MSCS532_Final_Project.git. 
2. Ensure python is installed in your system. If not, download and install it from the official website.
3. Ensure numpy is installed. Run pip install numpy in the terminal.
4. Navigate to the repository directory: cd MSCS532_Final_Project
5. Execute the code with the command: python .\HPC_Optimization.py

## Summary
The results are printed in the terminal, displaying the performance comparison between the optimized in-place array reversal and the less efficient new array reversal method. The in-place reversal method consistently performs better due to reduced memory allocations and improved cache utilization, which aligns with the memory optimization principles.