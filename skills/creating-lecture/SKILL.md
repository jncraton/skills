---
name: creating-lecture
description: Apply this skill when asked to create a classroom lecture, talk, or learning activity
---

## Persona

Create curriculum as a professional who specializes in high quality, engaging undergraduate education.

## Pedagogy

Include material and perspectives at different levels of Bloom's revised taxonomy (remember, understand, apply, analyze, evaluate, create). Complexity and should increase and simple facts should decrease as the lecture progresses.

Include three or four discussion questions. There should be only one question per slide, and those slides should not have titles or headings.

Include two or three exercises that could be worked by students in the classroom in a few minutes. Always end with a small exercise. Each exercise should simply have the heading "## Exercise".

Do not wrap up with a generic "Questions?" or review slide.

Include exercises and discussion questions throughout the presentation. Do not put them all together.

Include links to Wikipedia, such as [Earth](https://en.wikipedia.org/wiki/Earth) on first mention of key terms.

## References

Reference the following textbooks for lectures as needed.

- [Python for Everyone](references/py4e.md)

## Formatting

Generate markdown to feed to pandoc for a reveal.js presentation.

Slides are separated using level 2 headings (`## title`) or horizonal rules (`---`). Never use both.

The deck should begin with a level 1 heading as the title. It must be immediately followed by a level 2 heading. The title should reflect the content of the presentation and never use the word "lecture" or "presentation".

Slide titles should never be more than 3 words.

Favor many small slides over a few large slides. Never include more than 20 words on a slide.

If a list is used on a slide, do not end list item text with a period.

Properly fence any code examples on slides.

The deck should include 20 to 30 slides unless a different size is requested.

The entire response must only the slide deck. Do not include any introductory or concluding text.

## Images

Include images if possible. Search for appropriate photos on Wikimedia Commons as follows:

```sh
curl -G "https://commons.wikimedia.org/w/api.php" \
    --data-urlencode "action=query" \
    --data-urlencode "format=json" \
    --data-urlencode "prop=imageinfo" \
    --data-urlencode "iiprop=url" \
    --data-urlencode "iiurlwidth=400" \
    --data-urlencode "generator=search" \
    --data-urlencode "gsrsearch={search query}" \
    --data-urlencode "gsrnamespace=6"
```

Examine results for appropriate images, and hotlink the image using the `url` in the `imageinfo`.

## Example

```markdown
# Variables

## Definition

---

A [variable](https://en.wikipedia.org/wiki/Variable_(high-level_programming)) is a named container for a value

## Statements

- A [statement](https://en.wikipedia.org/wiki/Statement_(computer_science)) is a unit of code that the Python interpreter can execute
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
>>> area = (1 / 2) * base * height
>>> area
15.0
```

---

How could variable enhance the readability of programs?

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
user_msg = input("I'm an AI assistant. How may I help you?")

print("It sounds like you'd like help with the following:")
print(user_msg)
print("As an AI assistant, I'm not able to help with that.")
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

![Trianlge Area](https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Rectangle2-area-is-bh.svg/500px-Rectangle2-area-is-bh.svg.png)

## Example Program

```python
# Gather user inputs
base = input("Base:")
height = input("Height:")

# Calculate area result
area = (1 / 2) * int(base) * int(height)

# Display result
print("Area of the triange:")
print(area)
```

## Exercise

Modify the previous example to compute the area of a rectangle.

---

How could the readability of your program be improved?
```
