#!/usr/bin/env python3
"""Read-only inventory of a folder; does not unpack or modify game files."""
from __future__ import annotations
import argparse
import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

AUDIO_EXTS = {".wem", ".bnk", ".pck", ".ogg", ".wav", ".opus", ".mp3", ".flac", ".aiff"}
CONTAINER_EXTS = {".pak", ".ucas", ".utoc"}
META_EXTS = {".json", ".xml", ".ini", ".txt", ".csv"}
def classify(ext: str) -> str:
    if ext in AUDIO_EXTS: return "audio_or_audio_bank"
    if ext in CONTAINER_EXTS: return "game_container"
    if ext in META_EXTS: return "metadata_or_text"
    return "other"

def main() -> int:
    parser = argparse.ArgumentParser(description="Gera inventário sem alterar os arquivos.")
    parser.add_argument("folder", help="Pasta que será inventariada")
    parser.add_argument("--output", default="reports", help="Pasta de saída (padrão: reports)")
    args = parser.parse_args()
    root = Path(args.folder).expanduser().resolve()
    if not root.is_dir():
        parser.error(f"Pasta não encontrada: {root}")
    out = Path(args.output).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    for p in sorted(root.rglob("*")):
        if not p.is_file(): continue
        try:
            stat = p.stat()
            ext = p.suffix.lower()
            rows.append({
                "relative_path": str(p.relative_to(root)),
                "extension": ext or "[sem extensão]",
                "category": classify(ext),
                "size_bytes": stat.st_size,
                "modified_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat()
            })
        except (OSError, ValueError) as exc:
            rows.append({"relative_path": str(p), "extension": "", "category": "read_error",
                         "size_bytes": None, "modified_utc": "", "error": str(exc)})
    counts = Counter(r["category"] for r in rows)
    report = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source_folder_name": root.name,
        "total_files": len(rows),
        "category_counts": dict(counts),
        "files": rows,
        "notice": "Inventário somente leitura; nenhum arquivo foi extraído ou modificado."
    }
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = out / f"inventory_{stamp}.json"
    csv_path = out / f"inventory_{stamp}.csv"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    fields = ["relative_path", "extension", "category", "size_bytes", "modified_utc", "error"]
    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Arquivos encontrados: {len(rows)}")
    print(f"JSON: {json_path.resolve()}")
    print(f"CSV:  {csv_path.resolve()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
