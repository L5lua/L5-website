# blend()

Copies a region of pixels from one image to another.

The first parameter, `srcImage`, is the image object to blend.

The next four parameters, `sx`, `sy`, `sw`, and `sh` determine the region to blend from the source image. `(sx, sy)` is the top-left corner of the region. `sw` and `sh` are the regions width and height.

The next four parameters, `dx`, `dy`, `dw`, and `dh` determine the region of the canvas to blend into. `(dx, dy)` is the top-left corner of the region. `dw` and `dh` are the regions width and height.

The tenth parameter, `blendMode`, sets the effect used to blend the images' colors. The options are currently: `BLEND`, `NORMAL`, `ADD`, `MULTIPLY`, `SCREEN`, `LIGHTEST`, `DARKEST`, `REPLACE`

## Examples

![blend example 1](assets/blend1.webp)

```lua
local img0
local img1
require("L5")

function setup()
  size(100, 100)
  windowTitle("blend example") 
  -- Load the images.
  img0 = loadImage('assets/rockies.jpg')
  img1 = loadImage('assets/bricks.jpg')
  
  -- Use the mountains as the background.
  background(img0)
  
  -- Display the bricks 
  image(img1, 0, 0, 33, 100)
  
  -- Display the bricks faded into the landscape on the right.
  blend(img1, 0, 0, 33, 100, 67, 0, 33, 100, LIGHTEST)
  
  describe('A wall of bricks in front of a mountain landscape. The same wall of bricks appears faded on the right of the image.')
end
```

![blend 2 example](assets/blend2.webp)

```lua
local img0
local img1
require("L5")

function setup()
  size(100, 100)
  windowTitle("blend example") 
  -- Load the images.
  img0 = loadImage('assets/rockies.jpg')
  img1 = loadImage('assets/bricks.jpg')
  
  -- Use the mountains as the background.
  background(img0)
  
  -- Display the bricks 
  image(img1, 0, 0, 33, 100)
  
  -- Display the bricks partially transparent
  blend(img1, 0, 0, 33, 100, 67, 0, 33, 100, DARKEST)
  
  describe('A wall of bricks in front of a mountain landscape. The same wall of bricks transparent on the right of the image.')
end
```

![blend 3 example](assets/blend3.webp)

```lua
local img0
local img1
require("L5")

function setup()
  size(100, 100)
  windowTitle("blend example") 
  -- Load the images.
  img0 = loadImage('assets/rockies.jpg')
  img1 = loadImage('assets/bricks.jpg')
  
  -- Use the mountains as the background.
  background(img0)
  
  -- Display the bricks 
  image(img1, 0, 0, 33, 100)
  
  -- Display the bricks washed out into the landscape
  blend(img1, 0, 0, 33, 100, 67, 0, 33, 100, ADD)
  
  describe('A wall of bricks in front of a mountain landscape. The same wall of bricks appears washed out on the right side.')
end
```

## Syntax

```lua
blend(srcImage, sx, sy, sw, sh, dx, dy, dw, dh, blendMode)
```

## Parameters

| Parameter |                                                                                                    |
| -         | --                                                                                                 |
| srcImage  | Source image.                                                                                      |
| sx        | Integer: x-coordinate of the source's upper-left corner.                                           |
| sy        | Integer: y-coordinate of the source's upper-left corner.                                           |
| sw        | Integer: source image width.                                                                       |
| sh        | Integer: source image height.                                                                      |
| dx        | Integer: x-coordinate of the destination's upper-left corner.                                      |
| dy        | Integer: y-coordinate of the destination's upper-left corner.                                      |
| dw        | Integer: destination image width.                                                                  |
| dh        | Integer: destination image height.                                                                 |
| blendMode | Constant: the blend mode, either BLEND, NORMAL, ADD, MULTIPLY, SCREEN, LIGHTEST, DARKEST, REPLACE. |

## Related

* [copy()](copy.md)
* [filter()](filter.md)
* [get()](get.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
