"""Top-level package for Diary."""

__author__ = """anopenlife"""
__email__ = 'anopensourcecoder@gmail.com'
__version__ = '1.1.0'

from diary.diary import Diary
from diary.db import DB

__all__ = ["DB", "Diary"]
