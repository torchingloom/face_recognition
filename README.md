# FACE RECOGNITION

## Install OpenCV for Python on Mac OS X
```
brew tap homebrew/science
brew install opencv
brew list opencv | grep -E  "cv.*\.(py|so)"
for _ in $( brew list opencv | grep -E  "cv.*\.(py|so)" );
do
    ln -s $_ $( python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())" )
done
ls -lah $( python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())" ) | grep -E  "cv.*\.(py|so)"
```


## Install app
```
python setup.py install|devepol
```


## Run
```
%PYTHON_PATH%/bin/face_recognition %path/to/img%
```
