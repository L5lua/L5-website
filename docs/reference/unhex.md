# unhex()
 
Converts a `String` with a hexadecimal value to a  `Number`.

`unhex()` converts a string with its hexadecimal number value to a number. Hexadecimal (hex) numbers are base-16, which means there are 16 unique digits. Hex extends the numbers 0–9 with the letters A–F. For example, the number `11` (eleven) in base-10 is written as the letter `B` in hex.

The first parameter, `n`, is the hex string to convert. For example, `unhex('FF')`, returns the number 255. If an array is passed, as in `unhex({'00', '80', 'FF'})`, an array of numbers is returned.

## Examples

![unhex example 1](assets/unhex1.webp)

```lua
function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create a a hex string variable
  local original = 'FF'

  -- Convert the hex string to a number.
  local converted = unhex(original)

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(16)

  -- Display the original and converted values.
  text(original.." = "..converted, 50, 50)

  describe('The text "FF = 255" written in black on a gray background.')
end
```

![unhex example 2](assets/unhex2.webp)

```lua
function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create an array of numbers.
  local original = {'00', '80', 'FF'}

  -- Convert the numbers to hex strings.
  -- Only use two hex digits.
  local converted = unhex(original, 2)

  -- Style the text.
  textAlign(RIGHT, CENTER)
  textSize(16)

  -- Iterate over the converted values.
  for i=1,#converted do

    -- Calculate the y-coordinate.
    local y = (i + 1) * 25 - 25

    -- Display the original and converted values.
    text( original[i].." = "..converted[i], 80, y)
  end

  describe(
    'The text "00 = 0", "80 = 128", and "FF = 255" written on three separate lines. The text is in black on a gray background.'
  )
end
```

## Syntax

```lua
unhex(n)
```

```lua
unhex(ns)
```

## Parameters

| Parameter |                                                   |
| -         | --                                                |
| n         | String: value to convert.                         |
| ns        | Ordered table array of strings: value to convert. |

## Returns

Number: converted number.

## Related

* [hex()](hex.md)
* [boolean()](boolean.md)
* [byte()](byte.md)
* [char()](char.md)
* [unchar()](unchar.md)
* [float()](float.md)
