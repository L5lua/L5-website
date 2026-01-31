# Installation on Linux

This tutorial walks you through installing L5 with the Love (Love2d) framework on your Linux computer.

On Linux, installation through the command line is common. Since Linux is an open source family of operating systems the exact process may need to be altered for your particular Linux distribution.

## Install Love

Installing Love differs based on which Linux distribution you have.

### Install Love on Debian/Ubuntu-based distributions

```sh
sudo add-apt-repository ppa:bartbes/love-stable
sudo apt update
sudo apt install love
```

### Install Love on Arch Linux

```sh
sudo pacman -S love
```

### Install Love on Red Hat/Fedora/CentOS

```sh
sudo dnf install love
```

### Install Love on Void Linux

```sh
sudo xbps-install -S love
```

### Additional options to install Love

Love can also be installed in OpenSUSE, Gentoo, Solus, NixOS, via FlatPak on any distribution with Flatpak, or as a portable AppImage or built from source. See the [Love2d](https://love2d.org) website or check your package manager for more information.

## Download the L5 Starter project

Navigate to the directory where you'd like to save the L5-Starter folder and download the L5-Starter

```sh
cd path/to/folder
wget https://l5lua.org/L5-starter.zip
```

Uncompress it

```
unzip L5-starter.zip
```

## To run your program

Navigate to your L5-Starter directory

```sh
cd /path/to/L5-starter
```

And run your program

```sh
love .
```

It should now launch and you should see a new window open with your code sketch running.
![A yellow background window appearing on top of folder holding L5 Starter and love application](/assets/tutorials/install/linux1.webp "A yellow background window appearing on top of folder holding L5 Starter and love application")

**Next steps:** You've installed Love and have L5 on your computer and verified you can run your own programs. Check out [Getting Started](/getting-started) or the [tutorials](index.md) to learn more.

