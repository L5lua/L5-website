# textFont()

Sets the font used by the text() function.

The first parameter, `font`, sets the font. `textFont()` recognizes a font object loaded previously with loadFont().

The second parameter, `size`, is optional. It sets the font size in pixels. This has the same effect as calling textSize().

## Examples

![textFont example 1](assets/textFont1.webp)

```lua
require("L5")

function setup()
  size(100,100)
  background(200)
  font = loadFont('assets/inconsolata.otf')
  textFont(font)
  textSize(24)
  text('hi', 35, 55)

  describe('The text "hi" written in a black, monospace font on a gray background.')
end
```

![textFont example 2](assets/textFont2.webp)

```lua
require("L5")

function setup()
  size(100,100)
  background('black')
  fill('palegreen')
  font = loadFont('assets/inconsolata.otf')
  textFont(font, 10)

  text('You turn to the left and see a door. Do you enter?', 5, 5, 90, 90)
  text('>', 5, 70)

  describe('A text prompt from a game is written in a green, monospace font on a black background.')
end
```

## Syntax

```lua
textFont()
```

```lua
textFont(font, [size])
```

## Parameters

| Parameter |                                                    |
| -         | --                                                 |
| font      | Object: font object previously loaded via loadFont |
| size      | Number: font size in pixels                        |

## Related

* [textSize()](textSize.md)
* [loadFont()](loadFont.md)
* [text()](text.md)
* [textAlign()](textAlign.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
