# if()

A way to choose whether to run a block of code.

`if` statements are helpful for running a block of code based on a condition. For example, an `if` statement makes it easy to express the idea "Draw a circle if the mouse is pressed.":

```lua
if mouseIsPressed == true then
  circle(mouseX, mouseY, 20)
end
```

The statement header begins with the keyword `if`. The expression in parentheses `mouseIsPressed == true` is a `Boolean` expression that's either `true` or `false`. The code between `then` and `end` is the if statement's body. The body only runs if the `Boolean` expression is `true`.

The mouseIsPressed system variable is always `true` or `false`, so the code snippet above could also be written as follows:

```lua
if mouseIsPressed then
  circle(mouseX, mouseY, 20)
end
```

An `if`-`else` statement adds a block of code that runs if the `Boolean` expression is `false`. For example, here's an `if`-`else` statement that expresses the idea "Draw a circle if the mouse is pressed. Otherwise, display a message.":

```lua
if mouseIsPressed == true then
  -- When true.
  circle(mouseX, mouseY, 20)
else 
  -- When false.
  text('Click me!', 50, 50)
end
```

There are two possible paths, or branches, in this code snippet. The program must follow one branch or the other.

An `elseif` statement makes it possible to add more branches. `elseif` statements run different blocks of code under different conditions. For example, an `elseif` statement makes it easy to express the idea "If the mouse is on the left, paint the canvas white. If the mouse is in the middle, paint the canvas gray. Otherwise, paint the canvas black.":

```
if mouseX < 33 then
  background(255)
elseif mouseX < 67 then
  background(200)
else
  background(0)
end
```

`if` statements can add as many `elseif` statements as needed. However, there can only be one `else` statement and it must be last. Note that `elseif` requires a `then` after the statement being tested but `else` does not.

`if` statements can also check for multiple conditions at once. For example, the `Boolean` operator `and` checks whether two expressions are both `true`:

```lua
if keyIsPressed == true and key == 'p' then
  text('You pressed the "p" key!', 50, 50)
end
```

If the user is pressing a key AND that key is `'p'`, then a message will display.

The `Boolean` operator `or` checks whether at least one of two expressions is `true`:

```lua
if keyIsPressed == true or mouseIsPressed == true then
  text('You did something!', 50, 50)
end
```

If the user presses a key, or presses a mouse button, or both, then a message will display.

The body of an `if` statement can contain another `if` statement. This is called a "nested `if` statement." For example, nested `if` statements make it easy to express the idea "If a key is pressed, then check if the key is `'r'`. If it is, then set the fill to red.":

```
if keyIsPressed == true then
  if key == 'r' then
    fill('red')
  end
end
```

See [Boolean](Boolean.md) and [Number](Number.md) to learn more about these data types and the operations they support.

## Examples

![if example 1](assets/if1.gif)

```lua
-- Click the mouse to show the circle.

require("L5")

function setup()
  size(100, 100)

  describe(
    'A white circle on a gray background. The circle follows the mouse user clicks on the canvas.'
  )
end

function draw()
  background(200)

  if mouseIsPressed == true then
    circle(mouseX, mouseY, 20)
  end
end
```

![if example 2](assets/if2.gif)

```lua
-- Click the mouse to show different shapes.

require("L5")

function setup()
  size(100, 100)

  describe(
    'A white ellipse on a gray background. The ellipse becomes a circle when the user presses the mouse.'
  )
end

function draw()
  background(200)

  if mouseIsPressed == true then 
    circle(50, 50, 20)
  else 
    ellipse(50, 50, 20, 50)
  end
end
```

![if example 3](assets/if3.gif)

```lua
-- Move the mouse to change the background color.

require("L5")

function setup()
  size(100, 100)

  describe(
    'A square changes color from white to black as the user moves the mouse from left to right.'
  )
end

function draw()
  if mouseX < 33 then 
    background(255)
  elseif mouseX < 67 then
    background(200)
  else 
    background(0)
  end
end
```

![if example 4](assets/if4.gif)

```lua
-- Click on the canvas to begin detecting key presses.

require("L5")

function setup()
  size(100, 100)

  describe(
    'A white circle drawn on a gray background. The circle changes color to red when the user presses the r key.'
  )
end

function draw()
  background(200)

  if keyIsPressed == true then 
    if key == 'r' then 
      fill('red')
    end
  end

  circle(50, 50, 40)
end
```

## Related

* [boolean](Boolean.md)
* [for](for.md)
* [function](function.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
