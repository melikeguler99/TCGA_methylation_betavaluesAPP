# ShinyApp for Visualizing Beta Values from Methylation Arrays

## Overview

With this ShinyApp, you will be able to easily visualize your data, including beta values from methylation arrays downloaded using the **TCGA (The Cancer Genome Atlas)** database. The app allows you to upload one or more `.txt` files containing methylation beta values and generates sophisticated density plots to help analyze the methylation status of your data. The density plots are color-coded based on methylation levels, classified as:
- **Hypomethylated (UM)**: β-value range of 0 to 0.2 (green)
- **Hemimethylated (HM)**: β-value range of 0.2 to 0.8 (blue)
- **Hypermethylated (M)**: β-value range of 0.8 to 1.0 (purple)

This application makes it easy to analyze and compare the methylation status of different samples or CpG sites in your datasets.

## Features
- **Multiple file upload**: You can upload one or more `.txt` files at once.
- **Density Plot Generation**: The app generates density plots for each file to visualize the distribution of beta values across the methylation levels.
- **NA value handling**: Option to remove rows with NA values.
- **Color-coded visualization**: Methylation levels are represented with distinct colors for each classification (UM, HM, M).

## Prerequisites

- **Python 3.x** (Preferably 3.7+)
- **Required Libraries**:
  - `shiny` (for the interactive web application)
  - `pandas` (for data manipulation)
  - `seaborn` (for generating density plots)
  - `matplotlib` (for plot customization)

You can install the required libraries by running the following command:

```bash 
pip install shiny pandas seaborn matplotlib
```

How to Use the App

Launch the App:
Run the following command in the terminal:
```bash 
shiny run BetApp.py
```
Upload Data:
In the app's interface, click the "Choose Files" button to select one or more .txt files that contain the methylation beta values. Ensure that the files are tab-separated (with a CpG site identifier in the first column and the beta value in the second).
Generate Plots:
After selecting your files, click the "Generate Plots" button. The app will display density plots for each file, with the beta values grouped and color-coded by methylation levels (UM, HM, M).
Preview Data:
The app will also display a preview of the first few rows of the data from the uploaded files for verification.
File Format

The input files should be in .txt format with two columns:

CpG Site: Identifiers for the CpG sites.
Beta Value: The methylation beta values.

```bash
Example format:

cg00000292  0.877321206559696
cg00002426  0.963570230530168
cg00003994  0.021860620895483
...

```
