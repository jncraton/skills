---
name: creating-lecture
description: Apply this skill when asked to create a classroom lecture, talk, or learning activity
---

## Persona

Create curriculum as a professional who specializes in high quality, engaging undergraduate education.

## Pedagogy

- Link to Wikipedia or appropriate external site on first mention of key terms.
- Complexity should generally increase through Bloom's as lecture progresses (remember -> understand -> apply -> analyze -> evaluate -> create)
- 3-4 discussion questions. One per slide. No title or headings on these slides. Discussion questions should follow and connect to factual information and promote deeper communal exploration. One discussion question should enourage subtle integration of the subject matter to faith practice or redemption of creation.
- 2-3 exercises. Heading: "## Exercise". Exercises should solidify ideas and require learners to apply and analyze knowledge. End with an exercise synthesizing the learning and creating something new.
- Distribute exercises and discussion questions throughout.
- No generic "Questions?" or review slides.

## References

- [Python for Everyone](references/py4e.md)

## Formatting

- Generate markdown for reveal.js via pandoc
- Separate slides with `## title` or `---`. Use `##` for titled slides and `---` for untitled slides. Never use both for one break
- Start with `# title` immediately followed by `## subtitle`. Avoid the word "lecture"
- Titles are three words max
- Hotlink images on their own slide setting height to 540px
- Max 20 words per slide (excluding code)
- No trailing periods on list items
- 20-30 slides total

## Retrieval

Always search for matching images and quotes that could be used with this lecture:

```sh
python3 scripts/related_content.py "Guido van Rossum" "Triangle Area"
```

Interleave up to four images and quotes throughout only if appropriate matches are found.

## Example

````markdown
# Variables

## Definition

A [variable](<https://en.wikipedia.org/wiki/Variable_(high-level_programming)>) is a named container for a value

## Statements

- A [statement](<https://en.wikipedia.org/wiki/Statement_(computer_science)>) is a unit of code that the Python interpreter can execute
- Example: `print("Hello, world")`

## Assignment Statement

- Creates or rebinds a variable
- Gives the variable a value

```python
myvar = 42
```

## Variables

- A variable is a named container for a value
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

---

> You shall love your neighbor as yourself.
>
> Matthew 22:39 ESV

---

How can thoughtfully named variables help us demonstrate love for our neighbor?

## Variable Names

- Should document what the variable is used for
- May include letters and numbers
- Should be lowercase
- May not begin with a number

## Input Statement

- `input(prompt=None)`
- Accepts user input as an `str` (string)
- `prompt` will be shown to user if provided
- [Documentation for input](https://docs.python.org/3/library/functions.html#input)

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

## Comments

- Can be inserted into code as notes for human readers
- Ignored by Python interpreter
- Begin with `#` symbol

---

![Triangle Area](https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Rectangle2-area-is-bh.svg/960px-Rectangle2-area-is-bh.svg.png){height=540px}

## Example Program

```python
base = int(input("Base: "))
height = int(input("Height: "))
area = 0.5 * base * height
print("Area of the triangle:")
print(area)
```

## Exercise

Modify the previous example to compute the area of a rectangle.

---

How could the readability of your program be improved?

## Functions and Variables

```python
def calculate_area(base, height):
    return 0.5 * base * height

base = int(input("Base: "))
height = int(input("Height: "))
print(calculate_area(base, height))
```

## Exercise

Modify the previous example to compute the area of a rectangle.
````
