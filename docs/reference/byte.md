# byte()

Converts a `Boolean`, `String`, or `Number` to its byte value.

`byte()` converts a value to an integer (whole number) between -128 and 127. Values greater than 127 wrap around while negative values are unchanged. For example, 128 becomes -128 and -129 remains the same.

The parameter, `n`, is the value to convert. If `n` is a Boolean, as in `byte(false)` or `byte(true)`, the number 0 (`false`) or 1 (`true`) will be returned. If `n` is a string or number, as in `byte('256')` or `byte(256)`, then the byte value will be returned. Decimal values are ignored. If an array is passed, as in `byte({true, 123, '456'})`, then an array of byte values will be returned.

## Examples

![byte example 1](assets/byte1.webp)

```lua

require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create a Boolean variable.
  local original = true

  -- Convert the Boolean to its byte value.
  local converted = byte(original)

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(16)

  -- Display the original and converted values.
  -- the boolean must be converted to a string
  text(str(original).." : "..converted, 50, 50)

  describe('The text "true : 1" written in black on a gray background.')
end
```

![byte example 2](assets/byte2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create a string variable.
  local original = '256'

  -- Convert the string to its byte value.
  local converted = byte(original)

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(16)

  -- Display the original and converted values.
  text(original..' : '..converted, 50, 50)

  describe('The text "256 : 0" written in black on a gray background.')
end
```

![byte example 3](assets/byte3.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create a number variable.
  local original = 256

  -- Convert the number to its byte value.
  local converted = byte(original)

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(16)

  -- Display the original and converted values.
  text(original..' : '..converted, 50, 50)

  describe('The text "256 : 0" written in black on a gray background.')
end
```

![byte example 4](assets/byte4.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Create an array of values.
  local original = {false, '64', 383}

  -- Convert the array elements to their byte values.
  local converted = byte(original)

  -- Iterate over the converted array elements.
  for i=1,#converted do

    -- Style the circle.
    fill(converted[i])

    -- Calculate the x-coordinate.
    local x = (i + 1) * 25 - 25

    -- Draw the circle.
    circle(x, 50, 20)
  end

  describe(
    'Three gray circles on a gray background. The circles get lighter from left to right.'
  )
end
```

## Syntax

```lua
byte(n)
```

```lua
byte(ns)
```

## Parameters

| Parameter |                                          |
| -         | --                                       |
| n         | String/Boolean/Number: value to convert. |
| ns        | Ordererd table array: values to convert. |

## Returns

Number: converted byte value.

## Related

* [boolean()](boolean-function.md)
* [char()](char.md)
* [float()](float.md)
* [str()](str.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
