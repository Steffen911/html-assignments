# Hot Topics in Machine Learning Assignments

This repository contains the assignments for the course [IE 674 Hot Topics in Machine Learning](http://dws.informatik.uni-mannheim.de/en/teaching/courses-for-master-candidates/ie-674-hot-topics-in-machine-learning/)
at the University of Mannheim in the fall semester 2017.

## Assignments

- Linear Regression (Sep 29 - Oct 18): [html17-a1-stefschm](https://s3.eu-central-1.amazonaws.com/steffen911-papers/html17-a1-stefschm.pdf)
- Naive Bayes (Oct 19 - Nov 05): [html17-a2-stefschm](https://s3.eu-central-1.amazonaws.com/steffen911-papers/html17-a2-stefschm.pdf)
- Graphical Models (Nov 03 - Nov 26): [html17-a3-stefschm](https://s3.eu-central-1.amazonaws.com/steffen911-papers/html17-a3-stefschm.pdf)
- Neural Networks (Nov 23 - Dec 05): [html17-a4-stefschm](https://s3.eu-central-1.amazonaws.com/steffen911-papers/html17-a4-stefschm.pdf)

## Building the documents

Go into the respective folder and run `xelatex FILENAME.tex` or `/bin/bash build.sh` in the
corresponding subdirectory.

## Running the notebooks

The notebooks are build using the [jupyter/jupyter-notebook](https://hub.docker.com/r/jupyter/tensorflow-notebook/).

Start the docker image with `docker run -dp 8888:8888 --name notebook jupyter/tensorflow-notebook` to run jupyter locally with all dependencies.
It might be necessary to install further Python packages. Stick to the references in the notebooks.

Open Jupyter in the browser and import the .ipynb file and the input data from the UI.

Use `docker logs notebook` to get the browser URL with auth token.
