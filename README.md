# SimpleFlow

An interpreter for a deliberately simple scripting language, writen using ChatGPT 4 (The remainder of this readme was written with ChatGPT 3.5, with manual editing). 

# SimpleFlow Language Syntax

The SimpleFlow language is a simple scripting language that allows for basic control flow and input/output operations. This readme file describes the syntax of the SimpleFlow language as implemented by the provided interpreter.

## Basic Syntax

The SimpleFlow language is line-based, with each line of the program representing a single command or instruction. Lines may be empty, or may contain whitespace and comments. Comments start with the `?` character and continue until the end of the line.

## Commands

The following commands are supported by the SimpleFlow language:

### `pause <seconds>`

Pauses the program for the specified number of seconds. Example: `pause 5`

### `print <message>`

Prints the specified message to standard output. Example: `print Hello, World!`

### `goto <label> [<count>]`

Jumps to the specified label in the program. Each time the `goto` command is encountered, the jump is repeated, up to the threshold number `count`, if specified, before continuing to the next line of the program. Example: `goto loop 10`

### `end`

Ends the program. Example: `end`

## Labels

Labels are used to mark specific points in the program that can be jumped to with the `goto` command. Labels are defined by a line that ends with a colon (`:`) and are referenced by name in the `goto` command. Example: `loop:`

## Variables

The SimpleFlow language does not support variables.

## Execution

To execute a SimpleFlow program, run the provided interpreter with the filename of the program as the first command-line argument. If no filename is provided, a default program is executed. Example: `python3 simple_flow_interpreter.py my_program.sf`
