# Deployment Plan - Barangay Complaint System

## Target Environment
- Platform: Render (free tier)
- Language: Python
- Database: SQLite (development) / PostgreSQL (production)
- Repository: https://github.com/RAHHHKETT/siam

## Rollout Strategy
We will use a **Blue-Green Deployment** strategy:
- Blue = current live version
- Green = new version being deployed
- Switch traffic to Green only after all tests pass
- If Green fails, immediately switch back to Blue

## Deployment Steps
1. Push all changes to `main` branch
2. Connect GitHub repo to Render
3. Set environment variables on Render dashboard
4. Trigger deployment from Render dashboard
5. Verify the app is live and working
6. Update release notes

## Rollback Steps
1. Go to Render dashboard
2. Click on the service → **Deploys** tab
3. Find the last stable deployment
4. Click **Rollback to this deploy**
5. Verify the app is back to working state
6. Log the rollback in the defect log