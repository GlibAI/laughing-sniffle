from datetime import datetime


def extract_statement_period(data_path: str, image_path: str) -> (datetime, datetime):
    return None, None


def extract_opening_balance(data_path: str, image_path: str) -> float:
    return 0.0


def extract_table_headers(data_path: str, image_path: str) -> dict[int, str]:
    return {}


def extract_balance_amounts(data_path: str, image_path: str) -> list[float]:
    return []
