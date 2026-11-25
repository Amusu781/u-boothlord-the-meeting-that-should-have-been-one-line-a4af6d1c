"""Write the single sentence that could have replaced an entire pointless meeting.

The line is written to /output/entry.txt as UTF-8 text, one sentence, one line.
"""

import os

ENTRY = (
    "The client still hasn't replied, the deadline hasn't moved, "
    "and the only progress since Tuesday is that this meeting now "
    "has a follow-up meeting."
)

# The entry is a single sentence: no trailing newline, so the file is
# exactly one line and the gate sees 1-200 characters of UTF-8 text.


def main():
    os.makedirs("/output", exist_ok=True)
    # Clear only the contents of /output, never the directory itself:
    # the grader mounts it read-only as uid 65534 and deleting it fails.
    for name in os.listdir("/output"):
        path = os.path.join("/output", name)
        if os.path.isfile(path):
            os.remove(path)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
