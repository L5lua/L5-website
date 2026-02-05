# loadImage()

Loads an image from a specified file path. Possible image formats accepted are: `.jpg`, `.jpeg`, `.png`, `.bpm`, `.tga`, `.hdr`, `.pic`, `.exr`. **Unsupported filetypes include `.webp` and `.gif`.**

Alternatively, `loadImage()` can also take a [FileData, ImageData, CompressedImageData or ByteData object](https://www.love2d.org/wiki/love.graphics.newImage) via underlying Love2d framework. 

## Examples

![loadImage example 1](assets/loadImage1.webp)

```lua
local img
require("L5")

function setup()
  size(100, 100)
  windowTitle('loadImage example')
  -- Load the image
  img = loadImage('assets/flower.jpg')
  -- Draw the image.
  image(img, 0, 0, width, height)

  describe('Image of a pink flower in bloom.')
end
```

## Syntax

```lua
loadImage(path)
```

## Parameters

| Parameter |                                                                         |
| -         | --------------------------------------------------                      |
| path      | String: path of the image to be loaded or alternate love2d data object |

## Related

* [image()](image.md)
* [imageMode()](imageMode.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
