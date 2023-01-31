# Document Extraction Assignment

## Data
Sample data for this problem statement can be found in the `data` folder.
There are two sets of examples, and each set includes a json file and a image file.
For example, `data/1.json` and `data/1.jpg` are the json and image files for the first example.
The json file contains the following information -

1. `words`: list of words extracted from the page. Each word is represented by a dictionary with the following keys:
    - `text`: the text of the word
    - `w_min`: the x-coordinate of the top-left corner of the word
    - `h_min`: the y-coordinate of the top-left corner of the word
    - `w_max`: the x-coordinate of the bottom-right corner of the word
    - `h_max`: the y-coordinate of the bottom-right corner of the word
2. `table`: the location of the transaction table represented as a dictionary with the following keys:
    - `w_min`: the x-coordinate of the top-left corner of the table
    - `h_min`: the y-coordinate of the top-left corner of the table
    - `w_max`: the x-coordinate of the bottom-right corner of the table
    - `h_max`: the y-coordinate of the bottom-right corner of the table
3. `header`: the location of the transaction table header represented as a dictionary with the following keys:
    - `w_min`: the x-coordinate of the top-left corner of the header
    - `h_min`: the y-coordinate of the top-left corner of the header
    - `w_max`: the x-coordinate of the bottom-right corner of the header
    - `h_max`: the y-coordinate of the bottom-right corner of the header

Notes
- The coordinates are normalized to be between 0 and 1.
- OCR has already been done and the corresponding text is already provided to you. You do not need to do any OCR or Text Extraction.

## Problem Statement
Given a bank statement (pdf), we are interested in extracting the following information from the document:
1. Statement Period, which includes a start date and an end date
2. Opening balance amount
3. Transaction table headers
4. Balance amounts from the transaction table

The expected outputs for the two examples are provided in the `tests/test_extractors` file.

A visual example of extracted data is shown below:

### 1.jpg
![1.jpg](docs/1.jpg?raw=true "1.jpg")

### 2.jpg
![2.jpg](docs/2.jpg?raw=true "2.jpg")

## Evaluation
Evaluation will be done by running tests located in the `tests` folder.
The tests will check the following:
1. The statement period is extracted correctly (`test_statement_period`)
2. The opening balance amount is extracted correctly (`test_opening_balance`)
3. The transaction table headers are extracted correctly (`test_table_headers`)
4. The balance amounts from the transaction table are extracted correctly (`test_table_balance`)

Note: Do not modify the tests.

## Bonus
The following are optional tasks that will be evaluated separately:
1. Write an API server that accepts a json file and an image file and returns all the extracted data.

## Submission
1. Clone this repository to your local machine.
2. You should modify the `src/extractors.py` file. The functions have already been defined for you.
3. Run tests using `pytest` to check your implementation.
4. Create a tarball of your code and share it via email.

Note: If you have used any external libraries, please include them in the `requirements.txt` file.
