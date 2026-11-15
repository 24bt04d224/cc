@echo off
title Deploy to Free Domain (Surge.sh)
echo ============================================================
echo      Deploy Cloud Computing Portal to Free Custom Domain
echo ============================================================
echo.
echo Your production files are in: d:\Downloads\cc\dist
echo.
set /p domain="Enter your desired free domain (e.g. my-cc-portal.surge.sh): "
if "%domain%"=="" set domain=gsfc-cloud-computing.surge.sh

echo.
echo Deploying to: https://%domain%
echo (If this is your first time, Surge will ask for your email and a password)
echo.
npx surge d:\Downloads\cc\dist %domain%
echo.
echo ============================================================
pause
