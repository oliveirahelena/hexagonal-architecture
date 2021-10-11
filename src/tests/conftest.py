import sqlite3

import pytest


@pytest.fixture
def setup_database():
    conn = sqlite3.connect(":memory:")
    conn.execute(
        """CREATE TABLE IF NOT EXISTS products (
        "id" string,
        "name" string,
        "price" float,
        "status" string
    );"""
    )
    sample_data = [
        ("abc", "Product Test", 0, "disabled"),
        ("def", "Product Test 2", 10, "enabled"),
    ]
    conn.executemany("INSERT INTO products VALUES(?, ?, ? , ?)", sample_data)
    conn.commit()
    yield conn
    conn.close()
