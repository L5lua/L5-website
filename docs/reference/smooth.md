# smooth()

Draws certain features with smooth (anti-aliased) edges.

smooth() is active by default. noSmooth() is helpful for scaling up images without blurring. 

## Examples

![noSmooth() and smooth() example](assets/smooth.webp)

```lua
function setup() 
  size(400, 400)
  background(0)

  noSmooth()
  text("noSmooth",90,80)
  ellipse(120, 192, 144, 144)

  smooth()
  text("smooth",250,80)
  ellipse(280, 192, 144, 144)

  describe("Two white circles, drawn with smooth() and noSmooth()")
end
```

## Syntax

```lua
smooth()
```

## Related

* [noSmooth()](noSmooth.md)
