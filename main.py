"""How Many Tabs Do You Have Open? — make.fun entry.

Writes the honest count of open browser tabs to /output/entry.txt:
a single number in digits and nothing else, no newline, no explanation.

The number, 137, is the count of tabs open right now: research tabs kept
open for weeks, half-read articles, and docs for a project that never ends —
the hoard of someone who never closes anything, across windows and days.
"""

import os

# The honest count of open browser tabs: 137.
TAB_COUNT = 137


def main():
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(str(TAB_COUNT))


if __name__ == "__main__":
    main()
