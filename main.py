#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import subprocess
import csv
import shutil
from pathlib import Path
from datetime import datetime
import requests
import re

CK_JAR = "ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar"
CK_RECURSIVE = "true"
CK_THREADS = "0"
CK_COMMENTS = "true"

MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("repos")
RESULTS = Path(sys.argv[3]) if len(sys.argv) > 3 else Path("results")

HEADERS = {"Accept": "application/vnd.github+json"}
tok = os.getenv("GITHUB_TOKEN", "").strip()
if tok:
    HEADERS["Authorization"] = f"Bearer {tok}"

def fetch_top_java(max_repos: int):
    repos = []
    page = 1
    while len(repos) < max_repos and page <= 50:
        params = {
            "q": "language:Java stars:>1 fork:false archived:false",
            "sort": "stars",
            "order": "desc",
            "per_page": 100,
            "page": page,
        }
        r = requests.get(
            "https://api.github.com/search/repositories",
            headers=HEADERS, params=params, timeout=60
        )
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
        time.sleep(0.2)
    return repos[:max_repos]

def _to_float(x):
    try:
        return float(str(x).strip())
    except:
        return None

def extract_ck_metrics(ck_results_folder: Path):
    candidates = sorted(ck_results_folder.glob("*class.csv"))
    metrics = {"avg_cbo": 0, "avg_dit": 0, "avg_lcom": 0, "total_classes": 0, "loc_ck": 0}

    if not candidates:
        print(f"Nenhum *class.csv encontrado em {ck_results_folder}")
        return metrics

    csv_file = candidates[0]
    try:
        with open(csv_file, "r", encoding="utf-8", errors="ignore") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if not rows:
            return metrics

        cbo_vals, dit_vals, lcom_vals, loc_vals = [], [], [], []
        for row in rows:
            cbo = _to_float(row.get("cbo"))
            if cbo is not None:
                cbo_vals.append(cbo)
            dit = _to_float(row.get("dit"))
            if dit is not None:
                dit_vals.append(dit)
            lcom = _to_float(row.get("lcom"))
            if lcom is not None:
                lcom_vals.append(lcom)
            loc = _to_float(row.get("loc"))
            if loc is not None:
                loc_vals.append(loc)

        metrics["total_classes"] = len(rows)
        metrics["avg_cbo"] = round(sum(cbo_vals)/len(cbo_vals), 2) if cbo_vals else 0
        metrics["avg_dit"] = round(sum(dit_vals)/len(dit_vals), 2) if dit_vals else 0
        metrics["avg_lcom"] = round(sum(lcom_vals)/len(lcom_vals), 2) if lcom_vals else 0
        metrics["loc_ck"] = int(sum(loc_vals)) if loc_vals else 0

        print(
            f"CK: {csv_file.name} -> "
            f"CBO={metrics['avg_cbo']} DIT={metrics['avg_dit']} "
            f"LCOM={metrics['avg_lcom']} LOC={metrics['loc_ck']}"
        )
        return metrics

    except Exception as e:
        print(f"Erro ao ler {csv_file}: {e}")
        return metrics

def count_comment_lines(repo_path: Path):
    if not repo_path.exists():
        return {"total_comment_lines": 0, "java_files_count": 0}
    
    total_comment_lines = 0
    
    java_files = list(repo_path.rglob("*.java"))
    
    for java_file in java_files:
        try:
            with open(java_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            lines = content.split('\n')
            in_multi_comment = False
            
            for line_num, line in enumerate(lines, 1):
                original_line = line
                line_stripped = line.strip()
                
                if not line_stripped:
                    continue
                
                if in_multi_comment:
                    total_comment_lines += 1
                    if '*/' in original_line:
                        in_multi_comment = False
                    continue
                
                if line_stripped.startswith('//'):
                    total_comment_lines += 1
                    continue
                
                if line_stripped.startswith('/*') and '*/' in line_stripped and line_stripped.find('/*') < line_stripped.rfind('*/'):
                    total_comment_lines += 1
                    continue
                
                if line_stripped.startswith('/*'):
                    total_comment_lines += 1
                    if '*/' not in original_line:
                        in_multi_comment = True
                    continue
                
                comment_pos = original_line.find('//')
                if comment_pos >= 0:
                    before_comment = original_line[:comment_pos]
                    
                    double_quotes = 0
                    single_quotes = 0
                    i = 0
                    while i < len(before_comment):
                        if before_comment[i] == '\\':
                            i += 2  
                            continue
                        elif before_comment[i] == '"':
                            double_quotes += 1
                        elif before_comment[i] == "'":
                            single_quotes += 1
                        i += 1
                   
                    if double_quotes % 2 == 0 and single_quotes % 2 == 0:
                    
                        comment_content = original_line[comment_pos:].strip()
                        if len(comment_content) > 2:  
                            total_comment_lines += 1
                        continue
                
                multi_start = original_line.find('/*')
                if multi_start >= 0:
                    before_comment = original_line[:multi_start]
                    double_quotes = 0
                    single_quotes = 0
                    i = 0
                    while i < len(before_comment):
                        if before_comment[i] == '\\':
                            i += 2
                            continue
                        elif before_comment[i] == '"':
                            double_quotes += 1
                        elif before_comment[i] == "'":
                            single_quotes += 1
                        i += 1
                    
                    if double_quotes % 2 == 0 and single_quotes % 2 == 0:
                        total_comment_lines += 1
                        multi_end = original_line.find('*/', multi_start)
                        if multi_end == -1:
                            in_multi_comment = True
        
        except Exception as e:
            print(f"Erro ao processar {java_file}: {e}")
            continue
    
    return {
        "total_comment_lines": total_comment_lines,
        "java_files_count": len(java_files)
    }

def get_metrics(full_name: str):
    repo_url = f"https://api.github.com/repos/{full_name}"
    r = requests.get(repo_url, headers=HEADERS, timeout=60)
    r.raise_for_status()
    repo_data = r.json()

    stars = repo_data.get("stargazers_count", 0)
    created_at_full = repo_data.get("created_at", "")
    created_at = created_at_full.split('T')[0] if created_at_full else ""

    age_years = 0
    if created_at_full:
        try:
            created_date = datetime.fromisoformat(created_at_full.replace('Z', '+00:00'))
            current_date = datetime.now(created_date.tzinfo)
            age_days = (current_date - created_date).days
            age_years = round(age_days / 365.25, 2)
        except:
            age_years = 0

    num_releases = 0
    page = 1
    per_page = 100
    while True:
        r_releases = requests.get(
            f"https://api.github.com/repos/{full_name}/releases",
            headers=HEADERS,
            params={"per_page": per_page, "page": page},
            timeout=60
        )
        if r_releases.status_code == 404:
            num_releases = 0
            break

        r_releases.raise_for_status()
        items = r_releases.json()
        if not isinstance(items, list) or not items:
            break

        num_releases += sum(1 for rel in items if not rel.get("draft", False))

        link = r_releases.headers.get("Link", "")
        if len(items) < per_page and 'rel="next"' not in link:
            break

        page += 1
        time.sleep(0.2)

    time.sleep(0.2)

    return {
        "full_name": full_name,
        "stars": stars,
        "releases": num_releases,
        "created_at": created_at,
        "age_years": age_years
    }

def clone_repo(full_name: str):
    owner, repo = full_name.split("/", 1)
    dest = OUT / owner / repo
    if dest.exists():
        print(f"pulado (já existe): {full_name}")
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    url = f"https://github.com/{full_name}.git"

    git_cmd = shutil.which("git") or r"C:\Program Files\Git\cmd\git.exe"
    if not git_cmd or not Path(git_cmd).exists():
        raise RuntimeError("Git não encontrado. Instale o Git e garanta que 'git' esteja no PATH.")

    res = subprocess.run(
        [git_cmd, "clone", "--depth", "1", "--quiet", url, str(dest)],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if res.returncode == 0:
        print(f"OK   {full_name}")
        return dest
    else:
        print(f"Falha {full_name} :: {(res.stderr or res.stdout).strip()}")
        return None

def run_ck(repo_path: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    base_csv = out_dir / "ck_result"  

    cmd = [
        "java", "-jar", CK_JAR,
        str(repo_path),
        CK_RECURSIVE,
        CK_THREADS,
        CK_COMMENTS,
        str(base_csv)
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print(f"[CK ERRO] {repo_path} :: {(res.stderr or res.stdout).strip()}")
        return False
    else:
        print(f"[CK OK]   {repo_path}")
        return True

def append_summary_row(summary_csv: Path, row: dict, headers: list):
    new_file = not summary_csv.exists()
    with summary_csv.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=headers)
        if new_file:
            w.writeheader()
        w.writerow(row)

if __name__ == "__main__":
    if not Path(CK_JAR).exists():
        print(f"CK_JAR não encontrado {CK_JAR}")
        sys.exit(1)

    OUT.mkdir(parents=True, exist_ok=True)
    RESULTS.mkdir(parents=True, exist_ok=True)

    summary_csv = RESULTS / "repos_summary.csv"
    if summary_csv.exists():
        summary_csv.unlink()

    repos = fetch_top_java(MAX)

    summary_headers = [
        "full_name", "stars", "releases", "created_at", "age_years",
        "loc", "avg_cbo", "avg_dit", "avg_lcom", "total_classes",
        "total_comment_lines", "java_files_count"
    ]

    for i, full in enumerate(repos, 1):
        repo_path = clone_repo(full)
        if not repo_path:
            continue

        owner, repo = full.split("/", 1)
        repo_results = RESULTS / owner / repo

        ck_success = run_ck(repo_path, repo_results)

        ck_metrics = extract_ck_metrics(repo_results) if ck_success else {
            "avg_cbo": 0, "avg_dit": 0, "avg_lcom": 0, "total_classes": 0, "loc_ck": 0
        }
        comment_metrics = count_comment_lines(repo_path)

        meta = get_metrics(full)

        final_row = {
            **meta,
            "loc": ck_metrics.get("loc_ck", 0),
            "avg_cbo": ck_metrics.get("avg_cbo", 0),
            "avg_dit": ck_metrics.get("avg_dit", 0),
            "avg_lcom": ck_metrics.get("avg_lcom", 0),
            "total_classes": ck_metrics.get("total_classes", 0),
            "total_comment_lines": comment_metrics["total_comment_lines"],
            "java_files_count": comment_metrics["java_files_count"]
        }

        append_summary_row(summary_csv, final_row, summary_headers)
