# mouseMoved()
 
A function that's called when the mouse moves.

Declaring the function `mouseMoved()` sets a code block to run automatically when the user moves the mouse without clicking any mouse buttons:

```lua
function mouseMoved() 
  -- Code to run.
end
```

The mouse system variables, such as mouseX and mouseY, will be updated with their most recent value when `mouseMoved()` is called by L5:

```
function mouseMoved() 
  if mouseX < 50 then
    -- Code to run if the mouse is on the left.
  end

  if mouseY > 50 then
    -- Code to run if the mouse is near the bottom.
  end
end
```

## Examples

![mouseMoved example 1](assets/mouseDragged1.gif)

```lua
local value = 0

require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square with a black square at its center. The inner square becomes lighter as the mouse moves.'
  )
end

function draw()
  background(200)

  -- Style the square.
  fill(value)

  -- Draw the square.
  square(25, 25, 50)
end

function mouseMoved()
  -- Update the grayscale value.
  value = value + 5

  -- Reset the grayscale value.
  if value > 255 then
    value = 0
  end
end
```

## Syntax

```lua
mouseMoved()
```

## Related

* [mouseButton](mouseButton.md)
* [mouseWheel()](mouseWheel.md)
* [mouseClicked()](mouseClicked.md)
* [mouseDragged()](mouseDragged.md)
* [mouseX](mouseX.md)
* [mouseY](mouseY.md)
* [movedX](movedX.md)
* [movedY](movedY.md)
* [pmouseX](pmouseX.md)
* [pmouseY](pmouseY.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
