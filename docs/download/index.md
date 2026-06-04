## Downloads

L5 is free open source software available for Linux, Mac, Windows, Android and iOS.

L5 programs run using LÖVE (also called Love2d), a free, open-source framework. Love2D is a game framework, just like Gadot, Unity, or Unreal. You will use Love2D to run your L5 scripts. This is similar to using a browser to run HTML code.

Covered by this download tutorial:

- Download and Install Love2D
- Download and Open L5 Starter Folder

**Step-by-step install guides:**

??? "Install Windows"

    ## Install Windows

    This tutorial walks you through installing L5 with the Love (Love2d) framework on your Windows computer.

    1. Go to the [Love website](https://love2d.org) and click to download the 64-bit zipped Windows program.
    2. Your browser may show a warning. Click **"Keep"** or **"Save anyway"** to proceed with the download. It will download to your _Downloads_ folder by default.
    3. From the L5lua.org Download page, [download the L5 Starter project](/L5-starter.zip).
    4. Click **"Save"** when it asks you to save the L5-starter.zip file.
    5. Return to your _Downloads_ folder on your computer. **Right click** on the Love zip file and choose **"Extract All"**. Click **"Extract"** to extract it to your Downloads folder.
    6. Open the extracted Love folder and **double-click** the **love.exe** application to run it. Windows may show a security warning saying "Windows protected your PC". Click **"More info"** and then click **"Run anyway"**.
    7. You should see a window open with a flying bird-shaped balloon and clouds, verifying that Love is now properly installed on your computer. **At this point you can close the window.**
    8. Back in your downloads folder, **extract the L5-starter.zip file** the same way you extracted the Love zip file. Then **drag the L5-starter folder onto the love.exe application**. It should now launch and you should see a new window open with your code sketch.

??? "Install macOS"

    ## Install macOS

    This tutorial walks you through installing L5 with the Love (Love2d) framework on your Macintosh computer.

    **Video Tutorial**

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Ehs-fLQ5gfk?si=Cf-zsDI4APY6R8Wl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

    **Text and Screenshot Tutorial**

    1. Love is the underlying Framework that will allow L5 code to run on your computer. So we start by installing Love. Go to the [Love website](https://love2d.org) and click to download the 64-bit zipped Mac program.
    ![Love2d website with downloads](/assets/tutorials/install/mac1.webp 'Love2d website with downloads')
    2. Click **"Allow"** if it asks 'Do you want to allow downloads on "love2d.org"?' It should download to your _Downloads_ folder by default.
    ![Alert box asking permission to download Love2d](/assets/tutorials/install/mac2test.webp 'Alert box asking permission to install Love2d')
    3. Now on your desktop (called "Finder" on macOS) open up your _Downloads_ folder. You can right click and choose Open (see screenshot) or double click on Love to launch it.
    ![Folder with love application and L5 Starter folder](/assets/tutorials/install/mac3.webp 'Folder with love application and L5 Starter folder')
    4. A warning popup box opens to say the program and code is not verified by Apple since you will be writing your own custom code. If you can choose Open because you turned off restrictions, then choose Open! Otherwise, **DO NOT** move to the trash.
    ![Alert box stating macOS cannot verify the developer of love. The correct option is Open.](/assets/tutorials/install/mac4.webp 'Alert box stating macOS cannot verify the developer of love. The correct option is Open')
    5. If you weren't allowed to open it, go to your System Setting > Privacy &amp; Security. Scroll down to the Security section and next to **"love" was blocked to protect your Mac.** choose **Open Anyway**.
    ![System settings showing the Privacy and Security settings. Scroll down to Security and next to "love" was blocked to protect your mac, click to "Open Anyway".](/assets/tutorials/install/mac5.webp 'Alert box stating macOS cannot verify the developer of love. The correct option is Open')
    6. Now go back to your Downloads folder and **Double click** on Love. We only need to do this once! It's to verify Love works on your computer, which will allow L5 to run your custom code. You should see a window open with a flying bird-shaped balloon and clouds, verifying that Love is now properly installed on your computer. **At this point you can close the window.**
    ![A flying bird-shaped balloon and cartoon clouds](/assets/tutorials/install/mac6.webp 'A flying bird-shaped balloon and cartoon clouds')
    7. From the L5lua.org Download page, [download the L5 Starter project](/L5-starter.zip).
    ![L5 website download page with L5 Starter](/assets/tutorials/install/mac7.webp 'L5 website download page with L5 Starter')
    8. Click **"Allow"** if it asks 'Do you want to allow downloads on "l5lua.org"?'
    ![Alert box asking permission to download L5-Starter](/assets/tutorials/install/mac8test.webp 'Alert box asking permission to download L5 Starter')
    9. Back in your downloads folder, **drag the L5-starter folder onto the Love application in the folder**. It should now launch and you should see a new window open with your code sketch.
    ![A yellow background window appearing on top of folder holding L5 Starter and love application](/assets/tutorials/install/mac9.webp 'A yellow background window appearing on top of folder holding L5 Starter and love application')

??? "Install with Linux"

    ## Install Linux

    This tutorial walks you through installing L5 with the Love (Love2d) framework on your Linux computer.

    On Linux, installation through the command line is common. Since Linux is an open source family of operating systems the exact process may need to be altered for your particular Linux distribution.

    **Install Love**

    Installing Love differs based on which Linux distribution you have.

    **Install Love on Debian/Ubuntu-based distributions**

    ```sh
    sudo add-apt-repository ppa:bartbes/love-stable
    sudo apt update
    sudo apt install love
    ```

    **Install Love on Arch Linux**

    ```sh
    sudo pacman -S love
    ```

    **Install Love on Red Hat/Fedora/CentOS**

    ```sh
    sudo dnf install love
    ```

    **Install Love on Void Linux**

    ```sh
    sudo xbps-install -S love
    ```

    **Additional options to install Love**

    Love can also be found in the package manager for [most other distributions](https://repology.org/project/love/versions), including BSD and Haiku OS, or installed via [FlatPak](https://flathub.org/en/apps/org.love2d.love2d), or as a portable AppImage or built from source. See the [Love2d](https://love2d.org) website or check your package manager for more information.

    **Download the L5 Starter project**

    Navigate to the directory where you'd like to save the L5-Starter folder and download the L5-Starter

    ```sh
    cd path/to/folder
    wget https://l5lua.org/L5-starter.zip
    ```

    Uncompress it

    ```
    unzip L5-starter.zip
    ```

    **To run your program**

    Navigate to your L5-Starter directory

    ```sh
    cd /path/to/L5-starter
    ```

    And run your program

    ```sh
    love .
    ```

    It should now launch and you should see a new window open with your code sketch running.
    <img src="/assets/tutorials/install/linux1.webp" alt="A yellow background window appearing on top of folder holding L5 Starter and love application" title="A yellow background window appearing on top of folder holding L5 Starter and love application" width="600" />

Congratulations! You've now installed Love and have L5 on your computer and verified you can run your own programs. 

## Running Your Programs

There are two ways to run a L5 program -- one method is using the desktop and the other uses the command line interface (CLI). If you are new to computing or are unsure about the CLI, then run from the desktop!

IDEs such as ZeroBrane Studio, Sublime Text, VS Code, Notepad++, and SciTE all support launching LÖVE programs (the engine to run our L5 scripts), though require additional setup configuration not covered here.

??? "Running L5 from the desktop"

    The easiest way to run your L5 program is to drag the **folder** containing your main.lua onto the Love2d application. Remember to drag the **folder** containing `main.lua`, and not `main.lua` itself.

    It should launch and open a new window with your sketch running in it, or print an error message. If you're running the L5 Starter program, you should see a square window with a yellow background. Congratulations.

    **By default, `print()` output only appears if you run your program from the command line. To display print output directly in your sketch window add `printToScreen()` to your `setup()` function.**

    *Once you have a sucessfully running program, you're ready for your next steps writing programs with L5. Check out [L5 for Processing-p5.js programmers](/L5-for-processingp5), [tutorials](/tutorials) or the [reference](/reference).*

??? "Running L5 from the command line"

    === "Windows Command line"
        You can launch your programs from the command line and add the `--console` flag to be able to see print() and error() output as well:
        ```
        "C:\Program Files\LOVE\love.exe" --console "C:\Users\<YourUsername>\Desktop\L5-starter"
        ```
        Replace `<YourUsername>` and `Desktop\L5-starter` with your actual username and the location of your program folder.

    === "macOS Command Line"

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

    === "Linux Command line"

        In the Terminal, you can run `love path/to/L5-starter`. Or if you are in the folder with your program, run `love .` to launch your project from the current directory.

*Instructions adapted from [Love2d wiki: Getting Started](https://www.love2d.org/wiki/Getting_Started), GNU Free Documentation License 1.3.*

Amazing! Now you are ready to start learning with [First Steps](/getting-started.md). If you are familiar with Lua, p5.js, or Processing already, you should take a look at [L5 for Processing-p5.js Programmers]().
