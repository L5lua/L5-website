# randomGaussian()
 
Returns a random number fitting a Gaussian, or normal, distribution.

Normal distributions look like bell curves when plotted. Values from a normal distribution cluster around a central value called the mean. The cluster's standard deviation describes its spread.

By default, `randomGaussian()` produces different results each time a sketch runs. The randomSeed() function can be used to generate the same sequence of numbers each time a sketch runs.

There's no minimum or maximum value that `randomGaussian()` might return. Values far from the mean are very unlikely and values near the mean are very likely.

The version of `randomGaussian()` with no parameters returns values with a mean of 0 and standard deviation of 1.

The version of `randomGaussian()` with one parameter interprets the argument passed as the mean. The standard deviation is 1.

The version of `randomGaussian()` with two parameters interprets the first argument passed as the mean and the second as the standard deviation.

## Examples

![randomGaussian example 1](assets/randomGaussian1.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle('randomGaussian example')
  background(200)

  describe('Three horizontal black lines are filled in randomly. The top line spans entire canvas. The middle line is very short. The bottom line spans two-thirds of the canvas.')
end

function draw()
  -- Style the circles.
  noStroke()
  fill(0, 10)

  -- Uniform distribution between 0 and 100.
  local x = random(100)
  local y = 25
  circle(x, y, 5)

  -- Gaussian distribution with a mean of 50 and sd of 1.
  x = randomGaussian(50)
  y = 50
  circle(x, y, 5)

  -- Gaussian distribution with a mean of 50 and sd of 10.
  x = randomGaussian(50, 10)
  y = 75
  circle(x, y, 5)
end
```

## Syntax

```lua
randomGaussian([mean], [sd])
```

## Parameters

| Parameter |                                                                    |
| -         | --                                                                 |
| mean      | Number: mean.                                                      |
| sd        | Number: standard deviation.                                        |

## Returns

Number: random number.

## Related

* [random()](random.md)
* [noise()](noise.md)
* [randomSeed()](randomSeed.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
