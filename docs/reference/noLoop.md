# noLoop()
 
Stops the code in draw() from running repeatedly.

By default, draw() tries to run 60 times per second. Calling `noLoop()` stops draw() from repeating. The draw loop can be restarted by calling loop(). draw() can be run once by calling redraw().

The isLooping() function can be used to check whether a sketch is looping, as in `isLooping() == true`.

*Note: One small difference from p5/Processing is that in L5 placing noLoop() in setup() will prevent any running of the draw() loop, whereas in p5/Processing it will run exactly once before stopping.*

## Examples

![noLoop example 1](assets/noLoop1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A white half-circle on the left edge of a gray square.')
end

function draw()
  background(200)

  -- Calculate the circle's x-coordinate.
  local x = frameCount

  -- Draw the circle.
  -- Normally, the circle would move from left to right.
  circle(x, 50, 20)

  -- Turn off the draw loop.
  noLoop()
end
```

![noLoop example 2](assets/noLoop2.gif)

```lua
-- Click to stop the draw loop.
require("L5")

function setup()
  size(100, 100)

  -- Slow the frame rate.
  frameRate(5)

  describe('A white circle moves randomly on a gray background. It stops moving when the user clicks.')
end

function draw()
  background(200)

  -- Calculate the circle's coordinates.
  local x = random(0, 100)
  local y = random(0, 100)

  -- Draw the circle.
  -- Normally, the circle would move from left to right.
  circle(x, y, 20)
end

-- Stop the draw loop when the user double-clicks.
function mouseClicked()
  noLoop()
end
```

## Syntax

```lua
noLoop()
```

## Related

* [draw()](draw.md)
* [isLooping()](isLooping.md)
* [loop()](loop.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
