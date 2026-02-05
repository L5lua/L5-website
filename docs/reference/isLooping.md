# isLooping()
 
Returns `true` if the draw loop is running and `false` if not.

By default, draw() tries to run 60 times per second. Calling noLoop() stops draw() from repeating. The draw loop can be restarted by calling loop().

The `isLooping()` function can be used to check whether a sketch is looping, as in `isLooping() == true`.

## Examples

![isLooping example 1](assets/isLooping1.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A white circle drawn against a gray background. When the user clicks, the circle stops or resumes following the mouse.')
end

function draw()
  background(200)

  -- Draw the circle at the mouse's position.
  circle(mouseX, mouseY, 20)
end

-- Toggle the draw loop when the user clicks.
function mousePressed()
  if isLooping() then 
    noLoop()
  else 
    loop()
  end
end
```

## Returns

Boolean

## Related

* [loop()](loop.md)
* [noLoop()](noLoop.md)
* [draw()](draw.md)
* [for](for.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
