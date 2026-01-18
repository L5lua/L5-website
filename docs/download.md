L5 is free open source software available for Linux, Mac, Windows, Android and iOS. 

L5 is a library built on top of the framework LÖVE (also called Love2d).

To write code for L5 you need to install Love2d and the single L5.lua library file.

## Install

1. Download and install [Love2d](https://www.love2d.org/) with the free installer
2. Download the [L5 Starter project](L5-starter.zip) and extract it (double-click on Mac, right-click "Extract All..." on Windows)
3. Open main.lua in any text editor and begin coding!
4. Drag the L5-starter folder onto the Love2d application to run your program, or run from an IDE or command line for access to console messages

## Downloads

### L5 Starter Project (Recommended)

This compressed folder contains the *L5.lua* library, a starter *main.lua* file (with `require('L5')` already included), and a *README*.

[Download L5 Starter project](L5-starter.zip)

### Individual Downloads

**Latest version:** [Download L5.lua](https://raw.githubusercontent.com/L5lua/L5/main/L5.lua)

**Stable release (v0.1.2):** [Download L5.lua v0.1.2](https://raw.githubusercontent.com/L5lua/L5/v0.1.2/L5.lua)

## Offline Documentation

This L5 documentation site is available for download to run offline, with or without images.

* [Download L5lua.org with images (8MB ZIP)](https://github.com/L5lua/L5-website/archive/refs/heads/gh-pages.zip)
* [Download L5lua.org without images (2MB ZIP)](https://github.com/L5lua/L5-website/archive/refs/heads/gh-pages-lite.zip)

After downloading, extract the ZIP and serve the folder with a local web server. For a quick local server, navigate to the extracted folder in your command line and run `python -m http.server` (Python 3) or `python -m SimpleHTTPServer` (Python 2).

## Running your program

The easiest way to run your L5 program is to drag the folder containing your main.lua onto the Love2d application. But to see error messages and printing in the console you will want to run from an Integrated Development Environment (IDE) or command line. Here are platform-specific details:

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

The easiest way to run your program is to drag the folder onto either love.exe or a shortcut to love.exe. Remember to drag the folder containing `main.lua`, and not `main.lua` itself. 

However, to see print messages and error output in the console (helpful when coding and debugging), you'll want to use an IDE or run from the command line. IDEs such as ZeroBrane Studio, Sublime Text, VS Code, Notepad++, and SciTE all support launching LÖVE programs (the underlying framework used by L5), though may require some configuration.

Alternatively, you can launch from the command line with the `--console` flag:
```
"C:\Program Files\LOVE\love.exe" --console "C:\Users\<YourUsername>\Desktop\L5-starter"
```

Replace `<YourUsername>` and `Desktop\L5-starter` with your actual username and the location of your program folder.

---

*Installation instructions adapted from [Love2d wiki: Getting Started](https://www.love2d.org/wiki/Getting_Started), GNU Free Documentation License 1.3.*
