'''
    Python function to create a dictionary with transcript
    genome mapping information.
    :authors: shweta gopaulakrishnan (shwetagopaul92@gmail.com)
'''


def create_transcript_genome_map(map_file):
    '''
    Create a dictionary map of transcript genome information.

        Parameters:
            map_file (file): A four column (tab-separated) file containing the
                             transcripts user provides.
                             File Description:
                                - First column: Transcript Name
                                - Second Column: Chromosome Name
                                - Third Column: 0-based starting position
                                                on the chromosome
                                - Fourth Column: CIGAR String
                             Example: TR1 CHR1 3 8M7D6M2I2M11D7M


        Returns:
            mapping_transcript_genome (dict): Keys: Transcript Name
                                              Values: List with genomic mapping
                                                a. Chromosome name,
                                                b. 0-based starting position on
                                                   the chromosome,
                                                c. CIGAR string indicating
                                                   the mapping.
                                              Example:
                                              {"TR1": ["CHR1", "3",
                                                       "8M7D6M2I2M11D7M"],
                                               "TR2": ["CHR2", "10", "20M"] }
    '''
    mapping_transcript_genome = {}
    with open(map_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            # Parse each line of input file
            list_line = [l.strip() for l in line.split('\t')]
            # Create the dictionary with mapping information
            mapping_transcript_genome[list_line[0]] = [str(list_line[1]),
                                                       str(list_line[2]),
                                                       str(list_line[3])]
    return mapping_transcript_genome
