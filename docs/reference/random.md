# random()
 
Returns a random number or a random element from an array.

`random()` follows uniform distribution, which means that all outcomes are equally likely. When `random()` is used to generate numbers, all numbers in the output range are equally likely to be returned. When `random()` is used to select elements from an array, all elements are equally likely to be chosen.

By default, `random()` produces different results each time a sketch runs. The randomSeed() function can be used to generate the same sequence of numbers or choices each time a sketch runs.

The version of `random()` with no parameters returns a random number from 0 up to but not including 1.

The version of `random()` with one parameter works one of two ways. If the
argument passed is a number, `random()` returns a random number from 0 up to but not including the number. For example, calling `random(5)` returns values between 0 and 5. If the argument passed is a table, `random()` returns a random element from that table. For example, calling `random({'🦁', '🐯', '🐻'})` returns either a lion, tiger, or bear emoji.

The version of `random()` with two parameters returns a random number from a given range. The arguments passed set the range's lower and upper bounds. For example, calling `random(-5, 10.2)` returns values from -5 up to but not including 10.2.

## Examples

![random example 1](assets/random1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Get random coordinates between 0 and 100.
  local x = random(0, 100)
  local y = random(0, 100)

  -- Draw a point.
  strokeWeight(5)
  point(x, y)

  describe('A black dot appears in a random position on a gray square.')
end
```

![random example 2](assets/random2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create an array of emoticons.
  local emoticons = {'=)',':p','=|8^)'}

  -- Choose a random element from the array.
  local choice = random(emoticons)

  -- Style the text.
  textAlign(CENTER)
  textSize(20)

  -- Display the emoji.
  text(choice, 50, 50)

  describe('An emoticon face is displayed at random.')
end
```

![random example 3](assets/random3.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  -- Slow the frame rate.
  frameRate(5)

  describe('A black dot moves around randomly on a gray square.')
end

function draw() 
  background(200)

  -- Get random coordinates between 0 and 100.
  local x = random(100)
  local y = random(100)

  -- Draw the point.
  strokeWeight(5)
  point(x, y)
end
```

![random example 4](assets/random4.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  -- Slow the frame rate.
  frameRate(5)

  describe('A black dot moves around randomly in the middle of a gray square.')
end

function draw() 
  background(200)

  -- Get random coordinates between 45 and 55.
  local x = random(45, 55)
  local y = random(45, 55)

  -- Draw the point.
  strokeWeight(5)
  point(x, y)
end
```

![random example 5](assets/random5.webp)

```lua
local x = 50
local y = 50

require("L5")

function setup()
  size(100, 100)

  background(200)

  describe('A black dot moves around randomly leaving a trail.')
end

function draw() 
  -- Update x and y randomly.
  x = x + random(-1, 1)
  y = y + random(-1, 1)

  -- Draw the point.
  point(x, y)
end
```

## Syntax

```lua
random([min], [max])
```

```lua
random(choices)
```

## Parameters

| Parameter |                                  |
| -         | --                               |
| min       | Number: lower bound (inclusive). |
| max       | Number: upper bound (exclusive). |
| choices   | Table: table to choose from.     |

## Returns

Number: random number.

## Related

* [noise()](noise.md)
* [randomSeed()](randomSeed.md)
* [randomGaussian()](randomGaussian.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
