# Artifactory size comparison

This project aims to compare the artifactory instance and its tree in the zones of PA and VA.

**Table fo Contents:**

- [Artifactory size comparison](#artifactory-size-comparison)
  - [Initializing the project](#initializing-the-project)
    - [pipenv](#pipenv)
    - [global python or virtual environment](#global-python-or-virtual-environment)
  - [Running the project](#running-the-project)
    - [Setting environment variables:](#setting-environment-variables)


## Initializing the project

The project is tested on python `3.9`, but should work fine on all active versions
ranging from `3.7` to `3.10` with no or few refactoring.

You can install the project requirements using any of the following methods:

### pipenv

If you have pipenv and python `3.9` installed, you can simply run `pipenv install`
command and the project will be setup up.

You can check https://pipenv.pypa.io/en/latest/ for more details.

### global python or virtual environment
If you do not prefer to install pipenv (or even virtual environment), you can directly run the following command
in your working directory:

```shell
$ python -m pip install -r requirements.txt
```

**Note**: _Please do not forget to activate the virtual environment if you prefer to use the virtual environment._


## Running the project

before running the project do not forget to add 2 variables to the environment variables or create `.env` file
in the working directory.

### Setting environment variables:

in the terminal, you can simply run the following commands to add your environment variables:
```shell
$ export ARTIFACTORY_USERNAME="your_user_name"
$ export ARTIFACTORY_PASSWORD="your_password"
$ export ARTIFACTORY_URL_PA="https://your-pa-url.com"
$ export ARTIFACTORY_URL_VA="https://your-va-url.com"
```

or use `.env.sample` file as a template to create a `.env` file in your working directory.

You can simply run the following commands on your terminal (or with activated virtual environment)


**With Activated virtual environment:**
```shell
$ python main.py
```

**With pipenv:**
```shell
$ pipenv run main.py
```
