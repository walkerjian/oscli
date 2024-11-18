import pytest
from commands.parser import parse_help_text

def test_parse_help_text():
    sample_help = """
    Usage: docker [OPTIONS] COMMAND
      -h, --help    Show help information
      -v, --version Show version
    """
    expected = {
        "-h": "Show help information",
        "--help": "Show help information",
        "-v": "Show version",
        "--version": "Show version"
    }
    assert parse_help_text(sample_help) == expected
