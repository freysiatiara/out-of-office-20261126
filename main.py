"""The Painfully Honest Out-of-Office — make.fun bounty entry.

Writes a single-sentence out-of-office auto-reply (<=200 characters)
to the output path. Stdlib only.
"""

import os

ENTRY = (
    "I'm away until next week \u2014 and honestly, this break is overdue, "
    "so I'll answer your message with a clear head instead of a tired one."
)


def resolve_output_path():
    """Resolve where the entry goes.

    Precedence: ENTRY_OUTPUT env var, then OUTPUT_DIR / MAKEFUN_OUTPUT_DIR,
    then /output/entry.txt, falling back to the script's own directory when
    /output is not writable (local runs).
    """
    env_path = os.environ.get("ENTRY_OUTPUT")
    if env_path:
        return env_path
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    candidate = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        probe = os.path.join("/output", ".write_probe")
        with open(probe, "w") as fh:
            fh.write("probe")
        os.remove(probe)
        return candidate
    except OSError:
        here = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(here, "entry.txt")


def validate_entry(text):
    """Guard: the entry must be exactly one sentence of 1-200 characters."""
    cleaned = text.strip()
    assert 1 <= len(cleaned) <= 200, "entry must be 1-200 chars, got %d" % len(cleaned)
    assert cleaned.count(".") + cleaned.count("!") + cleaned.count("?") == 1, (
        "entry must be a single sentence"
    )
    return cleaned


def main():
    entry = validate_entry(ENTRY)
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(entry + "\n")
    os.chmod(path, 0o644)
    # Read-back check: what landed on disk must be exactly what we wrote.
    with open(path, "r", encoding="utf-8") as fh:
        on_disk = fh.read().rstrip("\n")
    assert on_disk == entry, "read-back mismatch"
    print("wrote %s (%d chars)" % (path, len(entry)))


if __name__ == "__main__":
    main()
