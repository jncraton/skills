---
name: quiz
description: Generate Canvas quiz
---

Only use multiple choice questions with four possible answers. A variety of questions should be provided focusing different levels of Bloom's revised taxonomy (remember, understand, apply, analyze, evaluate, create).

## Steps

1. Directly generate the json for a quiz as the user-supplied filename with a .json extension.
2. Build the qti zip file for the quiz using the following shell command: `uvx json2qti {quiz.json}`

## File Format

The output json file should be in this format.

1.  Quiz Title: The top-level key.
2.  Questions: Keys inside the object.
3.  Answers: A list of strings. The first answer is always the correct one.

Rough schema:

```json
{
  "Quiz Title": {
    "Question 1": ["correct", "distract", "distract", "distract"],
    "Question 2": ["correct", "distract", "distract", "distract"]
  }
}
```

Math example:

```json
{
  "Basic Math Quiz": {
    "What is 1+1?": ["2", "3", "4", "5"],
    "What is 1+2?": ["3", "4", "5", "6"]
  }
}
```

Code snippets may be included using markdown-style syntax:

- Inline Code: Wrap text in single backticks (\`).
- Block Code: Wrap text in triple backticks (\`\`\`).

Code example:

````json
{
  "Python Quiz": {
    "What does `print('hello')` output?": ["`hello` to stdout", "`hello` to stderr", "Nothing"],
    "What does this function do?\n```\ndef add(a, b):\n    return a + b\n```": [
      "Returns the sum of two numbers",
      "Returns the product of two numbers",
      "Prints the numbers"
    ]
  }
}
````
