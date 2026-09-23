---
name: class-deck
description: Create or refine class session slide deck
---

Produce slide deck like a professional who specializes in high quality, engaging undergraduate education.

Create clear teaching_goal and measurable learning_objectives saved in markdown file.

Complexity should increase through Bloom. Remember -> Understand -> Apply -> Analyze -> Evaluate -> Create

## Formatting

- Generate revealjs markdown saving the deck to file with md extension
- Begin deck with YAML frontmatter followed by `# title` immediately followed by `## subtitle`
- Separate slides with `## title` for titled slides or `---` for untitled slides
- Titles are three words max and avoid the word "lecture"
- Hotlink images on their own slide setting height=540px
- No trailing periods on list items

## Structure

- About twenty slides total
- Twenty words max per slide, excluding code
- Distribute some exercises and discussion questions throughout
- Discussion questions appear alone without title or heading and connect factual information to promote deeper communal exploration
- Exercise slides begin `## Exercise` and apply ideas
- No generic "Questions?" or review slides
- End with exercise synthesizing learning and creating something new

## Example

Example deck saved as `variables.md`

````markdown
---
teaching_goal: Students will understand variables and basic input and output.
learning_objectives:
  - Assign values to well named variables
  - Process input using input() and type conversions
  - Create program that displays computed result from input
---

# Variables

## Definition

A variable is a named container for a value

## Statements

- A statement is an entity that the interpreter can execute

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

- May include letters and numbers
- Should be lowercase
- May not begin with a number
- Should document what the variable is for

---

> You should name a variable using the same care with which you name a first-born child.
>
> Bob Martin

---

Who are variable names for?

## Input Statement

- `input(prompt)`
- Accepts user input as a string
- `prompt` will be shown to user

## input Example

```python
request = input("May I help?")

print("You want help with:")
print(request)
print("I am unable to help with that.")
```

## int

- `int` converts strings to integers

## Examples

```python
>>> int("4")
4
>>> int("red")
ValueError
>>> int(".5")
ValueError
```

## Example Program

```python
base = int(input("Base: "))
height = int(input("Height: "))
area = 0.5 * base * height
print("Area of triangle:")
print(area)
```

---

How could the readability of this program be improved?

## Exercise

Modify the previous example to compute the area of a rectangle.
````
