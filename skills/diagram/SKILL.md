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
    * { font-family: monospace; font-size: 24px; animation: 10s step-end infinite; }
    text { fill: black;  }
    rect { fill: none; stroke: black; stroke-width: 4; }

    @keyframes line1 { 
      0%, 20%, 40%, 60%, 80% { opacity: 0; }
      10%, 30%, 50%, 70% { opacity: 1; }
    }
    @keyframes line2 { 
      0%, 30%, 50%, 70%, 90% { opacity: 0; }
      20%, 40%, 60%, 80% { opacity: 1; }
    }
    
    @keyframes out0 { 
      0%, {opacity: 0; } 
      20%, { opacity: 1; }
    }
    @keyframes out1 { 0% {opacity: 0;} 40% { opacity: 1; } }
    @keyframes out2 { 0% {opacity: 0;} 60% { opacity: 1; } }
    @keyframes out3 { 0% {opacity: 0;} 80% { opacity: 1; } }

    @keyframes i0 { 0%,30% {opacity: 0;} 10% { opacity: 1; } }
    @keyframes i1 { 0%,50% {opacity: 0;} 30% { opacity: 1; } }
    @keyframes i2 { 0%,70% {opacity: 0;} 50% { opacity: 1; } }
    @keyframes i3 { 0% {opacity: 0;} 70% { opacity: 1; } }

    .line1 { animation-name: line1; }
    .line2 { animation-name: line2; }
    .i0 { animation-name: i0; }
    .i1 { animation-name: i1; }
    .i2 { animation-name: i2; }
    .i3 { animation-name: i3; }
    .out0 { animation-name: out0; }
    .out1 { animation-name: out1; }
    .out2 { animation-name: out2; }
    .out3 { animation-name: out3; }
  </style>

  <text x="40" y="80">for i in range(2):</text>
  <text x="100" y="130">print(i)</text>

  <rect x="30" y="45" width="340" height="50" class="line1" />
  <rect x="30" y="95" width="340" height="50" class="line2" />

  <text x="40" y="240">Variable i:</text>
  <text x="220" y="240" class="i0">0</text>
  <text x="220" y="240" class="i1">1</text>
  <text x="220" y="240" class="i2">2</text>
  <text x="220" y="240" class="i3">3</text>

  <text x="40" y="360">Terminal Output</text>
  <rect x="30" y="380" width="480" height="120" />
  
  <text x="60" y="450" class="out0">0</text>
  <text x="100" y="450" class="out1">1</text>
  <text x="140" y="450" class="out2">2</text>
  <text x="180" y="450" class="out3">3</text>
</svg>
```
