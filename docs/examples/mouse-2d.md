# Mouse 2D

This example uses two-dimensional mouse tracking to control both the position and size of rectangles. Moving the mouse in different directions creates different visual effects with symmetrical and inverse squares.

It demonstrates:

- using both `mouseX` and `mouseY` for 2D control
- creating inverse mouse control (using width and height minus mouse position)
- mapping mouse coordinates to shape properties
- creating visual symmetry through complementary operations
- simple but effective interactive design

From here, you can try:

- creating grids of mouse-responsive elements
- adding click detection to change drawing mode
- creating smooth transitions between mouse positions
- implementing multiple interactive objects with different responses
- adding rotation or other transformations based on mouse position

![animation of two translucent squares moving in opposite directions](/assets/examples/mouse-2d.gif "Two translucent rectangles that move with the mouse, one following it directly and one moving in the inverse direction")

```lua
require("L5")

function setup()
    size(640, 360)
    windowTitle("Mouse 2D")
    describe("Moving the mouse changes the position and size of each box")

    noStroke()
    rectMode(CENTER)
end

function draw()
    background(0.0)

    fill(255, 204)
    rect(mouseX, height / 2, mouseY / 2 + 10, mouseY / 2 + 10)

    fill(255, 204)

    local inverseX = width - mouseX
    local inverseY = height - mouseY
    rect(inverseX, height / 2, (inverseY / 2) + 10, (inverseY / 2) + 10)
end
```
