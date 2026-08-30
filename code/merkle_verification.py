#!/usr/bin/env python3
"""
Merkle Tree Verification - Simple Version
"""

import hashlib
import json
import subprocess
import sys

def double_sha256(b):
    return hashlib.sha256(hashlib.sha256(b).digest()).digest()

def merkle_root(txids):
    if not txids:
        return None
    hashes = [bytes.fromhex(txid)[::-1] for txid in txids]
    while len(hashes) > 1:
        if len(hashes) % 2 == 1:
            hashes.append(hashes[-1])
        hashes = [double_sha256(hashes[i] + hashes[i+1]) for i in range(0, len(hashes), 2)]
    return hashes[0][::-1].hex()

# Use bitcoin-cli directly with subprocess
def run_bitcoin_cli(command):
    cmd = ["/home/abbie/projects/bitcoin/build/bin/bitcoin-cli", "-regtest"] + command.split()
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}", file=sys.stderr)
        return None
    return result.stdout.strip()

# Get best block hash
block_hash = run_bitcoin_cli("getbestblockhash")
if not block_hash:
    print("Failed to get block hash. Make sure bitcoind is running.")
    sys.exit(1)

# Get block details as JSON
block_json = run_bitcoin_cli(f"getblock {block_hash} 2")
if not block_json:
    print("Failed to get block details.")
    sys.exit(1)

block = json.loads(block_json)

# Extract data
txids = [tx["txid"] for tx in block["tx"]]

print(f"Block Hash: {block_hash}")
print(f"Block Height: {block['height']}")
print(f"Number of transactions: {len(txids)}")
print(f"Merkle Root (from block): {block['merkleroot']}")
print(f"Merkle Root (computed):    {merkle_root(txids)}")
print(f"Match: {block['merkleroot'] == merkle_root(txids)}")
