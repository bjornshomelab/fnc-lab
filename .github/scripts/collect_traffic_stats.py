#!/usr/bin/env python3
"""
Traffic Statistics Collector for Applied-Ai-Philosophy Organization

This script fetches traffic statistics from all repositories in the
Applied-Ai-Philosophy organization and stores them in a structured format.

GitHub Traffic API provides:
- Views: Number of page views
- Clones: Number of repository clones
- Popular paths: Most visited paths
- Popular referrers: Top referrers

Note: Traffic data is only available for the last 14 days and requires
push access to the repository.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

import requests

# Constants
REQUEST_TIMEOUT = 30


def get_headers(token: str) -> dict:
    """Return standard headers for GitHub API requests."""
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
    }


def get_org_repos(token: str, org_name: str) -> list[dict]:
    """Fetch all repositories in the organization."""
    headers = get_headers(token)
    repos = []
    page = 1
    
    while True:
        url = f"https://api.github.com/orgs/{org_name}/repos"
        params = {"per_page": 100, "page": page}
        
        response = requests.get(url, headers=headers, params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        
        data = response.json()
        if not data:
            break
            
        repos.extend(data)
        page += 1
        
    return repos


def get_traffic_views(token: str, owner: str, repo: str) -> dict:
    """Fetch traffic views for a repository."""
    headers = get_headers(token)
    url = f"https://api.github.com/repos/{owner}/{repo}/traffic/views"
    
    try:
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            print(f"  ⚠️  No access to traffic data for {repo}")
            return {"count": 0, "uniques": 0, "views": []}
        raise


def get_traffic_clones(token: str, owner: str, repo: str) -> dict:
    """Fetch traffic clones for a repository."""
    headers = get_headers(token)
    url = f"https://api.github.com/repos/{owner}/{repo}/traffic/clones"
    
    try:
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            print(f"  ⚠️  No access to clone data for {repo}")
            return {"count": 0, "uniques": 0, "clones": []}
        raise


def get_popular_paths(token: str, owner: str, repo: str) -> list:
    """Fetch popular paths for a repository."""
    headers = get_headers(token)
    url = f"https://api.github.com/repos/{owner}/{repo}/traffic/popular/paths"
    
    try:
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            return []
        raise


def get_popular_referrers(token: str, owner: str, repo: str) -> list:
    """Fetch popular referrers for a repository."""
    headers = get_headers(token)
    url = f"https://api.github.com/repos/{owner}/{repo}/traffic/popular/referrers"
    
    try:
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            return []
        raise


def collect_all_traffic_stats(token: str, org_name: str) -> dict:
    """Collect traffic statistics for all repositories in the organization."""
    print(f"📊 Collecting traffic statistics for {org_name}")
    print("=" * 50)
    
    # Get all repositories
    repos = get_org_repos(token, org_name)
    print(f"Found {len(repos)} repositories\n")
    
    stats = {
        "organization": org_name,
        "collected_at": datetime.utcnow().isoformat() + "Z",
        "repositories": {},
        "summary": {
            "total_views": 0,
            "total_unique_views": 0,
            "total_clones": 0,
            "total_unique_clones": 0,
        },
    }
    
    for repo in repos:
        repo_name = repo["name"]
        print(f"📁 {repo_name}")
        
        # Collect all traffic data
        views = get_traffic_views(token, org_name, repo_name)
        clones = get_traffic_clones(token, org_name, repo_name)
        paths = get_popular_paths(token, org_name, repo_name)
        referrers = get_popular_referrers(token, org_name, repo_name)
        
        repo_stats = {
            "full_name": repo["full_name"],
            "description": repo.get("description", ""),
            "private": repo["private"],
            "views": {
                "total": views.get("count", 0),
                "unique": views.get("uniques", 0),
                "daily": views.get("views", []),
            },
            "clones": {
                "total": clones.get("count", 0),
                "unique": clones.get("uniques", 0),
                "daily": clones.get("clones", []),
            },
            "popular_paths": paths[:10],  # Top 10 paths
            "popular_referrers": referrers[:10],  # Top 10 referrers
        }
        
        stats["repositories"][repo_name] = repo_stats
        
        # Update summary
        stats["summary"]["total_views"] += views.get("count", 0)
        stats["summary"]["total_unique_views"] += views.get("uniques", 0)
        stats["summary"]["total_clones"] += clones.get("count", 0)
        stats["summary"]["total_unique_clones"] += clones.get("uniques", 0)
        
        print(f"   Views: {views.get('count', 0)} (unique: {views.get('uniques', 0)})")
        print(f"   Clones: {clones.get('count', 0)} (unique: {clones.get('uniques', 0)})")
        print()
    
    return stats


def save_stats(stats: dict, output_dir: Path) -> None:
    """Save statistics to files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save dated snapshot
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    snapshot_file = output_dir / f"traffic_{date_str}.json"
    
    with open(snapshot_file, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Saved snapshot to {snapshot_file}")
    
    # Save latest copy
    latest_file = output_dir / "traffic_latest.json"
    with open(latest_file, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Updated {latest_file}")
    
    # Generate markdown summary
    summary_file = output_dir / "README.md"
    generate_markdown_summary(stats, summary_file)
    print(f"✅ Generated {summary_file}")


def generate_markdown_summary(stats: dict, output_file: Path) -> None:
    """Generate a markdown summary of traffic statistics."""
    lines = [
        "# 📊 Traffic Statistics",
        "",
        f"**Organization:** {stats['organization']}  ",
        f"**Last Updated:** {stats['collected_at']}",
        "",
        "## Summary",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Total Views | {stats['summary']['total_views']:,} |",
        f"| Unique Visitors | {stats['summary']['total_unique_views']:,} |",
        f"| Total Clones | {stats['summary']['total_clones']:,} |",
        f"| Unique Cloners | {stats['summary']['total_unique_clones']:,} |",
        "",
        "## Repository Breakdown",
        "",
    ]
    
    # Sort repos by views
    sorted_repos = sorted(
        stats["repositories"].items(),
        key=lambda x: x[1]["views"]["total"],
        reverse=True,
    )
    
    lines.append("| Repository | Views | Unique | Clones | Unique |")
    lines.append("|------------|-------|--------|--------|--------|")
    
    for repo_name, repo_stats in sorted_repos:
        lines.append(
            f"| [{repo_name}](https://github.com/{repo_stats['full_name']}) | "
            f"{repo_stats['views']['total']:,} | "
            f"{repo_stats['views']['unique']:,} | "
            f"{repo_stats['clones']['total']:,} | "
            f"{repo_stats['clones']['unique']:,} |"
        )
    
    lines.extend([
        "",
        "---",
        "",
        "*This data is automatically collected daily by the traffic statistics workflow.*  ",
        "*GitHub traffic data is only available for the last 14 days.*",
    ])
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    """Main entry point."""
    # Get configuration from environment
    token = os.environ.get("GITHUB_TOKEN")
    org_name = os.environ.get("ORG_NAME", "Applied-Ai-Philosophy")
    
    if not token:
        print("❌ Error: GITHUB_TOKEN environment variable is required")
        print("   Create a Personal Access Token with 'repo' scope")
        print("   and add it as a repository secret named 'ORG_TRAFFIC_TOKEN'")
        sys.exit(1)
    
    # Collect statistics
    stats = collect_all_traffic_stats(token, org_name)
    
    # Print summary
    print("=" * 50)
    print("📈 Summary")
    print(f"   Total Views: {stats['summary']['total_views']:,}")
    print(f"   Unique Visitors: {stats['summary']['total_unique_views']:,}")
    print(f"   Total Clones: {stats['summary']['total_clones']:,}")
    print(f"   Unique Cloners: {stats['summary']['total_unique_clones']:,}")
    
    # Save to data directory
    output_dir = Path("data/traffic_stats")
    save_stats(stats, output_dir)
    
    print("\n✨ Traffic statistics collection complete!")


if __name__ == "__main__":
    main()
