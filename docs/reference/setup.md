# setup()
 
A function that's called once when the sketch begins running.

Declaring the function `setup()` sets a code block to run once automatically when the sketch starts running. It's used to perform setup tasks such as creating the canvas and initializing variables:

```lua
function setup() 
  -- Code to run once at the start of the sketch.
end
```

Code placed in `setup()` will run once before code placed in draw() begins looping. 

Note: `setup()` doesn’t have to be declared, but it’s common practice to do so.

## Examples

![setup example 1](assets/setup1.webp)

```lua
function setup()
  size(100, 100)
  windowTitle('setup example')

  background(200)

  -- Draw the circle.
  circle(50, 50, 40)

  describe('A white circle on a gray background.')
end
```

![setup example 2](assets/setup2.gif)

```lua
function setup()
  size(100, 100)

  -- Paint the background once.
  background(200)

  describe(
    'A white circle on a gray background. The circle follows the mouse as the user moves, leaving a trail.'
  )
end

function draw()
  -- Draw circles repeatedly.
  circle(mouseX, mouseY, 40)
end
```

![setup example 3](assets/setup3.gif)

```lua
local img

function setup()
  size(100, 100)
  img = loadImage('assets/bricks.jpg')

  -- Draw the image.
  image(img, 0, 0)

  describe(
    'A white circle on a brick wall. The circle follows the mouse as the user moves, leaving a trail.'
  )
end

function draw()
  -- Style the circle.
  noStroke()

  -- Draw the circle.
  circle(mouseX, mouseY, 10)
end
```

## Related

* [draw()](draw.md)
* [noLoop()](noLoop.md)
* [mousePressed()](mousePressed.md)
* [keyPressed()](keyPressed.md)
