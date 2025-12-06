# 📊 Traffic Statistics

**Organization:** Applied-Ai-Philosophy  
**Status:** Awaiting first collection run

## About

This directory contains traffic statistics collected automatically by the daily workflow.

The workflow runs every day at 06:00 UTC and collects:
- Page views and unique visitors
- Repository clones
- Popular paths
- Popular referrers

## Files

- `traffic_latest.json` - Most recent traffic data
- `traffic_YYYY-MM-DD.json` - Daily snapshots
- `README.md` - This summary (auto-generated)

## Setup Required

To enable traffic statistics collection, you need to:

1. Create a GitHub Personal Access Token with `repo` scope
2. Add the token as a repository secret named `ORG_TRAFFIC_TOKEN`

See the workflow at `.github/workflows/traffic-stats.yml` for details.

---

*This data is automatically collected daily by the traffic statistics workflow.*  
*GitHub traffic data is only available for the last 14 days.*
