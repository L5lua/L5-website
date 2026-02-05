# copy()

Copies pixels from a source image to a region of the canvas.

The first parameter, `srcImage`, is the image object to blend. The source image can be the canvas itself or an Image object. `copy()` will scale pixels from the source region if it isn't the same size as the destination region.

The next four parameters, `sx`, `sy`, `sw`, and `sh` determine the region to copy from the source image. `(sx, sy)` is the top-left corner of the region. `sw` and `sh` are the region's width and height.

The next four parameters, `dx`, `dy`, `dw`, and `dh` determine the region of the canvas to copy into. `(dx, dy)` is the top-left corner of the region. `dw` and `dh` are the region's width and height.

## Examples

![copy example 1](assets/copy1.webp)

```lua
local img

require("L5")

function setup()
  size(100, 100)
  img = loadImage('assets/flower.jpg')
  windowTitle("copy() example")

  -- Use the mountains as the background.
  background(img)

  -- Copy a region of pixels to another spot.
  copy(img, 7, 22, 10, 10, 35, 25, 50, 50)

  -- Outline the copied region.
  stroke(255)
  noFill()
  square(7, 22, 10)

  describe('An image of a flower. A square region is outlined in white. A larger square contains a pixelated view of the outlined region.');
end
```

## Syntax

```lua
copy(srcImage, sx, sy, sw, sh, dx, dy, dw, dh)
```

```lua
copy(sx, sy, sw, sh, dx, dy, dw, dh)
```

## Parameters

| Parameter | |
| - | -- |
| srcImage | Image: source image. |
| sx | Integer: x-coordinate of the source's upper-left corner. |
| sy | Integer: y-coordinate of the source's upper-left corner. |
| sw | Integer: source image width. |
| sh | Integer: source image height. |
| dx | Integer: x-coordinate of the destination's upper-left corner. |
| dy | Integer: y-coordinate of the destination's upper-left corner. |
| dw | Integer: destination image width. |
| dh | Integer: destination image height. |

## Related

* [blend()](blend.md)
* [filter()](filter.md)
* [get()](get.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
