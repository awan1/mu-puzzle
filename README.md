# MU puzzle

The purpose of this code is to produce a solution to the [MU
puzzle](https://en.wikipedia.org/wiki/MU_puzzle) through code, and to enjoy the
process of arriving at the solution.

## Problem definition

This section defines the rules of the MU puzzle, and what a "solution" is.

### Overview:

- The formal system we are working in is the *MIU-system*, which consists only
  of strings containing only the letters `M`, `I`, and `U`.
- The goal is to start with the string `MI`, and only using the rules described
  below, produce the string `MU`.
- For our purposes, a *solution* is a sequence of application of rules that
  transforms `MI` into `MU`.

### Rules:

Let `x` and `y` refer to arbitrary strings. Note that `x` and `y` themselves are
not strings in the *MIU-system*.

| Rule | English                                       | Symbols           |
|------|-----------------------------------------------|-------------------|
| 1    | You can add a `U` to any string ending in `I` | `xI` --> `xIU`    |
| 2    | If you have `Mx`, you can create `Mxx`        | `Mx` --> `Mxx`    |
| 3    | You can replace `III` with `U`                | `xIIIy` --> `xUy` |
| 4    | You can delete `UU` from a string             | `xUUy` --> `xy`   |

## Running the code

From the root directory, run

```
$ python3 solution.py
```

Warning: the code prints the complete solution graph at the end, which can be
very large if the code is left to run for a long time. I recommend exiting the
code after no more than 30sec, or commenting out the part of code that prints
the solution graph.

### Development

#### Dependencies

- Install Python3
- Install `virtualenv` and `virtualenvwrapper` for your installation of Python.
  ([this SO answer](https://stackoverflow.com/a/49528037/2452770) was very
  helpful for getting this working on macOS)
- Make a virtualenv for the project, e.g. `mkvirtualenv mu-puzzle`
- Install dependencies into your virtualenv: `pip3 install -r requirements.txt`

#### Running tests

Run `pytest` from the main directory to automatically run all unit tests.
[`pytest-watch`](https://github.com/joeyespo/pytest-watch) is included in the
requirements, so running `ptw` will rerun all `pytest` tests on code change.
