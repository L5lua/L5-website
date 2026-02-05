# textureWrap()

Changes the way textures behave when a shape’s uv coordinates go beyond the texture.

In order for texture() to work, a shape needs a way to map the points on its surface to the pixels in an image. Custom shapes created with vertex() require texture mappings to be passed as uv coordinates.

For texturing a custom shape each call to vertex() must include 4 arguments, as in `vertex(x, y, u, v)`, to map the vertex at coordinates `(x, y)` to the pixel at coordinates `(u, v)` within an image. 

## Examples

![textureWrap example 1](assets/textureWrap1.webp)

```lua
local img

require("L5")

function setup()
  size(300, 300)
  img = loadImage("assets/flower.jpg")
  textureMode(NORMAL)
  windowTitle("textureWrap example")
  describe("The texture is applied and tiled or clamped to the custom shape")
end

function draw() 
  background(0)
  translate(width/2, height/2)
  rotate(map(mouseX, 0, width, -PI, PI))
  if mouseIsPressed then
    textureWrap(REPEAT)
  else 
    textureWrap(CLAMP)
  end

  beginShape()
  texture(img)
  vertex(-100, -100, 0, 0)
  vertex(100, -100, 2, 0)
  vertex(100, 100, 2, 2)
  vertex(-100, 100, 0, 2)
  endShape()
end
```

## Syntax

```lua
textureWrap(wrap)
```

## Parameters

wrap: Either CLAMP or REPEAT.

## Related

* [texture()](texture.md)
* [textureMode()](textureMode.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
