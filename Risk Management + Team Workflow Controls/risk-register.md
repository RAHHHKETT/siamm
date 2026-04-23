# Risk Register

## Risk Score Formula
Risk Score = Likelihood × Impact
- Likelihood: 1 (Very Low) to 5 (Very High)
- Impact: 1 (Very Low) to 5 (Very High)

## Risks

| # | Risk | Likelihood (1-5) | Impact (1-5) | Risk Score | Mitigation Plan | Owner |
|---|------|-----------------|--------------|------------|-----------------|-------|
| R-01 | Team member becomes inactive or drops the subject | 4 | 5 | 20 | Redistribute tasks early, maintain shared docs so anyone can continue the work | Keith Austria |
| R-02 | GitHub conflicts due to multiple people editing the same file | 4 | 3 | 12 | Use feature branches, review PRs before merging | Oga |
| R-03 | Unclear requirements leading to wrong features being built | 3 | 4 | 12 | Review backlog regularly, confirm with instructor if unsure | Keith Austria |
| R-04 | Database data loss or corruption | 2 | 5 | 10 | Regular backups, use version-controlled database migrations | Oga |
| R-05 | Login/authentication security vulnerability | 2 | 5 | 10 | Use hashed passwords, validate all inputs, test for common exploits | Oga |
| R-06 | UI is too complex for barangay officers to use | 3 | 3 | 9 | Conduct simple user testing, keep UI minimal and clean | Saguilayan |
| R-07 | Sprint goals not met due to poor time management | 4 | 3 | 12 | Set internal deadlines 2 days before actual due date | Keith Austria |
| R-08 | Internet or power outages affecting development | 3 | 3 | 9 | Use GitHub Codespaces so work is cloud-based, not local only | All Members |
| R-09 | PDF export feature may not work on all browsers | 3 | 3 | 9 | Test on Chrome, Firefox, and Edge before release | Saguilayan |