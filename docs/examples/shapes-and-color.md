# Color

This expands on the Shape Primitives example by adding color. `background()` fills the canvas with one color, `stroke()` sets the color for drawing lines, and `fill()` sets the color for the inside of shapes. `noStroke()` and `noFill()` turn off line color and inner color, respectively.

Colors can be represented in many different ways. This example demonstrates several options.

![Shape primitives example](/assets/examples/shapes-and-color-color.webp "A light blue window with colored shape primitives in various shades of blues, reds, greens: rectangle overlapping square; ellipse, circle and arc creating appearance of an eye; individual line, triangle, and quad.")

```lua
require("L5")

function setup()
  size(720, 400)
  windowTitle('Color')

  -- Create text description output
  describe('A blue window with color shape primitives in color shades of purple, black,white and green: rectangle overlapping square; ellipse, circle and arc creating appearance of an eye; individual line, triangle, and quad.')

  -- Use degrees as units for angles
  -- The arc() function uses angles
  angleMode(DEGREES)

  -- CSS color name
  -- For a list of available color names, see:
  -- https:--www.w3.org/wiki/CSS/Properties/color/keywords
  background('steelblue')

  -- Set width of stroke to 4 units
  strokeWeight(4)

  -- The default color mode uses
  -- Red, green, and blue values
  -- On a scale of 0-255
  -- Light blue
  fill(200, 200, 255)

  -- Dark blue
  stroke(20, 20, 100)
  square(20, 20, 100)

  -- Dark red
  stroke(100, 20, 20)

  -- The rectangle uses the last set fill color,
  -- which is light blue, set before drawing the square
  rect(100, 40, 200, 100)

  -- Hue, saturation, and brightness values
  -- On scales of 0-360°, 0-100%, and 0-100% respectively
  colorMode(HSB)

  -- Light green
  fill(120, 70, 90)

  -- Dark green
  stroke(120, 60, 30)
  ellipse(540, 100, 300, 100)

  -- Dark fuchsia
  fill(300, 90, 30)

  -- Draw without lines
  noStroke()
  circle(560, 100, 100)

  -- Hue, saturation, and lightness values
  -- On scales of 0-360°, 0-100%, and 0-100% respectively
  -- This is similar to HSB (above),
  -- but whereas 100% brightness is the brightest version of that hue,
  -- 100% lightness is always white.
  colorMode(HSL)

  -- Light green
  fill(120, 70, 90)

  -- Dark green
  stroke(120, 60, 30)
  arc(540, 100, 300, 100, 180, 360, CHORD)

  -- Save current settings
  push()

  -- Switch back to red, green, blue color mode
  colorMode(RGB)

  -- Navy blue
  stroke(20, 10, 80)
  line(20, 200, 200, 350)

  -- Restore last saved settings
  pop()

  -- the triangle uses the same settings as the arc
  -- L5 currently does not preserve style (like stroke color) contained within push()/pop()
  -- this is the reason for adding colormodes here
  colorMode(HSB)
  stroke(120, 60, 30)
  triangle(250, 350, 350, 200, 450, 350)
  colorMode(RGB)

  -- Hex string
  -- This is a set of red, green, blue values
  -- Encoded in base 16
  stroke('#EFD8D8')

  -- Draw without inner color
  noFill()
  quad(500, 250, 550, 200, 700, 300, 650, 350)
end
```

## Related References

* [colorMode()](/reference/colorMode.md) - changing color modes
* [fill()](/reference/fill.md) - adding color to shapes
* [noStroke()](/reference/noStroke.md) - removing color outline from shapes

## Related Examples

* [Shape Primitives](shape-primitives.md) - Draw 2D shapes.

---

Color: Created by [Caleb Foss](https://github.com/calebfoss), [Darren Kessner](https://github.com/dkessner). From 2024 onwards, edited and maintained by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people). Adapted to L5 2025. Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

