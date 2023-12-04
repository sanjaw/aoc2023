import utils.commandline as cmd

def read_lines(file_path: str):
    '''
    Reads the file and returns all the lines

    @return lines
    '''
    try:
        num_lines = int(cmd.check_arg("l"))
    except (ValueError, TypeError):
        num_lines = -1

    lines = []
    with open(file_path, "r") as file:
        if num_lines != -1:
            lines = [str(next(file)) for _ in range(num_lines)]
        else:
            lines = file.readlines()

    return lines