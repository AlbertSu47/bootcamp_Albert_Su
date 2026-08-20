# Stage 06 — Data Preprocessing

## Cleaning Strategy

This homework applies a modular preprocessing workflow to the provided raw dataset.

- Missing values in `age`, `income`, and `score` are filled using each column's median.
- Columns with more than 50% missing values are dropped.
- Numeric columns `age`, `income`, and `score` are normalized to the range [0, 1].
- `zipcode` and `city` are preserved without normalization because they are categorical or identifier-like fields.
- The original and cleaned datasets are compared to verify the effects of preprocessing.
- The cleaned dataset is saved to `data/processed/sample_data_cleaned.csv`.

Reusable cleaning functions are stored in `src/cleaning.py`.
