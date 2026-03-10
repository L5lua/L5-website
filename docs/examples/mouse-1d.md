# Mouse 1D

This example creates a balanced visual display where moving the mouse left and right shifts the size and color balance between two rectangles. The horizontal mouse position controls a one-dimensional interaction.

It demonstrates:

- the `mouseX` variable for one-dimensional mouse tracking
- using mouse position to control both size and color
- the `map()` function to convert mouse coordinates to useful ranges
- creating complementary visual feedback
- using `rectMode(CENTER)` for easier rectangle positioning

From here, you can try:

- creating three or more balanced elements
- adding vertical mouse control (`mouseY`)
- implementing click detection to change behavior
- creating more complex relationships between mouse input and visual output
- adding animation that responds to mouse movement speed

![animation of two balanced gray rectangles shifting in size](/assets/examples/mouse-1d.gif "Two gray rectangles that shift their sizes and positions based on horizontal mouse movement")

```lua
require("L5")

function setup()
    size(640, 360)
    windowTitle("Mouse 1D")
    describe("Move the mouse left and right to shift the balance.")

    noStroke()
    colorMode(RGB, height, height, height)
    rectMode(CENTER)
end

function draw()
    background(0.0)

    local r1 = map(mouseX, 0, width, 0, height)
    local r2 = height - r1

    fill(r1)
    rect(width / 2 + r1 / 2, height / 2, r1, r1)

    fill(r2)
    rect(width / 2 - r2 / 2, height / 2, r2, r2)
end
```
