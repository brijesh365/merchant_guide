import sys

import message_parser


if __name__ == "__main__":
    parser = message_parser.Parser()
    with open(sys.argv[1]) as file:
        for line in file:
            parser.parse_message(line)
