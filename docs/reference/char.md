# char()
 
Converts a number or string to a single-character string.

`char()` converts numbers to their single-character string representations.

The parameter, `n`, is the value to convert. If a number is passed, as in `char(65)`, the corresponding single-character string is returned. If a string is passed, as in `char('65')`, the string is converted to an integer (whole number) and the corresponding single-character string is returned. If an array is passed, as in `char({65, 66, 67})`, an array of single-character strings is returned.

## Examples

![char example 1](assets/char1.webp)

```lua
function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create a number variable.
  local original = 65

  -- Convert the number to a char.
  local converted = char(original)

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(16)

  -- Display the original and converted values.
  text(original..' : '..converted, 50, 50)

  describe('The text "65 : A" written in black on a gray background.')
end
```

![char example 2](assets/char1.webp)

```lua
function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create a string variable.
  local original = '65'

  -- Convert the string to a char.
  local converted = char(original)

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(16)

  -- Display the original and converted values.
  text(original..' : '..converted, 50, 50)

  describe('The text "65 : A" written in black on a gray background.')
end
```

![char example 3](assets/char3.webp)

```lua
function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create an array of numbers.
  local original = {'65', 66, '67'}

  -- Convert the string to a char.
  local converted = char(original)

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(16)

  -- Iterate over elements of the converted array.
  for i=1,#converted do

    -- Calculate the y-coordinate.
    local y = (i + 1) * 25 - 25

    -- Display the original and converted values.
    text(original[i]..' : '..converted[i], 50, y)
  end

  describe(
    'The text "65 : A", "66 : B", and "67 : C" written on three separate lines. The text is in black on a gray background.'
  )
end
```

## Syntax

```lua
char(n)
```

```lua
char(ns)
```

## Parameters

| Parameter |                                               |
| -         | --                                            |
| n         | String/Number: value to convert.              |
| ns        | Ordered Table array: values to convert.       |

## Returns

String: converted single-character string.

## Related

* [boolean()](boolean.md)
* [byte()](byte.md)
* [float()](float.md)
* [str()](str.md)
