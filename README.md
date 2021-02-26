text_classification_demo
==============================

 A sample code to demonstrate basic multi label text classification using Spacy & SKLearn.

Project Organization
------------


    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks. "Multi classification-data.ipynb" is our main script file. 
    │
    ├── environment.yml   <- The configuration file for reproducing the analysis environment. Do check the "Posterior configuration" below, once the environment is created.
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   │
    │   ├── funct           <- Custom package to read source csv file
    	      └── read_data.py


Posterior configuration
-----------------------

Please execute these in your enviornment once it has been created with the yml file:

python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md


Please do ensure your are in the project's root directory before executing the below command:

pip install -e .

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
