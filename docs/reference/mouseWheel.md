# mouseWheel()
 
A function that's called when the mouse wheel moves.

*Note that the mouse must be over the sketch window to register.*

Declaring the function `mouseWheel()` sets a code block to run automatically when the user scrolls with the mouse wheel:

```lua
function mouseWheel() 
  -- Code to run
end
```

The mouse system variables, such as mouseX and mouseY, will be updated with their most recent value when `mouseWheel()` is called by L5:

```lua
function mouseWheel() 
  if mouseX < 50 then
    -- Code to run if the mouse is on the left.
  end

  if mouseY > 50 then
    -- Code to run if the mouse is near the bottom.
  end
end
```

The optional parameter returns `1` for up or `-1` for down. This will be opposite on macOS with "natural" scrolling enabled.

```lua
function mouseWheel(moveY) 
  -- Code to run that uses the event.
  print(moveY)
end
```

## Examples

![mouseWheel example 1](assets/mouseWheel1.gif)

```lua
local circleSize = 0

require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square. A white circle at its center grows up when the user scrolls the mouse wheel.'
  )
end

function draw()
  background(200)

  -- Draw the circle
  circle(50, 50, circleSize)
end

-- Increment circleSize when the user scrolls the mouse wheel.
function mouseWheel()
  circleSize = circleSize + 1
end

```

![mouseWheel example 2](assets/mouseWheel2.gif)

```lua
local direction = ''

require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square. An arrow at its center points up when the user scrolls up. The arrow points down when the user scrolls down.'
  )
end

function draw()
  background(200)
  fill(0)

  -- Style the text.
  textAlign(CENTER)
  textSize(16)

  -- Draw an arrow that points where
  -- the mouse last scrolled.
  text(direction, 50, 50)
end

-- Change direction when the user scrolls the mouse wheel.
function mouseWheel(event)
  if event > 0 then
    direction = 'up'
  else
    direction = 'down'
  end
end
```

## Syntax

```lua
mouseWheel([event])
```

## Parameters

| Parameter |                                             |
| -         | --                                          |
| event     | WheelEvent: optional `wheelEvent` argument. |


## Related

* [mouseButton](mouseButton.md)
* [mouseClicked()](mouseClicked.md)
* [mouseMoved()](mouseMoved.md)
* [mouseDragged()](mouseDragged.md)
* [mouseX](mouseX.md)
* [mouseY](mouseY.md)
* [movedX](movedX.md)
* [movedY](movedY.md)
* [pmouseX](pmouseX.md)
* [pmouseY](pmouseY.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
