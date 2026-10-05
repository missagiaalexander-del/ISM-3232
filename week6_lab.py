# Week6_lab.py
# AUthor: Alexander R. Missagia

records = [
    {
        "id": 1,
        "name": "Taylor",
        "category": "Travel",
        "amount": 1200.0,
        "status": "Pending",
    },
    {
        "id": 2,
        "name": "Jordan",
        "category": "Equipment",
        "amount": 450.0,
        "status": "Pending",
    },
    {
        "id": 3,
        "name": "Morgan",
        "category": "Software",
        "amount": 3500.0,
        "status": "Approved",
    },
    {
        "id": 4,
        "name": "Riley",
        "category": "Travel",
        "amount": 89.0,
        "status": "Pending",
    },
    {
        "id": 5,
        "name": "Alex",
        "category": "Equipment",
        "amount": 2200.0,
        "status": "Pending",
    },
]

LIMIT = 1000.0
HIGH = 2000
Total = 0
flagged = []
high_value = []

for rec in records:
    if rec["status"] == "Pending":
        Total += rec["amount"]
        if rec["amount"] > LIMIT:
            flagged.append(rec)
        if rec["amount"] > HIGH:
            high_value.append(rec)
