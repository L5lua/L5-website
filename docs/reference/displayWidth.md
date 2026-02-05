# displayWidth
 
A `Number` variable that stores the width of the screen display.

`displayWidth` is useful for running full-screen programs. Its value depends on the current pixelDensity().

Note: The actual screen width can be computed as `displayWidth * pixelDensity()`.

## Examples

![displayWidth example 1](assets/displayWidth1.webp)

```lua
require("L5")

function setup()
  -- Set the canvas' width and height
  -- using the display's dimensions.
  size(displayWidth, displayHeight)

  background(200)

  describe('A gray canvas that is the same size as the display.')
end
```

## Related

* [displayHeight](displayHeight.md)
* [displayDensity()](displayDensity.md)
* [size()](size.md)
* [fullscreen()](fullscreen.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
