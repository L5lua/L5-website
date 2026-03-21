# Computational Poetry with L5

## Overview

This is a beginner-level tutorial for participants in the [CCFest 2026](https://ccfest.rocks) online conference.

In this tutorial, you'll learn how to create generative visual poetry using L5, a creative coding library based on p5.js and Processing, but written in Lua. We'll explore how code can arrange words and images to create dynamic compositions.

**Time Required:** 60 minutes

**Prerequisites:** Previous knowledge working with p5.js or Processing is recommended.

## Learning Objectives

By the end of this tutorial, students should be able to:

- Understand the basics of L5 and how it relates to p5.js/Processing
- Draw text and shapes to the screen using code
- Create and manipulate arrays of strings
- Use randomness to create generative compositions
- Build a grid-based layout system
- Combine text, randomness, and interaction to create computational poetry

## What is L5?

L5 is a creative coding library that brings the simplicity and approachability of p5.js and Processing to the Lua programming language. If you've used p5.js or Processing before, you'll find L5 familiar - it uses the same basic structure with `setup()` and `draw()` functions, and similar function names for drawing shapes, working with color, and handling interaction.

L5 uses Lua syntax, which is known for being clean and beginner-friendly. Lua uses simple keywords like `function`, `end`, and `for` that make code easy to read.

L5 is heavily inspired by [permacomputing](https://permacomputing.net/), a growing movement responding to environmental and social conditions in computing. L5 is designed to be able to work on a wide variety of computers, to help prevent issues like needing to constantly upgrade, to work against "planned obsolescence", to consider constraints on consumption. The goal is for L5 to be a convivial tool that you can continue to use for years, with programs continuing to work long into the future.

While this is the goal, L5 is *alpha* software. The first version was released in December 2025. It has bugs, and does not fully implement all of Processing/p5. A number of people are working on the language to improve it.

## Installation

To get started with L5, you'll need to set it up on your computer:

- **Mac users:** [L5 Setup for Mac](https://l5lua.org/download/install-mac)
- **Windows users:** [L5 Setup for Windows](https://l5lua.org/download/install-windows)

Next you need a code editor to write your code. If you already use a code editor, use the one you're familiar with. If you have never used a code editor on your own computer, you can pick one like Visual Studio Code, SublimeText, or a dedicated Lua IDE like ZeroBrane Studio. 
If you don't have any IDE installed on your computer you can even use your built-in plaintext editor TextEdit on macOS in plain text mode, or Notepad on Windows. But keep in mind they are barebones environments without additional features like syntax highlighting that make it easier to write code.

Once you have 1) Love2d installed 2) L5-Starter downloaded and unzipped 3) and you've tested launching Love2d and making sure you've given your computer approval to launch it, then you're ready to go.

To test it all out: Try dragging **the folder** L5-Starter on top of the Love2d application file. It should launch and you should see a gold window appear. If it doesn't launch, you either didn't drag the folder or you need to give your computer permission to run an *un-signed application*, meaning that the developer didn't pay Apple to pre-approve this software (on macOS), or that you're giving Windows permission to run this downloaded program.

## Getting Started: Your First L5 Sketch

Every L5 sketch starts with requiring the L5 library file, which you'll see in the first line. We can start by looking at the L5-Starter sketch. Inside the folder, open up the *main.lua* file.

You can open it in your favorite code editor like Visual Studio Code or SublimeText, or use the built-in Notepad on Windows or TextEdit on macOS.

```lua
require("L5")

function setup()
  size(400, 400)

  -- Set the program title
  windowTitle("Basic sketch")

  describe('Draws a yellow background')
end

function draw()
  -- Fills the background with the color yellow
  background(255, 215, 0)
end
```

The `setup()` function runs once when your program starts. This is where we'll put code that only needs to happen at the beginning. `windowTitle()` specifies the nae for the title bar. `describe()` is an optional function for a text description of your program.

The lines beginning with `--` are comments: notes to yourself or anyone reading your code, but they will be ignored by the compiler when you ask it to run your program.

## Step 1: Changing the Background

Run your sketch by dragging and dropping the L5-starter folder on top of the Love application. You should see a window open and a golden yellow background. 

Now let's go back to our code. Let's start by changing the background color. Modify the background inside your `draw()` function. You can use RGB values:
Try changing `'gold'` to other colors like `'lightblue'`, `'pink'`, or `'lavender'`. You can use any of the [HTML Color Names](https://www.w3schools.com/colors/colors_names.asp), or RGB numbers like `background(255, 0, 255)` or hexadecimal: `background('#7FFFD4')`.


```lua
background('purple')
```

## Step 2: Drawing Basic Shapes

L5 can draw shapes just like p5.js. Let's add a circle:

Add this code inside your draw:

```lua
  fill('gold')
  circle(100, 100, 50)
```

So your draw() function should now look like:

```lua
function draw()
  -- Fills the background with the color yellow
  fill('gold')
  circle(100, 100, 50)
end
```

The `fill()` function sets the color for shapes, and `circle(x, y, diameter)` draws a circle at position (100, 100) with a diameter of 50 pixels.

Try drawing other shapes:
- `rect(x, y, width, height)` - draws a rectangle
- `ellipse(x, y, width, height)` - draws an ellipse
- `line(x1, y1, x2, y2)` - draws a line

If you have any previous experience wih Processing or p5.js you should feel right at home.

## Step 3: Drawing Text on Screen

**Let's remove our older code and replace it with this small program, where everything is written inside just the setup() function:**

We'll draw some text instead of shapes:

```lua
require('L5')

function setup()
  background('mintcream')
  fill('lawngreen')
  textSize(32)
  text('hello', 100, 100)
end
```

The `text()` function draws text at a specific position. The first parameter is the string to display, and the next two are the x and y coordinates.

Try changing:
- The word in quotes
- The numbers (position)
- The `textSize()` value
- Add `textAlign(CENTER, CENTER)` before the text to change alignment

## Step 4: Creating an Array of Strings

Instead of just one word, let's create a collection of words we can choose from. In Lua, we use curly braces `{}` to create arrays (called "tables" in Lua):

```lua
require('L5')

words = {"eye", "nose", "mouth", "ear", "brain"}

function setup()
  background('white')
  fill('black')
  textSize(32)
  text(words[1], 100, 100)
end
```

The array `words` holds multiple strings. We can access them using square brackets with a number. **Important:** Lua arrays start at index 1, not 0!

Try displaying different words by changing `words[1]` to `words[2]`, `words[3]`, etc.

## Step 5: Picking a Random String

Instead of always showing the same word, let's pick one randomly:

```lua
require('L5')

words = {"eye", "nose", "mouth", "ear", "brain"}

function setup()
  background('white')
  fill('black')
  textSize(32)
  text(random(words), 100, 100)
end
```

The `random()` function can pick a random item from an array when you pass it an array. Run your sketch multiple times - you should see different words!

Question: What would happen if this code was inside *draw()* instead of *setup()*, and how could you fix it?

## Step 6: Creating a Grid

Now we'll use loops to create a grid of positions where words could appear. We'll use two variables to control the grid spacing:

```lua
require('L5')

words = {"eye", "nose", "mouth", "ear", "brain"}

function setup()
  background('white')
  blockW = width/10
  blockH = height/10
  
  fill('black')
  textSize(24)
  
  for y=1,height,blockH do
    for x=1,width,blockW do
      text(random(words), x, y)
    end
  end
end
```

Let's break down the loop:

- `for y=1,height,blockH do` means "start at 1, go up to the canvas height, increasing by blockH each time"
- The nested loop does the same for x
- `width` and `height` are built-in variables that give you the canvas dimensions

This creates a grid of words across your entire canvas.

## Step 7: Randomly Showing or Hiding Words

Right now we're showing a word at every grid position. Let's make it more interesting by only sometimes showing a word:

```lua
require('L5')

words = {"eye", "nose", "mouth", "ear", "brain", "arm", "leg", "head", "foot"}

function setup()
  background('white')
  blockW = width/10
  blockH = height/10
  
  fill('black')
  textAlign(RIGHT, BOTTOM)
  textSize(24)
  
  for y=1,height,blockH do
    for x=1,width,blockW do
      if random() > 0.9 then
        text(random(words), x, y)
      end
    end
  end
end
```

The `if random() > 0.9 then` line checks if a random number (between 0 and 1) is greater than 0.9. This means only about 10% of the grid positions will show a word.

Try changing `0.9` to different values:
- `0.5` = 50% of positions show words
- `0.7` = 30% of positions show words
- `0.95` = only 5% of positions show words

## Step 8: Adding Interaction

Let's make it so clicking the mouse regenerates the composition:

```lua
require('L5')

words = {"eye", "nose", "mouth", "ear", "brain", "arm", "leg", "head", "foot"}

function setup()
  background('white')
  blockW = width/10
  blockH = height/10
  
  fill('black')
  textAlign(RIGHT, BOTTOM)
  textSize(24)
  
  for y=1,height,blockH do
    for x=1,width,blockW do
      if random() > 0.9 then
        text(random(words), x, y)
      end
    end
  end
end

function mousePressed()
  setup()
end
```

The `mousePressed()` function runs whenever you click the mouse. By calling `setup()` again, we redraw everything with new random positions!

## Making It Your Own

Now that you have the basic structure, try customizing it:

1. **Change the words:** Replace the body parts with your own theme
   - Emotions: "joy", "anger", "fear", "sadness"
   - Colors: "crimson", "azure", "golden", "silver"
   - Use words from a poem you wrote
   
2. **Adjust the density:** Change the `0.9` value to make it more or less crowded

3. **Experiment with text alignment:** Try `LEFT`, `RIGHT`, `CENTER` for horizontal and `TOP`, `CENTER`, `BOTTOM` for vertical

4. **Change the grid:** Make `blockW` and `blockH` smaller for a finer grid, or larger for bigger gaps

5. **Add color:** Try `fill('red')` or use RGB values like `fill(255, 0, 0)`

## Ways to extend 

* Incorporate animation in `draw()` to change your sketch over time

```lua
function draw()
  x = millis() / 5
  text(specialName, x, 200) -- Text will move to the right
end
```

* Make your composition respond to the mouse position

```lua
-- Text size changes with mouse X position
--textSize(mouseX / 10)  -- Don't run this yet! 
```

This can cause freezing if mouseX is 0 at the beginning of the sketch, so we can constrain it to have a minimum value.

```lua
textSize(constrain(mouseX,10,width) / 10)
```

Now the size will change but never get smaller than 10.

Or only show words near the mouse:

```lua
if dist(x, y, mouseX, mouseY) < 100 then
  text(random(words), x, y)
end
```

### Adding Images

L5 can also work with images. First, load an image in `setup()`:

```lua
img = loadImage('path/to/your/image.jpg')
```

Then draw it in your grid instead of (or alongside) text:

```lua
if random() > 0.9 then
  if random() > 0.5 then
    text(random(words), x, y)
  else
    image(img, x, y, 50, 50)
  end
end
```

### Rotating Text

Add rotation to make text appear at different angles:

```lua
push()
translate(x, y)
rotate(random() * TWO_PI)
text(random(words), 0, 0)
pop()
```

## Vocabulary

- **Generative:** Art or designs created by following a set of rules or algorithms, often involving randomness
- **Computational Poetry:** Using code and algorithms to create, arrange, or manipulate text as a form of poetic expression
- **Array/Table:** A collection of values stored together. In most languages this is called an array. In Lua, we say it is an *ordered* table. Each item in the table has a number (an order), starting at 1.
- **Parameter:** A value you pass into a function to customize how it works
- **Random:** Unpredictable; choosing something without a pattern
- **Iteration:** Repeating a process multiple times (like in a loop)

## Going Further

- **Artists to explore:** [Allison Parrish](https://www.decontextualize.com/), [Nick Montfort](https://nickm.com/), [Lillian-Yvonne Bertram](https://www.lillianyvonnebertram.com/)
- **Online computational poetry:** [Taper](https://taper.badquar.to/), [The HTML Review](https://thehtml.review), [Random Walk](https://randomwalk.club/)

## Resources

- [L5 Documentation](https://l5lua.org/reference)
- [More L5 Tutorials](https://l5lua.org/tutorials)
- [L5 Examples](https://l5lua.org/examples)

## Share Your Work!

Created something interesting? Need help polishing your code? Check out the new [L5 category](https://discourse.processing.org/c/l5/29) on the Processing Discourse forum. 

---

*This tutorial was created for CCFest and is available under a Creative Commons Attribution 4.0 International License.*
