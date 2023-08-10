# SearchingEngine

## Text Parsing and Searching System

This repository contains a Python project for parsing text files, searching words in the parsed data, and storing the results in a database file. 
The project consists of classes like Text, Word, and functions for parsing and searching.

### Classes

#### Text

The Text class represents a text file. It initializes by reading the content of the file and extracting individual words. The + operator is overloaded to concatenate the words of two Text instances.

#### Word

The Word class represents a word. It provides methods for lowercase conversion, symbol removal, checking word presence in a file, and normalizing a word against a reference file.

#### Parsing Files

The parse_files.py script parses two text files, creates instances of Text, combines their words, and stores the parsed results in a database file named db.txt.

#### Searching in Database

The search_in_db.py script searches for a specified word in the database file (db.txt) created by the parsing process. It returns the list of files where the word was found.
