#!/usr/bin/env python3

def lfsr_next(state, taps):
    feedback = 0
    for tap in taps:
        feedback ^= (state >> tap) & 1
    state = ((state << 1) | feedback) & 0xFFFF
    return state

def encrypt_flag(flag, seed, taps):
    state = seed
    out = []
    for ch in flag:
        ks_byte = 0
        for _ in range(8):
            state = lfsr_next(state, taps)
            ks_byte = ((ks_byte << 1) | (state & 1)) & 0xFF
        out.append(ch ^ ks_byte)
    return bytes(out)

FLAG = open("flag.txt", "rb").read().strip()
SEED = 0xACE1
TAPS = [15, 13, 12, 10]

cipher = encrypt_flag(FLAG, SEED, TAPS)

with open("cipher.txt", "w", encoding="utf-8") as f:
    f.write(cipher.hex())
