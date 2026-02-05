# frameRate()
 
Sets the number of frames to draw per second.

Calling `frameRate()` with one numeric argument, as in `frameRate(30)`, attempts to draw 30 frames per second (FPS). The target frame rate may not be achieved depending on the sketch's processing needs. Frame rates of 24 FPS and above are fast enough for smooth animations.

Calling `frameRate()` without an argument returns the current frame rate. The value returned is an approximation.

## Examples

![frameRate example 1](assets/frameRate1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A white circle on a gray background. The circle moves from left to right in a loop. It slows down when the mouse is pressed.')
end

function draw()
  background(200)

  -- Set the x variable based
  -- on the current frameCount.
  local x = frameCount % 100

  -- If the mouse is pressed,
  -- decrease the frame rate.
  if mouseIsPressed then
    frameRate(10)
  else 
    frameRate(60)
  end

  -- Use x to set the circle's
  -- position.
  circle(x, 50, 20)
end
```

![frameRate example 2](assets/frameRate2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A number written in black on a gray background. The number decreases when the mouse is pressed.')
end

function draw() 
  background(200)

  -- If the mouse is pressed, do lots
  -- of math to slow down drawing.
  if mouseIsPressed == true then
    for i = 0,1000000 do
      random()
    end
  end

  -- Get the current frame rate
  -- and display it.
  local fps = frameRate()
  fill(0)
  text(fps, 50, 50)
end
```

## Syntax

```lua
frameRate(fps)
```

```lua
frameRate()
```

## Parameters

| Parameter | |
| - | -- |
| fps | Number: number of frames to draw per second. |

## Related

* [frameCount](frameCount.md)
* [deltaTime](deltaTime.md)
* [millis()](millis.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
