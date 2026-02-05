# text()

Draws text to the canvas.

The first parameter, `str`, is the text to be drawn. The second and third
parameters, `x` and `y`, set the coordinates of the text's bottom-left
corner. See textAlign() for other ways to
align text.

The fourth and fifth parameters, `maxWidth` and `maxHeight`, are optional.
They set the dimensions of the invisible rectangle containing the text. By
default, they set its  maximum width and height. See
rectMode() for other ways to define the
rectangular text box. Text will wrap to fit within the text box. Text
outside of the box won't be drawn.

Text can be styled a few ways. Call the fill()
function to set the text's fill color. Call
stroke() and
strokeWeight() to set the text's outline.
Call textSize() and
textFont() to set the text's size and font,
respectively.

Note: `WEBGL` mode only supports fonts loaded with
loadFont(). Calling
stroke() has no effect in `WEBGL` mode.

## Examples

![text example 1](assets/text1.webp)

```lua
require("L5")

function setup()
  background(200)
  text('hi', 50, 50)

  describe('The text "hi" written in black in the middle of a gray square.')
end
```

![text example 2](assets/text2.webp)

```lua
require("L5")

function setup()
  size(100,100)
  background('black')
  textSize(22)
  fill('yellow')
  text('rainbows', 6, 20)
  fill('cornflowerblue')
  text('rainbows', 6, 45)
  fill('tomato')
  text('rainbows', 6, 70)
  fill('limegreen')
  text('rainbows', 6, 95)

  describe('The text "rainbows" written on several lines, each in a different color.')
end
```

![text example 3](assets/text3.webp)

```lua
require("L5")

function setup()
  size(100,100)
  background(200)
  local s = 'The quick brown fox jumps over the lazy dog.'
  text(s, 10, 10, 70, 80)

  describe('The sample text "The quick brown fox..." written in black across several lines.')
end
```

## Syntax

```lua
text(str, x, y, w)
```

## Parameters

| Parameter |                                                    |
| -         | --                                                 |
| str       | String/object/Number/Boolean: text to be displayed |
| x         | Number: x coordinate of the text box               |
| y         | Number: y coordinate of the text box               |

## Related

* [textWidth()](textWidth.md)
* [textAlign()](textAlign.md)
* [textFont()](textFont.md)
* [loadFont()](loadFont.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
