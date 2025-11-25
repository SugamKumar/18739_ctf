#!/usr/bin/env python3

CIPHER_FILE = "cipher.txt"

SEED = 0xACE1
TAPS = [15, 13, 12, 10] 
STATE_MASK = 0xFFFF      


def lfsr_next(state, taps):

    feedback = 0
    for tap in taps:
        feedback ^= (state >> tap) & 1
    state = ((state << 1) | feedback) & STATE_MASK
    return state


def generate_keystream(num_bytes, seed, taps):
    state = seed
    keystream = bytearray()

    for _ in range(num_bytes):
        ks_byte = 0
        for _ in range(8):
            state = lfsr_next(state, taps)
            ks_byte = ((ks_byte << 1) | (state & 1)) & 0xFF
        keystream.append(ks_byte)

    return bytes(keystream)


def solve():
    with open(CIPHER_FILE, "r", encoding="utf-8") as f:
        hex_data = f.read().strip()

    ciphertext = bytes.fromhex(hex_data)

    keystream = generate_keystream(len(ciphertext), SEED, TAPS)

    plaintext = bytes(c ^ k for c, k in zip(ciphertext, keystream))

    print(plaintext.decode(errors="replace"))


if __name__ == "__main__":
    solve()
