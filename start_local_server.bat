@echo off
title Cloud Computing Local Web Server
echo Starting local web server on port 8000...
echo Open your browser at http://localhost:8000
start "" "http://localhost:8000"
python -m http.server 8000
pause
