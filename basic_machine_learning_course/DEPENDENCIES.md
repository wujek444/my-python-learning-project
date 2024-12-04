Pre dependencies download configuration:
* Add hosts to trusted hosts in pip: ```pip config set global.trusted-host "pypi.org files.pythonhosted.org pypi.python.org"```
* Update pip: ```python -m pip install --upgrade pip```

Dependencies:
* Data analysis: ```pip install pandas```
* Connecting to Oracle DB: ```pip install oracledb sqlalchemy```
* scikit-learn - data modeling library (+ required dependencies): ```pip install numpy scipy scikit-learn```
* Python wrapper (optional): ```pip install IPython```

Pip install all dependencies:
```pip install pandas oracledb sqlalchemy numpy scipy scikit-learn IPython```