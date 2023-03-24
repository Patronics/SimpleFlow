#!/usr/bin/env python3

import time
import sys

def parse_line(line):
    line = line.strip()
    if not line or line.startswith('?'):
        return None
    tokens = line.split(None, 1)
    cmd = tokens[0]
    if len(tokens) == 1:
        if line.endswith(':'):
            return ('label', line[:-1], None)
        else:
            return (cmd, None, None)
    elif len(tokens) == 2:
        arg = tokens[1]
        if cmd == "goto":
            args = arg.split(None, 1)
            if len(args) == 1:
                return cmd, args[0], None
            else:
                return cmd, args[0], args[1]
        else:
            return cmd, arg, None
    else:
        raise ValueError(f"Invalid line: {line}")

def parse_program(program):
    lines = program.splitlines()
    commands = [parse_line(line) for line in lines]
    commands = [cmd for cmd in commands if cmd is not None]
    return commands

def run_program(commands):
    goto_labels = {cmd[1]: idx for idx, cmd in enumerate(commands) if cmd[0] == 'label'}
    loop_counters = {}
    idx = 0
    while idx < len(commands):
        cmd, arg, loop_arg = commands[idx]
        if cmd == "pause":
            time.sleep(float(arg))
        elif cmd == "print":
            print(arg)
        elif cmd == "goto":
            if arg not in goto_labels:
                raise ValueError(f"Invalid goto label: {arg}")
            if loop_arg:
                max_loops = int(loop_arg)
                if arg not in loop_counters:
                    loop_counters[arg] = 1
                else:
                    loop_counters[arg] += 1
                if loop_counters[arg] <= max_loops:
                    idx = goto_labels[arg]
                    continue
            else:
                idx = goto_labels[arg]
                continue
        elif cmd == "label":
            pass  # Ignore label lines
        else:
            raise ValueError(f"Invalid command: {cmd}")
        idx += 1

def main(file_path=None):
    default_program = """
        ? This is a simple example program
        print Start
        pause 1
        ? Program loop here
        loop:
        print InsideLoop
        pause 0.5
        goto loop 3
        ? Label for end of loop
        end_of_loop:
        print AfterLoop
        pause 1
        goto end
        ? Label for program end
        end:
    """

    if file_path:
        with open(file_path, 'r') as file:
            program = file.read()
    else:
        program = default_program

    try:
        commands = parse_program(program)
        run_program(commands)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
