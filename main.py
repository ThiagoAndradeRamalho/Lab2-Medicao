#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, time, subprocess
from pathlib import Path
import requests

MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 5
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("repos")

HEADERS = {"Accept": "application/vnd.github+json"}
tok = os.getenv("GITHUB_TOKEN", "").strip()
if tok:
    HEADERS["Authorization"] = f"Bearer {tok}"

def fetch_top_java(max_repos: int):
    repos = []
    page = 1
    while len(repos) < max_repos and page <= 10:  # Search API limita a 1000 (10x100)
        params = {
            "q": "language:Java stars:>1 fork:false archived:false",
            "sort": "stars",
            "order": "desc",
            "per_page": 100,
            "page": page,
        }
        r = requests.get("https://api.github.com/search/repositories",
                         headers=HEADERS, params=params, timeout=60)
        r.raise_for_status()
        items = r.json().get("items", [])
        if not items:
            break
        for it in items:
            full = it.get("full_name")
            if full and full not in repos:
                repos.append(full)
                if len(repos) >= max_repos:
                    break
        page += 1
        time.sleep(0.2)  # gentileza com a API
    return repos[:max_repos]

def get_metrics(full_name: str):
    #Nome do repositorio
    repo_url = f"https://api.github.com/repos/{full_name}"
    r = requests.get(repo_url, headers=HEADERS, timeout= 60)
    r.raise_for_status()
    repo_data = r.json()

    #Popularidade
    stars = repo_data.get("stargazers_count", 0)

    #Maturidade 

    created_at_full = repo_data.get("created_at", "")
    created_at = created_at_full.split('T')[0] if created_at_full else ""

    # 4. Atividade (número de releases)
    releases_url = f"https://api.github.com/repos/{full_name}/releases"
    try:
        r_releases = requests.get(releases_url, headers=HEADERS, timeout=60)
        r_releases.raise_for_status()
        releases = r_releases.json()
        num_releases = len(releases) if isinstance(releases, list) else 0
    except:
        num_releases = 0
    
    time.sleep(0.2)

    return {
    'full_name': full_name,
    'stars': stars,
    'releases': num_releases,
    'created_at': created_at
    }


def clone_repo(full_name: str):
    owner, repo = full_name.split("/", 1)
    dest = OUT / owner / repo
    if dest.exists():
        print(f"pulado (já existe): {full_name}")
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    url = f"https://github.com/{full_name}.git"
    res = subprocess.run(["git", "clone", "--depth", "1", "--quiet", url, str(dest)],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode == 0:
        print(f"OK   {full_name}")
    else:
        print(f"FALHA {full_name} :: {(res.stderr or res.stdout).strip()}")

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    repos = fetch_top_java(MAX)
    for i, full in enumerate(repos, 1):
        print(f"[{i}/{len(repos)}] {full}")
        clone_repo(full)
