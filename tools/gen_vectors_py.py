#!/usr/bin/env python3
import json, hashlib, os

def hash_tag(tag, x: bytes) -> bytes:
    t = hashlib.sha256(tag.encode()).digest()
    return hashlib.sha256(t + t + x).digest()

case = {
  "case_id": "placeholder-000",
  "N": 3, "t": 2,
  "ids": [1,2,3],
  "poly": {"a0": "00"*32, "a1": "11"*32},
  "commitments": ["02"+"00"*32, "02"+"11"*32],
  "P": "02"+"00"*32,
  "tweak": hash_tag("TapTweak", bytes.fromhex("00"*32)).hex(),
  "g_parity": 1,
  "Q": {"xonly": "00"*32, "full": "02"+"00"*32},
  "signers": [
    {"id":1,"secshare":"22"*32,"pubshare":"02"+"22"*32},
    {"id":2,"secshare":"33"*32,"pubshare":"02"+"33"*32},
    {"id":3,"secshare":"44"*32,"pubshare":"02"+"44"*32},
  ],
  "session": {
    "subset_ids": [1,2],
    "ser_ids": (1).to_bytes(4,'big').hex() + (2).to_bytes(4,'big').hex(),
    "pubnonces": {"1": ("02"+"55"*32)+("02"+"66"*32), "2": ("02"+"77"*32)+("02"+"88"*32)},
    "aggnonce": ("02"+"99"*32)+("02"+"aa"*32),
    "b": "bb"*32,
    "R": {"xonly":"cc"*32, "even": True},
    "m": "deadbeef",
    "e": "dd"*32,
    "partials": {"1":"ee"*32, "2":"ff"*32},
    "final_sig": {"R":"cc"*32, "s":"aa"*32}
  }
}

out = {"name":"frost-td-vectors", "version":"1", "cases":[case]}
print(json.dumps(out, separators=(",",":")))
