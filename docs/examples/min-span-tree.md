# Minimum Spanning Tree

A minimum spanning tree (MST) is an example of a visualization of [Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm) for finding the shortest lengths connecting all randomly placed dots. All of the points are [connected](https://visualgo.net/en/mst) in a tree path with the shortest total edge lengths, with only one path (no 'cycle').

![30 points connected with the shortest total length of lines, forming a tree structure](/assets/examples/min-span-tree.webp "30 points connected with the shortest total length of lines, forming a tree structure")

## How Prim's Algorithm Works

1. Start with any vertex (point) in the graph
2. Find the shortest edge connecting a visited vertex to an unvisited vertex
3. Add that edge to the tree and mark the new vertex as visited
4. Repeat steps 2-3 until all vertices are visited

This algorithm takes a *greedy* approach, always choosing the shortest available edge, which guarantees finding the minimum spanning tree.

## Code

```lua
require("L5")
-- Minimum Spanning Tree using Prim's algorithm
points = {}
numPoints = 30 -- how many points to draw
tree = {}  -- Edges in the MST
visited = {}

function setup()
  size(800, 600)
  windowTitle("Minimum Spanning Tree")
  background(255)
  
  -- Generate random points
  for i = 1, numPoints do
    points[i] = {
      x = random(0, width),
      y = random(0, height)
    }
  end
  
  -- Build MST using Prim's algorithm
  buildMST()

  describe("30 points connected with the shortest total length of lines, forming a tree structure.")
end

function buildMST()
  -- Start with first point
  visited[1] = true
  local numVisited = 1
  
  -- Build tree by adding edges one at a time
  while numVisited < numPoints do
    local minDist = math.huge --equivalent to infinity in Lua. alternatively, use a large number like 999999
    local minEdge = nil
    
    -- Find shortest edge connecting visited to unvisited
    for i = 1, numPoints do
      if visited[i] then
        for j = 1, numPoints do
          if not visited[j] then
            local d = dist(points[i].x, points[i].y, points[j].x, points[j].y)
            if d < minDist then
              minDist = d
              minEdge = {from = i, to = j, dist = d}
            end
          end
        end
      end
    end
    
    -- Add edge to tree
    if minEdge then
      table.insert(tree, minEdge)
      visited[minEdge.to] = true
      numVisited = numVisited + 1
    else
      break  -- No more edges found
    end
  end
end

function draw()
  background(255)
  
  -- Draw all edges in the MST
  stroke(100, 100, 255)
  strokeWeight(2)
  for _, edge in ipairs(tree) do
    local p1 = points[edge.from]
    local p2 = points[edge.to]
    line(p1.x, p1.y, p2.x, p2.y)
  end
  
  -- Draw all points
  noStroke()
  fill(50)
  for _, point in ipairs(points) do
    circle(point.x, point.y, 8)
  end
end
```

## More things to try

* You can change `numPoints` to see different densities
* Modify the point generation to use a grid pattern instead of random
* Color edges based on their length
* Animate the MST construction by adding edges one at a time

## Related References

* [if](/reference/if)
* [line()](/reference/line)
* [dist()](/reference/dist)
* [draw()](/reference/draw)
* [random()](/reference/random)
* [sqrt()](/reference/sqrt)
* [table](/reference/table)

## Related Examples

* [10print](10print.md) - An implementaton of the famous 1980s one-liner maze-drawing program
* [Animation with Events](animation-and-variables-animation-with-events.md) - Pause and resume animation.
* [Basic Pong](basic-pong.md) - A simple program demonstrating a basic implementation of pong with enemy AI player
* [Conway's Game of Life](conways-life.md) - An implementation of the zero-player game and simulation formulated by mathematician John Conway
* [Walking lines](walking-lines.md) - Visualizes randomly drawn lines bouncing around a box with their intersecting points highlighted

