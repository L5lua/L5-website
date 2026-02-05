# randomSeed()
 
Sets the seed value for the random() and randomGaussian() functions.

By default, `random()` and `randomGaussian()` produce different results each time a sketch is run. Calling `randomSeed()` with a constant argument, such as `randomSeed(99)`, makes these functions produce the same
results each time a sketch is run.

## Examples

![randomSeed example 1](assets/randomSeed1.webp)

```lua

require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Get random coordinates.
  local x = random(0, 100)
  local y = random(0, 100)

  -- Draw the white circle.
  circle(x, y, 10)

  -- Set a random seed for consistency.
  randomSeed(99)

  -- Get random coordinates.
  x = random(0, 100)
  y = random(0, 100)

  -- Draw the black circle.
  fill(0)
  circle(x, y, 10)

  describe('A white circle appears at a random position. A black circle appears at (47.3, 91.2).')
end
```

## Syntax

```lua
randomSeed(seed)
```

## Parameters

| Parameter |                                  |
| -         | --                               |
| seed      | Number: seed value.              |

## Related

* [random()](random.md)
* [randomGaussian()](randomGaussian.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
