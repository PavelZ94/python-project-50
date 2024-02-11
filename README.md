### Hexlet tests and linter status:
[![Actions Status](https://github.com/PavelZ94/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/PavelZ94/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/ee16b9a0af33f0b990c8/maintainability)](https://codeclimate.com/github/PavelZ94/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/ee16b9a0af33f0b990c8/test_coverage)](https://codeclimate.com/github/PavelZ94/python-project-50/test_coverage)

[![Python CI](https://github.com/PavelZ94/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/PavelZ94/python-project-50/actions/workflows/main.yml)

# Difference calculator

This is the second learning project.
It is CLI program to show the differences between two **JSON** of **YAML** files in next formats:
- stylish;
- plain;
- json.

## Installation:
To install the package you should have:
- Python 3.10+
- poetry

After you are sure that all programs are installed follow these steps:
- ```make install```
- ```make build```
- ```make package-reinstall```

## Commands to show the differences between files:
```gendiff <file_path1> <file_path2> --format <format>```

then:
- *< format >* - stylish/plain/json;
- *<file_path1>* - path of first file;
- *<file_path2>* - path of second file.

## Other useful commands:
```gendiff -h``` - shows help of using program


## Showing the project's work:

### Showing diffs between two flat .json files:
[![asciicast](https://asciinema.org/a/NOpxG6RrTPD0NvW8RP3C0uxJe.svg)](https://asciinema.org/a/NOpxG6RrTPD0NvW8RP3C0uxJe)

### Showing diffs between two flat .yml files:
[![asciicast](https://asciinema.org/a/cAPt71M6dzjKnfRQA6n33SZGl.svg)](https://asciinema.org/a/cAPt71M6dzjKnfRQA6n33SZGl)

### Showing diffs between two stylish .json and .yml files:
[![asciicast](https://asciinema.org/a/MPUod5brz5WMi1RDGRnKq7RtC.svg)](https://asciinema.org/a/MPUod5brz5WMi1RDGRnKq7RtC)

### Showing diffs between two files in plain format:
[![asciicast](https://asciinema.org/a/jjoPUNJ38PUeYcrN8P82ckDyy.svg)](https://asciinema.org/a/jjoPUNJ38PUeYcrN8P82ckDyy)

### Showing diffs between two files in json format:
[![asciicast](https://asciinema.org/a/FUK8POkczi9XcHGj824M5oVnd.svg)](https://asciinema.org/a/FUK8POkczi9XcHGj824M5oVnd)
