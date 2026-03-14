# Keyboard Functions

This example creates an interactive color typewriter where different letter cases produce different sized rectangles with different colors from the HSB color space.

It demonstrates:

- the `keyPressed()` callback function
- distinguishing between uppercase and lowercase keys
- using HSB color mode for easy hue variation
- managing state variables for continuous drawing
- wrapping text display horizontally and vertically
- creating visual feedback for keyboard input

From here, you can try:

- adding different shapes for different key categories
- incorporating `keyReleased()` for key release events
- creating a full text display that captures typed words
- creating animated transitions between letters

![animation of a color typewriter with varying heights](/assets/examples/keyboard-functions.gif "Colored rectangles of different heights appearing continuously as keys are typed, wrapping across the screen")

```lua
require("L5")

local maxHeight = 40
local minHeight = 20
local letterHeight = maxHeight
local letterWidth = 20

local x = -letterWidth
local y = 0

local newletter = false

local numChars = 26
local colors = {}

function setup()
    size(640, 360)
    windowTitle("Keyboard Functions")
    describe("Press letter keys to create forms in time and space")

    noStroke()
    colorMode(HSB, numChars)
    background(numChars / 2)

    -- Set a hue value for each key
    for i = 0, numChars - 1 do
        colors[i] = color(i, numChars, numChars)
    end
end

function draw()
    if newletter == true then
        -- Draw the "letter"
        local y_pos
        if letterHeight == maxHeight then
            y_pos = y
            rect(x, y_pos, letterWidth, letterHeight)
        else
            y_pos = y + minHeight
            rect(x, y_pos, letterWidth, letterHeight)
            fill(numChars / 2)
            rect(x, y_pos - minHeight, letterWidth, letterHeight)
        end
        newletter = false
    end
end

function textinput(text)    
    local alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if string.match(key, "^[A-Z]$") then
        keyIndex = string.find(alphabet, key) - 1
        letterHeight = maxHeight
        fill(colors[keyIndex])
    elseif string.match(key, "^[a-z]$") then
        keyIndex = string.find(alphabet, string.upper(key)) - 1
        letterHeight = minHeight
        fill(colors[keyIndex])
    else
        fill(0)
        letterHeight = 10
    end

    newletter = true

    -- Update the "letter" position
    x = x + letterWidth

    -- Wrap horizontally
    if x > width - letterWidth then
        x = 0
        y = y + maxHeight
    end

    -- Wrap vertically
    if y > height - letterHeight then
        y = 0
    end
end
```
