#!/usr/bin/env python3
from pathlib import Path
import sys

# Percorsi dai parametri
tex_file = Path(sys.argv[1])
template_file = Path(sys.argv[2])

# Controlla se il file .tex esiste
if not tex_file.exists():
    print(f"File {tex_file} non trovato.")
    sys.exit(1)

# Legge il file .tex
lines = tex_file.read_text(encoding="utf-8").splitlines()

# Se il template è già presente, esce
if lines and lines[0].strip() == "% template presente":
    print(f"Template già presente in {tex_file}")
    sys.exit(0)

# Legge il template
template_content = template_file.read_text(encoding="utf-8")

# Scrive il nuovo contenuto
tex_file.write_text("% template presente\n" + template_content + "\n" + "\n".join(lines), encoding="utf-8")
print(f"Template applicato a {tex_file}")
