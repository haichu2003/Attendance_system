# Instruction on how to install and run the GUI
## For developers

In the terminal, run
```
pip install pillow qreader opencv-python openpyxl
```

Try to run the application
```
python GUI.py
```

If there is problem with pyzbar (ImportError related with `lizbar-64.dll`)  

### On window
install [vcredist_x64.exe](https://www.microsoft.com/en-gb/download/details.aspx?id=40784) from the _Visual C++ Redistributable Packages for Visual Studio 2013_  

### On linux
```
sudo apt-get install libzbar0
```

### On MacOS
```
brew install zbar
```

## For other users
pending...