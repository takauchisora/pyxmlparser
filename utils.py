''' Utility functions that  build the configuration

dictionary and keeps track of input and output files

'''
import csv
import click




def _prepare_files_for_conversion(config_dict):


    ''' Prepare the output csv file after converting from XML '''

    with open(config_dict["xpathfile"], "r") as xpathfile:

        ''' Open the csv file which contains xpath '''

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



    return lines



def write_data_to_csv(tag_data, config_dict):



    ''' Function that writes some data to CSV '''


    if tag_data:

        with open(config_dict["outfile"], 'a') as outfile:

            writer = csv.writer(outfile, delimiter=",")
            writer.writerow(tag_data)
    else:

        # This segment needs to change.

        with open('Error-files-'+config_dict["outfile"], 'a') as outfile:

            writer = csv.writer(outfile, delimiter=",")
            writer.writerow(tag_data)


