<p align="center">
  <img width=300 src="https://i.imgur.com/IgYuZcu.png" />
  <h1 align="center">Tele QR</h1>
</p>

<p align="center">
  <img src="https://github.com/tjtanjin/tele-qr/actions/workflows/docker-hub.yml/badge.svg" />
  <img src="https://github.com/tjtanjin/tele-qr/actions/workflows/deployment.yml/badge.svg" />
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

##### Project Repository
```
https://github.com/tjtanjin/tele-qr
```

### Setup
The following section will guide you through setting up your own Tele QR (**[telegram](https://web.telegram.org/) account required**).
1) First, head over to [BotFather](https://t.me/BotFather) and create your own telegram bot with the `/newbot` command. After choosing an appropriate name and telegram handle for your bot, note down the **bot token** provided to you.
2) Next, `cd` to the directory of where you wish to store the project and clone this repository. An example is provided below:
    ```
    cd /home/user/exampleuser/projects/
    git clone https://github.com/tjtanjin/tele-qr.git
    ```
3) Once the project has been cloned, `cd` into it and install required dependencies with the following command:
    ```
    python3 -m pip install --no-cache-dir -r requirements.txt
    ```
4) Following which, create (or copy) a *.env* file at the root of the project using the provided [*.env.template*](https://github.com/tjtanjin/tele-qr/blob/master/.env.template). In order to run the bot, the bare minimum that needs to be done is for you to replace the **BOT_TOKEN** variable within the *.env* file with the token you received from [BotFather](https://t.me/BotFather).
5) You can also feel free to modify the other variables as you deem fit. Clear descriptions for the variables have been included in the [*.env.template*](https://github.com/tjtanjin/tele-qr/blob/master/.env.template) file.
6) You will also have to create an empty *images* folder in the root directory of the project to temporarily store the QR code image to be sent to the user:
    ```
    mkdir images
    ```
7) Finally, head to the root of the project and execute the following command to launch your bot:
    ```
    $ python3 main.py
    ```

### Deployment

#### Docker
For deployment, Docker is the preferred approach, especially if you would like to avoid the hassle of manually installing dependencies. If you are unfamiliar with docker, it is recommended you go through a quick tutorial for it first. This section **will not** dive into the details of docker usage.

1) First, if you have not done so, create a *.env* file from the provided [*.env.template*](https://github.com/tjtanjin/tele-qr/blob/master/.env.template) and update the variables (at the very least, you need to input a valid **BOT_TOKEN**). 
2) If you using the project as it is (**i.e. no intended code changes**), then simply run `./deploy.sh tele-qr` within the scripts folder and your deployment will be automatically done! Otherwise, if you wish to make code changes to the project, please read on.
3) Once you are done with your code changes, you would have to build your own docker image with the following command (take note to replace the tag `-t` with that of your own):
    ```
    docker build -t tjtanjin/tele-qr .
    ```
4) Upon obtaining your image, you may then start your container with the following command (remember to replace image name below if you built your own image):
    ```
    docker run -d --name qr --env-file .env tjtanjin/tele-qr:master
    ```
    Note: Notice that the *.env* file we configured in **step 1** is being passed via the `--env-file` argument. This is true for the auto deployment in **step 2** as well. Hence, ensure that you have setup your configuration properly before passing in the file.
5) Finally, you may wish to **update the deployment script** to reference your own image/container if you would like to have an easier deployment workflow.

#### Manual
Alternatively, if you are unfamiliar with docker or would like a more manual approach, you may also follow the guide [here](https://tjtanjin.medium.com/how-to-host-a-telegram-bot-on-ubuntu-a-step-by-step-guide-a38fb8c04f72) to setup the bot 24/7. Note that you would have to go through the steps in the [setup](#setup) section to setup the project manually as well.

### Team
* [Tan Jin](https://github.com/tjtanjin)

### Contributing
If you have code to contribute to the project, open a pull request and describe clearly the changes and what they are intended to do (enhancement, bug fixes etc).

Alternatively, you may contact me via [**discord**](https://discord.gg/X8VSdZvBQY) or simply raise bugs or suggestions by opening an [**issue**](https://github.com/tjtanjin/tele-qr/issues).

### Others
For any questions regarding the implementation of the project, you may reach out on [**discord**](https://discord.gg/X8VSdZvBQY) or drop an email to: cjtanjin@gmail.com.
