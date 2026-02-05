# loadPixels()

Loads the current value of each pixel on the canvas into the pixels array.

`loadPixels()` must be called before reading from or writing to pixels.

## Examples

![loadPixels example 1](assets/loadPixels1.webp)

```lua
local img
require("L5")

function setup()
  size(100, 100)
  windowTitle("loadPixels example")
  -- Load the image.
  img = loadImage('assets/rockies.jpg')

  -- Display the image.
  image(img, 0, 0, 100, 100)

  -- Get the pixel density.
  local d = pixelDensity()
  print(d)
  -- Calculate the halfway index in the pixels array.
  local halfImage = 4 * (d * width) * (d * height / 2)
print(4 * width * (height / 2))
  -- Load the pixels array.
  loadPixels()

  -- Copy the top half of the canvas to the bottom.
  for i=1,halfImage do
    pixels[i + halfImage] = pixels[i]
  end

  -- Update the canvas.
  updatePixels()

  describe('Two identical images of mountain landscapes, one on top of the other.')
end

```

## Syntax

```lua
loadPixels()
```

## Related

* [blend()](blend.md)
* [filter()](filter.md)
* [copy()](copy.md)
* [get()](get.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
