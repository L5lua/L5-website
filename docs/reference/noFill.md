# noFill()

Disables setting the fill color for shapes.

Calling `noFill()` is the same as making the fill completely transparent, as in `fill(0, 0)`. If both noStroke() and `noFill()` are called, nothing will be drawn to the screen.

## Examples

![noFill example 1](assets/noFill1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Draw the top square.
  square(32, 10, 35)

  -- Draw the bottom square.
  noFill()
  square(32, 55, 35)

  describe('A white square above an empty square. Both squares have black outlines.')
end
```

## Syntax

```lua
noFill()
```

## Related

* [fill()](fill.md)
* [background()](background.md)
* [clear()](clear.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
