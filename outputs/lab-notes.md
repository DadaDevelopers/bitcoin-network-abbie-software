Assignment 5: Bitcoin Network - Lab Notes

## Overview
This assignment explores Bitcoin's network architecture through 10 hands-on labs in regtest mode.

---

## Lab 1: Setting Up Regtest Environment
**Commands:**
- `bitcoind -regtest -daemon`
- `bitcoin-cli -regtest createwallet devwallet`
- `bitcoin-cli -regtest generatetoaddress 101 <address>`
- `bitcoin-cli -regtest getblockchaininfo`

**Observations:**
- Wallet "devwallet" created successfully
- 101 blocks generated, balance available
- Blockchain height: 101



---

## Lab 2: Running Multiple Nodes
**Commands:**
- Started second node on ports 18460/18461
- Connected nodes using `addnode`
- Verified with `getpeerinfo`

**Observations:**
- Nodes connected successfully
- Peer info shows inbound connection

**Key Learning:** Bitcoin nodes communicate via P2P network on different ports.

---

## Lab 3: Transaction Propagation
**Commands:**
- Sent transaction: `sendtoaddress <address> 5.0`
- Checked mempool on both nodes
- Mined transaction: `generatetoaddress 1 <address>`

**Observations:**
- Transaction appeared in mempool on both nodes
- Confirmed after mining 1 block

**Key Learning:** Transactions propagate to all connected nodes via the P2P network.

---

## Lab 4: Compact Block Relay (BIP152)
**Commands:**
- Started node with `-debug=net`
- Generated a block
- Checked debug.log for compact messages

**Observations:**
- No explicit compact block messages in regtest logs
- Compact blocks are enabled by default in Bitcoin Core v0.13.0+

**Key Learning:** BIP152 reduces bandwidth by sending transaction IDs instead of full transactions.

---

## Lab 5: Compact Block Filters (BIP157/158)
**Commands:**
- Restarted node with `-blockfilterindex=1`
- Retrieved block filter: `getblockfilter <blockhash>`

**Observations:**
- Block filter successfully retrieved
- Filter uses Golomb-Rice encoding for efficiency

**Key Learning:** Compact filters allow light clients to query for transactions efficiently.

---

## Lab 6: Merkle Tree Exploration
**Commands:**
- Retrieved best block hash
- Inspected block details
- Computed Merkle root programmatically

**Observations:**
- Computed Merkle root matched block header
- Confirmed cryptographic integrity

**Key Learning:** Merkle trees efficiently summarize all transactions in a block.

---

## Lab 7: Bloom Filters (BIP37)
**Commands:**
- Created Bloom filter using `pybloom_live`
- Added test data
- Tested membership

**Observations:**
- Probabilistic matching works as expected
- Deprecated due to privacy concerns

**Key Learning:** Bloom filters leak client interests to peers, leading to privacy risks.

---

## Lab 8: Consensus Rules
**Observations:**
- Consensus is enforced by all nodes independently
- Invalid blocks are rejected with "bad-blk" error

**Key Learning:** No single node can add invalid data to the blockchain.

---

## Lab 9: Peer Connections
**Commands:**
- `getpeerinfo | jq '[.[] | {addr, subver, inbound}]'`
- `getnetworkinfo`

**Observations:**
- Peer connection confirmed
- Protocol version: 70016**Key Learning:** Regtest mode allows instant block generation for testing.
- Subver: /Satoshi:30.0.0/

**Key Learning:** Each peer connection is a TCP link exchanging compact messages.

---

## Lab 10: Cleanup
**Commands:**
- Stopped both nodes
- Removed temporary data directories

**Observations:**
- All nodes stopped successfully
- Cleanup completed
