# Test suite in this repo is based on chrome browser
# Install needed libraries by Chrome Driver
```
sudo apt install libgconf-2-4 libatk1.0-0 libatk-bridge2.0-0 libgdk-pixbuf2.0-0 libgtk-3-0 libgbm-dev libnss3-dev libxss-dev
```
after installation make sure to run 
```
/home/<username>/.wdm/drivers/chromedriver/linux64/110.0.5481/chromedriver --version and it actually displays the version without errors
```
# To download and install chrome
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt -y install ./google-chrome-stable_current_amd64.deb
```
# Set a symbolic link from Windows Chrome to WSL as per ChromeDrivere requirements: 

https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver/01fde32d0ed245141e24151f83b7c2db31d596a4#requirements 

```
sudo ln -s '/mnt/c/Program Files/Google/Chrome/Application/chrome.exe' /usr/bin/google-chrome
```
# First you will need to configre your email and password in src/config.in
# Second run setup_venv.sh then run_test.sh to run pylint and pytest
# You also have the option to run the tests seperately by running 
```
. .venv/bin/activate
.venv/bin/python main.py
deactivate
```