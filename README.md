# Content

- [Content](#content)
- [Description](#description)
- [Prerequisites](#prerequisites)
    - [Visual Studio Code](#visual-studio-code)
    - [Caja](#caja)
    - [Caja-python](#caja-python)
    - [Caja-pyextensions](#caja-pyextensions)
- [Installation](#installation)
- [Compatibility](#compatibility)
- [To do list](#to-do-list)


# Description

This caja extension allows to open vscode on current directory just through the right-clicking.

![](img/des_1.png)
![](img/des_2.png)

The Python extension scripts are stored at

> ~/.local/share/caja-python/extensions/


# Prerequisites

## Visual Studio Code

The simplest way to install VS code is to download and install the package from [VS code official website](https://code.visualstudio.com/#alt-downloads)

## Caja

Caja is default file manager for mate desktop environment. If not installed yet, run
```console
$ sudo apt-get install caja
```

## Caja-python

One can install caja-python through running the following command
```console
$ sudo apt-get install caja-python
```

## Caja-pyextensions

Caja-pyextensions can be easily installed by one line command
```console
$ sudo apt-get install caja-pyextensions
```

alternatively, one can download and install the package from the [link](http://www.giuspen.com/software/caja-pyextensions_3.4.1-1_all.deb)

If the link is broken, refer to
https://www.giuspen.com/nautilus-pyextensions/


# Installation

1. Run Pyextension by clicking application icon or runnnig the command
![](img/ins_1.png)
```console
$ caja-pyextensions
```
2. Click "Add A PyExtension"

![](img/ins_2.png)

3. Download the cource code and chose "open-vscode-here.py"

![](img/ins_3.png)

4. Click the active box

![](img/ins_4.png)

5. Close Caja PyExtensions then restart Caja file manager
6. Go to Preference -> Extensions, then click the open-vscode-here extension

![](img/ins_5.png)

7. It should work after restarting Caja again

# Compatibility

This program only has been tested in Linux Mint 18.3. But it should work in any OS installed with the prerequisites.


# To do list

- [x] add installation guide
- [x] add more description