''' Utility functions that  build the configuration

dictionary and keeps track of input and output files

'''
import csv
import click




def _prepare_files_for_conversion(config_dict, verbose):


    ''' Prepare the output csv file after converting from XML '''

    with open(config_dict["xpathfile"], "r") as xpathfile:

        ''' Open the csv file which contains xpath '''

        if verbose:
            click.echo("Creating your output file....")

        try:

            lines = [line.rstrip('\n') for line in xpathfile]

            if len(lines) < 2:

                raise TypeError

        except TypeError:

            click.echo("The CSV file provided was Improperly Configured")




    with open(config_dict["outfile"], "w") as outfile:

        ''' Write columns to the output csv file '''



        writer = csv.writer(outfile)
        writer = writer.writerow(lines[1].split(','))

        if verbose:

            click.echo("The Output File has been created.")



    return lines



def write_data_to_csv(tag_data, config_dict):



    ''' Function that writes some data to CSV '''


    if tag_data:

        with open(config_dict["outfile"], 'a') as outfile:

            writer = csv.writer(outfile, delimiter=",", quoting=csv.QUOTE_NONE)
            writer.writerow(tag_data)
    else:

        # This segment needs to change.

        with open('Error-files-'+config_dict["outfile"], 'a') as outfile:

            writer = csv.writer(outfile, delimiter=",")
            writer.writerow(tag_data)




def null_check(elem, tag_data, config_dict, verbose):

    ''' If a corresponding tag is not present we add None values '''


    xpath_string_list = config_dict["xpath_string"].split("|")
    csv_columns = config_dict["csv_columns"].split(",")

    try:

        # Check each xpath to see if a value is empty
        if len(csv_columns) == len(xpath_string_list):


            for i in range(len(csv_columns)):

                if not elem.xpath(xpath_string_list[i]):

                    ''' Add None to the corresponsing index '''

                    tag_data.insert(i, None)

                    if verbose:

                        click.echo(tag_data)

        else:

            raise IndexError

    except IndexError:

        click.echo("Malformed XPath File.")
        exit(0)

    return tag_data
