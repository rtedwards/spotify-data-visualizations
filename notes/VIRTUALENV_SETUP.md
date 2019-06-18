# Setup virtual environment
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
https://medium.com/@eleroy/jupyter-notebook-in-a-virtual-environment-virtualenv-8f3c3448247
https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/

# Create new virtualenvironment `env`
python3 -m venv env

# List Virtual Environments in Conda
conda info -e

# Activate `env`
source env/bin/activate
source activate /Users/Berto/anaconda3/envs/python36

# Install a Jupyter kernel
# This will install a kernel inside the environment, to use to run in the Jupyter notebook there
ipython kernel install --user --name=.env

# Run Jupyter, and select the .venv kernel to run the notebook
jupyter notebook

# Install packages to anaconda environment
https://www.geeksforgeeks.org/python-add-packages-to-anaconda-environment/
