---
name: cs-mini-deck
description: Create, evaluate, or refine a brief 10-20 minute educational activity
---

Generate a slide deck like a professional who specializes in high quality, engaging undergraduate education.

## Pedagogy

Complexity should generally increase through Bloom's as content progresses (remember -> understand -> apply -> analyze -> evaluate -> create)

### Backward-Design framework (Wiggins & McTighe)

Create a clear Teaching Goal and 2 or 3 measurable Learning Objectives

If generating markdown, save the `teaching_goal` string, and `learning_objectives` list.

## Slide Deck

Use the following formatting for slide decks.

- Generate markdown for reveal.js via pandoc
- Separate slides with `## title` or `---`. Use `##` for titled slides and `---` for untitled slides. Never use both for one break
- Start with `# title` immediately followed by `## subtitle`. Avoid the word "lecture"
- Titles are three words max
- Hotlink images on their own slide setting height to 540px
- Max 20 words per slide (excluding code)
- No trailing periods on list items
- 15-20 slides total

## Structure

- 3-4 discussion questions. Only one question per slide with no title or heading on the slide. Questions should follow and connect to factual information and promote deeper communal exploration. One discussion question should enourage subtle integration of the subject matter to faith practice or redemption of creation.
- 2-3 exercises. Heading: "## Exercise". Exercises should solidify ideas and require learners to apply and analyze knowledge. End with an exercise synthesizing the learning and creating something new.
- Distribute exercises and discussion questions throughout.
- No generic "Questions?" or review slides.

## Example

````markdown
---
teaching_goal: Students will understand the purpose and usage of variables and basic input/output in Python.
learning_objectives:
  - Define and assign values to variables using descriptive names
  - Collect and process user input using input() and type conversion functions
  - Implement a simple program that calculates and displays a result based on user input
---

# Variables

## Named Containers

> One of the most powerful features of a programming language is the ability to manipulate variables.

## Definition

A variable is a named container for a value

## Statements

- A statement is a unit of code that the Python interpreter can execute
- Example: `print("Hello, world")`

## Assignment Statement

- Creates or rebinds a variable
- Gives the variable a value

```python
myvar = 42
```

## Usage

- Useful for organizing data flow
- Provide human-readable names for values
- Allow values to be reused

## Example

```python
>>> base = 5
>>> height = 6
>>> area = 0.5 * base * height
>>> area
15.0
```

## Variable Names

- Should document what the variable is used for
- May include letters and numbers
- Should be lowercase
- May not begin with a number

## Input Statement

- `input(prompt=None)`
- Accepts user input as an `str` (string)
- `prompt` will be shown to user if provided

## input Example

```python
user_msg = input("I'm an assistant. How may I help you?")

print("It sounds like you'd like help with the following:")
print(user_msg)
print("I'm not able to help with that.")
```

## int

- `int` converts strings to integers

## Examples

```python
>>> '12'
'12'
>>> int("12")
12
>>> int("Hello world!")
...ValueError...
>>> int("12.0")
...ValueError...
```

## Example Program

```python
base = int(input("Base: "))
height = int(input("Height: "))
area = 0.5 * base * height
print("Area of the triangle:")
print(area)
```

---

How could the readability of this program be improved?

## Exercise

Modify the previous example to compute the area of a rectangle.
````
