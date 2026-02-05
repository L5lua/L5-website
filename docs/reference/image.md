# image()

Draws an image to the canvas.

The second and third parameters, `dx` and `dy`, set the coordinates of the destination image's top left corner. See
imageMode() for other ways to position images.

## Examples

![image example 1](assets/image1.webp)

```lua
local img

require("L5")

function setup()
  size(100, 100)
  windowTitle('image example')
  img = loadImage('assets/flower.jpg')
  background(50)

  -- Draw the image.
  image(img, 0, 0)

  describe('Partial view of a photograph of a flower that extends offscreen.')
end
```

![image example 2](assets/image2.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle('image example')
  img = loadImage('assets/flower.jpg')
  background(50)

  -- Draw the image 50x50.
  image(img, 0, 0, 50, 50)

  describe('An image of a pink flower in bloom, sized to 50x50 pixels in the top left corner.')
end
```

![image 3 example](assets/image3.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle('image example')
  img = loadImage('assets/flower.jpg')
  background(50)

  -- Draw the image sized to the window.
  image(img, 0, 0, width, height)

  describe('An image of a pink flower in bloom sized to the window.')
end
```

## Syntax

```lua
image(img, x, y, [width], [height])
```

## Parameters

| Parameter |                                                           |
| -         | --                                                        |
| img       | image to display.                                         |
| x         | Number: x-coordinate of the top-left corner of the image. |
| y         | Number: y-coordinate of the top-left corner of the image. |
| width     | Number: width to draw the image.                          |
| height    | Number: height to draw the image.                         |

## Related

* [loadImage()](loadImage.md)
* [loadFont()](loadFont.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
