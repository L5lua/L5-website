# Conway's Game of Life

This example implements the famous [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) devised by British mathematician [John Conway](https://en.wikipedia.org/wiki/John_Horton_Conway). 

It is an example of a *zero-player game*, where after setting initial rules the simulation plays out algorithmically on its own without need for human intervention.

The original game as devised by Conway was for pen and gridded paper. Starting with any combination of cells in the grid either filled in (alive) or not (dead), the following rules were applied:

1. Any live cell with 2-3 neighbors survives
2. Any dead cell with exactly 3 neighbors becomes alive
3. All other cells die or stay dead

There are now hundreds of implementations in many programming languages. The game of life is an example of [cellular automata](https://en.wikipedia.org/wiki/Cellular_automaton).  Techniques are explored in a variety of applicatons including game design, studying [biology](https://en.wikipedia.org/wiki/Cellular_automaton#Biology), chemistry, physics, music, and computer science.

This program implements a basic version of the simulation. Press space bar to begin. You can click on individual cells to toggle their state, or draw directly on the grid. Pressing 'r' resets and pauses the game.

![Conways game of life running](/assets/examples/conways-life.gif)

```lua
require("L5")

-- Conway's Game of Life in L5
-- Click to toggle cells, press SPACE to pause/unpause, press R to reset

local cols, rows
local cellSize = 10
local grid = {}
local nextGrid = {}
local paused = true

function setup()
    size(800, 600)
    windowTitle("Conway's Game of Life")
    frameRate(10)
    
    -- Calculate grid dimensions
    cols = floor(width / cellSize)
    rows = floor(height / cellSize)
    
    -- Initialize grids
    initGrid()
    
    describe("Conway's Game of Life. Click to toggle cells. Press SPACE to start/pause. Press R to reset.")
end

function initGrid()
    -- Create empty grids
    for i = 1, cols do
        grid[i] = {}
        nextGrid[i] = {}
        for j = 1, rows do
            grid[i][j] = 0
            nextGrid[i][j] = 0
        end
    end
    
    -- Add initial random cells
    for i = 1, cols do
        for j = 1, rows do
            if random(1) < 0.2 then
                grid[i][j] = 1
            end
        end
    end
end

function draw()
    background(20)
    
    -- Draw grid
    for i = 1, cols do
        for j = 1, rows do
            local x = (i - 1) * cellSize
            local y = (j - 1) * cellSize
            
            if grid[i][j] == 1 then
                fill(255)
            else
                fill(50)
            end
            
            stroke(30)
            strokeWeight(1)
            rect(x, y, cellSize, cellSize)
        end
    end
    
    -- Update grid if not paused
    if not paused then
        computeNextGeneration()
    end
    
    -- Draw status text
    fill(255)
    noStroke()
    textSize(16)
    textAlign(LEFT, TOP)
    local status = paused and "PAUSED - Press SPACE to start" or "RUNNING - Press SPACE to pause"
    text(status, 10, 10)
    text("Click to toggle cells | Press R to reset", 10, 30)
end

function keyPressed()
    -- Toggle pause with spacebar
    if key == 'space' then
        paused = not paused
    end
    
    -- Reset with R
    if key == 'r' then
        initGrid()
        paused = true
    end
end

function computeNextGeneration()
    -- Calculate next generation
    for i = 1, cols do
        for j = 1, rows do
            local neighbors = countNeighbors(i, j)
            
            -- Conway's rules:
            -- 1. Any live cell with 2-3 neighbors survives
            -- 2. Any dead cell with exactly 3 neighbors becomes alive
            -- 3. All other cells die or stay dead
            
            if grid[i][j] == 1 then
                -- Cell is alive
                if neighbors == 2 or neighbors == 3 then
                    nextGrid[i][j] = 1
                else
                    nextGrid[i][j] = 0
                end
            else
                -- Cell is dead
                if neighbors == 3 then
                    nextGrid[i][j] = 1
                else
                    nextGrid[i][j] = 0
                end
            end
        end
    end
    
    -- Copy next generation to current grid
    for i = 1, cols do
        for j = 1, rows do
            grid[i][j] = nextGrid[i][j]
        end
    end
end

function countNeighbors(x, y)
    local count = 0
    
    -- Check all 8 neighbors
    for i = -1, 1 do
        for j = -1, 1 do
            -- Skip the center cell
            if not (i == 0 and j == 0) then
                -- Wrap around edges (toroidal topology)
                local col = ((x - 1 + i) % cols) + 1
                local row = ((y - 1 + j) % rows) + 1
                
                count = count + grid[col][row]
            end
        end
    end
    
    return count
end

function mousePressed()
    -- Toggle cell on click
    local col = floor(mouseX / cellSize) + 1
    local row = floor(mouseY / cellSize) + 1
    
    if col >= 1 and col <= cols and row >= 1 and row <= rows then
        if grid[col][row] == 0 then
            grid[col][row] = 1
        else
            grid[col][row] = 0
        end
    end
end

function mouseDragged()
    -- Allow drawing by dragging
    local col = floor(mouseX / cellSize) + 1
    local row = floor(mouseY / cellSize) + 1
    
    if col >= 1 and col <= cols and row >= 1 and row <= rows then
        grid[col][row] = 1
    end
end
```

## Related References

* [if](/reference/if)
* [for](/reference/for)
* [function](/reference/function)
* [local](/reference/local)
* [mouseDragged()](/reference/mouseDragged)

## Related Examples

* [10print](10print.md) - An implementaton of the famous 1980s one-liner maze-drawing program
* [Animation with Events](animation-and-variables-animation-with-events.md) - Pause and resume animation.
* [Basic Pong](basic-pong.md) - A simple program demonstrating a basic implementation of pong with enemy AI player
* [Minimum Spanning Tree](min-span-tree.md) - An example of implmenting Prim's algorithm for finding the shortest lengths to connect all randomly placed dots
* [Walking lines](walking-lines.md) - Visualizes randomly drawn lines bouncing around a box with their intersecting points highlighted

