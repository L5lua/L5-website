# Shape Primitives

This program demonstrates the use of the basic shape
primitive functions `square()`, `rect()`, `ellipse()`, `circle()`, `arc()`, `line()`, `triangle()`, `quad()`.

![Shape primitives example](/assets/examples/shapes-and-color-primitives.webp "A gray window with white shape primitives: rectangle overlapping square; ellipse, circle and arc creating appearance of an eye; individual line, triangle, and quad.")

```lua
require("L5")

function setup()
  size(720, 400)
  windowTitle('Shape Primitives')

  -- Create text description output
  describe('A gray window with white shape primitives: rectangle overlapping square; ellipse, circle and arc creating appearance of an eye; individual line, triangle, and quad.')

  -- Use degrees as units for angles
  -- The arc() function uses angles
  angleMode(DEGREES)

  -- Draw a light gray background
  background(220)

  -- Draw square
  -- x, y, size
  square(20, 20, 100)

  -- Draw rectangle on top of square
  -- This appears in front of the square because the function is called
  -- after (further down)
  -- Switching the order of square and rect will make the square appear on
  -- top of the rectangle
  -- x, y, width, height
  rect(100, 40, 200, 100)

  -- Draw eye shape with ellipse, circle, and arc

  -- Draw ellipse as outer eye shape
  -- x, y, width, height
  ellipse(540, 100, 300, 100)

  -- Draw circle as pupil
  -- x, y, diameter
  circle(560, 100, 100)

  -- Draw arc (compare to ellipse()) as eyelid
  -- x, y, width, height, start angle, stop angle, mode
  arc(540, 100, 300, 100, 180, 360, CHORD)

  -- Draw line
  -- x1, y1, x2, y2
  line(20, 200, 200, 350)

  -- Draw triangle
  -- x1, y1, x2, y2, x3, y3
  triangle(250, 350, 350, 200, 450, 350)

  -- Draw quadrilateral
  -- x1, y1, x2, y2, x3, y3, x4, y4
  quad(500, 250, 550, 200, 700, 300, 650, 350)

end
```

## Related References

* [arc()](/reference/arc.md) - Draws an arc
* [ellipse()](/reference/ellipse.md) - Draws an ellipse (oval)

## Related Examples

* [Color](shapes-and-color.md) - Add color to your sketch.

---

Shape primitives: Revised in 2023 by [Darren Kessner](https://github.com/dkessner). Created by [Caleb Foss](https://github.com/calebfoss), [Darren Kessner](https://github.com/dkessner). From 2024 onwards, edited and maintained by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people). Adapted to L5 2025.. Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
