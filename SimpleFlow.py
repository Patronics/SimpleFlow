import time

def parse_line(line):
    line = line.strip()
    if not line or line.startswith('?'):
        return None
    tokens = line.split(None, 1)
    if len(tokens) == 1:
        if line.endswith(':'):
            return ('label', line[:-1])
        else:
            return (tokens[0], None)
    elif len(tokens) == 2:
        return tokens
    else:
        raise ValueError(f"Invalid line: {line}")

def parse_program(program):
    lines = program.splitlines()
    commands = [parse_line(line) for line in lines]
    commands = [cmd for cmd in commands if cmd is not None]
    return commands

def run_program(commands):
    goto_labels = {cmd[1]: idx for idx, cmd in enumerate(commands) if cmd[0] == 'label'}
    idx = 0
    while idx < len(commands):
        cmd, arg = commands[idx]
        if cmd == "pause":
            time.sleep(float(arg))
        elif cmd == "print":
            print(arg)
        elif cmd == "goto":
            if arg not in goto_labels:
                raise ValueError(f"Invalid goto label: {arg}")
            idx = goto_labels[arg]
            continue
        elif cmd == "label":
            pass  # Ignore label lines
        else:
            raise ValueError(f"Invalid command: {cmd}")
        idx += 1

def main():
    program = """
        ? This is a simple example program
        print Hello
        pause 1
        print World
        pause 1
        goto end
        print NotExecuted
        ? Program ends here
        goto end
        ? Label for program end
        end:
    """

    try:
        commands = parse_program(program)
        run_program(commands)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
