---
title: Using GitHub Actions for Scheduled Tasks
videoId: eB0nUzAI7M8
---

From: [[fireship]] <br/> 

[[automating_with_github_actions | GitHub Actions]] can be used to run tasks on a specific, predetermined schedule <a class="yt-timestamp" data-t="10:55:56">[10:55:56]</a>. This capability addresses common problems, such as the need for regular database backups <a class="yt-timestamp" data-t="11:00:58">[11:00:58]</a>.

## Defining a Schedule

To trigger a workflow on a schedule, the `on` object in the workflow's YAML file uses the `schedule` event <a class="yt-timestamp" data-t="11:13:50">[11:13:50]</a>. The schedule is defined using `cron` syntax <a class="yt-timestamp" data-t="11:14:14">[11:14:14]</a>. For assistance with `cron` syntax, external tools like Crontab Guru can automatically generate schedules <a class="yt-timestamp" data-t="11:21:19">[11:21:19]</a>.

### Example Schedule

A common schedule might be to run a task every night at midnight <a class="yt-timestamp" data-t="11:25:27">[11:25:27]</a>.

## Real-World Example: Exporting Firestore Data

One practical application for scheduled tasks is the automated export of Firestore data, as the database does not currently provide automatic backups <a class="yt-timestamp" data-t="11:00:58">[11:00:58]</a>.

### Workflow Configuration

```yaml
# Example snippet for a scheduled workflow
on:
  schedule:
    # This example schedule runs every night at midnight
    - cron: '0 0 * * *'
jobs:
  export_firestore:
    runs-on: ubuntu-latest
    steps:
      - name: Setup Google Cloud SDK
        uses: google-github-actions/setup-gcloud@v0
        with:
          # Assumes GOOGLE_APPLICATION_CREDENTIALS secret is set
          service_account_key: ${{ secrets.GOOGLE_APPLICATION_CREDENTIALS }}
          project_id: your-gcp-project-id

      - name: Export Firestore Data
        run: |
          gcloud firestore export gs://your-storage-bucket
          # Additional commands could be added here
```

### Steps Involved

1.  **Set up `gcloud` CLI**: A dedicated [[automating_with_github_actions | GitHub Actions]] action, such as one maintained by Google Cloud Platform, sets up the `gcloud` CLI within the workflow's environment <a class="yt-timestamp" data-t="11:30:28">[11:30:28]</a>.
2.  **Run Export Commands**: Once `gcloud` is configured, commands can be executed to export Firestore data into a specified storage bucket <a class="yt-timestamp" data-t="11:34:39">[11:34:39]</a>. This process becomes fully automated, eliminating manual intervention <a class="yt-timestamp" data-t="11:40:42">[11:40:42]</a>.

Further details on setting up service accounts and `gcloud` are typically available in linked documentation <a class="yt-timestamp" data-t="11:44:03">[11:44:03]</a>.