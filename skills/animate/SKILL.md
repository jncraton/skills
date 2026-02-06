---
name: animate
description: Create a gif or svg animation
---

## Style

Keep the animation simple and limit visual noise. Text should be large enough to be visible by a classroom on a projector. Favor a white background with black text whenever possible.

## Example SVG

```svg
<svg width="540" height="540" viewBox="0 0 540 540" xmlns="http://www.w3.org/2000/svg">
  <text x="40" y="80" font-family="monospace" font-size="24" fill="black">for i in range(2):</text>
  <text x="96" y="120" font-family="monospace" font-size="24" fill="black">print(i)</text>
  <rect x="30" y="55" width="280" height="35" fill="none" stroke="black" stroke-width="5" stroke-linejoin="miter">
    <animate attributeName="opacity" values="1;1;0;0;1;1;0;0" dur="8s" repeatCount="indefinite" calcMode="discrete" />
  </rect>
  <rect x="30" y="95" width="280" height="35" fill="none" stroke="black" stroke-width="5" stroke-linejoin="miter">
    <animate attributeName="opacity" values="0;0;1;1;0;0;1;1" dur="8s" repeatCount="indefinite" calcMode="discrete" />
  </rect>
  <text x="40" y="240" font-family="monospace" font-size="24" fill="black">Variable i:</text>
  <text x="200" y="240" font-family="monospace" font-size="24" fill="black">
    <animate attributeName="opacity" values="0;1;1;1;1;0;0;0" dur="8s" repeatCount="indefinite" calcMode="discrete" />0
  </text>
  <text x="200" y="240" font-family="monospace" font-size="24" fill="black">
    <animate attributeName="opacity" values="0;0;0;0;0;1;1;1" dur="8s" repeatCount="indefinite" calcMode="discrete" />1
  </text>
  <text x="40" y="380" font-family="monospace" font-size="24" fill="black">Output:</text>
  <rect x="30" y="400" width="480" height="100" fill="none" stroke="black" stroke-width="5" stroke-linejoin="miter" />
  <text x="50" y="450" font-family="monospace" font-size="24" fill="black">
    <animate attributeName="opacity" values="0;0;0;1;1;1;1;1" dur="8s" repeatCount="indefinite" calcMode="discrete" />0
  </text>
  <text x="80" y="450" font-family="monospace" font-size="24" fill="black">
    <animate attributeName="opacity" values="0;0;0;0;0;0;0;1" dur="8s" repeatCount="indefinite" calcMode="discrete" />1
  </text>
</svg>
```