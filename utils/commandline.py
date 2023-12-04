import sys

def check_arg(command_arg: str):
    for idx, arg in enumerate(sys.argv[1:]):
        if arg == f"-{command_arg}":
            return sys.argv[idx + 1 + 1]