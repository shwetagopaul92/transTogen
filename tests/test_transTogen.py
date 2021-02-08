import pytest
from transTogen.transcript_genome_map import *
from transTogen.translate_coordinates import *
from transTogen.run_transTogen import *


@pytest.mark.parametrize(
    'tr_query, mapping, expected_result',
    [
        (
            ["TR1", 4],
            {
                "TR1": ["CHR1", "3", "8M7D6M2I2M11D7M"],
                "TR2": ["CHR2", "10", "20M"]
            },
            ["CHR1", 7],
        ),
        (
            ["TR2", 0],
            {
                "TR1": ["CHR1", "3", "8M7D6M2I2M11D7M"],
                "TR2": ["CHR2", "10", "20M"]
            },
            ["CHR2", 10],
        ),
        (
            ["TR1", 13],
            {
                "TR1": ["CHR1", "3", "8M7D6M2I2M11D7M"],
                "TR2": ["CHR2", "10", "20M"]
            },
            ["CHR1", 23],
        ),
        (
            ["TR2", 10],
            {
                "TR1": ["CHR1", "3", "8M7D6M2I2M11D7M"],
                "TR2": ["CHR2", "10", "20M"]
            },
            ["CHR2", 20],
        )
    ]
)


# Function to test translation from transcript to genomic coordinates
def test_translate_trtogeno(tr_query, mapping, expected_result):
    tr_result = translate_trtogeno(tr_query, mapping)
    assert tr_result == expected_result


# Function to test splitting of cigar string to operations
def test_split_cigar_string():
    split_result = split_cigar_string("3M2D1I")
    expected = ["M", "M", "M", "D", "D", "I"]
    assert split_result == expected
