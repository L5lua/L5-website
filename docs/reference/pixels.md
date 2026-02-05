# pixels()

An array containing the color of each pixel on the canvas.

Colors are stored as numbers representing red, green, blue, and alpha (RGBA) values. `pixels` is a one-dimensional array for performance reasons.

Each pixel occupies four elements in the `pixels` array, one for each RGBA value. For example, the pixel at coordinates (0, 0) stores its RGBA values at `pixels[0]`, `pixels[1]`, `pixels[2]`, and `pixels[3]`, respectively. The next pixel at coordinates (1, 0) stores its RGBA values at `pixels[4]`, `pixels[5]`, `pixels[6]`, and `pixels[7]`. And so on. The `pixels` array for a 100×100 canvas has 100 × 100 × 4 = 40,000 elements.

Some displays use several smaller pixels to set the color at a single point. The pixelDensity() function returns the pixel density of the canvas. High density displays often have a pixelDensity() of 2. On such a display, the `pixels` array for a 100×100 canvas has 200 × 200 × 4 = 160,000 elements.

Accessing the RGBA values for a point on the canvas requires a little math as shown below. The loadPixels() function must be called before accessing the `pixels` array. The updatePixels() function must be called after any changes are made.

## Examples

![pixels example 1](assets/pixels1.webp)

```lua

require("L5")

function setup()
  size(100, 100)
  windowTitle("pixels example")
  background(255)
  -- Load the pixels array.
  loadPixels()

  -- Set the dot's coordinates.
  local x = 50
  local y = 50

  -- Get the pixel density.
  local d = pixelDensity()

  -- Set the pixel(s) at the center of the canvas black.
  for i=1,d do
    for j=1,d do
      local index = 4 * ((y * d + j) * width * d + (x * d + i))
      -- Red.
      pixels[index] = 0
      -- Green.
      pixels[index + 1] = 0
      -- Blue.
      pixels[index + 2] = 0
      -- Alpha.
      pixels[index + 3] = 255
    end
  end

  -- Update the canvas.
  updatePixels()

  describe('A black dot in the middle of a gray rectangle.')
end

```

![pixels example 2](assets/pixels2.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("pixels example")

  -- Load the pixels array.
  loadPixels()

  -- Get the pixel density.
  local d = pixelDensity()

  -- Calculate the halfway index in the pixels array
  local halfImage = 4 * (d * width) * (d * height / 2)

  -- Make the top half of the canvas red
  for index=0,halfImage,4 do
      -- Red.
      pixels[index] = 255 
      -- Green.
      pixels[index + 1] = 0
      -- Blue.
      pixels[index + 2] = 0
      -- Alpha.
      pixels[index + 3] = 255
  end

  -- Update the canvas.
  updatePixels()

  describe('A red rectangle drawn above a gray rectangle.')
end
```

![pixels example 3](assets/pixels3.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("pixels example")

  local pink = color(255, 102, 204)

  -- Load the pixels array.
  loadPixels()

  -- Get the pixel density.
  local d = pixelDensity()

  -- Calculate the halfway index in the pixels array
  local halfImage = 4 * (d * width) * (d * height / 2)

  -- Make the top half of the canvas red
  for index=0,halfImage,4 do
      -- Red.
      pixels[index] = red(pink) 
      -- Green.
      pixels[index + 1] = green(pink)
      -- Blue.
      pixels[index + 2] = blue(pink)
      -- Alpha.
      pixels[index + 3] = alpha(pink)
  end

  -- Update the canvas.
  updatePixels()

  describe('A pink rectangle drawn above a gray rectangle.')
end
```

## Related

* [blend()](blend.md)
* [copy()](copy.md)
* [filter()](filter.md)
* [get()](get.md)
* [set()](set.md)
* [pixelDensity()](pixelDensity.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
