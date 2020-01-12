$date = Get-Date -Format "yyyyMMddHHmmss";
$dest = Join-Path .\bak ("ReadMe_" + $date + ".md")
Move-Item -Path ".\ReadMe.md" -Destination $dest -Force

Get-ChildItem ".\src" -Recurse -File -Filter "0*.md" | % { Get-Content $_.FullName -Encoding UTF8 | Add-Content -Encoding UTF8 "ReadMe.md"; Add-Content "ReadMe.md" -Encoding UTF8 -Value "`r`n" }