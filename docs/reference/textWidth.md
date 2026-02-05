# textWidth()

Calculates the maximum width of a string of text drawn when
text() is called.

## Examples

![textWidth example 1](assets/textWidth1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Style the text.
  textSize(28)
  strokeWeight(0.5)

  -- Calculate the text width.
  local s = 'yoyo'
  local w = textWidth(s)

  -- Display the text.
  text(s, 22, 55)

  -- Underline the text.
  line(22, 55, 22 + w, 55)

  describe('The word "yoyo" underlined.')
end
```

![textWidth example 2](assets/textWidth2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Style the text.
  textSize(28)
  strokeWeight(0.5)

  -- Calculate the text width.
  -- "\n" starts a new line.
  local s = 'yo\nyo'
  local w = textWidth(s)

  -- Display the text.
  text(s, 22, 55)

  -- Underline the text.
  line(22, 55, 22 + w, 55)

  describe('The word "yo" written twice, one copy beneath the other. The words are divided by a horizontal line.')
end
```

## Syntax

```lua
textWidth(str)
```

## Parameters

| Parameter |                                   |
| -         | --                                |
| str       | String: string of text to measure |


## Related

* [textAlign()](textAlign.md)
* [textFont()](textFont.md)
* [textWrap()](textWrap.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
