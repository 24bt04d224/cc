@echo off
title Launch Free Website via Netlify Drop
echo ============================================================
echo      Free Website Deployment via Netlify (10 Seconds)
echo ============================================================
echo.
echo Step 1: Netlify Drop website will open in your browser.
echo Step 2: The 'dist' folder with your portal will also open.
echo Step 3: Simply drag and drop the 'dist' folder into Netlify Drop!
echo.
echo You will immediately get a free HTTPS link, and you can change
echo the domain name to anything you want (e.g. my-exam-portal.netlify.app).
echo ============================================================
echo.
explorer "d:\Downloads\cc\dist"
start https://app.netlify.com/drop
pause
