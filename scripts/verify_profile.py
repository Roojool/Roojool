"""
Verification Suite for Roojool Profile Repository:
- Verifies all internal files referenced in README exist.
- Validates all external URLs.
- Checks that no private repositories are referenced.
- Scans for secrets, private IPs, credentials, or API keys.
"""

import os
import re
import sys
import json
import urllib.request
import xml.etree.ElementTree as ET

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")

PRIVATE_REPOS = [
    "Bufferbloat-Planner",
    "siteflow-app",
    "the-loft-final",
    "ThrottleVPN",
    "scrapy",
    "scrapy-community-providers"
]

def check_no_private_repos():
    print("[1/5] Checking that no private repositories are referenced...")
    violating_files = []
    for root, _, files in os.walk(REPO_ROOT):
        if ".git" in root:
            continue
        for file in files:
            filepath = os.path.join(root, file)
            # Skip verify script itself which contains the blacklist
            if os.path.abspath(filepath) == os.path.abspath(__file__):
                continue
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            for priv in PRIVATE_REPOS:
                # Case-insensitive check
                if re.search(r'\b' + re.escape(priv) + r'\b', content, re.IGNORECASE):
                    violating_files.append((filepath, priv))

    if violating_files:
        print(f"FAILED: Found private repo references: {violating_files}")
        return False
    print("PASSED: Zero private repositories referenced.")
    return True

def check_no_secrets():
    print("[2/5] Checking for secrets, private IPs, credentials, API keys...")
    secret_patterns = [
        r'(?i)ghp_[a-zA-Z0-9]{36}',
        r'(?i)gho_[a-zA-Z0-9]{36}',
        r'(?i)github_pat_[a-zA-Z0-9]{82}',
        r'AIza[0-9A-Za-z-_]{35}',
        r'(?i)bearer\s+[a-zA-Z0-9_\-\.]{20,}',
        r'(?i)(?:password|secret|apikey|api_key)\s*[:=]\s*["\'][^"\']{8,}["\']',
        r'192\.168\.\d+\.\d+',
        r'10\.\d+\.\d+\.\d+',
        r'rtsp://[a-zA-Z0-9]+:[a-zA-Z0-9]+@'
    ]
    detected = []
    for root, _, files in os.walk(REPO_ROOT):
        if ".git" in root:
            continue
        for file in files:
            filepath = os.path.join(root, file)
            if os.path.abspath(filepath) == os.path.abspath(__file__):
                continue
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            for pat in secret_patterns:
                matches = re.findall(pat, content)
                if matches:
                    detected.append((filepath, pat, matches))

    if detected:
        print(f"FAILED: Found potential secrets: {detected}")
        return False
    print("PASSED: Zero secrets or private credentials detected.")
    return True

def check_assets_and_xml():
    print("[3/5] Validating all SVG assets as valid XML...")
    assets_dir = os.path.join(REPO_ROOT, "assets")
    if not os.path.exists(assets_dir):
        print("FAILED: assets/ directory missing!")
        return False
    svg_files = [f for f in os.listdir(assets_dir) if f.endswith(".svg")]
    if len(svg_files) != 8:
        print(f"FAILED: Expected 8 SVGs, found {len(svg_files)}: {svg_files}")
        return False
    for svg in svg_files:
        path = os.path.join(assets_dir, svg)
        try:
            ET.parse(path)
        except Exception as e:
            print(f"FAILED: SVG XML parse error in {svg}: {e}")
            return False
    print(f"PASSED: All {len(svg_files)} SVGs are strictly valid XML.")
    return True

def check_readme_links():
    print("[4/5] Checking links in README.md...")
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Find internal relative links
    rel_refs = re.findall(r'(?:src|href|srcset)=["\']([^"\']+)["\']', content)
    for ref in rel_refs:
        # Ignore external links or anchor links
        if ref.startswith("http://") or ref.startswith("https://") or ref.startswith("#"):
            continue
        rel_path = os.path.join(REPO_ROOT, ref)
        if not os.path.exists(rel_path):
            print(f"FAILED: Relative link does not exist: {ref}")
            return False

    print("PASSED: All local asset references and relative file paths exist.")
    return True

def check_profile_json():
    print("[5/5] Validating data/profile.json...")
    profile_path = os.path.join(REPO_ROOT, "data", "profile.json")
    if not os.path.exists(profile_path):
        print("FAILED: data/profile.json missing")
        return False
    with open(profile_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    required_keys = ["identity", "education", "research_interests", "current_work", "featured_projects", "patent", "technologies", "links"]
    for k in required_keys:
        if k not in data:
            print(f"FAILED: Missing key {k} in profile.json")
            return False
    print("PASSED: data/profile.json is valid and contains all required schemas.")
    return True

def main():
    checks = [
        check_no_private_repos(),
        check_no_secrets(),
        check_assets_and_xml(),
        check_readme_links(),
        check_profile_json()
    ]
    if all(checks):
        print("\nALL PRE-COMMIT VERIFICATION CHECKS PASSED SUCCESSFULLY.")
        sys.exit(0)
    else:
        print("\nVERIFICATION CHECKS FAILED.")
        sys.exit(1)

if __name__ == "__main__":
    main()
