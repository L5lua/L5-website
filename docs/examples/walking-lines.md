# Walking Lines

The *Walking Lines* program visualizes randomly drawn lines bouncing around within a defined box, focusing on the intersection points that emerge from their interactions.

*Walking Lines was contributed by [Orllewin](https://orllewin.github.io/).*

![Intersecting lines bounce around the screen, their points of intersection highlighted with larger circles](/assets/examples/walking-lines.gif)

```lua
require("L5")

local lines = {}
local lineCount = 10
local velocity = 3

function setup()
  windowTitle('Walking Lines')
  size(680, 680)
  
  frameRate(30)
  
  for i = 1 , lineCount do
    local walkingLine = {}
    walkingLine.x1 = random(width)
    walkingLine.y1 = random(height)
    walkingLine.x2 = random(width)
    walkingLine.y2 = random(height)

    walkingLine.x1Direction = 1
    if(random() > 0.5) then
      walkingLine.x1Direction = -1
    end 
    walkingLine.y1Direction = 1
    if(random() > 0.5) then
      walkingLine.y1Direction = -1
    end
    walkingLine.x2Direction = 1
    if(random() > 0.5) then
      walkingLine.x2Direction = -1
    end
    walkingLine.y2Direction = 1
    if(random() > 0.5) then
      walkingLine.y2Direction = -1
    end
    table.insert(lines, walkingLine)
  end
  
  stroke(255)
  
  describe('Intersecting lines bounce around the screen, their points of intersection highlighted with larger circles')
end 

function draw()
  background(0)
  
  for i = 1, lineCount do
    
    local walkingLine = lines[i]
    
    -- update
    walkingLine.x1 = walkingLine.x1 + (velocity * walkingLine.x1Direction)
    walkingLine.y1 = walkingLine.y1 + (velocity * walkingLine.y1Direction)
    walkingLine.x2 = walkingLine.x2 + (velocity * walkingLine.x2Direction)
    walkingLine.y2 = walkingLine.y2 + (velocity * walkingLine.y2Direction)
    
    -- check bounds
    if(walkingLine.x1 > width or walkingLine.x1 < 0)then
      walkingLine.x1Direction = walkingLine.x1Direction * -1
    end
    
    if(walkingLine.y1 > height or walkingLine.y1 < 0)then
      walkingLine.y1Direction = walkingLine.y1Direction * -1
    end
    
    if(walkingLine.x2 > width or walkingLine.x2 < 0)then
      walkingLine.x2Direction = walkingLine.x2Direction * -1
    end
    
    if(walkingLine.y2 > height or walkingLine.y2 < 0)then
      walkingLine.y2Direction = walkingLine.y2Direction * -1
    end
    
    -- draw intersections
    for j = 1, lineCount do
      if(j ~= i)then
        local otherWalkingLine = lines[j]
        local intersectX, intersectY = intersectPointLines(walkingLine, otherWalkingLine)
        if(intersectX ~= -1)then
          circle(intersectX, intersectY, 10)
        end
      end
      
    end
    
    --draw
    line(walkingLine.x1, walkingLine.y1, walkingLine.x2, walkingLine.y2)    
  end
end

function intersectPointLines(a, b)
  return intersectPoint(a.x1, a.y1, a.x2, a.y2, b.x1, b.y1, b.x2, b.y2)
end

function intersectPoint(aX1, aY1, aX2, aY2, bX1, bY1, bX2, bY2)
  local a1 = aY2 - aY1
  local b1 = aX1 - aX2
  local c1 = a1 * aX1 + b1 * aY1
  
  local a2 = bY2 - bY1
  local b2 = bX1 - bX2
  local c2 = a2 * bX1 + b2 * bY1
  
  local delta = a1 * b2 - a2 * b1
  
  local iX = (b2 * c1 - b1 * c2) / delta
  local iY = (a1 * c2 - a2 * c1) / delta
  
  if(min(aX1, aX2) < iX and max(aX1, aX2) > iX and min(bX1, bX2) < iX and max(bX1, bX2) > iX) then
    return iX, iY
  else
    return -1, -1
  end
end
```

## Related References

* [if](/reference/if)
* [line()](/reference/line)
* [draw()](/reference/draw)
* [frameRate()](/reference/frameRate)
* [random()](/reference/random)

## Related Examples

* [10print](10print.md) - An implementation of the classic maze-drawing algorithm
* [Animation with Events](animation-and-variables-animation-with-events.md) - Pause and resume animation.
* [Basic Pong](basic-pong.md) - A simple program demonstrating a basic implementation of pong with enemy AI player
* [Conditions](animation-and-variables-conditions.md) - Use if and else statements to make decisions while your sketch runs.
* [Copy Image Data](imported-media-copy-image-data.md) - Paint from an image file onto the canvas.
* [Conway's Game Of Life](conways-life.md) - An implementation of the zero-player game and simulation formulated by mathematician John Conway
* [Minimum Spanning Tree](min-span-tree.md) - An example of implementing Prim's algorithm for finding the shortest lengths to connect all randomly placed dots

