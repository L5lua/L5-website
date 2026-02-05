# for
    
A way to repeat a block of code when the number of iterations is known.

`for` loops are helpful for repeating statements a certain number of times. For example, a `for` loop makes it easy to express the idea "draw five lines" like so:

```
for x = 10,100,20 do
  line(x, 25, x, 75)
end
```

The loop's header begins with the keyword `for`. Loops generally count up or count down as they repeat, or iterate. The statements in parentheses `x = 10, 100, 20` tell the loop how it should repeat:


* `x = 10` tells the loop to start counting at `10` and keep track of iterations using the variable `x`.
* `100` tells the loop to count up to `100`, inclusive (*note: Unlike Lua, both Java and Javascript treat the stop value as exclusive.*)
* `20`  tells the loop to count up by `20` at the end of each iteration.

The code following `do` until `end` is the loop's body. Statements in the loop body are repeated during each iteration of the loop.

`for` loops can also count down:

```
for d = 100,0,-10 do
  circle(50, 50, d)
end
```

`for` loops can also contain other loops. The following nested loop draws a grid of points:

```lua
-- Loop from left to right.
for x = 10,100,10 do

  -- Loop from top to bottom.
  for y = 10,100,10 do
    point(x, y)
  end

end
```

`for` loops are also helpful for iterating through the elements of an array. For example, it's common to iterate through an array that contains information about where or what to draw:

```lua
--Create an ordered table array of x-coordinates.
local xCoordinates = {20, 40, 60}

for i = 1,#xCoordinates do
  -- Update the element.
  xCoordinates[i] = xCoordinates[i] + random(-1, 1)

  -- Draw a circle.
  circle(xCoordinates[i], 50, 20)
end
```

If the array's values aren't modified, the `for...of` statement can simplify the code. They're similar to `for...in` loops in JavaScript, `for` loops in Python and `for-each` loops in C++ and Java. The following loops have the same effect:

```lua
-- Draw circles with a for loop.
local xCoordinates = {20, 40, 60}

for i = 1,#xCoordinates do
  circle(xCoordinates[i], 50, 20);
end
```

```lua
-- Draw circles with a for...in loop.
local xCoordinates = {20, 40, 60}

for i,x in ipairs(xCoordinates) do
  circle(x, 50, 20);
end
```

In the code snippets above, the variables `i` and `x` have different roles.

In the first snippet, `i` counts from `1` up to `3`, which is the length of `xCoordinates`, which we can get with prepending *#* to `#xCoordinates`. `i` is used to access the element in `xCoordinates` at index `i`.

In the second code snippet using Lua's function `ipairs()`, `x` isn't keeping track of the loop's progress or an index. During each iteration, `x` contains the next element of `xCoordinates`. `x` starts from the beginning of `xCoordinates` (`20`) and updates its value to `40` and then `60` during the next iterations.

## Examples

![for example 1](assets/for1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('Five black vertical lines on a gray background.')
end

function draw()
  background(200)

  -- Draw vertical lines using a loop.
  for x=10,100,20 do
    line(x, 25, x, 75)
  end
end
```

![for example 2](assets/for2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('Five white concentric circles drawn on a gray background.')
end

function draw()
  background(200)

  -- Draw concentric circles using a loop.
  for d = 100,0,-20 do
    circle(50, 50, d)
  end
end
```

![for example 3](assets/for3.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A grid of black dots on a gray background.')
end

function draw()
  background(200)

  -- Set the spacing for points on the grid.
  local space = 10

  -- Increase the stroke weight.
  strokeWeight(3)

  -- Loop from the left to the right.
  for x=space,100-1,space do
    -- Loop from the top to the bottom.
    for y=space,100-1,space do
      point(x, y)
    end
  end
end
```

![for example 4](assets/for4.webp)

```lua
-- Declare the variable xCoordinates and assign it an array of numbers.
local xCoordinates = {20, 40, 60, 80}

require("L5")

function setup()
  size(100, 100)

  describe('Four white circles drawn in a horizontal line on a gray background.')
end

function draw()
  background(200)

  -- Access the element at index i and use it to draw a circle.
  for i=1,#xCoordinates do
    circle(xCoordinates[i], 50, 20)
  end
end
```

![for example 5](assets/for4.webp)

```lua
-- Declare the variable xCoordinates and assign it an array of numbers.
local xCoordinates = {20, 40, 60, 80}

require("L5")

function setup()
  size(100, 100)

  describe('Four white circles drawn in a horizontal line on a gray background.')
end

function draw()
  background(200)

  -- Access each element of the array and use it to draw a circle.
  for _,x in ipairs(xCoordinates) do
    circle(x, 50, 20)
  end
end
```

## Related

* [function](function.md)
* [table](table.md)
* [while](while.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
