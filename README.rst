Dynamic Python Path for python
==============================

Dynamic Python Path, dpythonpath, dynamically loading and setting pythonpath through a config file and code. The code use the configuration can be freely moved to different location.

Installation
------------

Install using pip::

    pip install dpythonpath


Usage
-----

Python::

    1) startup program call dpythonpath.set_config_file(conf_file='my_path.yml')
       This may not needed, the file can be placed under where .git located, and discovered by dpythonpath
       project
         .git
         dpythonpath/
            config.yml
       only if your put config.yml w/ different name or under different directory other than under dpythonpath/
       then user need to call dpythonpath.set_config_file(conf_file='') method

    2) any other python code just call dpathpath.set_path('id')


Contributing
------------

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

License
-------
`MIT <https://choosealicense.com/licenses/mit/>`_
