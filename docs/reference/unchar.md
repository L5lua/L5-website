# unchar()
 
Converts a single-character `String` to a `Number`.

`unchar()` converts single-character strings to their corresponding integer (whole number).

The parameter, `n`, is the character to convert. For example, `unchar('A')`, returns the number 65. If an array is passed, as in `unchar({'A', 'B', 'C'})`, an array of integers is returned.

## Examples

![unchar example 1](assets/unchar1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create a string variable.
  local original = 'A'

  -- Convert the string to a number.
  local converted = unchar(original)

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(16)

  -- Display the original and converted values.
  text(original.." : "..converted, 50, 50)

  describe('The text "A : 65" written in black on a gray background.')
end
```

![unchar example 2](assets/unchar2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create an array of characters.
  local original = {'A', 'B', 'C'}

  -- Convert the string to a number.
  local converted = unchar(original)

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(16)

  -- Iterate over elements of the converted array.
  for i=1,#converted do

    -- Calculate the y-coordinate.
    local y = (i + 1) * 25 - 25

    -- Display the original and converted values.
    text(original[i].." : "..converted[i], 50, y)
  end

  describe(
    'The text "A : 65", "B : 66", and "C :67" written on three separate lines. The text is in black on a gray background.'
  )
end
```

## Syntax

```lua
unchar(n)
```

```lua
unchar(ns)
```

## Parameters

| Parameter |                                                   |
| -         | --                                                |
| n         | String: value to convert.                         |
| ns        | Ordered table array of strings: value to convert. |

## Returns

Number: converted number.

## Related

* [boolean()](boolean-function.md)
* [byte()](byte.md)
* [char()](char.md)
* [float()](float.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
