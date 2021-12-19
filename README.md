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

|------|-----------------------------------------------|-------------------|
| Rule | English                                       | Symbols           |
|------|-----------------------------------------------|-------------------|
| 1    | You can add a `U` to any string ending in `I` | `xI` --> `xIU`    |
|------|-----------------------------------------------|-------------------|
| 2    | If you have `Mx`, you can create `Mxx`        | `Mx` --> `Mxx`    |
|------|-----------------------------------------------|-------------------|
| 3    | You can replace `III` with `U`                | `xIIIy` --> `xUy` |
|------|-----------------------------------------------|-------------------|
| 4    | You can delete `UU` from a string             | `xUUy` --> `xy`   |
|------|-----------------------------------------------|-------------------|

## Running the code

TODO: provide instructions for running the code
