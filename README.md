# NanoPrepare 
Simple graphical user interface (GUI) to screen and pack nanoindentation curves for further analysis.

## Introduction 
This GUI  is designed to open nanoindentation data (force-dispplacement curves), screen them (eliminating bad curves) and packing them together in a bundle .json file to be used for further analysis. This packaged .json file can be opened and processed using the nanoindentation project: https://github.com/CellMechLab/nanoindentation. 

## Supported file types 
Right now, the following manufacturers' formats are supported: Optics 11 .txt files (both old and new versions are supported) and NanoSurf .txt files. 

## Installation 
No installer is currently provided. In order use the GUI, a Python 3 environment with the following packages is required: PyQt5, NumPy, SciPy, PyQtGraph.

## Running the GUI 
In order to access the GUI, run the prepare file from the command line:
```bash
python prepare.py 
```
