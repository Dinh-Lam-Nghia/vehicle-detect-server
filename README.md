# Vietnamese License Plate Recognition

This repository provides you with a detailed guide on how to training and build a Vietnamese License Plate detection and recognition system. This system can work on 2 types of license plate in Vietnam, 1 line plates and 2 lines plates.

## Installation

```bash
  git clone https://github.com/Marsmallotr/License-Plate-Recognition.git
  cd License-Plate-Recognition

  # install dependencies using pip 
  pip install -r ./requirement.txt
```

## run

  ```python
  flask run -h "IPv4 Address"
#  flask run -h 192.168.1.29
# python webcam.py
  ```

### err
```err

   Traceback (most recent call last):
    File "<frozen runpy>", line 198, in _run_module_as_main
    File "<frozen runpy>", line 88, in _run_code
    File "C:\Users\adminln\AppData\Roaming\Python\Python311\site-packages\flask\__main__.py", line 3, in <module>
      main()
    File "C:\Users\adminln\AppData\Roaming\Python\Python311\site-packages\flask\cli.py", line 1105, in main
      cli.main()
   ......................
   ...........
    File "<frozen importlib._bootstrap_external>", line 936, in exec_module
    File "<frozen importlib._bootstrap_external>", line 1073, in get_code
    File "<frozen importlib._bootstrap_external>", line 1130, in get_data
   FileNotFoundError: [Errno 2] No such file or directory: '[......]\\vehicle-detect-server\\yolov5\\hubconf.py'

```
**fix_err**

  - Download yolov5 (old version) from this link: [yolov5 - google drive](https://drive.google.com/file/d/1Vv_N_KgGrELZg7ratC-JewzzhQM1q4kg/view?usp=sharing)
  - Copy yolov5 folder to project folder



