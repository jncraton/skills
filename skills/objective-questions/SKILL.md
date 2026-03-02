---
name: objective-questions
description: Generate objective questions
---

Produce questions that have only one obvious answer, such that they can be automatically graded. Questions may be mutliple choice, but favor short, objective answers or numeric answers. If material is related to software, include programs that ensure students can read and understand code.

## Examples

1. What will be the output of the following Python program?

    i = 0

    while True:
        i += 1
        
        if i % 2 == 0:
            continue

        if i > 10:
            break

    print(i)

Answer: 11

2. On what line is the syntax error in this program?

    1 | end = 20
    2 |
    3 | for i in range(20)
    4 |    print(i)

Answer: 3

3. What Python keyword should replace the blank in order to allow this program to run correctly?

    ___ square(n):
        return n*n

    assert(square(2) == 4)

Answer: def

4. Consider the following simple lexer:

    import re

    def lex(text):
        rules = [
            ("operator", r"\+"),
            ("number", r"[0-9]+"),
        ]
        
        for token in text.split():
            for rule in rules:
                match = re.match(rule[1], token) 

                if match:
                        yield (rule[0], match[0])

How many total tokens would be yielded by the lexer for the input "12 + 34"?

Answer: 3
