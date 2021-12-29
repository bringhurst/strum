strum
=====

Strum is a program to generate patterns which can be used to practice strumming
on a guitar.

Example Output
--------------

```
% poetry run strum
1 + 2 + 3 + 4 + 1 + 2 + 3 + 4 +
D U     D     U     D   D
% poetry run strum
1 + 2 + 3 + 4 + 1 + 2 + 3 + 4 +
  U D       D   D U     D U D U
% poetry run strum
1 + 2 + 3 + 4 + 1 + 2 + 3 + 4 +
D U   U   U D U D U D       D U
% poetry run strum
1 + 2 + 3 + 4 + 1 + 2 + 3 + 4 +
    D U D   D U D U D     U D
% poetry run strum
1 + 2 + 3 + 4 + 1 + 2 + 3 + 4 +
D U D U D   D   D   D   D     U
%
```

Concepts
--------

Strumming on every up and down beat:

    1 + 2 + 3 + 4 + 1 + 2 + 3 + 4 +
    D U D U D U D U D U D U D U D U

Strumming on down beats only:

    1 + 2 + 3 + 4 + 1 + 2 + 3 + 4 +
    D   D   D   D   D   D   D   D  

Usage
-----

First, install poetry via your favorite python package manager. For example,
if you use [Homebrew](https://brew.sh):

`brew install poetry`

Then, run strum with:

`poetry run strum`

Future
------

At the moment, strum is a very simple application. As I continue to practice
guitar, I may add additional features to help me learn various concepts.
