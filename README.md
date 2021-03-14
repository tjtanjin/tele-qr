<p align="center">
  <img src="https://i.imgur.com/IgYuZcu.png" />
  <h1 align="center">Tele QR</h1>
</p>

## Table of Contents
* [Introduction](#introduction)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)
* [Team](#team)
* [Contributing](#contributing)
* [Others](#others)

### Introduction
Tele QR is a simple telegram bot that allows users to easily generate QR codes for text/links. Using it is as simple as dropping a text message to the [bot](https://t.me/teleqrbot)! The link is also shared below:
```
https://t.me/teleqrbot
```

### Features
Tele QR currently takes in a text message and generates a `.png` QR code for it.

### Technologies
Technologies used by Tele QR are as below:
##### Done with:

<p align="center">
  <img height="150" width="150" src="https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png"/>
</p>
<p align="center">
Python
</p>

##### Deployed on:
<p align="center">
  <img height="150" width="150" src="https://pbs.twimg.com/profile_images/1089877713408557056/aO_IAlp__400x400.jpg" />
</p>
<p align="center">
Upcloud
</p>

##### Project Repository
```
https://github.com/tjtanjin/tele-qr
```

### Setup
The following section will guide you through setting up your own Tele QR (telegram account required).
* First, head over to [BotFather](https://t.me/BotFather) and create your own telegram bot with the /newbot command. After choosing an appropriate name and telegram handle for your bot, note down the bot token provided to you.
* Next, cd to the directory of where you wish to store the project and clone this repository. An example is provided below:
```
$ cd /home/user/exampleuser/projects/
$ git clone https://github.com/tjtanjin/tele-qr.git
```
* Following which, create a config folder and within it, create a token.json file, saving the token you received from [BotFather](https://t.me/BotFather) as a value to the key "token" as shown below:
```
{"token": "your bot token here"}
```
* You will also have to create an empty `images` folder to temporarily store the QR code image to be sent to the user:
```
$ mkdir images
```
* Finally, from the base directory of the project, execute the following command and the terminal should print "running..." if everything has been setup correctly!
```
$ python3 main.py
```
* If you wish to host your telegram bot online 24/7, do checkout the guide [here](https://gist.github.com/tjtanjin/ce560069506e3b6f4d70e570120249ed).

### Team
* [Tan Jin](https://github.com/tjtanjin)

### Contributing
If you have code to contribute to the project, open a pull request and describe clearly the changes and what they are intended to do (enhancement, bug fixes etc). Alternatively, you may simply raise bugs or suggestions by opening an issue.

### Others
For any questions regarding the implementation of the project, please drop an email to: cjtanjin@gmail.com.
