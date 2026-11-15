@echo off
title Deploy to GitHub Pages (Free username.github.io)
echo ============================================================
echo      Deploy to GitHub Pages (Free *.github.io Domain)
echo ============================================================
echo.
echo Make sure you have created a repository on GitHub (e.g. 'cloud-computing').
set /p repo_url="Enter your GitHub Repository URL (e.g. https://github.com/24bt04d224/cc-portal.git): "
if "%repo_url%"=="" goto end

cd /d "d:\Downloads\cc\dist"
git init
git branch -M main
git add index.html
git commit -m "Deploy Cloud Computing Portal"
git remote add origin %repo_url%
git push -u origin main --force

echo.
echo ============================================================
echo Files pushed to GitHub!
echo Now go to your GitHub repository -> Settings -> Pages:
echo Set 'Source' to 'Deploy from a branch' -> Select 'main' branch -> Save.
echo Your free site will be live at: https://24bt04d224.github.io/...
echo ============================================================
:end
pause
