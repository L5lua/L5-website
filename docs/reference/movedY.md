# movedY()

A `Number` system variable that tracks the mouse's vertical movement.

`movedY` tracks how many pixels the mouse moves up or down between frames. `movedY` will have a negative value if the mouse moves up between frames and a positive value if it moves down. `movedY` can be calculated as `mouseY - pmouseY`.

## Examples

![movedY example 1](assets/movedY1.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square. The text "▲" appears when the user moves the mouse upward. The text "▼" appears when the user moves the mouse downward.'
  )
end

function draw()
  background(200)
  fill(0)

  -- Style the text.
  textAlign(CENTER)
  textSize(16)

  -- Display down when movedY is positive and
  -- up when it's negative.
  if movedY > 0 then
    text('down', 50, 50)
  elseif movedY < 0 then
    text('up', 50, 50)
  end
end

```

## Syntax

```lua
movedY
```

## Returns

Number: positive or negative number tracking vertical movement.

## Related

* [movedX](movedX.md)
* [mouseMoved()](mouseMoved.md)
* [mouseY](mouseY.md)
* [mouseClicked()](mouseClicked.md)
* [mouseButton](mouseButton.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
