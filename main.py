'''

The file that contains the entry point into the project.
This is a CLI that converts XML to CSV. More formats to be added soon.

'''

import click

from utils import _prepare_files_for_conversion
from parser_xml import _parse_xml


@click.command()
@click.argument("infile")
@click.argument("outfile")
@click.argument("tag")
@click.argument("xpathfile")
@click.option("--encoding",\
        help="Enter this flag if you have a encoding")

def parser_main(infile, outfile, tag, xpathfile, encoding):

    ''' Entry point function to collect all arguments from the command line '''

    # Build a configuration dictionary

    config_dict = {}

    config_dict["infile"] = infile
    config_dict["outfile"] = outfile

    config_dict["tag"] = tag
    config_dict["xpathfile"] = xpathfile

    if encoding:

        config_dict["encoding"] = encoding

    prepare_data = _prepare_files_for_conversion

    #Obtain XPATH string and also prepare csv file for output

    config_dict["xpath_string"] = prepare_data(config_dict)[0]


    # The XPATH string is present in the first line of the XPATh file

    _parse_xml(config_dict) # Calling the main parser function





    return True


