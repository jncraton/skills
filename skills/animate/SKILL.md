---
name: animate
description: Create a gif animation
---

Use manim to create a .gif animation using the following steps:

1. Generate and save the .py script using the same base name as the requested .gif
2. Run the following to generate and optimize the gif: `uvx manim -ql --format=gif {anim.py} -o {anim.gif} && gifsicle --optimize=3 --lossy=200 {anim.gif} -o {anim.gif}`

If the above command fails, the user may need to run the following at a system level:

sudo apt install build-essential python3-dev libcairo2-dev libpango1.0-dev gifsicle

## Style

Keep the animation simple and limit visual noise. Text should be large enough to be visible by a classroom on a projector. Favor a white background with black text whenever possible.

## Example Python File

```python
from manim import *

class OpeningManim(Scene):
    def construct(self):
        self.camera.background_color = WHITE
    
        p1_label = Text("P1", color=BLACK)
        p1_label.shift(LEFT*4)
        p1_label.shift(UP*3)

        p2_label = Text("P2", color=BLACK)
        p2_label.shift(UP*3)

        wq_label = Text("Wait Queue", color=BLACK)
        wq_label.shift(RIGHT*4)
        wq_label.shift(UP*3)
        self.add(p1_label)
        self.add(p2_label)
        self.add(wq_label)

        p1 = Square(4,color=BLACK)
        p1.shift(RIGHT*4)
        self.add(p1)
        p2 = Square(4,color=BLACK)
        self.add(p2)
        wq = Square(4,color=BLACK)
        wq.shift(LEFT*4)
        self.add(wq)

        a = Text("A (P1)", color=BLACK)
        a.shift(UP*1)
        a.shift(LEFT*4)
        self.add(a)

        b = Text("B (P1)", color=BLACK)
        b.shift(LEFT*4)
        self.add(b)

        c = Text("C (P2)", color=BLACK)
        c.shift(UP*1)
        self.add(c)

        text = Text("Thread A reads from file", color=BLACK)
        text.shift(DOWN*3)
        self.add(text)
        self.play(
            a.animate.shift(RIGHT*8, DOWN*0),
            b.animate.shift(UP*1),
        )
        self.remove(text)

        text = Text("Thread B reads from file", color=BLACK)
        text.shift(DOWN*3)
        self.add(text)
        self.play(
            b.animate.shift(RIGHT*8, DOWN*1),
        )
        self.remove(text)

        text = Text("Thread C reads from file", color=BLACK)
        text.shift(DOWN*3)
        self.add(text)
        self.play(
            c.animate.shift(RIGHT*4, DOWN*2),
        )
        self.remove(text)

        text = Text("Thread A read completes", color=BLACK)
        text.shift(DOWN*3)
        self.add(text)
        self.play(
            a.animate.shift(LEFT*8, 0),
            b.animate.shift(RIGHT*0, UP*1),
            c.animate.shift(RIGHT*0, UP*1),
        )
        self.remove(text)

        text = Text("Thread B read completes", color=BLACK)
        text.shift(DOWN*3)
        self.add(text)
        self.play(
            b.animate.shift(LEFT*8, DOWN*1),
            c.animate.shift(RIGHT*0, UP*1),
        )
        self.remove(text)

        text = Text("Thread C read completes", color=BLACK)
        text.shift(DOWN*3)
        self.add(text)
        self.play(
            c.animate.shift(LEFT*4, 0),
        )
        self.remove(text)

        text = Text("Thread A reads from file", color=BLACK)
        text.shift(DOWN*3)
        self.add(text)
        self.play(
            a.animate.shift(RIGHT*8, DOWN*0),
            b.animate.shift(UP*1),
        )
        self.remove(text)

        text = Text("Thread B reads from file", color=BLACK)
        text.shift(DOWN*3)
        self.add(text)
        self.play(
            b.animate.shift(RIGHT*8, DOWN*1),
        )
        self.remove(text)

        text = Text("Thread A read completes", color=BLACK)
        text.shift(DOWN*3)
        self.add(text)
        self.play(
            a.animate.shift(LEFT*8, 0),
            b.animate.shift(RIGHT*0, UP*1),
        )
        self.remove(text)

        text = Text("Thread B read completes", color=BLACK)
        text.shift(DOWN*3)
        self.add(text)
        self.play(
            b.animate.shift(LEFT*8, DOWN*1),
        )
        self.remove(text)
```