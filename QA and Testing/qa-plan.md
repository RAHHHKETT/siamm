# QA Plan - Barangay Complaint System

## Test Levels

### Unit Testing
- Test individual functions and components in isolation
- Tool: Pytest

### Integration Testing
- Test how modules work together (e.g., form submission + database)
- Tool: Pytest with mock database

### System Testing
- Test the entire application end-to-end
- Tool: Manual testing + browser testing

## Entry Criteria
- Code has been written and reviewed
- All unit tests are passing
- Feature branch has been merged to main via PR

## Exit Criteria
- All unit tests pass with 0 failures
- No S1 or S2 severity bugs are open
- Defect log has been updated

## Severity Levels

| Level | Description | Example |
|-------|-------------|---------|
| S1 | Critical - system is unusable | Login completely broken |
| S2 | High - major feature not working | Cannot submit complaint |
| S3 | Medium - minor feature issue | Wrong status label shown |
| S4 | Low - cosmetic or trivial issue | Typo in button text |