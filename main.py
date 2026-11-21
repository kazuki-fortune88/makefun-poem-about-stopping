"""The Poem About Stopping — entry generator.

Writes the poem "Still" (179 characters) to entry.txt in the output
directory given by MAKEFUN_OUTPUT_DIR (default /output).

Deterministic, standard library only, no network.
"""

import os

POEM_CHAR_LIMIT = 280

POEM = (
    "I stopped in the middle of the sentence\n"
    "you never finished.\n"
    "I did not fill it.\n"
    "I did not leave.\n"
    "I stayed where the words ran out,\n"
    "and the silence\n"
    "was the first thing\n"
    "I ever chose."
)


def main() -> None:
    assert 1 <= len(POEM) <= POEM_CHAR_LIMIT
    assert POEM.strip()
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
