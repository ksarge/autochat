## Installation
- Create and activate a python virtual environment (google it)
- Run `pip install -r requirements.txt`

## Usage
`python3 autochat/application.py`

Waits 5 seconds (this is when you need to put your cursor where you need the text sent), and then runs your command until you press stop. The enter key is automatically pressed after the command. The time between each command is a randomly generated value (in seconds) in between the two times provided to the GUI.


## Pics
![Alt text](screenshots/main_display.png?raw=true "Optional Title")


## Newlines and Scripting
The command can be broken into chunks by separating each part you want on separate lines with a semicolon.
`hello;world`
This would result in the following being written to the screen:
```
hello
world
```

You can also call out to custom commands implemented in `commands.py`. 

`+buy huge jug pack;{sleep 1};confirm`

This would result in the following being written to the screen with a 1 second delay in between the first line and the second line:
```
+buy huge jug pack
confirm
```
