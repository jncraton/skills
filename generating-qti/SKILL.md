---
name: generating-qti
description: Apply this skills to generate a quiz or test for an LMS in QTI format
---

Only use multiple choice questions with four possible answers. A variety of questions should be provided focusing different levels of Bloom's revised taxonomy (remember, understand, apply, analyze, evaluate, create).

## Steps

Two files are created based on the base name provided by the user. They must be generated in the following order:

1. Directly generate the json for a quiz as the user-supplied filename with a .json extension.
2. Build the qti zip file for the quiz using the following shell command: `pipx run json2qti {quiz json from step 1}`

## Text File Format

The output text file should be in this format:

```json
{
  "Generated quiz title": {
    "What is 1+1?": ["2", "3", "4", "5"],
    "What is 1+2?": ["3", "4", "5", "6"]
  }
}
```

The correct answer must always be listed first.
