transTogen: Python Tool to Translate Transcript to Genomic Coordinates
======================================================================

transTogen is a Python Command Line Tool that helps transalte transcript to genomic coordinates.

The objective is then to translate a (0-based) transcript coordinate to a (0 based) genome coordinate. For example the fifth base in TR1 (i.e. TR1:4) maps to genome coordinate CHR1:7. Similarly, TR1:13 maps to CHR1:23 and TR1:14 maps to an insertion immediately before CHR1:24.

**Note**
--------

Please find Sphinx generated **documentation** at

    > cd docs/build 
    > cd html
    > open index.html 

Documentation was generated using: 

    > cd docs
    > make html 

Installation:
-------------

The source code can be found at: <https://github.com/shwetagopaul92/transTogen.git>

Follow the following steps to get the tool installed on your system:

    > git clone https://github.com/shwetagopaul92/transTogen.git
    > cd transTogen/
    > pip3 install -e .

Requirements can be found in requirements.txt.

    > pip3 install -r requirements.txt

Working with transTogen:
------------------------
- Inputs:

  1. A four column (tab-separated) file containing the transcripts. The first column is the transcript name, and the remaining three columns indicate it’s genomic mapping: chromosome name, 0-based starting position on the chromosome, and CIGAR string indicating the mapping.
  2. A two column (tab-separated) file indicating a set of queries. The first column is a transcript name, and the second column is a 0-based transcript coordinate.

- Output:
  1. The output is a four column tab separated file with one row for each of the input
     queries.The first two columns are exactly the two columns from the second input file, and the remaining two columns are the chromosome name and chromosome coordinate, respectively.

To get started:


    transTogen -h
    usage: transTogen [-h] query_file mapping_file output_file
    Tool to translate transcript coordinates to genomic coordinates. eg:
    transTogen <query_file.txt> <mapping_file.txt> <output_file.txt>
    positional arguments:
      query_file    Tab-separated file containing queries with transcript name and
                    coordinate; eg: TR1 4
      mapping_file  Tab-separated file transcript with genome mapping information
                    eg: TR1 CHR1 3 8M7D6M2I2M11D7M
      output_file   File store generated output file with result
    optional arguments:
     -h, --help    show this help message and exit


**Example:**
------------

There is test data in data/ that can be used to run the tool.

    transTogen data/transcript-query.txt data/transcript-map.txt data/result.txt

Contents of output file (data/result.txt):

    TR1	4	CHR1	7
    TR2	0	CHR2	10
    TR1	13	CHR1	23
    TR2	10	CHR2	20

Testing:
--------
- Pytest has been used to test the package.
- Expected results are used to check against the result from a function.


Documentation:
--------------
- Every function in the package is documented with a summary, required parameters and return values.
- Exceptions taken care of are noted as wetall.
- **Sphinx** document generator has been used to document the package.

Style:
-----
- **PEP-8** Community-preferred style guidelines are followed.
- **pycodestyle** was used to check style against PEP-8 conventions.

      > cd pytest 
      > pytest -v 
Strengths:
----------
- User-friendly command line tool with lot of help messages.
- Code is efficiently written in PEP-8 style and documented with Sphinx for easy understanding.
- Code is split into functions in separate files for efficient organization and
  easier for troubleshooting errors.
- Data structures like dictionary is used for efficiently organizing the transcript to genome   
  mapping information.
- Exceptions are provided at different instances
      1. Check if a given transcript query exists
         in transcript genome mapping.
      2. Check if the transcript location provided
         falls withing length of transcript.
- Input file path provided by user is checked for validity.
- Testing covers the entire package.

Limitations & Future Improvements:
----------------------------------
- With more functionality, classes can also be used to describe the mapping
  between transcript and genomes.
