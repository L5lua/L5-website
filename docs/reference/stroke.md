# stroke()

Sets the color used to draw points, lines, and the outlines of shapes.

Calling `stroke(255, 165, 0)` or `stroke('orange')` means all shapes drawn after calling `stroke()` will be filled with the color orange. The way these parameters are interpreted may be changed with the colorMode() function.

The version of `stroke()` with one parameter interprets the value one of three ways. If the parameter is a `Number`, it's interpreted as a grayscale value. If the parameter is a `String`, it's interpreted as a CSS color string. A color object can also be provided to set the stroke color.

The version of `stroke()` with two parameters interprets the first one as a grayscale value. The second parameter sets the alpha (transparency) value.

The version of `stroke()` with three parameters interprets them as RGB, HSB, or HSL colors, depending on the current `colorMode()`.

The version of `stroke()` with four parameters interprets them as RGBA, HSBA, or HSLA colors, depending on the current `colorMode()`. The last parameter sets the alpha (transparency) value.

## Examples

![stroke example 1](assets/stroke1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- A grayscale value.
  strokeWeight(4)
  stroke(51)
  square(20, 20, 60)

  describe('A white square with a dark charcoal gray outline.')
end
```
![stroke example 2](assets/stroke2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- R, G and B values
  stroke(255, 204, 0)
  strokeWeight(4)
  square(20, 20, 60)

  describe('A white square with a yellow outline.')
end
```
![stroke example 3](assets/stroke3.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  
  -- Use HSB color
  colorMode(HSB)

  -- H, S and B values
  strokeWeight(4)
  stroke(255, 204, 100)
  square(20, 20, 60)

  describe('A white square with a royal blue outline.')
end
```

![stroke example 4](assets/stroke4.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  
  -- A named HTML color name
  stroke('red')
  strokeWeight(4)
  square(20, 20, 60)

  describe('A white square with a royal blue outline.')
end
```

![stroke example 5](assets/stroke5.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  
  -- a color object
  stroke(color(0, 0, 255))
  strokeWeight(4)
  square(20, 20, 60)

  describe('A white square with a blue outline.')
end
```

![stroke example 6](assets/stroke6.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  
  -- three digit hex notation
  stroke('#fae')
  strokeWeight(4)
  square(20, 20, 60)

  describe('A white square with a pink outline.')
end
```


## Syntax

```lua
stroke(v1, v2, v3, [alpha])
```

## Parameters

| Parameter |                                                                                    |
| -         | --                                                                                 |
| v1        | Number: red value if color mode is RGB or hue value if color mode is HSB.          |
| v2        | Number: green value if color mode is RGB or saturation value if color mode is HSB. |
| v3        | Number: blue value if color mode is RGB or brightness value if color mode is HSB.  |
| alpha     | Number: alpha value, controls transparency (0 - transparent, 255 - opaque).        |
| value     | String: a color string name                                                        |
| gray      | number: a grayscale value                                                          |
| values    | table: a table array containing red, gren, blue and alpha components of color      |
| color     | color: the stroke color                                                            |

## Related

* [strokeWeight()](strokeWeight.md)
* [noStroke()](noStroke.md)
* [fill()](fill.md)
* [noFill()](noFill.md)
* [background()](background.md)
* [clear()](clear.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
