# Project Name


A template repository which can be used as a starting point for scientific analyses.


## Quickstart (Windows/macOS/Linux)


```bash
# 1) Create local env and install deps
uv venv --seed --python 3.12
uv sync --all-extras --group dev



```

First create a repository in the Github web interface without readme, licence and gitignore. 
 

```bash
git init
git remote add origin git@github.com/[username]/repo_template.git
git add .
git commit -m "Initial commit"
git push -u origin main
```


