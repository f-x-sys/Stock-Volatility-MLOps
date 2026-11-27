# Create one initial synthetic data-validation test.
# This is a preliminary test to establish CI, not the final required testing suite.

import pandas as pd


def test_no_duplicate_stock_dates():
    df = pd.DataFrame({
        "permno": [10001, 10001],
        "date": ["2025-01-02", "2025-01-03"]
    })

    assert not df.duplicated(
        subset=["permno", "date"]
    ).any()