from fly_in import hello
from fly_in.parsing.Parser import Parser
from sys import argv


def main():
    print(Parser.from_str(argv[1]).groups())
