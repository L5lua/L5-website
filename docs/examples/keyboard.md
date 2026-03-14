# Keyboard

This example responds to keyboard input by detecting which letter key is pressed and drawing visual forms in different positions based on the key pressed.

It demonstrates:

- the `keyPressed()` callback function
- detecting letter keys using string byte operations
- converting character input to identifiable indices
- mapping key indices to screen positions
- creating dynamic visual output based on keyboard input

From here, you can try:

- detecting non-letter keys and handling them differently
- changing colors or shapes based on the key pressed
- storing key history to create patterns
- using arrow keys for directional input
- creating a keyboard input handler for game controls

![animation of colored rectangles appearing as keys are pressed](/assets/examples/keyboard.gif "Colored rectangles drawn at different horizontal positions as letter keys are pressed")

```lua
require("L5")

function setup()
    size(640, 360)
    windowTitle("Keyboard")
    describe("Press letter keys to create forms in time and space")

    noStroke()
    background(0)

    rectWidth = width / 4
end

function draw()
    -- Keep draw() here to continue looping while waiting for keys
end

function keyPressed()
    local keyIndex = -1
    -- Convert the built-in key variable from a string to its byte value
    local keyByte = string.byte(key)

    if (keyByte >= string.byte('A') and keyByte <= string.byte('Z')) then
        keyIndex = keyByte - string.byte('A')
    elseif (keyByte >= string.byte('a') and keyByte <= string.byte('z')) then
        keyIndex = keyByte - string.byte('a')
    end

    if (keyIndex == -1) then
        -- If it's not a letter key, clear the screen
        background(0)
    else
        -- If it's a letter key, fill a rectangle
        fill(millis() % 255)
        x = map(keyIndex, 0, 25, 0, width - rectWidth)
        rect(x, 0, rectWidth, height)
    end
end
```
