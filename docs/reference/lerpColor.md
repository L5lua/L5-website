# lerpColor()

Blends two colors to find a third color between them.

The `amt` parameter specifies the amount to interpolate between the two values. 0 is equal to the first color, 0.1 is very near the first color, 0.5 is halfway between the two colors, and so on. Negative numbers are set to 0. Numbers greater than 1 are set to 1. This differs from the behavior of lerp. It's necessary because numbers outside of the interval [0, 1] will produce strange and unexpected colors.

The way that colors are interpolated depends on the current colorMode().

## Examples

![lerpColor example 1](assets/lerpColor1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Create color objects to interpolate between.
  local from = color(218, 165, 32)
  local to = color(72, 61, 139)

  -- Create intermediate colors.
  local interA = lerpColor(from, to, 0.33)
  local interB = lerpColor(from, to, 0.66)

  -- Draw the left rectangle.
  noStroke()
  fill(from)
  rect(10, 20, 20, 60)

  -- Draw the left-center rectangle.
  fill(interA)
  rect(30, 20, 20, 60)

  -- Draw the right-center rectangle.
  fill(interB)
  rect(50, 20, 20, 60)

  -- Draw the right rectangle.
  fill(to)
  rect(70, 20, 20, 60)

  describe(
    'Four rectangles. From left to right, the rectangles are tan, brown, brownish purple, and purple.'
  )
end
```

## Syntax

```lua
lerpColor(c1, c2, amt)
```

## Parameters

| Parameter |                                                                           |
| -         | --                                                                        |
| c1        | color: interpolate from this color (any value created by color() function |
| c2        | color: interpolate to this color (any value created by color() function   |
| amt       | number: number between 0 and 1                                            |


## Related

* [alpha()](alpha.md)
* [color()](color.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
