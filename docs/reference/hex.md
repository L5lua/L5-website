# hex()
 
Converts a number to a string with its hexadecimal value.

`hex()` converts a number to a string with its hexadecimal number value. Hexadecimal (hex) numbers are base-16, which means there are 16 unique digits. Hex extends the numbers 0–9 with the letters A–F. For example, the number `11` (eleven) in base-10 is written as the letter `B` in hex.

The first parameter, `n`, is the number to convert. For example, `hex(20)`, returns the string `'00000014'`. If an array is passed, as in `hex({1, 10, 100})`, an array of hexadecimal strings is returned.

The second parameter, `digits`, is optional. If a number is passed, as in `hex(20, 2)`, it sets the number of hexadecimal digits to display. For example, calling `hex(20, 2)` returns the string `'14'`.

## Examples

![hex example 1](assets/hex1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create a number variable.
  local original = 20

  -- Convert the number to a hex string.
  local converted = hex(original)

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(14)

  -- Display the original and converted values.
  text(original..' = '..converted, 50, 50)

  describe('The text "20 = 00000014" written in black on a gray background.')
end
```

![hex example 2](assets/hex2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create a number variable.
  local original = 20

  -- Convert the number to a hex string.
  -- Only display two hex digits.
  local converted = hex(original, 2)

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(16)

  -- Display the original and converted values.
  text(original..' = '..converted, 50, 50)

  describe('The text "20 = 14" written in black on a gray background.')
end
```

![hex example 3](assets/hex3.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create an array of numbers.
  local original = {1, 10, 100}

  -- Convert the numbers to hex strings.
  -- Only use two hex digits.
  local converted = hex(original, 2)

  -- Style the text.
  textAlign(RIGHT, CENTER)
  textSize(16)

  -- Iterate over the converted values.
  for i=1,#converted do

    -- Calculate the y-coordinate.
    local y = (i + 1) * 25 - 25

    -- Display the original and converted values.
    text(original[i]..' = '..converted[i], 75, y)
  end

  describe(
    'The text "1 = 01", "10 = 0A", and "100 = 64" written on three separate lines. The text is in black on a gray background.'
  )
end
```

## Syntax

```lua
hex(n, [digits])
```

```lua
hex(ns, [digits])
```

## Parameters

| Parameter |                                         |
| -         | --                                      |
| n         | Number: value to convert.               |
| digits    | Number: number of digits to include.    |
| ns        | Ordered table array: values to convert. |

## Returns

String: converted hexadecimal value.

## Related

* [boolean()](boolean-function.md)
* [byte()](byte.md)
* [char()](char.md)
* [float()](float.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
