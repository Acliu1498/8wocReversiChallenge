Reversi Challenge
=================

What is Reversi?
----------------

Reversi is a simple board game played on an 8x8 board with black and
white disks. You can find detailed rules to the game on Wikipedia:

<https://en.wikipedia.org/wiki/Reversi>

Your challenge
--------------

Write a command-line program in the language of your choice that:

-   accepts a [JSON-formatted](https://en.wikipedia.org/wiki/JSON) board state move via [stdin](https://en.wikipedia.org/wiki/Standard_streams)
-   prints a [JSON-formatted](https://en.wikipedia.org/wiki/JSON) board state to [stdout](https://en.wikipedia.org/wiki/Standard_streams) that is the
    result of applying the move to the input board state.

An example Python script, `example_solution_template.py` that reads from
stdin and writes to stdout is provided.  It does not solve the challenge,
however -- that's up to you!

Your program will be called by sending your program a JSON board state
through its `stdin`, and its performance will be evaluated based on the
JSON board state your program prints to its `stdout`. The formatting of
your output JSON does not matter -- only the structure and values need to
match the expected output.

The next sections describe the input that will be given to your program,
and the output that is expected from it:

### Input

Your input will be a JSON object containing a board state and a player
move; for example:

```json
{
    "board": [
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 2, 1, 0, 0, 0,
                0, 0, 0, 1, 2, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0
             ],
    "move":  {
                "player": 1,
                "column": 4,
                "row":    3
             }
}
```

`board` is an array of integers of length 64, conceptually arranged in
rows and columns. Counting from zero:

-   Item 0 is the upper-left cell of the board.
-   Item 7 is the upper-right cell of the board.
-   Item 56 is the lower-left cell of the board.
-   Item 63 is the lower-right cell of the board.

`move` is an object describing the next move:

-   `player`: Either `1` (black) or `2` (white)
-   `column`: A value from `1` (leftmost column) to `8`
    (rightmost column)
-   `row`: A value from `1` (top column) to `8` (bottom column)

### Output

Your output must be a JSON object containing the new board state after
applying the player's move; for example:

```json
{
    "board": [
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 1, 0, 0, 0, 0,
                0, 0, 0, 1, 1, 0, 0, 0,
                0, 0, 0, 1, 2, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0
             ]
}
```

`board`: Same structure as the `board` array in the input.

How to Start
------------

You can find some starting materials on GitHub. You don't need to be
able to run these Python scripts to create your program, but you may
find them helpful to verify that your code works.

<https://github.com/WycliffeAssociates/8woc2018_reversi>

### tests/tests.json

This is a set of tests that will be run against your code. Your code must
pass at least these tests. Each test contains an `input` object that is
passed to your program's `stdin` as JSON, and an `expected` object that is
compared against your program's output to `stdout`.

An excerpt from the file containing one test is shown below:

```json
[
  {
    "input": {
      "board": [
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 2, 1, 0, 0, 0,
        0, 0, 0, 1, 2, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0
      ],
      "move": {
        "player": 1,
        "column": 4,
        "row":    3
      }
    },
    "expected": {
      "board": [
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 1, 1, 0, 0, 0,
        0, 0, 0, 1, 2, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0
      ]
    }
  },
  ...
]
```

### tester.py

A Python script that runs the tests against an executable. You may find it
helpful to run this against your executable to ensure the tests pass. It
will print a JSON object containing the result of the test, and return 1 if
any of the tests failed.

```bash
# Run tester
./tester.py ./your-executable > test_results.json
```

### example_solution_template.py

A sample executable that naively returns the board state it was given.
This will fail all tests.

```bash
# Test naive executable
./tester.py ./example_solution_template.py > all_tests_fail.json
# Print errorlevel of 1 (at least one test failed)
echo $? 
```
