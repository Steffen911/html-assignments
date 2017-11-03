# Hot Topics in Machine Learning Assignments

This repository contains the assingments for the Hot Topics in Machine Learning
course at the University of Mannheim in the fall semester 2017.

## Assignments

- Linear Regression (Sep 29 - Oct 18): html17-a1-stefschm
- Naive Bayes (Oct 19 - Nov 05): html17-a2-stefschm
- Graphical Models (Nov 03 - Nov 26): html17-a3-stefschm

## Building the documents

Go into the respective folder and run `xelatex FILENAME.tex` or `/bin/bash build.sh`

## Running the notebook

The notebooks are build using the [jupyter/scipy-notebook](https://hub.docker.com/r/jupyter/scipy-notebook/).

Start the docker image with `docker run -dp 8888:8888 --name notebook jupyter/scipy-notebook` to run jupyter locally with all dependencies.

Run `docker cp /path/to/data notebook:/tmp` to move the data into the notebook. Open the jupyter
in the browser afterwards and import the .ipynb file from the UI.

Use `docker logs notebook` to get the browser URL with auth token.
