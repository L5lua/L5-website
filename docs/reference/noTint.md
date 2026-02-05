# noTint()

Removes the current tint set by tint().

`noTint()` restores images to their original colors.

## Examples

![noTint example 1](assets/noTint1.webp)

```lua
local img
-- Load the image.
require("L5")

function setup()
  size(100, 100)
  img = loadImage("assets/flower.jpg")
  windowTitle("noTint example")

  -- Left.
  -- Tint with a CSS color string.
  tint('red')
  image(img, 0, 0, 50, 100)

  -- Right.
  -- Remove the tint.
  noTint()
  image(img, 50, 0, 50, 100)

  describe('Two images of a flower side-by-side. The image on the left has a red tint.')
end
```

## Related

* [tint()](tint.md)
* [filter()](filter.md)
* [color()](color-object.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
