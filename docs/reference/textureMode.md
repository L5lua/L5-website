# textureMode()

Changes the coordinate system used for textures when they’re applied to custom shapes.

In order for texture() to work, a shape needs a way to map the points on its surface to the pixels in an image. Custom shapes created with vertex() require texture mappings to be passed as uv coordinates.

Each call to vertex() must include 4 arguments, as in `vertex(x, y, u, v)`, to map the vertex at coordinates `(x, y)` to the pixel at coordinates `(u, v)` within an image. 

`textureMode()` changes the coordinate system for uv coordinates.

The parameter, `mode`, accepts two possible constants. If `NORMAL` is passed, as in `textureMode(NORMAL)`, then the texture’s uv coordinates can be provided in the range 0 to 1 instead of the image’s dimensions. This can be helpful for using the same code for multiple images of different sizes. 

## Examples

![textureMode example 1](assets/textureMode1.webp)

```lua
require("L5")

function setup()
  size(400, 400)
  windowTitle("Example of textureMode")
  noStroke()
  img = loadImage("assets/flower.jpg")
  --textureMode(NORMAL)
  beginShape()
  texture(img)
  vertex(40, 80, 0, 0)
  vertex(320, 20, img:getWidth(), 0)
  vertex(380, 360, img:getWidth(), img:getHeight())
  vertex(160, 380, 0, img:getHeight())
  endShape()
  describe("wrapping a flower texture around a polygon and specified u,v mapping")
end
```

## Syntax

```lua
textureMode(mode)
```

## Parameters

Either IMAGE or NORMAL.

## Related

* [texture()](texture.md)
* [textureWrap()](textureWrap.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
