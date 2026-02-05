## Number

A number that can be positive, negative, or zero.

The Number data type is useful for describing values such as position, size, and color. A number can be an integer such as 20 or a decimal number such as 12.34. For example, a circle's position and size can be described by three numbers:

```lua
circle(50, 20, 20)
```

```lua
circle(50, 20, 12.34)
```

Numbers support basic arithmetic and follow the standard order of operations: Parentheses, Exponents, Multiplication, Division, Addition, and Subtraction (PEMDAS). For example, it's common to use arithmetic operators with p5.js' system variables that are numbers:

```lua
-- Draw a circle at the center
circle(width / 2, height / 2, 20)
```

```lua
-- Draw a circle that moves from left to right.
circle(frameCount * 0.01, 50, 20)
```

Here's a quick overview of the arithmetic operators:

```lua
1 + 2 -- Add
1 - 2 -- Subtract
1 * 2 -- Multiply
1 / 2 -- Divide
1 % 2 -- Remainder
1 ^ 2 -- Exponentiate
```

It's common to update a number variable using arithmetic. For example, an object's location can be updated like so:

```lua
x = x + 1
```

The statement above adds 1 to a variable `x` using the `+` operator. *Lua does not have the assignment operators such as *+=*, *-=*, *\*=*, */=*, *%=*.*

See [Boolean](Boolean.md) for more information about comparisons and conditions.

Expressions with numbers can also produce special values when something goes wrong.

```lua
sqrt(-1) -- nan
1 / 0 -- inf
```

The value `nan` stands for [Not-A-Number](https://www.lua.org/manual/5.2/manual.html#2.1). `nan` appears when calculations or conversions don't work. `inf` stands for infinity, a value that's larger than any number. It appears during certain calculations.

## Examples

![Number example 1](assets/Number1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Draw a circle at the center.
  circle(50, 50, 70)

  -- Draw a smaller circle at the center.
  circle(width / 2, height / 2, 30)

  describe('Two concentric, white circles drawn on a gray background.')
end
```

![Number example 2](assets/Number2.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A white circle travels from left to right on a gray background.')
end

function draw()
  background(200)

  circle(frameCount * 0.05, 50, 20)
end
```

## Related

* [Boolean](Boolean.md)
* [for](for.md)
* [function](function.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
