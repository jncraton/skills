---
name: class-deck
description: Create or refine engaging undergraduate class session slide deck
---

Begin with teaching_goal and measurable learning_objectives saved in YAML block.

Complexity should generally increase through Bloom: Remember and Understand -> Apply or Analyze -> Evaluate or Create

Save deck as revealjs markdown for pandoc with a .md extension.

## Formatting

- Open deck with `# title` immediately followed by new slide
- Begin slides with `## title` for titled slides or `---` for untitled slides
- Titles are three words max and avoid the word "lecture"
- Discussion questions appear alone without title or heading
- Exercise slides begin `## Exercise` and apply ideas
- Hotlink images on their own slide setting height=540px
- No trailing periods on list items

## Structure

- About twenty slides total
- Twenty max words per slide, excluding code
- Spread applied exercises and communal exploration questions throughout
- No review or question invitation slides
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

---

![Triangle Area](https://upload.wikimedia.org/wikipedia/commons/7/7c/TriangleArea.svg){height=540px}

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
