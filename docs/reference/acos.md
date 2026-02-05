# acos()
 
Calculates the arc cosine of a number.

`acos()` is the inverse of cos(). It expects arguments in the range -1 to 1. By default, `acos()` returns values in the range 0 to π (about 3.14). If the angleMode() is `DEGREES`, then values are returned in the range 0 to 180.

## Examples

![acos example 1](assets/acos1.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  fill(0)

  background(200)

  -- Calculate cos() and acos() values.
  local a = PI
  local c = cos(a)
  local ac = acos(c)

  -- Display the values.
  text(round(a, 3), 35, 25)
  text(round(c, 3), 35, 50)
  text(round(ac, 3), 35, 75)

  describe('The numbers 3.142, -1, and 3.142 written on separate rows.')
end
```

![acos example 2](assets/acos2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Calculate cos() and acos() values.
  local a = PI + QUARTER_PI
  local c = cos(a)
  local ac = acos(c)

  -- Display the values.
  text(round(a, 3), 35, 25)
  text(round(c, 3), 35, 50)
  text(round(ac, 3), 35, 75)

  describe('The numbers 3.927, -0.707, and 2.356 written on separate rows.')
end
```

## Syntax

```
acos(value)
```

## Parameters

| Parameter |                                                  |
| -         | --                                               |
| value     | Number: value whose arc cosine is to be returned |

## Returns

Number: arc cosine of the given value.

## Related

* [angleMode()](angleMode.md)
* [cos()](cos.md)
* [asin()](asin.md)
* [atan()](atan.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
