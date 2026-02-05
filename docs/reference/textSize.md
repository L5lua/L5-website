# textSize()

Sets the font size when text() is called.

Note: Font size is measured in pixels.

Calling `textSize()` without an argument returns the current size.

## Examples

![textSize example 1](assets/textSize1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Top.
  textSize(12)
  text('Font Size 12', 10, 30)

  -- Middle.
  textSize(14)
  text('Font Size 14', 10, 60)

  -- Bottom.
  textSize(16)
  text('Font Size 16', 10, 90)

  describe('The text "Font Size 12" drawn small, "Font Size 14" drawn medium, and "Font Size 16" drawn large.')
end
```

## Syntax

```lua
textSize(size)
```

## Parameters

| Parameter | |
| - | -- |
| size | Number: size of the letters in units of pixels. |

## Related

* [text()](text.md)
* [textAlign()](textAlign.md)
* [loadFont()](loadFont.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
