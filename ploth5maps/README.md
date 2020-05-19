# Plotting pixel maps from HDF5 files

This tool generates an animated gif of the traffic flow in a city during one day using maps pixel based.

## How to use
There is a dummy file created to show how to use the libraries:

```
python run.py -i <input file> -c <channel>
```
*Parameters:*
* **-i , --input:** HDF5 file with the information about the traffic flow. There are some example files in *input/datasets*.
* **-c, --channel:** Refers to the channel selected to plot [0-red, 1-green, 2-blue].

At the end of the process the animated gif must be generated into the directory **output/gifs** with the same name of the source file.
