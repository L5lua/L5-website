## STRUCTURE

## Shape

### 2D Primitives

* [arc()](arc.md)
* [ellipse()](ellipse.md)
* [circle()](circle.md)
* [line()](line.md)
* [point()](point.md)
* [quad()](quad.md)
* [rect()](rect.md)
* [square()](square.md)
* [triangle()](triangle.md)

### Attributes

* [ellipseMode()](ellipseMode.md)
* [noSmooth()](noSmooth.md)
* [rectMode()](rectMode.md)
* [smooth()](smooth.md)
* [strokeJoin()](strokeJoin.md)
* [strokeWeight()](strokeWeight.md)

### Curves

* [bezier()](bezier.md)

## UNFINISHED PAGES

* {} (curly braces - defines a table for arrays, classes, objects, dictionaries, data and more)
* [] (access items from an ordered table aka "array")
* -- (comment)
* --[[ (multi-line comment) ]]--
* = (assign global variable)
* local (assign local variable)
* ==
* nil
* true
* false
* setup()
* draw()
* for i=1,5 do end
* loop
* noLoop()
* isLooping() -- equals true or false
* exit() (quits/stops/exits the program)
* redraw() (executes draw one time)
* windowTitle() 
* function (used to define a new user-defined function)

## Control

### Conditionals

* break (finish a loop that contains it)
* if
* then
* end
* elseif

### Relational Operators

* == (equality)
* ~= (inequality)

### Iteration

* for (runs a set number of times)
* while do (runs while true, checks before executing)
* repeat until (loops but checks condition at end. executes at least once)

### Logical Operators

* and 
* or 
* not 

## Environment
* size()
* print()
* deltaTime
* describe() --implementing as text to console, takes string input, should be in setup
* displayDensity()
* displayHeight 
* displayWidth 
* focused --boolean var
* frameCount
* frameRate()
* fullscreen() --returns true if in fullscreen, false otherwise. if passed true, turns on fullscreen, or turns off if passed false. equivalent to p5.js implementation
* width (width of canvas in pixels)
* height (height of canvas in pixels)
* resizeWindow() (function that runs when window is resized)

## I/O

### Input
* loadStrings() --takes filename as arg, returns table
* loadTable() --takes 1 or 2 arguments: filename, optional "header" string if header in csv or tsv present. Detects suffix (csv, tsv or lua) and processes accordingly. Saves to a table.

### Output
* saveStrings() --takes table and output filename as arguments
* saveTable() --takes table and filename as arguments, and optional format "csv","tsv" or "lua". Auto-selects output based on filename suffix if third argument empty.

### Time and Date
* millis()
* day()
* month()
* year()

## Events

### Keyboard

* key
* keyIsDown() --not in Processing
* keyIsPressed --boolean, called keyPressed in Processing
* keyPressed()
* keyReleased()
* keyTyped()

### Mouse

* mouseButton --A variable that returns which mouse button was last pressed: LEFT, RIGHT or CENTER
* mouseClicked() --called once after a mouse button pressed and released
* mouseDragged() -- called while mouse moves and a mouse button is pressed
* mouseIsPressed --boolean, called mousePressed in Processing
* mouseMoved() --called when mouse moved, no button pressed
* mousePressed() --called once after mouse button pressed
* mouseReleased() --called once when a mouse button released
* mouseWheel() --runs once while wheel is moving if passed x,y then can return change of -1 or 1 for x (left or right), -1 or 1 for y (up or down)
* mouseX --horizontal coordinate of mouse
* mouseY --vertical coordinate of mouse
* movedX --mouseX-pmouseX, not in Processing
* movedY --mouseY-pmouseY, not in Processing
* pmouseX --mouseX in previous frame
* pmouseY --mouseY in previous frame

### Touch -- Not under development. Could be added later if interest.

## SHAPE

### 2D Primitives

* arc()
* circle()
* ellipse()
* line()
* point()
* rect()
* square()
* triangle()

### Attributes

* ellipseMode()
* rectMode()
* strokeCap() --default: ROUND, also SQUARE. no EXTEND.
* strokeWeight()
* noSmooth()
* smooth()
* strokeJoin() --MITER, BEVEL, NONE. No ROUND. MITER is default. Also affected by strokeCap (because of Love2d's internals)

### Curves
* curve()


### Creating & Reading
* alpha() (gets alpha aka 4th value of a color)
* blue() (gets blue aka 3rd value of a color)
* red() (gets red value of a color)
* color() (creates a color object) --G, G,A R,G,B  R,G,B,A or html color name. affected by colormode.
* green() (gets the green value of a color)
* hue() - IN-PROCESS (gets the hue value of a color)

### Setting
* background() --G, G,A R,G,B  R,G,B,A or html color name. affected by colorMode.
* clear()
* HSB --mode, a constant
* HSL --mode, a constant
* colorMode() --default: RGB. alternately: HSB, HSL. optional second val sets max color values.
* fill() - G, G,A R,G,B  R,G,B,A or html color name. affected by colorMode.
* noFill()
* noStroke()
* stroke() --G, G,A R,G,B  R,G,B,A or html color name. affected by colorMode.

### Transform
* push() (saves previous drawing style settings)
* pop() (restores previous drawing style settings)
* translate()
* rotate()
* scale()

## Constants
* HALF_PI (1.57079...)
* PI (3.14159...)
* QUARTER_PI (0.78539...)
* TAU (6.28318...)
* TWO_PI (6.28318...)

### Math
* random() --takes 1 or 2 arguments. if a table name is given, returns a random value from the table
* randomSeed()
* noise() --1, 2 or 3 dimensional Simplex noise generation
* abs()
* ceil()
* floor()
* round()
* constrain()
* map()
* dist()
* max()
* min()

### Trigonometry
* angleMode()
* degrees()
* radians()
* sin()
* cos()
* tan()

## Typography
* loadFont() --create new font
* text() --display text, at x,y
* textFont() --change to loaded font
* textWidth() --returns width of text
* textHeight() -- returns height of text
* textAlign() --first parameter sets horizontal alignment LEFT (default), CENTER, or RIGHT. Optional second parameter sets TOP, CENTER or BOTTOM vertical alignment.
* textSize()

### Loading and Displaying
* image()
* imageMode()
* loadImage()
* noTint()
* tint()
* save()
* cursor() (see https://www.love2d.org/wiki/love.mouse.setCursor )
* noCursor()

### Pixels

* filter() --implemented basic implementation with shaders
