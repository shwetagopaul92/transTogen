'''
    Take user input from command line and translate
    transcript coordinates to genomic coordinates
'''

# Import required modules
import argparse
from . import transcript_genome_map as tgm
from . import translate_coordinates as tc


# Main function
def main():

    '''
        Usage:
        Main function that takes user inputs of two files
        and outputs the result file:

        I. Inputs:
            1. Transcript Genome Map File:
            Description:
                A four column (tab-separated) file containing the transcripts.
                The first column is the transcript name, and the remaining
                three columns indicate it’s genomic mapping:
                chromosome name, 0-based starting position on the chromosome,
                and CIGAR string indicating the mapping.
            2. Query Regions File:
            Description:
                A two column (tab-separated) file indicating
                a set of queries.
                The first column is a transcript name, and the
                second column is a 0-based transcript coordinate.
        II. Output:
            1. Output file:
            Description:
                The output is a four column tab separated file with
                one row for each of the input queries.
                The first two columns are exactly the
                two columns from the second input file,
                and the remaining two columns are the
                chromosome name and chromosome coordinate, respectively.

    '''

    # Use argparse to take command line arguments from user
    parser = argparse.ArgumentParser(description='''
                                    Tool to translate transcript coordinates
                                    to genomic coordinates.
                                    eg: transTogen <query_file.txt>
                                                   <mapping_file.txt>
                                                   <output_file.txt>
                                    ''')
    parser.add_argument('query_file', metavar='query_file',
                        help='Tab-separated file \
                        containing queries with transcript name \
                        and coordinate; eg: TR1 4')
    parser.add_argument('mapping_file', metavar='mapping_file',
                        help='Tab-separated file \
                        transcript with genome mapping information \
                        eg: TR1 CHR1 3 8M7D6M2I2M11D7M')
    parser.add_argument('output_file', metavar='output_file',
                        help='File store generated \
                        output file with result')

    # Validate the file path arguments

    args = parser.parse_args()
    args_query_file = args.query_file
    args_mapping_file = args.mapping_file
    args_output_file = args.output_file

    # Create a dictionary to hold mapping information
    transcript_mapping = tgm.create_transcript_genome_map(args_mapping_file)

    # Translate transcript to genomic coordinates & writes result
    with open(args_query_file, 'r') as in_f:
        with open(args_output_file, 'w') as out_f:
            line = in_f.readline()
            while line != "":
                # Parse the input query file
                query = [l.strip() for l in line.split('\t')]
                result = tc.translate_trtogeno(query, transcript_mapping)
                # Write to output file
                out_f.write(query[0])
                out_f.write('\t')
                out_f.write(query[1])
                out_f.write('\t')
                for item in result:
                    out_f.write(str(item))
                    out_f.write('\t')
                out_f.write('\n')
                line = in_f.readline()


if __name__ == "__main__":
    main()
