---
name: diagram
description: Create an svg digram or animation
---

## Style

Keep the animation simple and limit visual noise. Text should be large enough to be visible by a classroom on a projector. Favor a white background with black text when possible. Generate 540x540px or 960x540px images by default.

Prefer `<style>` block using tag oriented rather than class oriented rules. Use 24px monospace font. Use stroke-width: 4 for lines.

## Example SVG

```svg
<svg width="540" height="540" viewBox="0 0 540 540" xmlns="http://www.w3.org/2000/svg">
  <style>
    * { font-family: monospace; font-size: 24px; animation: 8s step-end infinite; }
    text { fill: black;  }
    rect { fill: none; stroke: black; stroke-width: 4; }
    .high { opacity: 0; }
    .val { opacity: 0; }
    .out { opacity: 0; }

    @keyframes h1 { 0%, 50% { opacity: 1; } 25%, 75% { opacity: 0; } }
    @keyframes h2 { 25%, 75% { opacity: 1; } 50%, 100% { opacity: 0; } }
    
    @keyframes v0 { 5%, 45% { opacity: 1; } 55%, 100% { opacity: 0; } }
    @keyframes v1 { 0%, 45% { opacity: 0; } 55%, 95% { opacity: 1; } }
    
    @keyframes o0 { 35%, 100% { opacity: 1; } }
    @keyframes o1 { 85%, 100% { opacity: 1; } }

    .h1 { animation-name: h1; }
    .h2 { animation-name: h2; }
    .var0 { animation-name: v0; }
    .var1 { animation-name: v1; }
    .out0 { animation-name: o0; }
    .out1 { animation-name: o1; }
  </style>

  <text x="40" y="80">for i in range(2):</text>
  <text x="100" y="130">print(i)</text>

  <rect x="30" y="45" width="340" height="50" class="high h1" />
  <rect x="30" y="95" width="340" height="50" class="high h2" />

  <text x="40" y="240">Variable i:</text>
  <text x="220" y="240" class="val var0">0</text>
  <text x="220" y="240" class="val var1">1</text>

  <text x="40" y="360">Terminal Output</text>
  <rect x="30" y="380" width="480" height="120" />
  
  <text x="60" y="450" class="out out0">0</text>
  <text x="100" y="450" class="out out1">1</text>
</svg>
```
