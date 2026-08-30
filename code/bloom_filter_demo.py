#!/usr/bin/env python3
"""
Bloom Filter Demo for Bitcoin (BIP37)
"""

try:
    from pybloom_live import BloomFilter
    print("pybloom_live installed ✅")
    
    # Create Bloom filter
    bf = BloomFilter(capacity=1000, error_rate=0.001)
    
    # Add some data
    bf.add("txid_123456")
    bf.add("address_abc123")
    bf.add("block_hash_xyz")
    
    # Test membership
    print("\n=== Membership Tests ===")
    print(f"  Contains 'txid_123456'?   {bf.__contains__('txid_123456')}")
    print(f"  Contains 'fake_txid'?     {bf.__contains__('fake_txid')}")
    print(f"  Contains 'address_abc123'? {bf.__contains__('address_abc123')}")
    
    print(f"\n=== Filter Stats ===")
    print(f"  Bitarray length: {len(bf.bitarray)} bits")
    print(f"  Bitarray (first 80 bits): {str(bf.bitarray)[:80]}...")
    
    print("\n=== BIP37 Bloom Filters ===")
    print("  Purpose: SPV wallets filter blocks to find relevant transactions")
    print("  Privacy Issue: Clients reveal their interests to peers")
    print("  Status: Deprecated in favor of BIP157/158 (Compact Block Filters)")
    
except ImportError:
    print("pybloom_live not installed.")
    print("Install with: pip install pybloom-live")
    print("\n=== Bloom Filter Concept ===")
    print("  - Probabilistic data structure for set membership")
    print("  - Used in BIP37 for SPV wallet filtering")
    print("  - Returns false positives (but never false negatives)")
    print("  - Deprecated due to privacy leaks")
    print("  - Replaced by BIP157/158 Compact Filters")
