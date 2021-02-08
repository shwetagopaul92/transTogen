'''
    Split the cigar string and translate transcript to genomic
    coordinates to write to result.
    :authors: shweta gopaulakrishnan (shwetagopaul92@gmail.com)
'''
# Import required modules
from collections import Counter


# Split cigar string
def split_cigar_string(cgr_string):
    '''
    Split the Cigar String into separate operations.
        Parameters:
            cgr_string (str): CIGAR string indicating the mapping.
                        Example: '3M2D1I'
        Returns:
            cigar_split (list): A list with cigar operations split.
                                Example: ['M','M','M','D','D','I']
    '''
    cigar_list = list(cgr_string)
    cigar_split = []
    nums = []
    for val in range(0, len(cigar_list)):
        if cigar_list[val].isnumeric():
            # Handle multiple digits before a cigar operation
            nums = nums + [cigar_list[val]]
        else:
            digit = ''.join(nums)
            # Split the cigar operations
            cigar_split.append(list(cigar_list[val]*int(digit)))
            nums = []
    cigar_split = [item for sublist in cigar_split for item in sublist]
    return cigar_split


# Translate coordinates
def translate_trtogeno(query_transcript, transcript_mapping):
    '''
    Translate transcript coordinates to genomic coordinates.
        Parameters:
            query_transcript (list): A list containing user query with
                                     transcript name and 0-based
                                     transcript coordinate.
                                     Example: ["TR1", 4]
            transcript_mapping (dict): Dictionary with transcript
                                       genome mapping.
                                       Example:
                                       {
                                        "TR1": ["CHR1",
                                                "3", "8M7D6M2I2M11D7M"],
                                        "TR2": ["CHR2", "10", "20M"]
                                       }

        Returns:
            translated_result (list): A list containing translated
                                      genomic coordinates.
                                      Example: ["CHR2", 7]
        Exceptions:
            1. Check if a given transcript query exists
               in transcript genome mapping.
            2. Check if the transcript location provided
               falls withing length of transcript.
    '''
    transcript_name = query_transcript[0]
    transcript_coord = query_transcript[1]
    translated_result = []
    if transcript_name not in transcript_mapping:
        raise Exception("Given transcript {}".format(query_transcript)
                        + "does not exist in the map! \
                        Please enter a valid one")
    else:
        for key in transcript_mapping:
            if key == transcript_name:
                values = transcript_mapping[key]
                # Grab the cigar string
                chr_name = values[0]
                start = values[1]
                cigar_string = values[2]
        # Split the cigar string into operations
        cigar_values = split_cigar_string(cigar_string)
        cigar_values_count = Counter(cigar_values)
        transcript_len = cigar_values_count['M'] + cigar_values_count['I']

        if int(transcript_coord) >= int(transcript_len):
            raise Exception(
                'Transcript location provided does not \
                 fall within length of transcript'
            )

        transcript_pos = 0
        genome_pos = int(start)
        i = 0

        # Parse through the cigar_values list one by one
        while transcript_pos <= int(transcript_coord):
            cigar = cigar_values[i]
            if cigar == "M":
                # M: match on both transcript and genome;
                # increase both positions by 1
                transcript_pos += 1
                genome_pos += 1
            elif cigar == "D":
                # D: deletion on the transcript; that is present on the genome
                genome_pos += 1
            else:
                # I: insertion on the transcript; not present on the genome
                transcript_pos += 1
            i = i + 1

        # genomic_loc has the translated coordinate from transcript to genome
        if cigar == "I":
            genomic_loc = genome_pos
        else:
            genomic_loc = genome_pos - 1
    translated_result.append(chr_name)
    translated_result.append(genomic_loc)
    return translated_result
