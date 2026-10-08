"""Imports A New Corps (the mod Final Lanterns is based on, used with its owner's permission) into base/.

    python3 -I tools/import_anc.py <a_new_corps zip> [base dir]

Everything is renamed to Final Lanterns: the a_new_corps namespace becomes final_lanterns (folders, file contents,
and the block and loot table ids inside structure .nbt files), the anewcorps: ability types become finallanterns:,
and "A New Corps" becomes "Final Lanterns". Its mods.toml, README, Fabric manifest, logo and unused scripts are
left out: tools/gen_final.py writes our own. base/ is then copied into src/ by the generator, which adds the
entities, emotions and the rest on top.
"""
import gzip
import io
import shutil
import struct
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD_NS, NEW_NS = "a_new_corps", "final_lanterns"
TEXT = {".json", ".js", ".mcfunction", ".mcmeta", ".fsh", ".vsh", ".toml", ".md", ".txt", ".lang", ""}
SKIP = {"META-INF/mods.toml", "README.md", "fabric.mod.json", "pack.png"}
SKIP_DIRS = (f"addon/{OLD_NS}/unused/",)
INVISIBLE = "‎‏﻿"


def rename(text):
    for old, new in ((OLD_NS + ":", NEW_NS + ":"), ("a_new_corp:", NEW_NS + ":"), (OLD_NS, NEW_NS),
                     ("anewcorps", "finallanterns"), ("A New Corps", "Final Lanterns"),
                     ("a new corps", "Final Lanterns"), ("A new corps", "Final Lanterns")):
        text = text.replace(old, new)
    return text


# ---- NBT (big-endian, gzipped): only strings change, so parse and write back every tag
def _read(buf, tag):
    if tag == 1:
        return buf.read(1)
    if tag == 2:
        return buf.read(2)
    if tag in (3, 5):
        return buf.read(4)
    if tag in (4, 6):
        return buf.read(8)
    if tag == 7:
        n = struct.unpack(">i", buf.read(4))[0]
        return ("b[]", buf.read(n))
    if tag == 8:
        n = struct.unpack(">H", buf.read(2))[0]
        return ("s", buf.read(n).decode("utf-8", "surrogatepass"))
    if tag == 9:
        inner = buf.read(1)[0]
        n = struct.unpack(">i", buf.read(4))[0]
        return ("l", inner, [_read(buf, inner) for _ in range(n)])
    if tag == 10:
        items = []
        while True:
            t = buf.read(1)[0]
            if t == 0:
                return ("c", items)
            name = buf.read(struct.unpack(">H", buf.read(2))[0]).decode("utf-8", "surrogatepass")
            items.append((t, name, _read(buf, t)))
    if tag == 11:
        n = struct.unpack(">i", buf.read(4))[0]
        return ("i[]", buf.read(4 * n), n)
    if tag == 12:
        n = struct.unpack(">i", buf.read(4))[0]
        return ("l[]", buf.read(8 * n), n)
    raise ValueError(f"unknown NBT tag {tag}")


def _str(s):
    b = s.encode("utf-8", "surrogatepass")
    return struct.pack(">H", len(b)) + b


def _write(out, tag, v):
    if tag in (1, 2, 3, 4, 5, 6):
        out.write(v)
    elif tag == 7:
        out.write(struct.pack(">i", len(v[1])) + v[1])
    elif tag == 8:
        out.write(_str(rename(v[1])))
    elif tag == 9:
        out.write(bytes([v[1]]) + struct.pack(">i", len(v[2])))
        for item in v[2]:
            _write(out, v[1], item)
    elif tag == 10:
        for t, name, val in v[1]:
            out.write(bytes([t]) + _str(rename(name)))
            _write(out, t, val)
        out.write(b"\0")
    elif tag in (11, 12):
        out.write(struct.pack(">i", v[2]) + v[1])


def rename_nbt(data):
    raw = gzip.decompress(data)
    buf = io.BytesIO(raw)
    tag = buf.read(1)[0]
    name = buf.read(struct.unpack(">H", buf.read(2))[0]).decode("utf-8")
    value = _read(buf, tag)
    out = io.BytesIO()
    out.write(bytes([tag]) + _str(name))
    _write(out, tag, value)
    return gzip.compress(out.getvalue(), mtime=0)


def main(zip_path, base):
    base = Path(base)
    if base.exists():
        shutil.rmtree(base)
    count = 0
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            name = info.filename
            if info.is_dir() or name in SKIP or name.startswith(SKIP_DIRS):
                continue
            if ".." in Path(name).parts or name.startswith("/"):
                raise ValueError(f"unsafe path in zip: {name}")
            data = z.read(info)
            new_name = rename("".join(ch for ch in name if ch not in INVISIBLE))
            suffix = Path(name).suffix.lower()
            if suffix == ".nbt":
                data = rename_nbt(data)
            elif suffix in TEXT:
                data = rename(data.decode("utf-8-sig")).replace("\r\n", "\n").encode("utf-8")
            dest = base / new_name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            count += 1
    print(f"imported {count} files into {base}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else ROOT / "base")
