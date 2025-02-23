import sys
import lang_op.parser as pr


def main():
    if len(sys.argv) < 2:
        print("Uso: lang <rutoa de archivo .lang>")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r") as file:
        content = file.read()

    pr.parser.parse(content)


if __name__ == "__main__":
    main()
