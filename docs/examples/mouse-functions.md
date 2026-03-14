# Mouse Functions

This example demonstrates mouse interaction events by allowing the user to click and drag a box around the screen. Different mouse states are highlighted with color changes.

It demonstrates:

- the `mousePressed()` callback function for detecting mouse button presses
- the `mouseDragged()` callback function for detecting drag events
- the `mouseReleased()` callback function for detecting mouse button releases
- tracking mouse offset for smooth dragging
- using state variables to control behavior
- creating interactive draggable objects

From here, you can try:

- creating multiple draggable objects
- implementing collision detection between draggable objects
- adding snap-to-grid functionality
- creating different drag behaviors (rotate, scale, etc.)
- storing the positions of dragged objects for saving/loading
- adding visual feedback like shadows or outlines during dragging

![animation of a draggable gray square on a black background](/assets/examples/mouse-functions.gif "A gray square that changes color when hovering over it and can be dragged around the screen with the mouse")

```lua
require("L5")

local bx = 0
local by = 0
local boxSize = 75
local overbox = false
local locked = false
local xOffset = 0.0
local yOffset = 0.0

function setup()
    size(640, 360)
    windowTitle("Mouse Functions")
    describe("Click on the box and drag it across the screen.")

    noStroke()
    rectMode(RADIUS)

    bx = width / 2.0
    by = height / 2.0
    boxSize = 75
    overbox = false
    locked = false
    xOffset = 0.0
    yOffset = 0.0
end

function draw()
    background(0)

    -- Test if the cursor is over the box 
    if ((mouseX > bx - boxSize and mouseX < bx + boxSize) and (mouseY > by - boxSize and mouseY < by + boxSize)) then
        overbox = true
        if (not locked) then
            stroke(255)
            fill(153)
        end

    else
        stroke(153)
        fill(153)
        overbox = false
    end

    rect(bx, by, boxSize, boxSize)
end

function mousePressed()
    if (overbox) then
        locked = true
        fill(255, 255, 255)
    else
        locked = false
    end
    xOffset = mouseX - bx
    yOffset = mouseY - by
end

function mouseDragged()
    if (locked) then
        bx = mouseX - xOffset
        by = mouseY - yOffset
    end
end

function mouseReleased()
    locked = false
end
```
