---
name: deck
description: Craft slide deck
---

Save deck as revealjs markdown for pandoc with a .md extension.

## Formatting

- Open with `# title` immediately followed by new slide
- Begin slides with `## title` for titled slides or `---` for untitled slides
- Titles are three words max and avoid the word "lecture"
- Hotlink images on their own slide setting height=540px
- Twenty max words per slide, excluding code
- No trailing periods on list items

## Example

Example deck saved as `deck.md`

````markdown
# Deck

## Slide 1

- List item
- Next item

---

![image](https://example.com/image.png){height=540px}

## Slide 3

Hello world
````
