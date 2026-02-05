# noise()
 
Returns random numbers that can be tuned to feel organic.

Values returned by random() and randomGaussian() can change by large amounts between function calls. By contrast, values returned by `noise()` can be made "smooth". Calls to `noise()` with similar inputs will produce similar outputs. `noise()` is used to create textures, motion, shapes, terrains, and so on. Ken Perlin invented `noise()` while animating the original <em>Tron</em> film in the 1980s.

*The version of noise in L5 varies from p5.js and Processing. It returns [simplex noise](https://en.wikipedia.org/wiki/Simplex_noise) for 2 and 3 input arguments.* Simplex noise is an algorithm designed in 2001 by Ken Perlin to address limitations in his classic noise function, notably relating to speed, complexity and higher order dimensions.

`noise()` always returns values between 0 and 1. It returns the same value for a given input while a sketch is running. `noise()` produces different results each time a sketch runs. <s>The noiseSeed() function can be used to generate the same sequence of Perlin noise values each time a sketch runs.</s>

The character of the noise can be adjusted by scaling the inputs. `noise()` interprets inputs as coordinates. The sequence of noise values will be smoother when the input coordinates are closer. 

The version of `noise()` with one parameter computes noise values in one dimension. This dimension can be thought of as space, as in `noise(x)`, or time, as in `noise(t)`.

The version of `noise()` with two parameters computes noise values in two dimensions. These dimensions can be thought of as space, as in `noise(x, y)`, or space and time, as in `noise(x, t)`.

The version of `noise()` with three parameters computes noise values in three dimensions. These dimensions can be thought of as space, as in `noise(x, y, z)`, or space and time, as in `noise(x, y, t)`. *Note that the version of `noise()` that takes [3 parameters](https://love2d.org/wiki/love.math.noise) actually computes the original Perlin noise algorithm, not Simplex*.

## Examples

![noise example 1](assets/noise1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A black dot moves randomly on a gray square.')
end

function draw()
  background(200)

  -- Calculate the coordinates.
  local x = 100 * noise(0.005 * frameCount)
  local y = 100 * noise(0.005 * frameCount + 10000)

  -- Draw the point.
  strokeWeight(5)
  point(x, y)
end
```

![noise example 2](assets/noise2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A black dot moves randomly on a gray square.')
end

function draw() 
  background(200)

  -- Set the noise level and scale.
  local noiseLevel = 100
  local noiseScale = 0.005

  -- Scale the input coordinate.
  local nt = noiseScale * frameCount

  -- Compute the noise values.
  local x = noiseLevel * noise(nt)
  local y = noiseLevel * noise(nt + 10000);

  -- Draw the point.
  strokeWeight(5)
  point(x, y)
end
```

![noise example 3](assets/noise3.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A hilly terrain drawn in gray against a black sky.')
end

function draw() 
  -- Set the noise level and scale.
  local noiseLevel = 100
  local noiseScale = 0.02

  -- Scale the input coordinate.
  local x = frameCount
  local nx = noiseScale * x

  -- Compute the noise value.
  local y = noiseLevel * noise(nx)

  -- Draw the line.
  line(x, 0, x, y)
end
```

![noise example 4](assets/noise4.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A calm sea drawn in gray against a black sky.')
end

function draw() 
  background(200)

  -- Set the noise level and scale.
  local noiseLevel = 100;
  local noiseScale = 0.002

  -- Iterate from left to right.
  for x = 1,width do
    -- Scale the input coordinates.
    local nx = noiseScale * x
    local nt = noiseScale * frameCount

    -- Compute the noise value.
    local y = noiseLevel * noise(nx, nt)

    -- Draw the line.
    line(x, 0, x, y)
  end
end
```

![noise example 5](assets/noise5.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Set the noise level and scale.
  local noiseLevel = 255
  local noiseScale = 0.01

  -- Iterate from top to bottom.
  for y=1,height do
    -- Iterate from left to right.
    for x = 0,width do
      -- Scale the input coordinates.
      local nx = noiseScale * x
      local ny = noiseScale * y

      -- Compute the noise value.
      local c = noiseLevel * noise(nx, ny)

      -- Draw the point.
      stroke(c)
      point(x, y)
    end
  end

  describe('A gray cloudy pattern.')
end
```

![noise example 6](assets/noise6.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A gray cloudy pattern that changes.')
end

function draw() 
  -- Set the noise level and scale.
  local noiseLevel = 255
  local noiseScale = 0.009

  -- Iterate from top to bottom.
  for y=1,height do
    -- Iterate from left to right.
    for x=1,width do
      -- Scale the input coordinates.
      local nx = noiseScale * x
      local ny = noiseScale * y
      local nt = noiseScale * frameCount

      -- Compute the noise value.
      local c = noiseLevel * noise(nx, ny, nt)

      -- Draw the point.
      stroke(c)
      point(x, y)
    end
  end
end
```

## Syntax

```lua
noise(x, [y])
```

## Parameters

| Parameter |                                                                    |
| -         | --                                                                 |
| x         | Number: x-coordinate in noise space.                               |
| y         | Number: y-coordinate in noise space.                               |
| z         | Number: z-coordinate in noise space.                               |

## Returns

Number: Simplex noise value at specified coordinates.

## Related

* [random()](random.md)
* [randomGaussian()](randomGaussian.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
