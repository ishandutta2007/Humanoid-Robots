import os
import subprocess
import re

os.chdir(r"C:\Users\ishan\Documents\Projects\Humanoid-Robots")

def run(cmd):
    subprocess.run(cmd, shell=True)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Step 1: Emojis
content = content.replace("# Humanoid-Robots", "# 🤖 Humanoid-Robots")
content = content.replace("#Huanoid robots by DOF", "## 📊 Humanoid robots by DOF")
with open("README.md", "w", encoding="utf-8") as f: f.write(content)
run('git add . && git commit -m "added emojis"')

# Step 2: SEO
content = content.replace("# 🤖 Humanoid-Robots", "# 🤖 Humanoid-Robots - Ultimate Directory of Advanced Robotics\n\nDiscover the most advanced humanoid robots ranked by their Degrees of Freedom (DoF). This comprehensive list covers enterprise, commercial, and research robotics, providing insights into pricing, applications, and manufacturers.")
with open("README.md", "w", encoding="utf-8") as f: f.write(content)
run('git add . && git commit -m "seo optimised"')

# Step 3: Badges left
left_badges = '<p align="center">\n<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>\n'
content = content.replace("# 🤖 Humanoid-Robots - Ultimate Directory", left_badges + "</p>\n\n# 🤖 Humanoid-Robots - Ultimate Directory")
with open("README.md", "w", encoding="utf-8") as f: f.write(content)
run('git add . && git commit -m "badges to left added"')

# Step 4: Badges right
right_badge = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>\n'
content = content.replace("</p>", right_badge + "</p>")
with open("README.md", "w", encoding="utf-8") as f: f.write(content)
run('git add . && git commit -m "badges to right added"')

# Step 5: Star history
star_history = """
## ⭐ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FHumanoid-Robots&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Humanoid-Robots&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Humanoid-Robots&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Humanoid-Robots&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
content += star_history
with open("README.md", "w", encoding="utf-8") as f: f.write(content)
run('git add . && git commit -m "star history added"')

# Step 6: fix chartrepos
if 'chartrepos' in content:
    content = content.replace('chartrepos', 'chart?repos')
    with open("README.md", "w", encoding="utf-8") as f: f.write(content)
    run('git add . && git commit -m "fixed star plot"')

# Step 7: replace awesome link
if 'https://github.com/sindresorhus/awesome' in content:
    content = content.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')
    with open("README.md", "w", encoding="utf-8") as f: f.write(content)
    run('git add . && git commit -m "invalid awesome link fixed"')
