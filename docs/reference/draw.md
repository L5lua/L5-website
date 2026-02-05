# draw()
 
A function that's called repeatedly while the sketch runs.

Declaring the function `draw()` sets a code block to run repeatedly once the sketch starts. It’s used to create animations and respond to user inputs:

```lua
function draw() {
  -- Code to run repeatedly.
end
```

This is often called the "draw loop" because L5 calls the code in `draw()` in a loop behind the scenes. By default, `draw()` tries to run 60 times per second. The actual rate depends on many factors. The drawing rate, called the "frame rate", can be controlled by calling [frameRate()](frameRate.md). The number of times `draw()` has run is stored in the system variable [frameCount](frameCount.md).

Code placed within `draw()` begins looping after
[setup()](setup.md) runs. `draw()` will run until the user closes the sketch. `draw()` can be stopped by calling the [noLoop()](noLoop.md) function. `draw()` can be resumed by calling the [loop()](loop.md) function.

## Examples

![draw example 1](assets/draw1.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  -- Paint the background once.
  background(200)

  describe(
    'A white circle on a gray background. The circle follows the mouse as the user moves, leaving a trail.'
  )
end

function draw()
  -- Draw circles repeatedly.
  circle(mouseX, mouseY, 40)
end
```

![draw example 2](assets/draw2.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe(
    'A white circle on a gray background. The circle follows the mouse as the user moves.'
  )
end

function draw()
  -- Paint the background repeatedly.
  background(200)

  -- Draw circles repeatedly.
  circle(mouseX, mouseY, 40)
end
```

![draw example 3](assets/draw3.gif)

```lua
-- Click the canvas to change the circle's color.
require("L5")

function setup()
  size(100, 100)

  describe(
    'A white circle on a gray background. The circle follows the mouse as the user moves. The circle changes color to pink when the user double-clicks.'
  )
end

function draw()
  -- Paint the background repeatedly.
  background(200)

  -- Draw circles repeatedly.
  circle(mouseX, mouseY, 40)
end

-- Change the fill color when the user clicks.
function mouseClicked()
  fill('deeppink')
end
```

## Related

* [setup()](setup.md)
* [isLooping()](isLooping.md)
* [loop()](loop.md)
* [for](for.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
