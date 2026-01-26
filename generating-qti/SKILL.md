---
name: generating-qti
description: Apply this skills to generate a quiz or test for an LMS in QTI format
---

Only use multiple choice questions with four possible answers. A variety of questions should be provided focusing different levels of Bloom's revised taxonomy (remember, understand, apply, analyze, evaluate, create).

## Steps

Two files are created based on the base name provided by the user. They must be generated in the following order:

1. Directly generate the text for a quiz as the user-supplied filename with a .txt extension.
2. Build the qti zip file for the quiz using the following shell command: `yes "" | pipx run text2qti {quiz text file from step 1}`

## Text File Format

The output text file should be in this format:

```markdown
Quiz title: Addition
Quiz description: Checking addition.

1.  What is 2+3?
a)  6
b)  1
*c) 5
d) 7

2.  What is 1+2?
a)  6
*b)  3
c) 5
d) 7
```

Note that `*` is used to denote the correct answer.
