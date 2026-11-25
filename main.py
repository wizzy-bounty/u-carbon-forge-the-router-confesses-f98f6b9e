import os

ENTRY = "I waited until the detective named the killer to collect on every password change you've blamed on me."


def write_entry(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
