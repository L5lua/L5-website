L5 is free open source software available for Linux, Mac, Windows, Android and iOS. 

L5 is a library built on top of the framework LÖVE (also called Love2d).

To write code for L5 you need to install Love2d and the single L5.lua library file.

## Install

1. Download and install [Love2d](https://www.love2d.org/) with the free and simple installer
2. Download L5.lua
3. Make a new folder for your project. Inside it create a `main.lua` file to write your code in. Be sure to include `require ("L5")` in the top of your program. 
4. Add a copy of L5.lua to your folder. 

## Downloads

**Latest version:** [Download L5.lua](https://raw.githubusercontent.com/L5lua/L5/main/L5.lua)

**Stable release (v0.1.0):** [Download L5.lua v0.1.0](https://raw.githubusercontent.com/L5lua/L5/v0.1.0/L5.lua)

## Running your program

In general, the easiest way to run your program is to save your `main.lua` file inside a folder, then drag that entire folder onto your Love2d application folder to launch it. Don't forget to put `require('L5')` at the top of the file.

### Linux

In the Terminal, you can run `love path/to/main.lua`. Or if you are in the folder with your program `love .` to launch.

---

### Mac

Drag and drop the folder holding L5.lua and your main.lua onto the Love application.

OR

If you are comfortable navigating in the Terminal and Love is installed in your applications folder you can run:

```sh
open -n -a love "~/path/to/my-program"
```

This will not send debugging/print information to the Terminal, such as any `describe()` text. To see printed text you need to run the Love program from Applications, like this:

```sh
/Applications/love.app/Contents/MacOS/love ~/path/to/my-program
```

You can set up an alias in your Terminal session to call the binary when you use love by adding an alias to your `~/.zshrc` file (Z shell configuration file).

Open the file with:

```sh
open -a TextEdit ~/.zshrc
```

You may have to run

```sh
touch ~/.zshrc
```

first if the file does not yet exist.

Then paste in the following code and save the file:

```sh
# alias to love
alias love="/Applications/love.app/Contents/MacOS/love"
```

Now you can call love from the command line like Linux and Windows:

```sh
love ~/path/to/my-program
```

If this doesn't works you should reload the .zshrc file like this:

```sh
source ~/.zshrc
```

and try it again.

---

### Windows

ZeroBrane Studio, Sublime Text, VS Code, Notepad++, and SciTE allow you to launch your program from within their code editors, though may take some special configuration.

Otherwise, the easiest way to run your program is to drag the folder onto either love.exe or a shortcut to love.exe. Remember to drag the folder containing `main.lua`, and not `main.lua` itself.

You can also launch the game from the command line:

```
"C:\Program Files\LOVE\love.exe" "C:\games\mygame"
```

You can create a shortcut to do this; simply make a shortcut to love.exe, right-click on it and select "Properties", and then put the command line you want in the "Target" box for the shortcut.

On Windows, there is a special command-line option which will attach a console to the window, allowing you to see the result of print calls (equivalent to setting t.console=true in conf.lua or running lovec.exe.

```
"C:\Program Files\LOVE\love.exe" --console
```

---

*Installation instructions adapted from [Love2d wiki: Getting Started](https://www.love2d.org/wiki/Getting_Started), GNU Free Documentation License 1.3.*
