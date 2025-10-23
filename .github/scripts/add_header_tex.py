#!/usr/bin/env python3
import os
import sys

# === CONFIGURAZIONE ===
HEADER_FILE = ".github/latex_header.tex"  # percorso del file .tex contenente l'header
SRC_DIR = "src"  # directory da scansionare

# Leggi l'header dal file
try:
    with open(HEADER_FILE, 'r', encoding='utf-8') as f:
        HEADER = f.read() + "\n"
except FileNotFoundError:
    print(f"Errore: file header {HEADER_FILE} non trovato.")
    sys.exit(1)

def has_header(path):
    """Controlla se il file contiene già l'header leggendo le prime righe."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            first_lines = ''.join([f.readline() for _ in range(10)])  # legge le prime 10 righe
        return HEADER.strip().splitlines()[0] in first_lines
    except Exception as e:
        print(f"Errore leggendo {path}: {e}")
        return False

def add_header(path):
    """Aggiunge l'header all'inizio del file .tex."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(path, 'w', encoding='utf-8') as f:
        f.write(HEADER + content)
    print(f"✅ Aggiunto header a: {path}")

def main():
    for root, _, files in os.walk(SRC_DIR):
        for file in files:
            if file.endswith(".tex"):
                path = os.path.join(root, file)
                # Aggiungi header solo se il file è "nuovo" (non contiene ancora l'header)
                if not has_header(path):
                    add_header(path)

if __name__ == "__main__":
    main()
