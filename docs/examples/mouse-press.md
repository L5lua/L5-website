# Mouse Press

This example creates a crosshair that follows the mouse position. The stroke color changes when the mouse button is pressed, creating an inverted visual effect.

It demonstrates:

- the `mouseIsPressed` built-in variable to check if mouse button is held down
- creating dynamic visual feedback based on input state
- simple shapes (lines) controlled by mouse position
- conditional rendering based on input state

From here, you can try:

- drawing more complex shapes instead of just lines
- creating different visual modes based on mouse state
- adding trails or previous positions to create patterns
- adding keyboard modifiers to change behavior

![animation of a crosshair that changes color when mouse button is pressed](/assets/examples/mouse-press.gif "A white and black crosshair following the mouse that inverts colors when the mouse button is pressed")

```lua
require("L5")

function setup()
    size(640, 360)
    windowTitle("Mouse Press")
    describe("Move and press the mouse button to position the shape and invert the color")

    noSmooth()
    fill(126)
    background(102)
end

function draw()
    if (mouseIsPressed) then
        stroke(255)
    else
        stroke(0)
    end

    line(mouseX - 66, mouseY, mouseX + 66, mouseY)
    line(mouseX, mouseY - 66, mouseX, mouseY + 66)
end
```
