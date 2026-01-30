# Data Structure Garden

By Portia Morrell, Jaleesa Trapp, Kate Maschmeyer. Adapted to L5 by Lee Tusman.

---

*Note: If you are running your programs by dragging their project folder onto the Love application, be sure to add the `printToScreen()` function within your setup() to be able to see the output of `print()` commands in your program window.*

![Data Garden 12](/assets/tutorials/data-garden12.gif)

In this tutorial, you will use L5 to simulate an interactive flower garden. In this project, your digital canvas will come to life with 20 randomly generated flowers, each a different color and size. Users can also add diversity to the garden by clicking on the canvas to add new, unique flowers. Each flower is programmed with a wilting animation. This animation causes the flowers to slowly shrink and vanish, much like the natural cycle of a flower’s life.

In this tutorial, you will:

* Explore data structures like objects (built from Lua's [table](/reference/table) data structure) by defining, creating, and using your own objects.
* Explore and use methods to perform actions on built-in objects like arrays (also built out of Lua tables!).
* Use iteration with for loops to manage multiple objects at once.

## Prerequisites

Before you begin, you should be able to:

* Add and customize shapes and color on the canvas using L5
* Declare, initialize, use, and update custom variables, and functions with parameters and return values
* Add animation on the canvas
* Comment code and address error messages
* Create and use custom functions
* Understand how to use for loops to manage repetitive tasks

In this tutorial, you will learn how to:

* get a basic understanding of Lua tables
* define objects
* create and use custom functions to update and draw objects
* manage multiple objects using arrays 

Let’s begin!

* To get started, create a new folder to hold your project and give it a name like `data-garden`. Place a copy of the `L5.lua` library in the folder. Finally, create a new blank code document in the code editor of your choice. Make sure to write `require("L5")` at the top of the text file, and save the document under the name `main.lua`. The rest of our code will go in this file.

## Objects 

We have learned that variables can store one value at a time (a number, string, or Boolean). Arrays can store multiple values in indices. 

**If you are new to Lua, it's important to understand that Lua uses the [table](/reference/table) data structure both to build arrays as well as objects.** 

Sometimes, however, we want to store several pieces of related data about one thing together. We can do this using objects, which bundle data together by pairing properties and values. In Lua we also use a table to build objects. Properties are special types of variables or names that are associated with an object. Each property stores a value. For example, if we wanted to create an object based on a flower, it could have properties that describe its location (x and y) and ASCII character symbol.  

## Step 1: Make your first object

Let’s start our flower garden by creating one flower. We can start by drawing it using an ASCII character, so we need data on the x-coordinate, the y-coordinate, and the character for our flower. We'll use a '@' symbol to represent our first flower

* Create a flower object by bundling the flower’s canvas coordinates with the character used to draw it. Let’s store the object in a variable named flower. Add this code above `setup()`: 

```lua
-- Flower Object
local flower = {
  x = 200,
  y = 100,
  char = '@' 
}

function setup()
  size(400, 400)
end
```

* Print your object to the console by adding the following line of code in `setup()`. Note that we loop through our table of key-value pairs using `pairs(tablename)`:

```lua
for i,val in pairs(flower) do
  print(i,val)
end
```

which returns the output:

```text
x	200
y	100
char	@
```

* Set the background to 'lightblue'

Your code should look like this:

![Data garden 1](/assets/tutorials/data-garden1.webp)

```lua
require("L5")

-- Flower Object
local flower = {
  x = 200,
  y = 100,
  char = '@' 
}

function setup()
  size(400, 400)
  
  -- Print object in console.
  for i,val in pairs(flower) do
    print(i,val)
  end
end

function draw()
  background('lightblue')
end
```

Try [running your code](https://l5lua.org/download/#running-your-program). You should see your flower object printed out to the console. 

Here’s the general syntax for defining an object:

```lua
-- Define an object
local objectName = {
  property1 = value1,
  property2 = value2,
  property3 = value3
}
```

The syntax for objects uses:

* curly braces (`{}`) to enclose a bundle of properties; 
* Properties can be names, such as the names of variables or functions, or they can be strings, or even other tables. When using spaces in property names, Lua requires square brackets to interpret them correctly. For example, I might create an object with a property for a 'first name' and a 'last name,' like this:

```lua
local ironMan = {
  ['first name'] = 'Tony',
  ['last name'] = 'Stark'
}
```

* If your property has no spaces, the quotes and brackets around the property name are optional, such as `first_name = 'Tony'`.
* an equal sign (`=`) to separate each property with specific values;
  * Values can be of any datatype, and can even be a function!
* commas (`,`) to separate each `[property] = value` pair

You can store objects by initializing new variables when you define them. In the code above, you declared a variable named flower. You then initialized the flower variable with an object whose properties represent a flower that can be drawn on the window.

To check the properties and values of an object, you printed the key value pairs from the table.

## Step 2: Use your object

You can access any value stored in object properties by using its square bracket name as shown above or its variable name, property name, and dot notation like so (as long as the property name doesn't have spaces in it or special characters, in which case you will need to use the square brackets syntax):

```lua
-- Access the object's property1 value with dot notation.
objectName.property1
```

* Use the [text()](/reference/text) function with flower object properties to place the flower on the canvas.
* We can specify a color for the text and place that before writing to the screen
  * In [draw()](/reference/draw), add the following code:

```lua
-- Fill shapes and text with a specified carnation pink color
fill('pink')
  
-- Display flower object.
text(flower.char, flower.x, flower.y)
```

* You can use [textSize()](/reference/textSize) before the text function to set the size of the flower.

```lua
-- Increase the text size
text(100)
```

Your code should look like this:

![Data garden 2](/assets/tutorials/data-garden2.webp)

```lua
require("L5")

-- Flower Object
local flower = {
  x = 200,
  y = 100,
  char = '@' 
}

function setup()
  size(400, 400)
end

function draw()
  background('lightblue')

  -- Increase the text size
  textSize(100)

  -- Fill shapes and text with a specified carnation pink color
  fill('pink')
  
  -- Display flower object
  text(flower.char, flower.x, flower.y)
end
```

To access values in the flower object, we use [dot notation](https://www.lua.org/pil/16.html), which uses the dot operator to access properties and values within objects.

In th ecode above, you accessed:

* the character for the flower with `flower.char` 
* the x-coordinate with `flower.x`
* the y-coordinate with `flower.y`

Since these values represent strings and numbers, they can be used in the [text()](/reference/text) function, similar to the way variable names are used to access the value they store.

Visit the L5 reference to learn more about [tables](/reference/table).

### Try this!

* Add a `size` property to the flower object.
* Replace the `textSize()` value with the `flower` object's `size`.

## Step 3: Define a `createFlower()` function

Now, let’s define a function that can display different flowers on the canvas. We will define a `createFlower()` function that will allow us to customize the flower objects we create. We want to make sure that we can change the x- and y-coordinates for different flowers. We also want to change their `size` and `color`. One way to do that is to add new properties to the flower object for size and color. In this project, we also want the flower to appear, then disappear after some time. To do this, we will also include a `lifespan` property for our flower object. 

We want our `createFlower()` to return information when it’s called, just like the built-in `text()` function returns text on the canvas. Therefore, we must specify a return value. Using return values is a great way to save information computed by the function in a variable or array. 

In this example, we will be using [random()](/reference/random) to create variety in our flowers when they’re drawn on the canvas. 

* Define the `createFlower()` function, which creates a random flower object. All values will be set randomly each time `createFlower()` is called.
  * Outside of [draw()](/reference/draw) and [setup()](/reference/setup), add the following function declaration:

```lua
-- Function that creates a random flower object.
function createFlower() 
  -- Define a flower object.
  local flower = {
    x = random(20, 380),
    y = random(20, 380),
    size = random(20, 75),
    lifespan = random(255, 300),
    color = color(random(255), random(255), random(255)),
  }
  -- Return the flower object.
  return flower
end
```

* Test the `createFlower()` function by using it to create a flower object, and store it in a variable called `myFlower`.
  * Add the following in the [draw()](/reference/draw) function:
  
```lua
-- Create flower object
local myFlower = createFlower()
```

Draw an [ellipse](/reference/ellipse) on the canvas using `myFlower` properties.
  * Add the following in the [draw()](/reference/draw) function:  

```lua
-- Use flower object properties to draw an ellipse.
fill(myFlower.color)
ellipse(myFlower.x, myFlower.y, myFlower.size)
```

* Slow down the rate at which each flower appears by changing the frame rate to one frame per second. In [setup()](/reference/setup), add: `frameRate(1)`.

Your code should look like this:

![Data garden 3](/assets/tutorials/data-garden3.gif)

```lua
require("L5")

function setup() 
  size(400, 400)
  frameRate(1)
end
function draw() 
  background("lightblue")

  -- Create flower object.
  local myFlower = createFlower()

  -- Use flower object properties to draw an ellipse.
  fill(myFlower.color)
  ellipse(myFlower.x, myFlower.y, myFlower.size)
end
function createFlower() 
  -- Define flower object.
  local flower = {
    x = random(20,380),
    y = random(20,380),
    size = random(20,75),
    lifespan = random(255,300),
    color = color(random(255), random(255), random(255)),
  }
  
  -- Return flower object.
  return flower
end
```

In the code above, you use `createFlower()` to create and return a new flower object with random values, then store the object in the variable `myFlower`. `myFlower` is used to access its property’s random values, which are used to draw an ellipse on the canvas. Each time [draw()](/reference/draw) runs, a new random flower object is created, and its properties are used to draw a new random ellipse on the canvas. 

Visit the L5 reference to learn more about [random()](/reference/random).

### Try this!

* Change the random range for the flower’s x and y location and size.
* Get creative with the color generation; maybe it’s shades of only blues, reds, or purples.

## Step 4: Define the `drawFlower()` function with a parameter

Now that we know that `createFlower()` creates and returns a new flower object, let’s define the `drawFlower()` function. Our `drawFlower()` function will receive a flower object as an argument and place it on the canvas. This will help make our code organized and manageable.

* Outside of all other functions, define the `drawFlower()` function with one parameter representing a flower object.

```lua
function drawFlower(flower)
end
```

* Inside the `drawFlower()` function, draw the attributes of a flower, including the petals and center of the flower. Remember to use the flower object properties for the `x` and `y` locations, `size`, and `color`. You can add the following code to the function body:

```lua
noStroke()
fill(flower.color)

-- Draw petals.
ellipse(flower.x, flower.y, flower.size / 2, flower.size);
ellipse(flower.x, flower.y, flower.size, flower.size / 2)

-- Draw a yellow center.
fill(255, 204, 0)
circle(flower.x, flower.y, flower.size / 2)
```

Next, we will test the `drawFlower()` function. Add the following to the [draw()](/reference/draw) function:

```lua
-- Testing drawFlower().
let flower1 = createFlower();
drawFlower(flower1)
```

Your code should look similar to this:

![Data garden 4](/assets/tutorials/data-garden4.gif)

```lua
require("L5")

function setup()
  size(400, 400)
  frameRate(1)
end

function draw()
  background("lightblue")

  -- Testing drawFlower().
  local flower1 = createFlower()
  drawFlower(flower1)
end

function createFlower()
  local flower = {
    x = random(20,380),
    y = random(20,380),
    size = random(20,75),
    lifespan = random(255,300),
    color = color(random(255), random(255), random(255))
  }
  return flower
end

function drawFlower(flower) 
  noStroke()
  fill(flower.color)

  -- Draw petals.
  ellipse(flower.x, flower.y, flower.size / 2, flower.size)
  ellipse(flower.x, flower.y, flower.size, flower.size / 2)

  -- Draw a yellow center.
  fill(255, 204, 0)
  circle(flower.x, flower.y, flower.size / 2)
end
```

In the code above, `createFlower()` is used to create and return a random flower that is stored in `flower1`. The random flower (`flower1`) is then passed into `drawFlower()`, which accesses the flower object properties to draw a flower on the canvas. This process occurs each time the [draw()](/reference/draw) function runs, so random flowers appear and disappear on the canvas. 

### Try this!

Change and modify the flower drawing using other 2D shapes:

* [ellipse()](/reference/ellipse)
* [square()](/reference/square)
* [quad()](/reference/quad)
* [triangle()](/reference/triangle)
* [line()](/reference/line)
* [point()](/reference/point)
* [arc()](/reference/point)

## Step 5: Learn to use arrays

Before we move on to making our garden of flowers by using an array, let’s better understand how arrays work with a few simple examples. Arrays are objects that can store multiple values in one variable name. Each value is stored in an element with a specific location known as its index. **The index of the first element in any array in Lua is 1.**

**Tables are used for arrays and objects in Lua.**

Example of building an array with a Lua table:

```lua
-- This is an ordered table, AKA a list or array
local fruits = {'apple', 'banana', 'cherry', 'dragon fruit', 'elderberry', 'fig', 'grape', 'honeydew'}
```

Each item in this array can be accessed with a number, beginning at the index 1.

```lua
print(fruits[1]) -- 'apple'
print(fruits[3]) -- 'cherry'
```

Prepending a `#` to a table gives us the length (total elements) in an array. So we can get the very last item from the list very easily, no matter how many items are in that array.

```
print(fruits[#fruits]) -- 'honeydew'
```

### Example 1: Creating and drawing an array of names

![Data garden 5](/assets/tutorials/data-garden5.webp)

```lua
require("L5")

-- Create an array flowers
local flowers = {"Rose", "Daisy", "Tulip"}

function setup()
  size(200, 200)

  background(220)

  -- Draw the first name.
  fill('red')
  text(flowers[1], 10, 50)
  
  -- Draw the second name.
  fill('green')
  text(flowers[2], 10, 100)
  
  -- Draw the third name.
  fill('blue')
  text(flowers[3], 10, 150)
end
```

```lua
local flowers = {"Rose", "Daisy", "Tulip"}
```

In this example, we’ve created an array using curly brackets (`{ }`) and commas that separate each element in the array. The array is a collection of strings, each representing a type of flower, and is stored in a variable called `flowers`. Each element of the array holds a string with a flower name. Each element can be accessed using its index number. For example, `"Rose"` is located at index `1`, `"Daisy"` at index `2`, and `"Tulip"` at index `3`.

```lua
local rose = flowers[1]
```

In the code snippet above, we access the first element of the `flowers` array at index 1 using the index notation: `flowers[1]`. In the example above, this syntax is used to place text on the canvas with the names accessed from various elements in the `flowers` array.

We then assign that value to a new variable named `rose`. `rose` now holds the string `"Rose"`, which is the first flower name in the `flowers` array. Values stored in other elements can be accessed in the same way.

### Example 2: Using a `for` loop to iterate through the array of names

![Data Garden 6](/assets/tutorials/data-garden6.webp)

```lua
require("L5")

-- Create an array flowers
local flowers = {"Rose", "Daisy", "Tulip"}

function setup()
  size(200, 200)
end

function draw()
  background(220)
  fill(0)
  
  -- Use a for loop to iterate over the array.
  for i=1,#flowers do
    text(flowers[i], 10, 50 * i)
  end
end
```

Our second example uses a `for` loop to iterate through each element in the array and print the text on the canvas. *Iteration* is a process where a block of code is executed repeatedly for each element in an array. 

```lua
for i=1,#flowers do
  text(flowers[i], 10, 50 * i)
end
```

To iterate, the code snippet above uses a `for` loop that “looks through” each element of the flower array. According to the `for` loop, the index i starts at 1 and increases with each iteration until it reaches the max number of elements in the array. *Arrays in Lua start their index at 1*. The last element in the array can be accessed by referencing the item stored at the length of the array. The number of elements in any array can be accessed by using the array`#` symbol. In the for loop above, the length of the flowers array is accessed using `#flowers`. To access the values in the array, we use `flowers[i]` in the `for` loop in the [text()](/reference/text) function to display the value in each element as text on the canvas.

### Example 3: Adding new elements to the array

![Data Garden 7](/assets/tutorials/data-garden7.webp)

```lua
require("L5")

-- Create an array flowers
local flowers = {"Rose", "Daisy", "Tulip"}

function setup()
  size(200, 200)
  table.insert(flowers, "Sunflower"); --add new element

  background(220)
  fill(0)
  
  -- Use a for loop to iterate over the array.
  for i=1,#flowers do
    text(flowers[i], 10, 40 * i)
  end
end
```

```lua
local flowers = {
"Rose", "Daisy", "Tulip" --Inserted elements will go here
}

-- Add a new element to the end of the array
table.insert(flowers, "Sunflower")
```

Using the array method [table.insert()](https://www.luadocs.com/docs/functions/table/insert), you can add a new element to the end of the array. In this example, we are adding "Sunflower" to the end of the `flowers` array.

### Example 4: Removing an array element

![Data Garden 8](/assets/tutorials/data-garden8.webp)

```lua
require("L5")

-- Create an array flowers
local flowers = {"Rose", "Daisy", "Tulip"}

function setup()
  size(200, 200)
  fill(0)
  
  -- Starting at index 1, remove one flower.
  table.remove(flowers, 1)

  background(220)
  
  for i=1,#flowers do
    text(flowers[i], 10, 50 * i)
  end
end
```

```lua
local flowers = {"Rose", "Daisy", "Tulip"}

-- remove one element from flowers at index 1
table.remove(flowers, 1)
```

In order to remove elements from an array, we use the function [table.remove()](https://www.luadocs.com/docs/functions/table/remove). The function `table.remove(flowers, 1)` modifies the flowers array with two parameters: one for the array, and another for the index of where to start removing. You can optionally add a third that specifies the number of elements to remove. `table.remove(flowers, 1)` results in the removal of `"Rose"` from the array, leaving only `"Daisy"` and `"Tulip"`.

### Example 5: Using `for..in` loop for arrays


![Data Garden 9](/assets/tutorials/data-garden9.webp)

```lua
require("L5")

-- Create an array flowers
local flowers = {"Rose", "Daisy", "Tulip"}

function setup()
  size(200, 200)
  
  background(220)
  fill(0)
  local y = 50
  
  -- Use the for loop with ipairs to look at each element as a variable.
  for i, flower in ipairs(flowers) do
    text(flower, 10, i * y)
  end
end
```

```lua
for i, flower of ipairs(flowers) do
-- flower declares a variable to store each current element
-- ipairs is the keyword to loop through each ordered element in an array
-- flowers is the name of the array to loop over

  --do something with the current element
  print(flower)
end
```

We can also iterate over an array using a `for..in` loop. The `flower` variable temporarily stores each element during the loop’s iteration. The `print(flower)` statement inside the loop prints the name of each flower to the console, cycling through `"Rose"`, `"Daisy"`, and `"Tulip"` in order.

Using a `for...in` loop can make code easier to read when things become more complex.

### Step 6: Generate multiple flowers with an array

Now, it’s time to generate multiple flowers on the screen using arrays.

* First, declare the `flowers` array at the top of your program. The curly brackets with nothing in them represent an empty array of flowers.

```lua
-- Array of flowers.
local flowers = {}
```

* Outside of all other functions, define the `flowerPower()` function.

```lua
-- Function to create 20 flowers.
function flowerPower()
end
```

Inside `flowerPower()`, create 20 flower objects using a `for` loop and add them to your `flowers` array.


```lua
for i=1,20 do
  -- Create a flower in a random location.
  local flower = createFlower()
  -- Add the flower to the flowers array.
  table.insert(flowers, flower1)
end
```

Call the `flowerPower()` function in the [setup()](/reference/setup) function to create the 20 flower objects.

```lua
flowerPower()
```

* Use the `for..in` loop with `ipairs` for arrays in the [draw()](/reference/draw) function to draw each flower in the `flowers` array. The `for..in` loop reads, for each flower element in the array of flowers, call `drawFlower()`.

```lua
for i,flower in ipairs(flowers) do
  drawFlower(flower)
end
```

Your code should look similar to this:

![Data Garden 10](/assets/tutorials/data-garden10.webp)

```lua
require("L5")

-- Array of flowers.
local flowers = {}

function setup()
  size(400, 400)
  frameRate(1)

  -- Generate 20 flowers.
  flowerPower()
end
function draw()
  background("lightblue")

  -- For each flower in the array of flowers.
  for _,flower in ipairs(flowers) do
    drawFlower(flower)
  end
end

-- Function to create 20 flowers.
function flowerPower()
  for i=1,20 do
    -- Create a flower in a random location.
    local flower = createFlower()

    -- Add the flower to the flowers array.
    table.insert(flowers, flower)
  end
end

-- ... createFlower() and drawFlower()
function createFlower()
  local flower = {
    x = random(20,380),
    y = random(20,380),
    size = random(20,75),
    lifespan = random(255,300),
    color = color(random(255), random(255), random(255))
  }
  return flower
end

function drawFlower(flower) 
  noStroke()
  fill(flower.color)

  -- Draw petals.
  ellipse(flower.x, flower.y, flower.size / 2, flower.size)
  ellipse(flower.x, flower.y, flower.size, flower.size / 2)

  -- Draw a yellow center.
  fill(255, 204, 0)
  circle(flower.x, flower.y, flower.size / 2)
end
```

### Try this!

Add a parameter to your `flowerPower()` function so you can easily start with as many flowers as you like.

## Step 7: Update the flowers in the array

Now that we have tested the array of flowers, let’s draw the wilting effect. One of the benefits of using an array to control the flowers is the ability to update values in each flower. 

* Outside of all other functions, define a function called `updateAndDrawFlowers()`:

```lua
function updateAndDrawFlowers()
end
```

This function will look at each flower in the array and will draw the flower.

```lua
for i,flower in ipairs(flowers) do
  drawFlower(flower)
end
```

* Inside the `for` loop, decrease the flower object’s `size` and `lifespan` to simulate wilting. 

Add a wilting animation effect, which will decrease the flower size by 1% after the `drawFlower()` function draws the flower. We create the wilting effect by multiplying the current size by 0.99 and storing it back into the flower’s `size` property. Then decrement the lifespan and store it in the flower’s `lifespan` variable. 

```lua
-- Wilting effect for the flower
flower.size = flower.size * 0.99

-- Reduce lifespan.
flower.lifespan = flower.lifespan - 1
```

* When the flower object’s `lifespan` is zero or negative, we’ll remove it from the array by using the [table.remove()](https://www.luadocs.com/docs/functions/table/remove) method. 

```  
for i,flower in ipairs(flowers) do
  -- Draw the flower.
  drawFlower(flower)

  -- Wilting effect for the flower.
  flower.size = flower.size * 0.99

  -- Reduce lifespan
  flower.lifespan = flower.lifespan - 1
  
  if flower.lifespan <= 0 then 
    -- Remove wilted flower.
    table.remove(flowers, i)
  end
end
```

* Add `updateAndDrawFlowers()` to the [draw()](/reference/draw) function.

* Remove the call to `frameRate(1)` from `setup()`.

Your code should look similar to this:

![Data Garden 11](/assets/tutorials/data-garden11.gif)

```lua
require("L5")

-- Array of flowers.
local flowers = {}; 

function setup()
  size(400, 400)
  
  -- Generate 20 flowers.
  flowerPower(); 
end

function draw()
  background('lightblue')
  
  -- Call your new function.
  updateAndDrawFlowers()
end

-- Define your new function
function updateAndDrawFlowers()
  for i,flower in ipairs(flowers) do

    -- Draw the flower.
    drawFlower(flower)

    -- Apply wilting effect by reducing size by 1%
    flower.size = flower.size * 0.99

    -- Reduce lifespan
    flower.lifespan = flower.lifespan - 1
    
    if flower.lifespan <= 0 then 
      -- Remove wilted flower.
      table.remove(flowers, i)
    end
  end
end

-- Function to create 20 flowers.
function flowerPower()
  for i=1,20 do
    -- Create a flower in a random location.
    local flower1 = createFlower()
    
    -- Add the flower to the flowers array.
    table.insert(flowers,flower1)
  end
end

function createFlower()
  local flower = {
    x = random(20,380),
    y = random(20,380),
    size = random(20, 75),
    lifespan = random(255,300),
    color = color(random(255), random(255), random(255))
  } 
  
  return flower
end

function drawFlower(flower)
  noStroke()
  fill(flower.color)
  
  -- Draw petals.
  ellipse(flower.x, flower.y, flower.size / 2, flower.size)
  ellipse(flower.x, flower.y, flower.size, flower.size / 2)

  -- Draw center.
  fill(255, 204, 0)
  circle(flower.x, flower.y, flower.size / 2)
  
end
```

### Try this!

Experiment with the wilting effect using subtraction, random numbers, or any other ideas you come up with.

## Step 8: Add more flowers to the array with `mousePressed()`

Finally, let’s add more flowers to the canvas by using [mousePressed()](/reference/mousePressed), `mouseX](/reference/mouseX), and [mouseY](/reference/mouseY) to add another flower object to the flowers array each time the window is clicked.

* Outside of all other functions, write your `mousePressed()` function:

```lua
function mousePressed()
  local flower = createFlower()
  
  -- reassign x to be mouseX
  flower.x = mouseX
  
  -- reassign y to be mouseY
  flower.y = mouseY
  
  -- add the flower to the flowers array
  table.insert(flowers, flower)
end
```

Your code should look something like this:

![Data Garden 12](/assets/tutorials/data-garden12.gif)

```
require("L5")

-- Array of flowers.
local flowers = {}; 

function setup()
  size(400, 400)
  
  -- Generate 20 flowers.
  flowerPower(); 
end

function draw()
  background('lightblue')
  
  -- Call your new function.
  updateAndDrawFlowers()
end

function mousePressed()
  local flower = createFlower()

  -- reassign x to be mouseX
  flower.x = mouseX; 
  
  -- reassign y to be mouseY
  flower.y = mouseY

  -- add the flower to the flowers array
  table.insert(flowers,flower)
end

function updateAndDrawFlowers()
  for i,flower in ipairs(flowers) do

    -- Draw the flower.
    drawFlower(flower)

    -- Apply wilting effect by reducing size by 1%
    flower.size = flower.size * 0.99

    -- Reduce lifespan
    flower.lifespan = flower.lifespan - 1
    
    if flower.lifespan <= 0 then 
      -- Remove wilted flower.
      table.remove(flowers, i)
    end
  end
end

-- Function to create 20 flowers.
function flowerPower()
  for i = 1, 20 do
    -- Create a flower in a random location.
    local flower1 = createFlower()
    
    -- Add the flower to the flowers array.
    table.insert(flowers,flower1)
  end
end

function createFlower()
  local flower = {
    x = random(20,380),
    y = random(20,380),
    size = random(20, 75),
    lifespan = random(255,300),
    color = color(random(255), random(255), random(255))
  } 
  return flower
end

function drawFlower(flower)
  noStroke()
  fill(flower.color)
  
  -- Draw petals.
  ellipse(flower.x, flower.y, flower.size / 2, flower.size)
  ellipse(flower.x, flower.y, flower.size, flower.size / 2)

  -- Draw center.
  fill(255, 204, 0)
  circle(flower.x, flower.y, flower.size / 2)
  
end
```

### Try this!

* Add multiple flowers around the `mouseX` and `mouseY` locations when the mouse is pressed.
* Experiment with different shapes or colors for the flowers. 
* Introduce new elements to the garden, like bees or butterflies, and see how they interact with the flowers. 

## Conclusion

Congratulations on completing the Data Structure Garden tutorial!

Throughout this journey, you learned about the fundamental concepts of objects and arrays (built with tables) to create a dynamic and interactive garden simulation. Using arrays, you’ve managed multiple objects elegantly and efficiently, each with their own properties and behaviors. This is a powerful skill in the world of programming, opening doors to more complex and interactive applications.

Once again, well done on completing this tutorial. Keep experimenting, keep coding, and most importantly, enjoy learning and creating!

## Resources

* [Objects in Lua](https://www.lua.org/pil/16.html)
* [Arrays in Lua](https://www.lua.org/pil/11.1.html)
* [Expressions and Operators](https://www.lua.org/manual/2.4/node9.html)

By Portia Morrell, Jaleesa Trapp, Kate Maschmeyer. Adapted to L5 by Lee Tusman. [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
