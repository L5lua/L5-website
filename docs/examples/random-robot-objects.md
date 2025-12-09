# Random Robot Objects

This object-oriented programming example program demonstrates two different Lua patterns - classes with metatables (Robot) and simple tables with methods (box). It consists of a Robot class definition and simple box object. 

The box object demonstrates a simpler object-oriented structure of a table with methods. Lua's power of [first-class functions](https://softwarepatternslexicon.com/lua/lua-programming-fundamentals/first-class-functions-and-closures/) is represented here.

A first-class function means they can be:

* Stored in tables (like in the `box` table)
* Assigned to variables (like `display = function(self) ... end`)
* Passed as arguments to other functions
* Returned from functions

The `box` object demonstrates this with `display` and `move` functions stored as values in the box, just like `x`, `y` and `size` are numbers.

The Robot demonstrates uses of [metatables](https://www.tutorialspoint.com/lua/lua_metatables.htm).

* `Robot.__index = Robot` sets up the metatable
* `setmetatable(robot, Robot)` links each instance to the Robot table
* This enables [method lookup](https://cyevgeniy.github.io/luadocs/02_basic_concepts/ch04.html) - when you call `robot:move()`, Lua looks in the Robot table to find the `move` function

Advanced ways to extend the program:

* add more robot behaviors - make robots change colors when they collide with each other
* score counter - count how many times the box teleports to robots
* different robot types - a FastRobot that moves twice as fast as the others
* mouse interaction - Create new robots at the mouse position when clicked
* Box trail - a line showing the box's history
* Chase - make robots chase the box
* power-ups - add collectible items that change robot speed, size or behavior
* animated sprites - multiple images to animate movement

![Random robots moving around the screen. One robot grabs the yellow box, but it is stolen again several times by other robots](/assets/examples/random-robot-objects.gif "Random robot objects roam around the screen. One robot grabs the yellow box, but it is again stolen several times by other robots.")

```lua
require("L5")

-- Note: The Robot class definition below could be moved to a separate file robot.lua
-- and then loaded with: local Robot = require("robot")

Robot = {}
Robot.__index = Robot -- Tells Lua to use Robot's metatable to find methods

-- Global vars
robots = {}  -- Table to hold all robot instances
robotImg = nil

function setup()
  size(800, 600)
  windowTitle("Robots OOP example")
  robotImg = loadImage("assets/robot.png")
  imageMode(CENTER)
  rectMode(CENTER)
  strokeWeight(3)
  fill("gold")
  stroke("goldenrod")
  
  -- Initialize box position
  box.x = random(width)
  box.y = random(height)
  
  -- Create 10 robots
  for i = 1, 10 do
    table.insert(robots, Robot:new())
  end
end

function draw()
  background("lightblue")
  
  -- Update and draw box
  box:move()
  box:display()
  
  -- Update and draw all robots
  for i = 1, #robots do
    robots[i]:move()
    robots[i]:display()
  end
end

-- Robot class definition
function Robot:new(x, y, w, h)
  local robot = {
    x = x or random(width), 
    y = y or random(height), 
    w = w or 70, 
    h = h or 70,
    xspeed = random(-2, 2), 
    yspeed = random(-2, 2)
  }
  setmetatable(robot, Robot)  -- Links the instance to Robot class
  return robot
end

function Robot:move()
  self.x = self.x + self.xspeed 
  self.y = self.y + self.yspeed
  
  -- Bounce off walls
  if self.y > height or self.y < 0 then 
    self.yspeed = self.yspeed * -1 
  end
  if self.x > width or self.x < 0 then 
    self.xspeed = self.xspeed * -1 
  end
end

function Robot:display()
  image(robotImg, self.x, self.y, self.w, self.h)
end

-- Box object using simple table with methods
-- Demonstrates first-class functions stored as table values
box = {
  x = nil,  -- Initialized in setup() after random() is seeded
  y = nil,
  size = 40,
  
  display = function(self)
    square(self.x, self.y, self.size)
  end,
  
  move = function(self)
    -- Teleport to nearest robot if close enough
    for i = 1, #robots do
      if dist(self.x, self.y, robots[i].x, robots[i].y) < self.size then
        self.x = robots[i].x    
        self.y = robots[i].y
        break
      end
    end
  end
}
```

## Related References

* [for](/reference/for)
* [imageMode()](/reference/imageMode)
* [loadImage()](/reference/loadImage)
* [rectMode()](/reference/rectMode)
* [table](/reference/table) 
* [random()](/reference/random)

