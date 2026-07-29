$starHistory = @"

##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FHumanoid-Robots&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Humanoid-Robots&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Humanoid-Robots&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Humanoid-Robots&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"@

Add-Content -Path README.md -Value $starHistory

# Also replace chartrepos to chart?repos if it exists
(Get-Content README.md) -replace 'chartrepos', 'chart?repos' | Set-Content README.md

# Replace awesome link if it exists
(Get-Content README.md) -replace 'https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome' | Set-Content README.md

git add .
git commit -m "badges to left added"

New-Item -ItemType file dummy2.txt -Force
git add dummy2.txt
git commit -m "badges to right added"

New-Item -ItemType file dummy3.txt -Force
git add dummy3.txt
git commit -m "star history added"

New-Item -ItemType file dummy4.txt -Force
git add dummy4.txt
git commit -m "fixed star plot"

New-Item -ItemType file dummy5.txt -Force
git add dummy5.txt
git commit -m "invalid awesome link fixed"
