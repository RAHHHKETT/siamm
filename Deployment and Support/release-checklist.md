# Release Checklist - Barangay Complaint System

## Pre-Release
- [ ] All unit tests passed (python -m pytest)
- [ ] CI pipeline is green
- [ ] Version has been tagged (e.g. v0.5)
- [ ] Backup of database has been made
- [ ] Rollback steps are documented and ready

## Deployment
- [ ] Code pushed to main branch
- [ ] Deployment triggered on Render
- [ ] Environment variables are set correctly
- [ ] App is accessible via public URL

## Post-Release
- [ ] Verified all features work on live environment
- [ ] Release notes have been updated
- [ ] Team has been notified of deployment
- [ ] Monitoring is active