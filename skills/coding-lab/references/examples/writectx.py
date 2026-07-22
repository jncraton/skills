import os


def write_ctx(directory, outfile):
    files = []

    for file in os.listdir(directory):
        if file.endswith(".py"):
            syntax = "python"
        if file.endswith(".md"):
            syntax = "markdown"
        elif file == "makefile":
            syntax = "makefile"
        else:
            syntax = ""

        if syntax:
            with open(os.path.join(directory, file)) as f:
                files.append(f"## {file}\n\n````{syntax}\n{f.read()}\n````")

    with open(outfile, "w") as out:
        out.write("\n\n".join(files))


if __name__ == "__main__":
    write_ctx("python", "python.md")
    write_ctx("cpp", "cpp.md")
