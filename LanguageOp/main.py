import sys
import parser


def main():
    if len(sys.argv) < 2:
        print("Uso: mi_comando <ruta>")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r") as file:
        content = file.read()

    parser.parser.parse(content)


if __name__ == "__main__":
    main()
