# RMIT-Security-in-Computing-and-IT-SnakeCoin-Enhancement
This repository contains a sample Blockchain program implemented in Python. It's part of an academic project under RMIT University.

![image](https://user-images.githubusercontent.com/79836947/160737604-273c62fd-1503-4ce6-a292-a351665cc2e1.png#gh-dark-mode-only)
![image](https://user-images.githubusercontent.com/79836947/160738358-eaa88731-2a44-4004-ab9a-3d83a2268742.png#gh-light-mode-only)

## Academic Integrity Warning

Cheating is a serious offense. For serious breaches of academic integrity, students can be charged with academic misconduct. Possible penalties include cancellation of results and expulsion, which can result in the cancellation of a student's program.

For more information, please refer to the following links:
 
 - [RMIT Academic Integrity Awareness Micro Credential](https://www.rmit.edu.au/study-with-us/levels-of-study/short-courses/academic-integrity-awareness)
 - [Academic Integrity at RMIT](https://www.rmit.edu.au/students/my-course/assessment-results/academic-integrity)

## Overview of SnakeCoin

A blockchain is a growing list of records, called blocks, that are linked using cryptography. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. In this project, we create a simple blockchain with 20 blocks, including the genesis block (the first block). Each block is linked to the previous one via its hash.

## Implementation

The project implements a `Block` class that defines the structure for each block. The `Block` class includes a method for hashing the blocks.

Two functions are defined outside the `Block` class:

1. `create_genesis_block()`: This function creates the first block in the chain (genesis block).
2. `next_block(last_block)`: This function creates each subsequent block in the chain.

## Running the code

Ensure that Python 3 is installed on your machine. Then, run the script with:

```bash
python3 blockchain.py
```
Replace blockchain.py with the name of the file that contains the code.
