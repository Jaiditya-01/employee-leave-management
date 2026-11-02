# leave_app.py
def check_leave_balance(balance, requested_days):
    if not isinstance(requested_days, int) or requested_days < 0:
        return "Invalid"
    if requested_days == 0:
        return "Zero"
    if requested_days <= balance:
        return "Valid"
    return "Insufficient"

# Append this to leave_app.py
def request_leave(employee_name, balance, requested_days):
    status = check_leave_balance(balance, requested_days)
    if status == "Valid":
        return f"Leave approved for {employee_name}. Remaining balance: {balance - requested_days}"
    return f"Leave rejected for {employee_name}. Reason: {status}"

if __name__ == "__main__":
    print("Leave Balance Check:", check_leave_balance(10, 3))