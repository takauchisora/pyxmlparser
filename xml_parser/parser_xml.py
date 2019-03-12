'''

This project is a small extension of the lxml module. This provides CLI to convert a flat XML

structure into a .csv or .xlsx structure initially. I might add more formats in the future.
Ultimately we would also want to deal with nested structures. This file is a part of the
module that deals with xml and is single source for xml file parsing.

'''

from lxml import etree
import click

from .utils import write_data_to_csv, null_check


def _fast_iter(context, func, config_dict, verbose, *args, **kwargs):
    ''' Build XML Tree and clear '''

    for event, elem in context:
        func(elem, config_dict, verbose, *args, **kwargs)  # Decorated Function
        elem.clear()

        for ancestor in elem.xpath('ancestor-or-self::*'):
            while ancestor.getprevious() is not None:
                del ancestor.getparent()[0]
    del context




def _process_element(elem, config_dict, verbose):

    ''' Business Logic to convert XML to csv '''

    tag_data = elem.xpath(config_dict["xpath_string"])



    if len(tag_data) != len(config_dict["csv_columns"]):

        # If the the lengths are not equal we know there are missing elements.
        # There might be a better way to do this.

        tag_data = null_check(elem, tag_data, config_dict, verbose)




    if config_dict["outfile"].endswith(".csv"):


        if verbose:

            click.echo(tag_data)


        write_data_to_csv(tag_data, config_dict)


def _parse_xml(config_dict, verbose):


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
                            encoding=config_dict["encoding"],\
                            strip_cdata=False, events=("end",))




    _fast_iter(context, _process_element, config_dict, verbose)



