"""
Minimal helpers that match the Notation section of the spec.
EC math is implemented later (C generator provides canonical vectors).
"""

import hashlib

def hash_tag(tag: str, x: bytes) -> bytes:
    """hash_tag(tag, x) = SHA256(SHA256(tag) || SHA256(tag) || x)"""
    t = hashlib.sha256(tag.encode("utf-8")).digest()
    return hashlib.sha256(t + t + x).digest()

def bytes32(n: int) -> bytes:
    return n.to_bytes(32, "big")

def int_from32(b: bytes) -> int:
    if len(b) != 32:
        raise ValueError("need 32 bytes")
    return int.from_bytes(b, "big")
