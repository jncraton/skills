---
name: class-deck
description: Create or refine class session slide deck
---

Generate a slide deck like a professional who specializes in high quality, engaging undergraduate education.

### Backward Design Framework

Create a clear Teaching Goal and a few measurable learning objectives. Save the teaching_goal and learning_objectives in markdown.

## Pedagogy

Complexity should increase through Bloom's. Remember -> Understand -> Apply -> Analyze -> Evaluate -> Create

## Slide Deck

Use the following formatting for slide decks.

- Generate markdown for revealjs via pandoc saving the deck to file with md extension
- Start with `# title` immediately followed by `## subtitle`
- Separate slides with `## title` for titled slides or `---` for untitled slides. Never use both for one break
- Titles are three words max and avoid the word "lecture"
- Hotlink images on their own slide setting height to 540px
- No trailing periods on list items
- Max twenty words per slide (excluding code)
- About twenty slides total

## Structure

- Distribute a few exercises and discussion questions throughout.
- Discussion questions appear alone with no title or heading.Questions connect to factual information and promote deeper communal exploration. One discussion question should encourage subtle integration of faith practice or redemption of creation
- Exercise slides begin `## Exercise` and solidify ideas through application and analysis. End with an exercise synthesizing learning and creating something new
- No generic "Questions?" or review slides

## Example

Example slide deck saved as `variables.md`

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

`print("Hello, world")`

## Assignment Statement

- Creates or rebinds a variable
- Gives the variable a value

```python
height = 5
```

## Usage

- Useful for organizing data flow
- Provide human-readable names for values
- Allow values to be reused

## Example

```python
>>> base = 3
>>> height = 4
>>> area = 0.5 * base * height
>>> area
6.0
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
user_msg = input("How may I help you?")

print("You want help with:")
print(user_msg)
print("I am not able to help with that.")
```

## int

- `int` converts strings to integers

## Examples

```python
>>> '7'
'7'
>>> int("4")
4
>>> int("red")
...ValueError...
>>> int("9.0")
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
