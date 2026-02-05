# str()
 
Converts a `Boolean` or `Number` to `String`.

`str()` converts values to strings. See the String reference page for guidance on using template literals instead.

The parameter, `n`, is the value to convert. If `n` is a Boolean, as in `str(false)` or `str(true)`, then the value will be returned as a string, as in `'false'` or `'true'`. If `n` is a number, as in `str(123)`, then its value will be returned as a string, as in `'123'`. If an array is passed, as in `str({12.34, 56.78})`, then an array of strings will be returned.

## Examples

![str example 1](assets/str1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create a Boolean variable.
  local original = false

  -- Convert the Boolean to a string.
  local converted = str(original)

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(16)

  -- Display the original and converted values.
  text(str(original).." : "..converted, 50, 50)

  describe('The text "false : false" written in black on a gray background.')
end
```

![str example 2](assets/str2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create a number variable.
  local original = 123

  -- Convert the number to a string.
  local converted = str(original)

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(16)

  -- Display the original and converted values.
  text(original.." = "..converted, 50, 50)

  describe('The text "123 = 123" written in black on a gray background.')
end
```

![str example 3](assets/str3.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Create an array of numbers.
  local original = {12, 34, 56}

  -- Convert the numbers to strings.
  local strings = str(original)

  -- Create an empty string variable.
  local final = ''

  -- Concatenate all the strings.
  for _,s in ipairs(strings) do
    final = final .. s
  end

  -- Style the text.
  textAlign(CENTER, CENTER)
  textSize(16)

  -- Display the concatenated string.
  text(final, 50, 50)

  describe('The text "123456" written in black on a gray background.')
end
```

## Syntax

```lua
str(n)
```

## Parameters

| Parameter |                                               |
| -         | --                                            |
| n         | String/Boolean/Number: value to convert.      |
| ns        | Ordered Table array: values to convert.       |


## Returns

String: converted string.

## Related

* [boolean()](boolean-function.md)
* [byte()](byte.md)
* [char()](char.md)
* [float()](float.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
