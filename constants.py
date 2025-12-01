DEFAULT_MODEL = "deepseek-r1:8b"

OUTPUT_FORMAT = {
    "account": "string",
    "amount": "int",
    "txn_type": "debit|credit",
    "payee": "string|null",
    "payer": "string|null",
    "category": "string|null",
}

DEFAULT_CATEGORIES = ["Salary", "EMI", "Food", "Travel", "Bills", "Shopping"]
