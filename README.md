# Latest Release
Latest release is pre-release v0.1

[Releases Page](github.com/LaazV/ParsePlot/Releases)

# Usage


## Binary 

- Drag and drop any file with correct syntax to "parse.exe";
- A file named "custom.js" will be created;
- Open "index.html".

## Source Code

### Dependencies

```
julian.py
importlib
regex
``` 

- Run parse.py with the data file as its first argument;

```python ~\parse.py data.txt```

OR

- Drag and drop any file with correct syntax to "parse.py";
- A file named "custom.js" will be created;
- Open "index.html".


## Compiling

Install pyinstaller

```pip install pyinstaller```

```"\path\to\python\files\pyinstaller-script.py" parse.py```
