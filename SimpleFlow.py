#!/usr/bin/env python3
import sys
import time

def simple_flow_interpreter(file_name=None):
    if file_name:
        with open(file_name, 'r') as file:
            program = file.read().split('\n')
    else:
        program = ['pause 1', 'print Hello, World!', 'pause 1', 'end']

    labels = {}
    counters = {}

    for idx, line in enumerate(program):
        if line.startswith('?'):
            continue
        if line.endswith(':'):
            labels[line[:-1]] = idx

    line_number = 0
    while line_number < len(program):
        line = program[line_number].strip()
        if line.startswith('?'):
            line_number += 1
            continue

        parts = line.split()

        if len(parts) == 0:
            line_number += 1
            continue

        command, args = parts[0], parts[1:]

        if command == "pause":
            time.sleep(float(args[0]))
        elif command == "print":
            print(" ".join(args))
        elif command == "goto":
            label = args[0]
            count = int(args[1]) if len(args) > 1 else 1

            counter_key = f"{label}_{line_number}"

            if counter_key not in counters:
                counters[counter_key] = count

            if counters[counter_key] > 0:
                line_number = labels[label]
                counters[counter_key] -= 1
                continue
        elif command == "end":
            break

        line_number += 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        simple_flow_interpreter(sys.argv[1])
    else:
        simple_flow_interpreter()
