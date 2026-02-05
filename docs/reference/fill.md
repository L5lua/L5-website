# fill()

Sets the color used to fill shapes.

Calling `fill(255, 165, 0)` or `fill('orange')` means all shapes drawn after the fill command will be filled with the color orange.

The version of `fill()` with one parameter interprets the value one of three ways. If the parameter is a `Number`, it's interpreted as a grayscale
value. If the parameter is a `String`, it's interpreted as a CSS color string. A color table (called a *color object* in p5.js) can also be provided to set the fill color, in the form `{R, G, B}` or `{R, G, B, A}`.

The version of `fill()` with three parameters interprets them as RGB, HSB, or HSL colors, depending on the current colorMode(). The default color space is RGB, with each value in the range from 0 to 255.

## Examples

![fill example 1](assets/fill1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- A grayscale value.
  fill(51)
  square(20, 20, 60)

  describe('A dark charcoal gray square with a black outline.')
end
```
![fill example 2](assets/fill2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- R, G, B values
  fill(255, 204, 0)
  square(20, 20, 60)

  describe('A yellow square with a black outline.')
end
```

![fill example 3](assets/fill3.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- R, G, B & A values
  fill(255, 0, 0, 128)
  square(20, 20, 60)

  describe('A semi-transparent red square with a black outline.')
end
```

![fill example 4](assets/fill4.webp)

```
require("L5")

function setup()
  size(100,100)
  background(200)
  
  -- a color object
  local c = color(0, 0, 255)
  fill(c)
  square(20,20,60)
  
  describe('A blue square with black outline')
end
```

![fill example 5](assets/fill5.webp)

```lua
require("L5")

function setup()
  size(100,100)
  background(200)
  
  -- a color table
  fill({0, 0, 255})
  square(20,20,60)
  
  describe('A blue square with black outline')
end
```

![fill example 6](assets/fill6.webp)

```lua
require("L5")

function setup()
  size(100,100)
  background(200)
  
  -- a color string HTML name
  fill('lawngreen')
  square(20,20,60)
  
  describe('A lawn green bratty square with black outline')
end
```


## Syntax

```lua
fill(gray, [alpha])
```

```lua
fill(v1, v2, v3, [alpha])
```

```lua
fill(colorstring)
```

```lua
fill({gray, [alpha]})
```

```lua
fill({v1, v2, v3, [alpha]})
```

## Parameters

| Parameter   |                                                                                    |
| -           | --                                                                                 |
| gray        | Number: grayscale value                                                            |
| v1          | Number: red value if color mode is RGB or hue value if color mode is HSB.          |
| v2          | Number: green value if color mode is RGB or saturation value if color mode is HSB. |
| v3          | Number: blue value if color mode is RGB or brightness value if color mode is HSB.  |
| alpha       | Number: alpha value, controls transparency (0 - transparent, 255 - opaque).        |
| colortable  | table: a color table in the form {gray}, {gray, alpha}, {R, B, B} or {R, G, B, A}  |
| colorstring | string: color string in 3 or 6-digit hex code or HTML color name                   |

## Related

* [color()](color-object.md)
* [background()](background.md)
* [clear()](clear.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
