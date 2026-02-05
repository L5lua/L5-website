# noStroke()

Disables drawing points, lines, and the outlines of shapes.

Calling `noStroke()` is the same as making the stroke completely transparent, as in `stroke(0, 0)`. If both `noStroke()` and noFill() are called, nothing will be drawn to the screen.

## Examples

![noStroke example 1](assets/noStroke1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  noStroke()
  square(20, 20, 60)

  describe('A white square with no outline.')
end
```

## Syntax

```lua
noStroke()
```

## Related

* [stroke()](stroke.md)
* [fill()](fill.md)
* [noFill()](noFill.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
