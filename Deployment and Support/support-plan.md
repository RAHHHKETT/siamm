# Support Plan - Barangay Complaint System

## Support Process
1. User reports an issue via GitHub Issues or group chat
2. QA Lead (Enerio) reviews and logs it in the defect log
3. Issue is assigned to the relevant team member
4. Fix is implemented via feature branch and PR
5. Fix is tested and merged to main
6. User is notified of the resolution

## Common Issues and Solutions

| Issue | Possible Cause | Solution |
|-------|---------------|---------|
| Cannot log in | Wrong credentials | Reset password |
| Complaint not submitting | Empty required fields | Check all fields are filled |
| Page not loading | Server down | Check Render dashboard |
| Status not updating | Database error | Restart the service on Render |

## Escalation Process
- **S1/S2 bugs** → Immediately notify Keith Austria (Scrum Master)
- **S3/S4 bugs** → Log in defect log, fix in next sprint
- **Server down** → Oga (Backend) to investigate within 1 hour

## Response Times
| Severity | Response Time | Resolution Time |
|----------|--------------|-----------------|
| S1 | 1 hour | 4 hours |
| S2 | 4 hours | 24 hours |
| S3 | 24 hours | 1 week |
| S4 | 1 week | Next sprint |