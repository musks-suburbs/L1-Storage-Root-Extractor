# app.py
from web3 import Web3
import sys
import time

RPC_URL = "https://mainnet.infura.io/v3/your_api_key"
CONTRACT_ADDRESS = "0x00000000219ab540356cBB839Cbe05303d7705Fa"

def fetch_storage_root(address):
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        print("❌ RPC connection failed")
        sys.exit(1)

    addr = Web3.to_checksum_address(address)
    block = w3.eth.get_block("latest")
    proof = w3.eth.get_proof(addr, [], block.number)

    return proof.storageHash.hex(), block.number

if __name__ == "__main__":
    print("🔍 Fetching L1 storage root for ZK soundness verification...")
    time.sleep(0.2)

    root, block = fetch_storage_root(CONTRACT_ADDRESS)

    print("Contract:", CONTRACT_ADDRESS)
    print("Block:", block)
    print("Storage root:", root)
    print("✅ Storage root retrieved. Use it for L1↔L2 soundness or ZK proof inputs.")
