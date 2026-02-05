# asin()
 
Calculates the arc sine of a number.

`asin()` is the inverse of sin(). It expects input values in the range of -1 to 1. By default, `asin()` returns values in the range -π ÷ 2 (about -1.57) to π ÷ 2 (about 1.57). If the angleMode() is `DEGREES` then values are returned in the range -90 to 90.

## Examples

![asin example 1](assets/asin1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Calculate sin() and asin() values.
  local a = PI / 3
  local s = sin(a)
  local as = asin(s)

  -- Display the values.
  text(round(a, 3), 35, 25)
  text(round(s, 3), 35, 50)
  text(round(as, 3), 35, 75)

  describe('The numbers 1.047, 0.866, and 1.047 written on separate rows.')
end
```

![asin example 2](assets/asin2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  fill(0)
  background(200)

  -- Calculate sin() and asin() values.
  local a = PI + PI / 3
  local s = sin(a)
  local as = asin(s)

  -- Display the values.
  text(round(a, 3), 35, 25)
  text(round(s, 3), 35, 50)
  text(round(as, 3), 35, 75)

  describe('The numbers 4.189, -0.866, and -1.047 written on separate rows.')
end
```

## Syntax

```lua
asin(value)
```

## Parameters

| Parameter |                                                  |
| -         | --                                               |
| value     | Number: value whose arc sine is to be returned   |

## Returns

Number: arc sine of the given value

## Related

* [acos()](acos.md)
* [angleMode()](angleMode.md)
* [atan()](atan.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
