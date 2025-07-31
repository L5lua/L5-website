# strokeJoin()

**Note: strokeJoin in L5 has different parameter options than Processing and p5.js.**

Sets the style of the joints that connect line segments.

Joints are either mitered (`MITER`), beveled (`BEVEL`), or none (`NONE`). The default joint is `MITER`.

The argument passed to `strokeJoin()` must be written in ALL CAPS because the constants `MITER`, `BEVEL`, and `NONE` are defined this way. Lua is a case-sensitive language.

## Examples

![strokeJoin example](assets/strokeJoin.webp)

```lua
function setup() 
  size(200,200)
  background(200)

  -- Style the line.
  noFill()
  strokeWeight(10)
  strokeJoin(MITER) --default

  -- Draw the line.
  triangle(20,20,40,20,30,50)

  translate(50,0)
  strokeJoin(BEVEL)
  triangle(20,20,40,20,30,50)

  translate(50,0)
  strokeJoin(NONE)
  triangle(20,20,40,20,30,50)

  describe('3 triangles with stroke join styles mitered, beveled and none.')end
```

## Syntax

```lua
strokeJoin(join)
```

## Parameters

| Parameter |                                                     |
| -         | --------------------------------------------------  |
| join      | Constant: either MITER, BEVEL or NONE               |

## Related

* [stroke()](stroke.md)
* [strokeWeight()](strokeWeight.md)
