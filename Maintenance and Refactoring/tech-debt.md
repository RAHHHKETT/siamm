# Technical Debt Log - Barangay Complaint System

## What is Technical Debt?
Technical debt refers to shortcuts or quick fixes made during development that need to be improved later for better code quality, maintainability, and performance.

## Technical Debt Items

| # | Description | Location | Priority | Status |
|---|-------------|----------|----------|--------|
| TD-01 | validate_complaint() function has no specific error messages, just returns True/False | tests/test_complaint.py | High | Fixed |
| TD-02 | Hardcoded status codes (1, 2, 3) instead of using constants or enums | tests/test_complaint.py | High | Pending |
| TD-03 | No logging system in place for tracking errors or user actions | server/index.js | Medium | Pending |
| TD-04 | No input sanitization on complaint form fields | client/src/pages/ | High | Pending |
| TD-05 | Database queries are not optimized, no indexing on complaint table | server/database.js | Medium | Pending |

## Selected Debt to Fix: TD-01
**Before (bad):**
```python
def validate_complaint(title, description, category):
    if not title or not description or not category:
        return False
    if len(title) < 5:
        return False
    return True
```

**After (improved):**
```python
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
```

## Why This Matters
Returning specific error messages instead of just False makes debugging easier and gives users better feedback on what went wrong.