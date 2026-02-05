# movedX

A `Number` system variable that tracks the mouse's horizontal movement.

`movedX` tracks how many pixels the mouse moves left or right between frames. `movedX` will have a negative value if the mouse moves left between frames and a positive value if it moves right. `movedX` can be calculated as `mouseX - pmouseX`.

## Examples

![movedX example 1](assets/movedX1.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square. The text ">>" appears when the user moves the mouse to the right. The text "<<" appears when the user moves the mouse to the left.'
  )
end

function draw()
  background(200)
  fill(0)

  -- Style the text.
  textAlign(CENTER)
  textSize(16)

  -- Display >> when movedX is positive and
  -- << when it's negative.
  if movedX > 0 then
    text('>>', 50, 50)
  elseif movedX < 0 then
    text('<<', 50, 50)
  end
end
```

## Syntax

```lua
movedX
```

## Returns

Number: positive or negative number tracking horizontal movement.

## Related

* [movedY](movedY.md)
* [mouseMoved()](mouseMoved.md)
* [mouseX](mouseX.md)
* [mouseClicked()](mouseClicked.md)
* [mouseButton](mouseButton.md)





---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
