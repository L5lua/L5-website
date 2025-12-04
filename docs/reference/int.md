# int()
 
Converts a `Boolean`, `String`, or decimal `Number` to an integer.

`int()` converts values to integers. Integers are positive or negative numbers without decimals. If the original value has decimals, as in -34.56, they're removed to produce an integer such as -34.

The parameter, `n`, is the value to convert. If `n` is a Boolean, as in `int(false)` or `int(true)`, then the number 0 (`false`) or 1 (`true`) will be returned. If `n` is a string or number, as in `int('45')` or `int(67.89)`, then an integer will be returned. If an array is passed, as in `int({12.34, 56.78})`, then a table array of integers will be returned.

Note: If a value can't be converted to a number, as in `int('giraffe')`, then the value `nil` will be returned.

## Examples

![int example 1](assets/int1.webp)

```lua
function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create a Boolean variable.
  local original = false

  -- Convert the Boolean to an integer.
  local converted = int(original)

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(16)

  -- Display the original and converted values.
  text(str(original)..' : '..str(converted), 50, 50)

  describe('The text "false : 0" written in black on a gray background.')
end
```

![int example 2](assets/int2.webp)

```lua
function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create a string variable.
  local original = '12.34'

  -- Convert the string to an integer.
  local converted = int(original)

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(14)

  -- Display the original and converted values.
  text(original..' ≈ '..converted, 50, 50)

  describe('The text "12.34 ≈ 12" written in black on a gray background.')
end
```

![int example 3](assets/int2.webp)

```lua
function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create a decimal number variable.
  local original = 12.34

  -- Convert the decimal number to an integer.
  local converted = int(original)

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(14)

  -- Display the original and converted values.
  text(original.." ≈ "..converted, 50, 50)

  describe('The text "12.34 ≈ 12" written in black on a gray background.')
end
```

![int example 4](assets/int4.webp)

```lua
function setup()
  size(100, 100)

  background(200)

  -- Create an array of strings.
  local original = {'60', '30', '15'}

  -- Convert the strings to integers.
  local diameters = int(original)

  for _,d in ipairs(diameters) do
    -- Draw a circle.
    circle(50, 50, d)
  end

  describe('Three white, concentric circles on a gray background.')
end
```


## Syntax

```lua
int(n)
```

```lua
int(ns)
```

## Parameters

| Parameter |                                           |
| -         | --                                        |
| n         | String/Boolean/Number: value to convert.  |
| ns        | Ordered table (array): values to convert. |

## Returns

Number: converted number.

## Related

* [boolean()](boolean.md)
* [byte()](byte.md)
* [char()](char.md)
* [float()](float.md)
* [str()](str.md)
