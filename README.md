# PyXmlParser - Python XML Parser


## Project Motivation


We have tons of parsers today. Most good. But I did not find a parser that parses insanely large files, not without paying for it anyway.

This project is mainly deals with such a situation. If your file is small. Welcome! Although there are a lot if other utilities out there too that might even be
faster.

pyxmlparser is tested against a file 100 GB in size. Did quite well. Please note that since we iteratively scan through the majority of the file pyxmlparser is a little slower.

But then again there is no such thing as a free lunch. This project is an attempt to avoid those memory errors that can drive anyone against the wall.


This project is called pyxmlparser for now. Ultimately the goal is to deal with other formats as well.


[![PyPI version](https://badge.fury.io/py/pyxmlparser.svg)](https://badge.fury.io/py/pyxmlparser)

Python Module to convert XML to csv. Project under developement. Not a stable release.
Subsequent versions will be able to convert the files to different formats.
Works Extremely well with Large XML files.



### Prerequisites

python version 3.4 or above
lxml
click

### Installing -

```python
pip install pyxmlparser
```
Navigate to the folder where the XML file is present on the terminal. 
call the function pyxmlparser with the other required inputs.
Eg: pyxmlparser xml_filename output_csv_name.csv xpathstring_csvcolumns.txt --encoding='xml-file-encoding'

## Deployment Notes

This is not a Stable Release.The project is currently under development

please follow this github link for updates: https://github.com/takauchisora/pyxmlparser

## Versioning

Follow the GitHub Link for updates. 

https://github.com/takauchisora/pyxmlparser

Pull Requests are welcome. Please create a separate branch.

Some rules:

- Try to follow PEP8 to the best of your ability unless it makes the code look ugly.
- Be Nice.
- Issues can be opened on the Issues page. I will attend to them within the next day.


## License

This project is licensed under the BSD License - see the [LICENSE.rst](LICENSE.rst) file for details

