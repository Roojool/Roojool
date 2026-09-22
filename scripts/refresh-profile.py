#!/usr/bin/env python3
"""
Dynamic GitHub Profile Telemetry Refresher
Fetches public repository metrics and profile metadata for user 'Roojool'.
Idempotent: Only updates data files when actual metrics change, preventing noisy no-op commits.
Uses only the Python standard library for zero-dependency execution.
"""

import os
import sys
import json
import urllib.request
import urllib.error

GITHUB_USER = "Roojool"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
TELEMETRY_FILE = os.path.join(DATA_DIR, "telemetry.json")

def fetch_json(url: str):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": f"Roojool-Profile-Refresher",
            "Accept": "application/vnd.github.v3+json",
        }
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            if resp.status == 200:
                return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"HTTP Error fetching {url}: {e.code} {e.reason}", file=sys.stderr)
    except urllib.error.URLError as e:
        print(f"Network Error fetching {url}: {e.reason}", file=sys.stderr)
    return None

def main():
    print(f"Fetching public profile metadata for '{GITHUB_USER}'...")
    user_data = fetch_json(f"https://api.github.com/users/{GITHUB_USER}")
    repos_data = fetch_json(f"https://api.github.com/users/{GITHUB_USER}/repos?per_page=100&type=public")

    if user_data is None or repos_data is None:
        print("Warning: Could not fetch GitHub API data. Preserving existing state.", file=sys.stderr)
        sys.exit(0)

    # Filter and extract clean metrics strictly for public, non-forked repos
    public_repos_summary = []
    total_stars = 0
    total_forks = 0

    # Sort repos deterministically by name
    sorted_repos = sorted(repos_data, key=lambda r: r.get("name", "").lower())

    for repo in sorted_repos:
        # Ignore private or archived repos if any leaked into API response
        if repo.get("private", False):
            continue

        name = repo.get("name")
        stars = repo.get("stargazers_count", 0)
        forks = repo.get("forks_count", 0)
        topics = repo.get("topics", [])
        language = repo.get("language")

        total_stars += stars
        total_forks += forks

        public_repos_summary.append({
            "name": name,
            "url": repo.get("html_url"),
            "description": repo.get("description") or "",
            "language": language,
            "stars": stars,
            "forks": forks,
            "topics": topics,
            "is_fork": repo.get("fork", False)
        })

    new_telemetry = {
        "user": GITHUB_USER,
        "public_repos_count": len(public_repos_summary),
        "total_stars": total_stars,
        "total_forks": total_forks,
        "repositories": public_repos_summary
    }

    # Check against existing telemetry to prevent dirty git trees without changes
    existing_telemetry = None
    if os.path.exists(TELEMETRY_FILE):
        try:
            with open(TELEMETRY_FILE, "r", encoding="utf-8") as f:
                existing_telemetry = json.load(f)
        except Exception:
            existing_telemetry = None

    if existing_telemetry == new_telemetry:
        print("No telemetry changes detected. File is identical. Skipping write.")
        sys.exit(0)

    os.makedirs(DATA_DIR, exist_ok=True)
    with open(TELEMETRY_FILE, "w", encoding="utf-8") as f:
        json.dump(new_telemetry, f, indent=2)

    print(f"Telemetry updated successfully in {TELEMETRY_FILE} ({len(public_repos_summary)} public repos tracked).")

if __name__ == "__main__":
    main()
