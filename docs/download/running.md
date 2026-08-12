# Running Your Programs

There are several different ways to run a L5 program: through VSCodium / VS Code, using the desktop, or through the command line interface (CLI). If you are new to computing or are unsure about the CLI, then we recommend the L5 extension in VSCodium / VSCode or running from the desktop.

## Using the L5 extension

If you are using a text editor such as VSCodium or Visual Studio Code (VS Code), you can install an extension that will allow you to run your sketches by pushing a button.

If you haven't installed the extension yet, in VSCodium or VS Code, open the extension menu and install L5:

![Open the extension menu on the left side and search L5 on the top](/assets/tutorials/install/extension1.webp "Open the extension menu on the left side and search L5 on the top")

![Search for L5 in the search bar](/assets/tutorials/install/extension2.webp "Search for L5 in the search bar")

![Press install](/assets/tutorials/install/extension3.webp "Press install")

Click to download the [L5-starter folder](/L5-starter.zip) and extract it. In your text editor, click open folder and navigate to the L5-starter folder. 

![Open folder](/assets/tutorials/install/open-folder.webp "Open folder")

Once it is installed and you have already created a `main.lua` file (or you downloaded the L5-starter folder), a new button appears in the bottom left corner. If the button does not appear, make sure you have opened a single folder that contains `main.lua` and `L5.lua`.

![Run L5 button in the bottom left corner](/assets/tutorials/install/run-l5.webp "Run L5 button in the bottom left corner")

If you are running the extension for the first time, it will prompt you to open your extension settings. 

![Open extension settings](/assets/tutorials/install/extension-open-settings.webp "Open extension settings")

In the settings panel that opens, you will need to specify the path to Love in the input text box at the bottom. The *path* is where Love exists on your computer. 

* **Windows**: The path is already provided in the text box and you do not need to change anything. 
* **Linux**: Use `love` if installed globally or the full path, usually `/usr/bin/love`
* **Mac**: By default, Love will be in your Downloads folder. In Finder, drag Love from Downloads to your Applications folder. In the VSCode settings, change the path to `/Applications/love.app/Content/MacOS/love`

![Change the text in the text box to your OS path](/assets/tutorials/install/extension-path1.webp "Change the text in the text box to your OS path")

When you want to see your sketch in action, press "Run L5". 

![Run L5](/assets/tutorials/install/run-l5.webp "Run L5")

You can close the window or push the "Stop" button to stop running your sketch. 

![Close the sketch by closing the window or by pressing Stop](/assets/tutorials/install/stop-l5.webp "Close the sketch by closing the window or by pressing Stop")

You can read more about the settings of the extension in the [extension docs](https://github.com/L5lua/L5-vscode-extension#l5-extension). You can also download it directly from the [OpenVSX Marketplace](https://open-vsx.org/extension/l5lua/l5) or the [VS Marketplace](https://marketplace.visualstudio.com/items?itemName=l5lua.l5lua). 

## Running L5 from the desktop

Start by downloading the [L5 Starter](http://l5lua.org/L5-starter.zip), a folder containing the L5.lua library file and a starter main.lua file with a simple L5 program. Right click and extract (Windows, Linux)) or uncompress (macOS) the folder.

The easiest way to run your L5 program is to drag the **folder** containing your main.lua onto the Love2d application. Remember to drag the **folder** containing `main.lua`, and not `main.lua` itself.

It should launch and open a new window with your sketch running in it, or print an error message. If you're running the L5 Starter program, you should see a square window with a yellow background. Congratulations.

**By default, `print()` output only appears if you run your program from the command line. To display print output directly in your sketch window add `printToScreen()` to your `setup()` function.**

*Once you have a sucessfully running program, you're ready for your next steps writing programs with L5. Check out [L5 for Processing-p5.js programmers](/L5-for-processingp5), [tutorials](/tutorials) or the [reference](/reference).*

## Running L5 from the command line

### Windows CLI

You can launch your programs from the command line and add the `--console` flag to be able to see print() and error() output as well:

```
"C:\Program Files\LOVE\love.exe" --console 
"C:\Users\<YourUsername>\Desktop\L5-starter"
```
Replace `<YourUsername>` and `Desktop\L5-starter` with your actual username and the location of your program folder.

### macOS CLI

There are a few extra steps to smoothly set up command line usage for L5 in the command line on Mac. 

If Love is installed in your applications folder you can run:

```sh
open -n -a love "~/path/to/my-program"
```

This will not send debugging and print information to the Terminal nor any `describe()` text. To see printed text in the command line you need to run the Love program from Applications, like this:

```sh
/Applications/love.app/Contents/MacOS/love ~/path/to/my-program
```

You can set up an alias in your Terminal session to call the binary when you use love by adding an alias to your `~/.zshrc` file (Z shell configuration file).

Open the file with:

```sh
open -a TextEdit ~/.zshrc
```

You may have to create the file first if it does not yet exist.

```sh
touch ~/.zshrc
```

Then paste in the following code and save the file:

```sh
# alias to love
alias love="/Applications/love.app/Contents/MacOS/love"
```

Now you can call love from the command line like Linux and Windows:

```sh
love ~/path/to/my-program
```

If this doesn't works you should reload the .zshrc file and then try running the program again.

```sh
source ~/.zshrc
love ~/path/to/my-program
```

### Linux CLI

In the Terminal, you can run `love path/to/L5-starter`. Or if you are in the folder with your program, run `love .` to launch your project from the current directory.

It should now launch and you should see a new window open with your code sketch running.
<img src="/assets/tutorials/install/linux1.webp" alt="A yellow background window appearing on top of folder holding L5 Starter and love application" title="A yellow background window appearing on top of folder holding L5 Starter and love application" width="600" />

Now you are ready to start learning with [First Steps](../tutorials/first-steps.md). If you are familiar with Lua, p5.js, or Processing already, you should take a look at [L5 for Processing-p5.js Programmers](../tutorials/L5-for-processingp5.md).

*Instructions adapted from [Love2d wiki: Getting Started](https://www.love2d.org/wiki/Getting_Started), GNU Free Documentation License 1.3.*
  
