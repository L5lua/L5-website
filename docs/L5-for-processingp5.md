# L5 for Processing and p5.js programmers

L5 stands on the shoulders of Processing and p5.js. You will be able to use your previous knowledge to get started right away and learn Lua in the process.

L5 was built to be fun, fast, and resource-light. It is in many cases faster than Processing or p5.js programs. It works cross-platform and on older machines. Lua's syntax is simpler and constrained compared to JavaScript and Processing-Java. Some things are easier in L5, but some things are not. L5 currently does not have 3d functionality. It only supports one video format (ogg theora). It is a younger and still developing language dialect compared to its older siblings.

In most cases, L5 functions are similar or equivalent to Processing functions. In some cases, p5.js functionality has been targeted or added. For example, like in p5.js you can use [HTML color names from or hexadecimal](https://en.wikipedia.org/wiki/Web_colors) instead of only the default RGB and RGBA values from Processing.

## Lua tips

### Global and local variables

**Unlike in Processing (Java) and p5.js (JavaScript), by default all variables in L5 (Lua) have global scope unless specified as local.** 

```lua
function setup()
  name = "Nina" 
end
  
function draw()
  print(name) --prints out "Nina"
end
```

To create a variable with block scope, specify `local`.

```lua
function setup()
  local name = "Nina"
end

function draw()
  print(name) --prints out "nil"
end
```

To concatenate variables together or to combine with other strings, use `..`

```lua
local name = "Nina"
print("My name is "..name) --prints out "My name is Nina"
```

### Commenting

A comment starts with `--` instead of `//`

Multi-line comments can be created by surrounding them with `--[[` and `]]--`.

### Tables all the way down

The main data structure of Lua is the *table*. This is used to construct arrays and objects, for example.

```lua
wu_tang_clan = {"RZA", "GZA", "Ol' Dirty Bastard", "Inspectah Deck", "Raekwon", "Ghostface Killah", "Method Man", "Masta Killa"}
```

And following from this...

### 1-based indexing!

You may have heard that Lua uses 1-based indexing. If you haven't, well now you've heard it.

In other words, the first item in an ordered array is `1` where in many other C-based languages the first ordered element is `0`.

```lua

wu_tang_clan = {"RZA", "GZA", "Ol' Dirty Bastard", "Inspectah Deck", "Raekwon", "Ghostface Killah", "Method Man", and "Masta Killa"}

print("First rapper up is "..wu_tang_clan[1])
--prints: First rapper up is RZA.
```

There are some cool advantages in Lua for working with ordered tables.

The `#` prepending the table name will always give you its *length*.

```lua
print("There are "..#wu_tang_clan.." members of Wu Tang Clan")
```

This makes it easy to work with tables in a loop.

You can build associative tables, commonly known as a *dictionary*, *map* or *key-value pairs*. You can access their value through specifying a named index, or through dot notation.

```lua
local characters = {
  ["Mario"] = "Plumber",
  ["Luigi"] = "Plumber",
  ["Bowser"] = "Monster"
}

print("Mario is a "..characters["Mario"])

--Alternatively, you could write:
print("Mario is a "..characters.Mario)
```

The brackets are optional if your parameter is a single string with no spaces. 

```lua
local characters = {
  mario = "Plumber"
}
```

You can easily add properties to a table, using bracket notation or dot notation.

```lua
local museum = {} --initializes the table
museum['location'] = "Los Angeles"
museum.name = "Museum of Jurassic Technology"
```

### Loops in Lua

*[For](/reference/for) loops* have simple syntax. By default the iterator increments by 1.

```lua
for i=1,5 do
  print(i)
end
```

You can optionally specify to increment or decrement by a different value.

```lua
for i=100, 0, -2 do
  print(i)
end
-- counts backwards from 100 to 0, decreasing by 2 each iteration
```

If you want to iterate through a table of values, the syntax is clear and efficient in Lua since prepending `#` to a table's name gives you its length, and since tables are ordered beginning at 1, we can count up from 1 to the table's length:

```lua
print("The Wu Tang Clan, starring:")
for i=1,#wu_tang_clan do
  print(wu_tang_clan[i])
end
```

Lua also has special functions for working with tables. `ipairs` iterates through an ordered table (aka an *array*). `pairs` iterates through an associative table (aka *key-value pairs*). 

```lua
names = {"John","Paul","George","Ringo","Yoko"}
for i,name in ipairs(names) do
  print(i,name)
end
```

This will produce

```text
1	John
2	Paul
3	George
4	Ringo
5	Yoko
```

You will commonly see `_` when you don't need to print out or work with the iterator.

```
names = {"John","Paul","George","Ringo","Yoko"}
print("The Beatles:")
for _,name in ipairs(names) do
  print(name)
end
```

This will produce 

```text
The Beatles:
John
Paul
George
Ringo
Yoko
```

`pairs` is used to iterate over all key-value pairs in a table. 

```lua
local menu = {
  breakfast = "yogurt",
  lunch = "salad",
  dinner = "tacos"
}

for key, value in pairs(menu) do
  print("For "..key.." I ate "..value)
end
```

This will produce

```text
For breakfast I ate yogurt
For dinner I ate tacos
For lunch I ate salad
```

**Note: In an associative table of key-value pairs (rather than an ordered table array), there is no guarantee that the values will be output in a specific order.** If you run the above code, you may find the *dinner* gets printed before *lunch* even though lunch was listed first in the table, but there are mechanisms to specify an exact order.

## Conditionals

Lua uses `if`, `elseif` and `else` to create conditionals. `then` is required after your `if` and `elseif` conditional.

```lua
if porridgeTemp > 75 then
  print("This bowl of porridge is too hot!")
elseif porridgeTemp < 45 then
  print("This bowl of porridge is too cold!")
else
  print("This bowl of porridge is just right.")
end
```

Unlike Java and JavaScript, there is no switch statement in Lua.

## Other Lua Gotchas and Tips

* Lua is a dynamically typed language. You don't specify types (integer, floats, etc).
* Functions and loops use `end` rather than curly brackets `{ }` for specifying scope. Loops also use `do`.
* **There are no `++` or `+=` shortcuts in Lua. To increment a variable by 1 for example, you write `x = x + 1`**
* The semicolon `;` is not needed at the end of lines

## Conversion equivalences

| Lua                             | JavaScript                         | Java                                   |
|---------------------------------|------------------------------------|----------------------------------------|
| `function func() ... end`       | `function func() {...}`            | `void func() {...}`                    |
| `true` and `false`              | `true` and `false`                 | `true` and `false`                     |
| `a and b` (logical AND)         | `a && b`                           | `a && b`                               |
| `a or b` (logical OR)           | `a || b`                           | `a || b`                               |
| `not a`                         | `!a`                               | `!a`                                   |
| `a ~= b` (not-equal)            | `a != b`                          | `a != b`                                |
| `i = i + 1` (increment)         | `i++`                              | `i++`                                  |
| `i = i - 1` (decrement)         | `i--`                             | `i--`                                   |
| `a <= b and b < c`              | `a <= b && b < c`                  | `a <= b && b < c`                      |
| `for i=1, limit do ... end`     | `for (let i=0; i<limit; i++) {...}` | `for (int i = 0; i < limit; i++) {...}` |
| `for i=start, limit, step do ... end` | `for (let i=start; i<limit; i+=step) {...}` | `for (int i = start; i < limit; i += step) {...}` |
| `for _, b in ipairs(table_of_balls) do ... end` | `for (let b of arrayOfBalls) {...}` | `for (Ball b : arrayOfBalls) {...}`     |
| `local myColor = '#FFCC00'`    | `let myColor = '#FFCC00'`          | `String myColor = "#FFCC00";`         |

## Object orientation in Lua

OOP can be implemented in Lua using tables.


## More info on Lua

Lua maintains a great documentation site with [reference manuals](https://lua.org/manual/). The [lua-users Tutorial Directory](http://lua-users.org/wiki/TutorialDirectory) has beginning and advanced tutorials on the language and its features. The Lua Users wiki has a section on [Object Oriented Programming](http://lua-users.org/wiki/ObjectOrientedProgramming) with many examples.
