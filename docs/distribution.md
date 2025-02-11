We keep the latest stable release of the ```pyviz3d``` package available on [PyPy](https://packaging.python.org/tutorials/packaging-projects/).

## PyPi

Loosely following the instructions from [[1](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)]

```
$ pip install twine
```

In your home folder, set up `~/.pypirc`:

```
[distutils]
index-servers=
    pypi
    testpypi
[testpypi]
repository: https://test.pypi.org/legacy/
username: your username
```

To test the release without modifying the public PyPi release.
First, this creates `dist` and `pyviz3d.egg-info` folders which can then be uploaded to the pypi test repository given the correct credentials.

- Make sure to update the version in the `setup.py`, it has to be newer then the last uploaded one.
- If additional data files are added, update the `MANIFEST.in` file accordingly.
- Delete the previous dist files `rm -rf ./dist/*.tar.gz`
```
$ python setup.py sdist
$ twine upload --repository testpypi dist/*  # this is an alternative
$ pip install -i https://test.pypi.org/simple/ pyviz3d
```

When everything works, prepare a new release on github:
```
https://github.com/francisengelmann/pyviz3d/releases
```

After that, the public release can be added to the public PyPi repository:
```
$ python setup.py sdist
$ twine upload dist/*
```

## Anaconda
The Anaconda package is created from the pypi package
and is hosted on Anaconda Cloud
[[2]]( https://docs.anaconda.com/anaconda-cloud/user-guide/tasks/work-with-packages/)
```
$ conda install anaconda-client conda-build conda-verify
$ conda config --set anaconda_upload no
$ conda skeleton pypi pyviz3d
$ conda build pyviz3d
```
