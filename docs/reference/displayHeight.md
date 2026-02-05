# displayHeight
 
A `Number` variable that stores the height of the screen display.

`displayHeight` is useful for running full-screen programs. Its value depends on the current pixelDensity().

Note: The actual screen height can be computed as `displayHeight * pixelDensity()`.

## Examples

![displayHeight example 1](assets/displayHeight1.webp)

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

* [displayWidth()](displayWidth.md)
* [displayDensity()](displayDensity.md)
* [size()](size.md)
* [fullscreen()](fullscreen.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
