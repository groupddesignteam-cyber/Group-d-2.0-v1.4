---
description: How to deploy the Group D landing page to Firebase Hosting
---

# Project Deployment Guide

Follow these steps to deploy the latest version of the website to the live server.

## 1. Check Authentication
If deployment fails with "Failed to get Firebase project" or permission errors, you need to log in again.

```powershell
# Run this in your terminal
firebase login
```
- A browser window will open.
- Log in with the Google account that has access to the Firebase project.
- Click "Allow".

## 2. Select Project (Optional)
Ensure you are connected to the correct project: `group-d-landing-page-2025`

```powershell
firebase use group-d-landing-page-2025
```

## 3. Deploy
Run the deployment command. This uploads your files in the local directory to the web server.

```powershell
// turbo
firebase deploy --only hosting
```

## 4. Verification
After the command finishes successfully, it will show a `Hosting URL`.
- Live URL: [https://group-d-landing-page-2025.web.app](https://group-d-landing-page-2025.web.app)
