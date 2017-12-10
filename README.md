*author: Stas Turanskyi*

# PBC-tasks
# Pyton Bootcamp tasks folder

## Day 1


### *Vagrantfile*
Addeded config file for Vagrant with specified IP 192.168.33.10 and VM name "pospravahatqc".

To run VM:

install Vagrant
copy vagrantfile to VM directory
* run `vagrant up` to start vm in Virtual box with IP 192.168.33.10 and VM name "pospravahatqc"
* run `vagrant halt` to stop vm.

### 
*day1_code.py
* `fib_n`
To get fibonacci sequence run it with parameter of sequence size. Return list of values. Return empty list if parameter less or equal 0. Return empty set if paramenter is not int.

* `arnums`
Return set of unique pairs with specified sum. Return empty set if no any pairs with specified sum

## Day 2

### *Unit tests*
* added with code to unit test file for "fib_n(n)" for pytest
* added with code to unit test file for "arnums(*args)" for pytest

### *Virtual environment*
* added provision section to vargantfile

Preparing the virtual environment for project.
* creation before use `python -m venv venv`.
* activate by run source `venv/bin/activate.bat`
* to install packages from saved `pip install -r requirements.txt`.

### *Config updates*
- File Requirements.txt updated with `pytest`, `selenium`.

## Day 3
### Structuring project:

```
├── README.md               <- This file. Contains all information need to know to work with this code
├── app_code                <- Main package for Code
├── tests                   <- Main package for Tests
└── requirements.txt        <- Contains all required dependencies
```


### Add parametrize tests:

```
└── tests                  
```
  test file  `test_arnums_param.py`
  

```
	PAIRSSET = [
    ([2, 6, 7, 9, 0], 0, ( )),
    ([3, 7, 10, 2, 2, 1], 1, [(3, 7)]),
    ([1, 9, 5, 5, 3, 8], 2, [(1, 9), (5, 5)]),
    ([1, 9, 5, 5, 3, 7, 7, 3, 5, 5, 9, 1], 3, [(1, 9), (3, 7), (5, 5)])
]
@pytest.mark.arnums`
@pytest.mark.parametrize("number_list,count,pairs", PAIRSSET)`
```

* test file: test_fibo_param.py

```
FIBOSET = [
    ( 2, 2, [0, 1]),
    ( 3, 3, [0, 1, 1]),
    ( 5, 5, [0, 1, 1, 2, 3]),
    ( 15, 15, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])
]  
@pytest.mark.arnums
@pytest.mark.parametrize("number_list,count,pairs", FIBOSET)
```

## Day 4:
Decorator module added. Contains basic example with log usage.
```
└── app_code
	decorator_app.py
```
