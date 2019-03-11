'''

This project is a small extension of the lxml module. This provides CLI to convert a flat XML

structure into a .csv or .xlsx structure initially. I might add more formats in the future. Ultimately we

would also want to deal with nested structures.

'''

from lxml import etree
import click

import csv

def _fast_iter(context, func, config_dict, *args, **kwargs):
    ''' Build XML Tree and clear '''

    for event, elem in context:
        func(elem, config_dict, *args, **kwargs)  # Decorated Function
        elem.clear()

        for ancestor in elem.xpath('ancestor-or-self::*'):
            while ancestor.getprevious() is not None:
                del ancestor.getparent()[0]
    del context




def _process_element(elem, config_dict):

    ''' Business Logic to convert XML to csv '''

    tag_data = elem.xpath(config_dict["xpath_string"])

    if tag_data:

        with open(config_dict["outfile"], 'a') as outfile:

            writer = csv.writer(outfile, delimiter=",")
            writer.writerow(tag_data)
    else:

        with open('Error-files-'+config_dict["outfile"], 'a') as outfile:

            writer = csv.writer(outfile, delimiter=",")
            writer.writerow(tag_data)





def _parse_xml(config_dict):


    '''

    Parse the .xml file to and build a xml tree before converting it to .csv

    '''

    data_file = config_dict["infile"] # Too lazy to change the name

    if not config_dict.get("encoding"):




        context = etree.iterparse(data_file,\
                tag=config_dict["tag"],\
                strip_cdata=False, events=("end",))


    else:

        context = etree.iterparse(data_file,\

                tag=config_dict["tag"],\
                encoding=config_dict["encoding"],
                strip_cdata=False, events=("end",))




    _fast_iter(context, _process_element, config_dict)



