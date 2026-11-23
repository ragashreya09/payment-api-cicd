
def process_payment(amount):
    if amount <= 0:
        return "Payment failed"

    return f"Payment successful: ${amount:.2f}"


if __name__ == "__main__":
    print(process_payment(100))
