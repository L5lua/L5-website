# redraw()
 
Runs the code in draw() once.

By default, draw() tries to run 60 times per second. Calling noLoop() stops draw() from repeating. Calling `redraw()` will execute the code in the draw() function once.

## Examples

![redraw example 1](assets/redraw1.gif)

```lua
-- Click the canvas to move the circle.
local x = 0

function setup()
  size(100, 100)

  -- Turn off the draw loop.
  noLoop()

  describe(
    'A white half-circle on the left edge of a gray square. The circle moves a little to the right when the user clicks.'
  )
end

function draw()
  background(200)

  -- Draw the circle.
  circle(x, 50, 20)

  -- Increment x.
  x = x + 5
end

-- Run the draw loop when the user clicks.
function mouseClicked()
  redraw()
end
```

## Syntax

```lua
redraw()
```

## Related

* [draw()](draw.md)
* [isLooping()](isLooping.md)
* [loop()](loop.md)
* [noLoop()](noLoop.md)
