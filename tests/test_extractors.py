from src.extractors import (extract_statement_period, extract_opening_balance, extract_table_headers,
                            extract_balance_amounts)


def test_statement_period():
    start_date, end_date = extract_statement_period(data_path='./data/1.json', image_path='./data/1.jpg')
    assert start_date.day == 21
    assert start_date.month == 7
    assert start_date.year == 2021
    assert end_date.day == 21
    assert end_date.month == 8
    assert end_date.year == 2021

    start_date, end_date = extract_statement_period(data_path='./data/2.json', image_path='./data/2.jpg')
    assert start_date.day == 1
    assert start_date.month == 5
    assert start_date.year == 2022
    assert end_date.day == 31
    assert end_date.month == 5
    assert end_date.year == 2022


def test_opening_balance():
    opening_balance = extract_opening_balance(data_path='./data/1.json', image_path='./data/1.jpg')
    assert opening_balance == 73325.23

    opening_balance = extract_opening_balance(data_path='./data/2.json', image_path='./data/2.jpg')
    assert opening_balance == 151254.96


def test_table_headers():
    table_headers = extract_table_headers(data_path='./data/1.json', image_path='./data/1.jpg')
    assert table_headers[0] == 'Date'
    assert table_headers[1] == 'Description'
    assert table_headers[2] == 'Amount'
    assert table_headers[3] == 'Balance'

    table_headers = extract_table_headers(data_path='./data/2.json', image_path='./data/2.jpg')
    assert table_headers[0] == 'Date'
    assert table_headers[1] == 'Transaction Description'
    assert table_headers[2] == 'Charge'
    assert table_headers[3] == 'Debit Amount'
    assert table_headers[4] == 'Credit Amount'
    assert table_headers[5] == 'Balance'


def test_table_balance():
    balance_amounts = extract_balance_amounts(data_path='./data/1.json', image_path='./data/1.jpg')
    assert len(balance_amounts) == 25
    assert balance_amounts[0] == 73325.23
    assert balance_amounts[-1] == 73325.23
    balance_amounts = extract_balance_amounts(data_path='./data/2.json', image_path='./data/2.jpg')
    assert len(balance_amounts) == 12
    assert balance_amounts[0] == 151254.96
    assert balance_amounts[-1] == 140276.15
