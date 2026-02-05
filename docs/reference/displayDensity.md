# displayDensity()
 
Returns the display's current pixel density.

## Examples

![displayDensity example 1](assets/displayDensity1.webp)

```lua
require("L5")

function setup()
  size(100,100)
  -- Create a canvas and draw
  -- a circle.
  background(200)
  circle(50, 50, 70)

  describe('A fuzzy white circle drawn on a gray background. The circle becomes sharper when the mouse is pressed.')
end

function mousePressed()
  -- Get the current display density.
  local d = displayDensity()
  -- And print it out
  print(d)

  -- Paint the background and
  -- draw a circle.
  background(200)
  circle(50, 50, 70)
end
```

## Returns

Number: current pixel density of the display

## Related

* [size()](size.md)
* [fullscreen()](fullscreen.md)
* [pixels](pixels.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
