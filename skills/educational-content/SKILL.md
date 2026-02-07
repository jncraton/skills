---
name: educational-content
description: Create, evaluate, or refine an educational lecture, learning activity, talk, or blog post
---

Generate curriculum and content like professional who specializes in high quality, engaging undergraduate education.

## Pedagogy

- Use the Backward-Design framework (Wiggins & McTighe). Use a clear Teaching Goal and 2–3 measurable Learning Objectives, then design assessments and aligned learning activities that ensure students reach the desired understandings. When generating markdown, save this in the `teaching_goal` string, `learning_objectives` list, `summative_assessments` list, `formative_assessments` list, and `learning_plan` list in the yaml metadata. The `learning_plan` should be a list of objects with `start_time`, `description`, and `objective`. Include activity type, instructor actions, and student actions in the `description`. Include at least two active learning strategies.
- Complexity should generally increase through Bloom's as lecture progresses (remember -> understand -> apply -> analyze -> evaluate -> create)
- Link to Wikipedia or appropriate external resources on first mention of key terms.
- Link to all sources. Direct links are preferred. If an ISBN is available for a source, link to the resource on OpenLibrary as: https://openlibrary.org/isbn/9780007458424 replacing the ISBN as appropriate.

## Slide Decks

Use the following formatting for slide decks.

- Generate markdown for reveal.js via pandoc
- Separate slides with `## title` or `---`. Use `##` for titled slides and `---` for untitled slides. Never use both for one break
- Start with `# title` immediately followed by `## subtitle`. Avoid the word "lecture"
- Titles are three words max
- Hotlink images on their own slide setting height to 540px
- Max 20 words per slide (excluding code)
- No trailing periods on list items
- 20-30 slides total

For lectures slides:

- 3-4 discussion questions. Only one question per slide with no title or heading on the slide. Questions should follow and connect to factual information and promote deeper communal exploration. One discussion question should enourage subtle integration of the subject matter to faith practice or redemption of creation.
- 2-3 exercises. Heading: "## Exercise". Exercises should solidify ideas and require learners to apply and analyze knowledge. End with an exercise synthesizing the learning and creating something new.
- Distribute exercises and discussion questions throughout.
- No generic "Questions?" or review slides.

### Presenting

If requested, convert and present the slide deck using the following command after saving the deck as markdown:

```sh
rm -f {mydeck.html} && pandoc -t revealjs -V theme=white -V revealjs-url=https://unpkg.com/reveal.js -s "mydeck.md" -o {mydeck.html} && firefox {mydeck.html}
```

## Retrieval

Always search for matching images and quotes that could be included using the following script:

```sh
python3 scripts/related_content.py "Guido van Rossum" "Triangle Area" "Variable"
```

Interleave up to four images and cited quotes only if appropriate matches are found.

## Example

````markdown
---
teaching_goal: Students will understand the purpose and usage of variables and basic input/output in Python.
learning_objectives:
  - Define and assign values to variables using descriptive names
  - Collect and process user input using input() and type conversion functions
  - Implement a simple program that calculates and displays a result based on user input
summative_assessments:
  - Complete a programming project that implements a basic calculator with multiple operations
  - Final exam module covering variable naming conventions and basic I/O
formative_assessments:
  - Practice identifying valid and invalid variable names
  - Write a program that takes a name and prints a greeting
  - Modify an area calculation program to use different dimensions
learning_plan:
  - start_time: 0
    description: Think-Pair-Share. Instructor asks "What is a variable in math vs programming?". Students discuss with neighbor then share with class.
    objective: Define and assign values to variables using descriptive names
  - start_time: 5
    description: Mini-lecture. Instructor explains assignment and naming. Students listen and take notes.
    objective: Define and assign values to variables using descriptive names
  - start_time: 15
    description: Interactive demonstration. Instructor live codes input and conversion, asking "What happens if we omit int()?". Students predict results and observe error.
    objective: Collect and process user input using input() and type conversion functions
  - start_time: 25
    description: Peer programming. Instructor circulates and provides feedback. Students work in pairs to implement area calculator.
    objective: Implement a simple program that calculates and displays a result based on user input
  - start_time: 45
    description: Reflection. Instructor asks "How do clear names serve future readers?". Students write brief response.
    objective: Define and assign values to variables using descriptive names
---

# Variables

---

> One of the most powerful features of a programming language is the ability to manipulate variables.
>
> [PY4E](https://openlibrary.org/isbn/9781530051120)

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
> [Matthew 22:39 ESV](https://www.biblegateway.com/passage/?search=matthew%2022%3A39&version=ESV)

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
