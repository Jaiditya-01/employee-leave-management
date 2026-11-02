# leave_app.py
def check_leave_balance(balance, requested_days):
    if not isinstance(requested_days, int) or requested_days < 0:
        return "Invalid"
    if requested_days == 0:
        return "Zero"
    if requested_days <= balance:
        return "Valid"
    return "Insufficient"

if __name__ == "__main__":
    print("Leave Balance Check:", check_leave_balance(10, 3))