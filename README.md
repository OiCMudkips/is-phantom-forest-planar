# Is the Phantom Forest planar?

Apparently not.

```
?/is-phantom-forest-planar > make virtualenv_run
python3 -m venv virtualenv_run
?/is-phantom-forest-planar > source virtualenv_run/bin/activate
(virtualenv_run) ?/is-phantom-forest-planar > make install
pip install -rrequirements-dev.txt
Collecting Cython==0.29.24
  Using cached Cython-0.29.24-cp39-cp39-macosx_10_9_x86_64.whl (1.9 MB)
Installing collected packages: Cython
Successfully installed Cython-0.29.24
cd planarity && pip install .
Processing /Users/victorzhou/is-phantom-forest-planar/planarity
Requirement already satisfied: setuptools in /Users/victorzhou/is-phantom-forest-planar/virtualenv_run/lib/python3.9/site-packages (from planarity==0.4.1) (54.2.0)
Using legacy 'setup.py install' for planarity, since package 'wheel' is not installed.
Installing collected packages: planarity
    Running setup.py install for planarity ... done
Successfully installed planarity-0.4.1
(virtualenv_run) ?/is-phantom-forest-planar > ./twisted_forest_planarity.py 
Is phantom forest (detailed maps) planar?: False
Is phantom forest (simple map) planar?: False
```
