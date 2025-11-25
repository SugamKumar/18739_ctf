# Stream Confusion

Stream Confusion is a cryptography challenge built using cmgr-style challenge framework. It uses a custom 16‑bit register–based stream cipher to encrypt a short flag and exposes only the ciphertext to players.

## Challenge idea

A 16‑bit register with fixed taps and seed is used to generate a byte keystream.  
Each byte of the plaintext flag is combined with one byte of this keystream to produce `cipher.txt`.  
Solvers must reconstruct the keystream and recover the flag from the provided parameters and ciphertext.

## Files

- `problem.md` – Problem description and hints.
- `flag.txt` – Flag string.
- `encrypt.py` – Builds `cipher.txt` from `flag.txt` using the custom stream cipher.
- `cipher.txt` – Hex‑encoded ciphertext distributed to players.
- `solver.py` – Reference solution used to verify the challenge.
- `Dockerfile` – Container image used by cmgr.

## Local testing

1. Put the flag in `flag.txt`.
2. Run `python3 encrypt.py` to regenerate `cipher.txt`.
3. Run `python3 solver.py` and confirm it prints the flag.