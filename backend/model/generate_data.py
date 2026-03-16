import pandas as pd
import numpy as np
import random

n = 20000

def generate():

    data = []

    for i in range(n):

        num_returns = np.random.poisson(2)
        refund_amount = np.random.uniform(100,5000)
        time_gap = np.random.randint(1,50)
        mismatch = np.random.binomial(1,0.1)
        category_risk = np.random.randint(1,5)
        loyalty = np.random.randint(1,10)
        reason_pattern = np.random.randint(0,3)

        fraud_prob = (
            (num_returns > 4) * 0.4 +
            (mismatch * 0.3) +
            (category_risk / 10) +
            (refund_amount > 3000) * 0.2 +
            (time_gap < 3) * 0.15
        )

        fraud_prob = min(max(fraud_prob,0),1)

        fraud = 1 if random.random() < fraud_prob else 0

        data.append([
            num_returns,
            refund_amount,
            time_gap,
            mismatch,
            category_risk,
            loyalty,
            reason_pattern,
            fraud
        ])

    df = pd.DataFrame(data, columns=[
        "num_returns",
        "refund_amount",
        "time_gap",
        "mismatch",
        "category_risk",
        "loyalty",
        "reason_pattern",
        "fraud"
    ])

    df.to_csv("fraud_dataset.csv", index=False)

    print("Dataset generated:", len(df))


generate()