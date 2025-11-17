# README.md
# L1 Storage Root Extractor

## Overview
This repository provides a small utility for fetching the **storage root** of an Ethereum smart contract on L1.  
The storage root is a critical component used in ZK systems and soundness verification processes, such as in projects like Aztec, Zama, rollups, and other proof-based architectures.

## Files
1. app.py — the main script.
2. README.md — instructions and documentation.

## Installation
1. Install Python 3.10+
2. Install dependencies:
   pip install web3
3. Replace `your_api_key` in `RPC_URL` with your Infura or custom RPC endpoint.

## Usage
Run the script:
   python3 app.py  
Or specify a contract address:
   python3 app.py 0xYourContract

## What the Script Does
The script:
- Connects to an Ethereum RPC provider.
- Retrieves the latest block.
- Extracts the contract’s storage root.
- Prints the block number and the storage root hash used in ZK and soundness verification systems.

## Expected Output
You will see:
- The contract address  
- The latest block number  
- The storage root hash  
- A confirmation that the state root was successfully retrieved

## Notes
- The extracted storage root can be used as a public input for ZK rollups, soundness proofs, and state verification systems.
- Works with any EVM-compatible network simply by changing the RPC_URL.
- For privacy-sensitive systems (e.g., Aztec), you may use a private RPC node for more accurate state synchronization.
