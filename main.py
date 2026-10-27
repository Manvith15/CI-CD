def calculate_total(amount):
    gst = amount * 0.05
    total = amount + gst
    return round(total, 2)


if __name__ == "__main__":
    print("CI Pipeline Lab")
    print("Total with GST:", calculate_total(100))
