# boolean()
 
Converts a `String` or `Number` to a `Boolean`.

`boolean()` converts values to `true` or `false`.

The parameter, `n`, is the value to convert. If `n` is a string, then `boolean('true')` will return `true` and every other string value will return `false`. If `n` is a number, then `boolean(0)` will return `false` and every other numeric value will return `true`. If an array is passed, as `in boolean({0, 1, 'true', 'blue'})`, then an array of Boolean values will be returned.

## Examples

![boolean example 1](assets/boolean1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Create a number variable.
  local original = 0

  -- Convert the number to a Boolean value.
  local converted = boolean(original)

  -- Style the circle based on the converted value.
  if converted == true then
    fill('blue')
  else 
    fill('red')
  end

  -- Draw the circle.
  circle(50, 50, 40)

  describe('A red circle on a gray background.')
end
```

![boolean example 2](assets/boolean2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Create a string variable.
  local original = 'true'

  -- Convert the string to a Boolean value.
  local converted = boolean(original)

  -- Style the circle based on the converted value.
  if converted == true then
    fill('blue')
  else
    fill('red')
  end

  -- Draw the circle.
  circle(50, 50, 40)

  describe('A blue circle on a gray background.')
end
```

![boolean example 3](assets/boolean3.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Create an array of values.
  local original = {0, 'hi', 123, 'true'}

  -- Convert the array to Boolean values.
  local converted = boolean(original)

  -- Iterate over the array of converted Boolean values.
  for i=1,#converted do

    -- Style the circle based on the converted value.
    if converted[i] == true then
      fill('blue')
    else 
      fill('red')
    end

    -- Calculate the x-coordinate.
    local x = (i + 1) * 20 - 20

    -- Draw the circle.
    circle(x, 50, 15)
  end

  describe(
    'A row of circles on a gray background. The two circles on the left are red and the two on the right are blue.'
  )
end
```

## Syntax

```lua
boolean(n)
```

```lua
boolean(ns)
```

## Parameters

| Parameter |                                           |  
| -         | --                                        |
| n         | String/Boolean/Number: value to convert.  |
| ns        | Ordered table array of values to convert. |

## Returns

Boolean: converted boolean value.

## Related

* [byte](byte.md)
* [char](char.md)
* [hex](hex.md)
* [int](int.md)
* [str](str.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
