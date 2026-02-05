# min()
 
Returns the smallest value in a sequence of numbers.

`min()` accepts any amount of number arguments or a table of values and returns the smallest number.

## Examples

![min example 1](assets/min1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Calculate the minimum of 10, 5, and 20.
  local m = min(10, 5, 20)

  -- Style the text.
  textAlign(CENTER)
  textSize(16)

  -- Display the min.
  text(m, 50, 50)

  describe('The number 5 written in the middle of a gray square.')
end
```

![min example 2](assets/min2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  fill(0)
  background(200)

  -- Create a table of numbers
  local numbers = {10, 5, 20}

  -- Calculate the maximum of the table
  local m = min(numbers)

  -- Style the text.
  textAlign(CENTER)
  textSize(16)

  -- Display the max.
  text(m, 50, 50)

  describe('The number 5 written in the middle of a gray square.')
end
```

## Syntax

```lua
min(n1, n2, .....)
```

```lua
min(table)
```

## Parameters

| Parameter |                                        |
| -         | --                                     |
| n1        | Number: first number to compare.       |
| n2        | Number: second number to compare.      |
| ...       | Number: additional numbers to compare. |
| table     | Table: table of numbers to compare.    |

## Returns

Number: smallest number.

## Related

* [max()](max.md)
* [abs()](abs.md)
* [floor()](floor.md)
* [constrain()](constrain.md)
* [dist()](dist.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
