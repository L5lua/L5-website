# Storing Input

This example records mouse positions over time and displays them as a trail of circles. The most recent positions are drawn largest, creating a smooth motion trail effect.

It demonstrates:

- storing historical data in arrays
- implementing a circular buffer pattern
- using modulo operator (`%`) for array wrapping
- the `frameCount` variable for frame tracking
- creating motion trails with decreasing opacity/size
- efficient memory usage by reusing array slots

From here, you can try:

- adding color variation to the trail based on age
- implementing trails for multiple objects
- using trails for collision detection
- creating fade-out effects for old trail points
- storing different types of data (velocity, acceleration, etc.)
- playback of recorded input sequences
- using trails to visualize object paths over time

![animation of mouse trail showing translucent circles](/assets/examples/storing-input.gif "A trail of translucent circles following the mouse cursor, with larger circles representing more recent positions")

```lua
require("L5")

local num = 60
local mx
local my

function setup()
    size(640, 360)
    windowTitle("Storing Input")
    describe(" Move the mouse across the screen to change the position of the circles and store them")

    noStroke()

    mx = {}
    my = {}

    for i = 0, num - 1 do
        mx[i] = 0
        my[i] = 0
    end

    fill(255, 153)
end

function draw()
    background(51)

    -- Cycle through the array, using a different entry on each frame.
    -- Using modulo (%) like this is faster than moving all the values over
    local which = frameCount % num
    mx[which] = mouseX
    my[which] = mouseY

    for i = 0, num - 1 do
        -- which+1 is the smallest (the oldest in the array)
        local index = (which + 1 + i) % num
        ellipse(mx[index], my[index], i, i)
    end
end
```
