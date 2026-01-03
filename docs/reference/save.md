# save()
 
Saves a png image from the display window. `save()` can optionally take one argument with the filename to save under. If the filename does not end with a `.png` extension then it will be automatically appended to the filename. Images are saved to the project folder.

**Note that it is not recommended to call this function within draw as it will save repeatedly on every render.**

If the user doesn't have write permission for the current directory then it will save to a default directory and print a warning and output location. 

## Examples

save example 1

```lua
function setup()
  fill(0)
  ellipse(random(width),random(height),random(100),random(100))

  -- Saves the canvas as an image to a specified filename
  save('mySketch.png')

  describe('An example for saving a sketch window as an image.')
end
```

save example 2

```lua
function setup()
  fill(0)
  ellipse(random(width),random(height),random(100),random(100))
  
  -- Saves the canvas as an image to a randomly generated filename
  save()
  
  describe('An example for saving a canvas as an image.')
end
```

## Syntax

```lua
save(filename)
```

```lua
save()
```

## Parameters

| Parameter |                                                                               |
| -         | --                                                                            |
| filename  | String: any sequence of letters and numbers, optionally with '.png' extension |


## Related

* [print()](print.md)
* [loadImage()](loadImage.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
