# Assignment 5: Bitcoin Network

## Overview
This assignment explores Bitcoin's network architecture through 10 hands-on labs in regtest mode.

## Labs Completed
-  Lab 1: Setting Up Regtest Environment
-  Lab 2: Running Multiple Nodes
-  Lab 3: Transaction Propagation and Mempool
-  Lab 4: Compact Block Relay (BIP152)
-  Lab 5: Compact Block Filters (BIP157/158)
-  Lab 6: Merkle Tree Exploration
-  Lab 7: Bloom Filters (BIP37)
-  Lab 8: Observing Consensus Rules
-  Lab 9: Visualizing Peer Connections
-  Lab 10: Cleanup

## Key Learnings
- How Bitcoin nodes communicate and propagate data
- How mempool, blocks, and filters interact
- How consensus ensures network integrity
- Real-world Bitcoin Core operations

## Files
- `outputs/` - All lab outputs
- `code/` - Custom scripts
- `lab-notes.md` - Observations and insights

## How to Run
```bash
# Start Bitcoin Core
./build/bin/bitcoind -regtest -daemon
./build/bin/bitcoin-cli -regtest loadwallet "devwallet"

# Run scripts
python3 code/merkle_verification.py
python3 code/bloom_filter_demo.py
