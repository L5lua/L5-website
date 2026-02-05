# local
    
Declares a new variable in the current block scope.

A variable is a container for a value. For example, a variable might contain a creature's x-coordinate as a `number` or its name as a `string`. Variables can change value by reassigning them as follows:

```lua
local x = 10

-- Reassign x to 50.
x = 50
```

**Note: Unlike JavaScript and Java, when a variable is declared without prepending `local` such as `x = 10` it is global by default, *even when declared inside a function.* In contrast, declaring a variable with `local` means it only exists within the block defined by its start and closing `end`.** For example, the following code would print an output of `nil` because `x` is declared as a local variable within the `setup()` function's block:

```lua
require("L5")

function setup()
  size(100, 100)

  local x = 50
end

function draw() 
  background(200)

  -- x was declared in setup(), so it can't be referenced here.
  circle(x, 50, 20) --will result in x being nil
end
```

**Variables declared without *local* are in the global scope.** A variable that's in the global scope can be used and changed anywhere in a sketch:

```lua
require("L5")

function setup()
  createCanvas(100, 100)
  
  x = 50 --created without local, so is global
end

function draw() 
  background(200)

  -- Change the value of x.
  x = x + 10

  circle(x, 50, 20)
end
```

## Examples

![local example 1](assets/local1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(220)

  -- Style the text.
  textAlign(CENTER)
  textSize(16)
  fill('black')
  windowTitle("variable creation.")

  -- Create the message variable.
  local message = 'Hello, L5!'

  -- Display the message.
  text(message, 50, 50)

  describe('The text "Hello, L5!" written on a gray background.')
end
```

![local example 2](assets/local2.gif)

```lua
local x = 0

require("L5")

function setup()
  size(100, 100)

  describe('A white circle moves from left to right against a gray background.')
end

function draw()
  background(220)

  -- Change the value of x.
  x = x + 1

  circle(x, 50, 20)
end
```

## Related

* [if](if.md)
* [function](function.md)
* [for](for.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
