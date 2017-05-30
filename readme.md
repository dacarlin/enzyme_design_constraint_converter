# Enzyme design constraint converter tool 

Convert your Rosetta enzyme design style constraints to regular Rosetta constraints using these scripts. 

## Input files 

To use these scripts, you need:  

- PDB file containing enzyme design header, protein coordinaties, and ligand coordinates
- params file, conformer file for ligand (if necessary) 
- enzyme design constraint file

## Run the example 

Change into `example_run`, edit `sub.sh` to point to your local copy of Rosetta, and run `bash sub.sh`. The output constraint file is called `example_output.cst`. 

## Instructions for use  

First, make a new directory to keep your files in. Copy the example files in and edit the provided `example_flags` text file to use your input files instead of the example. 

Next, edit `sub.sh` to point to your local copy of Rosetta and your flags file. 

Run the tool with 

```bash
bash sub.sh
``` 

and your output files will appear in your working directory. The output constraint file is called `example_output.cst` by default, but you can edit this in `protocol.xml`. 
