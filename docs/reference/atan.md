# atan()
 
Calculates the arc tangent of a number.

`atan()` is the inverse of tan(). It expects input values in the range of -Infinity to Infinity. By default, `atan()` returns values in the range -π ÷ 2 (about -1.57) to π ÷ 2 (about 1.57). If the angleMode() is `DEGREES` then values are returned in the range -90 to 90.

## Examples

![atan example 1](assets/atan1.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  fill(0)

  background(200)

  -- Calculate tan() and atan() values.
  local a = PI / 3
  local t = tan(a)
  local at = atan(t)

  -- Display the values.
  text(round(a, 3), 35, 25)
  text(round(t, 3), 35, 50)
  text(round(at, 3), 35, 75)

  describe('The numbers 1.047, 1.732, and 1.047 printed on separate rows.')
end

```

![atan example 2](assets/atan2.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  fill(0)

  background(200)

  -- Calculate tan() and atan() values.
  local a = PI + PI / 3
  local t = tan(a)
  local at = atan(t)

  -- Display the values.
  text(round(a, 3), 35, 25)
  text(round(t, 3), 35, 50)
  text(round(at, 3), 35, 75)

  describe('The numbers 4.189, 1.732, and 1.047 printed on separate rows.')
end
```

## Syntax

```lua
atan(value)
```

## Parameters

| Parameter |                                                   |
| -         | --                                                |
| value     | Number: value whose arc tangent is to be returned |

## Returns

Number: arc tangent of the given value

## Related

* [acos()](acos.md)
* [angleMode()](angleMode.md)
* [asin()](asin.md)
* [atan2()](atan2.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
