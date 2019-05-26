# Setup virtual environment
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
https://medium.com/@eleroy/jupyter-notebook-in-a-virtual-environment-virtualenv-8f3c3448247

# Create new virtualenvironment `env`
python3 -m venv env

# Activate `env`
source env/bin/activate

# Install a Jupyter kernel
# This will install a kernel inside the environment, to use to run in the Jupyter notebook there
ipython kernel install --user --name=.env

# Run Jupyter, and select the .venv kernel to run the notebook
jupyter notebook
