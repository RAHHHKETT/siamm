# Unit Tests - Barangay Complaint System

def validate_complaint(title, description, category):
    if not title:
        raise ValueError("Title is required")
    if not description:
        raise ValueError("Description is required")
    if not category:
        raise ValueError("Category is required")
    if len(title) < 5:
        raise ValueError("Title must be at least 5 characters")
    return True

def calculate_risk_score(likelihood, impact):
    return likelihood * impact

def get_complaint_status(status_code):
    statuses = {
        1: "Pending",
        2: "In Progress",
        3: "Resolved"
    }
    return statuses.get(status_code, "Unknown")

def is_valid_email(email):
    return "@" in email and "." in email

def assign_severity(risk_score):
    if risk_score >= 15:
        return "S1"
    elif risk_score >= 10:
        return "S2"
    elif risk_score >= 5:
        return "S3"
    else:
        return "S4"


# ── Tests ──
def test_valid_complaint():
    assert validate_complaint("Noise Complaint", "Loud music at night", "Noise") == True

def test_invalid_complaint_missing_title():
    try:
        validate_complaint("", "Loud music at night", "Noise")
        assert False
    except ValueError as e:
        assert str(e) == "Title is required"

def test_risk_score_calculation():
    assert calculate_risk_score(4, 5) == 20

def test_complaint_status():
    assert get_complaint_status(1) == "Pending"
    assert get_complaint_status(3) == "Resolved"
    assert get_complaint_status(99) == "Unknown"

def test_valid_email():
    assert is_valid_email("keith@gmail.com") == True
    assert is_valid_email("notanemail") == False

def test_assign_severity():
    assert assign_severity(20) == "S1"
    assert assign_severity(10) == "S2"
    assert assign_severity(5) == "S3"
    assert assign_severity(2) == "S4"