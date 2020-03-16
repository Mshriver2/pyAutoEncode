# pyAutoEncode
Make your encodes a breeze with python.

## Installation
Install AutoHotkey v1.2+  
Install Python 2.7  
Install Pip Packages:  
```shell
pip install pynput
pip install clipboard

optional:
pip install pyfiglet
```

## Usage
Execute wav2ac3.ahk  
Run "python encode.py" in a terminal and follow the prompts.

## Contributing
To begin Contributing to this project follow these commands.

```shell
git clone https://github.com/Mshriver2/pyAutoEncode.git
cd pyAutoEncode/
```

## TODO
* ~~Find a way to execute avs2yuv script in a git-bash terminal using Python~~
* ~~use unique .avs file names to allow multiple encodes at once~~
* ~~create a function to convert the wav files to ac3 with sound forge~~
* ~~finish ahk file that executes sound forge commands~~
* ~~add a function that allows you to run a test encode and returns the estimated file size~~
* ~~create checks in the functions to check if the ac3 file, wav file, encode mkv file, or avs file already exits~~
* create a function to take screenshots using AvspMod or a CLI screenshot tool (ffmpeg or screengen in awsmfunc for CLI screens)
* use the aimg api to upload screenshots Automatically - https://img.awesome-hd.me/settings
* add build status shields to readme - https://shields.io/
* add screenshots to readme
* create and add a banner image to the top of readme


## FAQ
Q. Can I adjust the x264 command?  
A. Yes you may adjust the x264 from config file (insert file name here)

Q. Where can I find my API key for the AHD img auto screenshot upload?  
A. Login to https://img.awesome-hd.me/settings

Q. Does this script working on Windows Server?  
A. Yes but you may have to follow the install instructions in the optional folder.

Q. Why is my Sound Forge opening the wrong folder and or saving to the wrong folder?  
A. You have to open Sound Forge manually the first time and open a file where your wav files are located, and
manually save the file into the directory where you want it next time. After doing this it use the correct directory's
automatically through the script the next time.

## Credits
mshriver2  
sd31117
