# float()
 
Converts a string or boolean to a floating point (decimal) number.

`float()` converts strings that resemble numbers, such as `'12.34'`, into numbers.

The parameter, `str`, is the string value to convert. For example, calling `float('12.34')` returns the number `12.34`.  If an array of strings is passed, as in `float({'12.34', '56.78'})`, then an array of numbers will be returned.

A boolean 'true' will be converted to 1, and 'false' will be converted to 0.

Note: If a string can't be converted to a number, as in `float('giraffe')`, then the value `nil` will be returned.

## Examples

![float example 1](assets/float1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create a string variable.
  local original = '12.3'

  -- Convert the string to a number.
  local converted = float(original)

  -- Double the converted value.
  local twice = converted * 2

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(12)

  -- Display the original and converted values.
  text(original..' × 2 = '..twice, 50, 50)

  describe('The text "12.3 × 2 = 24.6" written in black on a gray background.')
end
```

![float example 2](assets/float2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Create an array of strings.
  local original = {'60', '30', '15'}

  -- Convert the strings to numbers.
  local diameters = float(original)

  for _,d in pairs(diameters) do
    -- Draw a circle.
    circle(50, 50, d)
  end

  describe('Three white, concentric circles on a gray background.')
end
```

## Syntax

```lua
float(str)
```

```lua
float(boolean)
```

```lua
float(table)
```

## Parameters

| Parameter |                                                                   |
| -         | --                                                                |
| str       | String: string to convert.                                        |
| ns        | Ordered table: array of strings and/or booleans to convert. |

## Related

* [boolean()](boolean-function.md)
* [str()](str.md)
* [byte()](byte.md)
* [char()](char.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
