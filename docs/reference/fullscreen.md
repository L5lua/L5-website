# fullscreen()
 
Toggles full-screen mode. Calling `fullscreen()` makes the sketch full-screen or if already set fullscreen it returns to its original size.

## Examples

![fullscreen example 1](assets/fullscreen1.webp)

```lua
require("L5")

function setup()
  background(200)

  describe('A gray canvas that switches between default and full-screen display when clicked.')
end

-- If the mouse is pressed,
-- toggle full-screen mode.
function mousePressed()
  fullscreen()
end
```

## Syntax

```lua
fullscreen()
```

## Related

* [size()](size.md)
* [mousePressed()](mousePressed.md)
* [displayWidth](displayWidth.md)
* [displayHeight](displayHeight.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
