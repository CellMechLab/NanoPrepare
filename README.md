# NanoPrepare 
Simple graphical user interface (GUI) to screen and pack nanoindentation curves for further analysis.

## Introduction 
This GUI  is designed to open nanoindentation data (force-displacement curves), screen them (eliminating bad curves) and packing them together in a bundle .json file to be used for further analysis. This packaged .json file can be opened and processed using the nanoindentation project: https://github.com/CellMechLab/nanoindentation. 

## Documentation 
A step-by-step guide and video tutorials on how to use the software is avilable in our recent paper:

- Ciccone, G., Azevedo Gonzalez Oliva, M., Antonovaite, N., Lüchtefeld, I., Salmeron-Sanchez, M. and Vassalli, M., 2021. Experimental and data analysis workflow for soft matter nanoindentation. Journal of Visualized Experiments (10.3791/63401
).

## Supported file types 
Right now, the following manufacturers' formats are supported: Optics 11 .txt files (both old and new versions are supported) and NanoSurf .txt files, and other standard AFM formats provided through the afmformats library.

## Installation 
No installer is currently provided. In order use the GUI, a Python 3 environment with the following packages is required: PyQt5, NumPy, SciPy, PyQtGraph.

## Running the GUI 
In order to access the GUI, run the prepare file from the command line:
```bash
python prepare.py 
```

## Citation 
If you use this software in your publication and research, please cite the following papers: 

- Ciccone, G., Azevedo Gonzalez Oliva, M., Antonovaite, N., Lüchtefeld, I., Salmeron-Sanchez, M. and Vassalli, M., 2021. Experimental and data analysis workflow for soft matter nanoindentation. Journal of Visualized Experiments (10.3791/63401
).

- Lüchtefeld, I., Bartolozzi, A., Mejía Morales, J., Dobre, O., Basso, M., Zambelli, T. and Vassalli, M., 2020. Elasticity spectra as a tool to investigate actin cortex mechanics. Journal of nanobiotechnology, 18(1), pp.1-11 (doi.org/10.1186/s12951-020-00706-2).

