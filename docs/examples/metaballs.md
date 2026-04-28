# Metaballs

Metaballs are *blobby objects* that meld together when they come into close proximity, appearing organically shaped. It is also reminiscent of cellular mitosis. 

When running the example, try pressing the arrow keys right or left to change the threshold of cohesion, or up and down arrow keys to alter the amount of (invisible) balls that make up the metaballs.

*Metaballs was contributed by Tomasz Stecko.*

![Organic metaballs bounce around the screen in a screensaver effect](/assets/examples/metaballs.gif)

```lua
require("L5")

dmin=0
dmax=800

function setup()
  size(dmax, dmax)
  windowTitle("lava lamp")
end

-- invisible balls that bounce around (flat velocity)
Ball={}
  function Ball:new()
      data={
      vx=math.random(1,3)*-1^math.random(1,2), vy=math.random(1,3)*-1^math.random(1,2),
      x=math.random(dmin,dmax), y=math.random(dmin,dmax),
      r=math.random(60,120)
      }
      setmetatable(data, self)
      self.__index = self
      return data
  end

  -- screensaver style bouncing around the edges
  function Ball:move()
    self.x=self.x+self.vx
    self.y=self.y+self.vy
    if self.x<dmin then self.x=dmin self.vx=-1*self.vx end
    if self.x>dmax then self.x=dmax self.vx=-1*self.vx end
    if self.y<dmin then self.y=dmin self.vy=-1*self.vy end
    if self.y>dmax then self.y=dmax self.vy=-1*self.vy end
  end

-- initialize some balls
function get_balls(n_balls)
  local balls={}
  for i = 1, n_balls do
      balls[i] = Ball:new()
  end
  return balls
end

-- tweak the behavior of balls
threshold=2.5
n_balls=10
balls=get_balls(n_balls)

-- point grid to calculate balls contribution to effect
grid={}
n=1
g_size=10
g_steps=dmax/g_size
for i=0,g_steps do
  for j=0,g_steps do
    grid[n]={x=i*g_size,y=j*g_size,v=0}
    n=n+1
  end
end

function draw()
  -- draw background
  background(0,0,0)
   -- move invisible balls
  for i=1, #balls do balls[i]:move() end

  -- calculate value of every dot in the grid
  for i=1, #grid do
      v1=0
      g=grid[i]
      
      -- every ball contributes
      for i=1,#balls do
        b=balls[i]
        v2=(b.r*b.r)/((g.x-b.x)*(g.x-b.x)+(g.y-b.y)*(g.y-b.y))
        v1=v1+v2
      end

      grid[i].v=v1
  end

  -- draw dots when they reach threshold
  for i=1, #grid do  
      if grid[i].v>=threshold then
          fill(color(114, 222, 194))
          noStroke()
          circle(grid[i].x,grid[i].y,10)
      end
  end
end

-- press arrow keys to mess with metaball count and 'physics'
function keyPressed() 
  if key == 'left' and threshold-0.5>=0 then threshold=threshold-0.5 end
  if key == 'right' and threshold+0.5<=4 then threshold=threshold+0.5 end

  if key == 'down' and n_balls-1>=2 then
      n_balls = n_balls-1
      balls=get_balls(n_balls)
  end

  if key == 'up' and n_balls+1<=20 then
      n_balls = n_balls+1
      balls=get_balls(n_balls)
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

