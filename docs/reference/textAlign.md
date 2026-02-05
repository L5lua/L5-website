# textAlign()

Sets the way text is aligned when text() is called.

By default, calling `text('hi', 10, 20)` places the bottom-left corner of the text's bounding box at (10, 20).

The first parameter, `horizAlign`, changes the way text() interprets x-coordinates. By default, the x-coordinate sets the left edge of the bounding box. `textAlign()` accepts
the following values for `horizAlign`: `LEFT`, `CENTER`, or `RIGHT`.

The second parameter, `vertAlign`, is optional. It changes the way text() interprets y-coordinates. By default, the
y-coordinate sets the bottom edge of the bounding box. `textAlign()` accepts the following values for `vertAlign`: `TOP`, `BOTTOM`, `CENTER`, or `BASELINE`.

## Examples

![textAlign example 1](assets/textAlign1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Draw a vertical line.
  strokeWeight(0.5)
  line(50, 0, 50, 100)

  -- Top line.
  textSize(16)
  textAlign(RIGHT)
  text('ABCD', 50, 30)

  -- Middle line.
  textAlign(CENTER)
  text('EFGH', 50, 50)

  -- Bottom line.
  textAlign(LEFT)
  text('IJKL', 50, 70)

  describe('The letters ABCD displayed at top-left, EFGH at center, and IJKL at bottom-right. A vertical line divides the canvas in half.')
end
```

![textAlign example 2](assets/textAlign2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  strokeWeight(0.5)

  -- First line.
  line(0, 12, width, 12)
  textAlign(CENTER, TOP)
  text('TOP', 50, 12)

  -- Second line.
  line(0, 37, width, 37)
  textAlign(CENTER, CENTER)
  text('CENTER', 50, 37)

  -- Third line.
  line(0, 62, width, 62)
  textAlign(CENTER, BASELINE)
  text('BASELINE', 50, 62)

  -- Fourth line.
  line(0, 97, width, 97)
  textAlign(CENTER, BOTTOM)
  text('BOTTOM', 50, 97)

  describe('The words "TOP", "CENTER", "BASELINE", and "BOTTOM" each drawn relative to a horizontal line. Their positions demonstrate different vertical alignments.')
end
```

## Syntax

```lua
textAlign(horizAlign, [vertAlign])
```

```lua
textAlign()
```

## Parameters

| Parameter | |
| - | -- |
| horizAlign | Constant: horizontal alignment, either LEFT,
                           CENTER, or RIGHT. |
| vertAlign | Constant: vertical alignment, either TOP,
                           BOTTOM, CENTER, or BASELINE. |

## Related

* [rect()](rect.md)
* [ellipse()](ellipse.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
