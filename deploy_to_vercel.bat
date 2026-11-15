@echo off
title Deploy to Vercel
echo ============================================================
echo      Deploy Cloud Computing Portal to Vercel
echo ============================================================
echo.
echo Option 1: One-Click Instant Deployment via GitHub (Recommended)
echo Option 2: Deploy directly from Terminal CLI (npx vercel)
echo.
set /p choice="Choose Option [1 or 2, default is 1]: "
if "%choice%"=="" set choice=1

if "%choice%"=="1" (
    echo.
    echo Opening Vercel Import in your browser...
    echo 1. Sign in with GitHub
    echo 2. Click 'Deploy'
    echo Your site will be live at: https://cc-...vercel.app
    start https://vercel.com/new/clone?repository-url=https%%3A%%2F%%2Fgithub.com%%2F24bt04d224%%2Fcc
    goto end
)

if "%choice%"=="2" (
    echo.
    echo Running Vercel CLI...
    echo (Vercel will ask you to login with your browser or email)
    npx vercel
    goto end
)

:end
echo.
echo ============================================================
pause
