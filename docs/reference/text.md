# text()

Draws text to the canvas.

The first parameter, `str`, is the text to be drawn. The second and third parameters, `x` and `y`, set the left edge of text and its baseline. See textAlign() for other ways to align text.

The fourth parameter, `maxWidth` is optional. It sets the dimensions of the invisible rectangle containing the text. By default, it sets its  maximum width. Text will wrap to fit within the width of the text box. 

Text color can be set with `fill()`. Text size and font can be set with `textSize()` and `textFont()`.

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
| w         | Number: width of the text box                      |

## Related

* [fill()](fill.md)
* [textWidth()](textWidth.md)
* [textAlign()](textAlign.md)
* [textFont()](textFont.md)
* [textSize()](textSize.md)
* [loadFont()](loadFont.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
