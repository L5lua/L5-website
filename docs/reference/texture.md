# texture()

Sets a texture to be applied to vertex points. The `texture()` function must be called between `beginShape()` and `endShape()` and before any calls to `vertex()`. 

You will need to specify uv coordinates in each `vertex()`. A uv cordinate indicates the placement of the mesh texture onto the shape, normally between 0 and 1.

*Note: Works similar to Processing's implementation rather than p5.js.*

## Examples

![texture example 1](assets/texture1.webp)

```lua
require("L5")

function setup()
  size(400, 400)
  windowTitle("texture() example")
  noStroke()
  textureMode(NORMAL)

  flower = loadImage("assets/flower.jpg")

  beginShape()
  texture(flower)
  vertex(40, 80, 0, 0)
  vertex(320, 20, 1, 0)
  vertex(380, 360, 1, 1)
  vertex(160, 380, 0, 1)
  endShape()
  
  describe("Wrapping a mesh texture around a custom shape with coordinates specified with u,v")
end
```

## Syntax

```
texture(image)
```

## Related

* [textureMode()](textureMode.md)
* [textureWrap()](textureWrap.md)
* [beginShape()](beginShape.md)
* [endShape()](endShape.md)
* [vertex()](vertex.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
