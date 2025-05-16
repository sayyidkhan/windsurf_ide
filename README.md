# windsurf_ide

# 📁 File Downloader and Splitter (GitHub Actions)

This repository contains a GitHub Actions workflow that:
1. Downloads a file from a specified URL
2. Splits it evenly into 10 parts
3. Uploads the parts as an artifact for download

---

## 🚀 How It Works

The workflow is defined in `.github/workflows/run-download-split.yml`.

- The Python script (`download_and_split.py`) performs the download and splitting.
- The split files are stored as GitHub Action artifacts (not committed to the repo).

---

## 🔁 Triggering the Workflow

### ✅ Option 1: Manual Trigger
You can manually run the workflow from GitHub's UI:

1. Go to the **Actions** tab in your repo.
2. Select the workflow: **"Download and Split File Monthly"**
3. Click **“Run workflow”** (top-right button)
4. Hit **Run workflow** again in the modal

### 📅 Option 2: Automatic Monthly Trigger
This workflow is automatically scheduled to run on:

🗓️ 1st day of every month at 00:00 UTC

yaml
Copy
Edit

You can change this schedule by editing the `cron` expression in `.github/workflows/run-download-split.yml`.

---

## 📥 Retrieving the Output

1. After the workflow finishes, go to the **Actions** tab
2. Open the latest run
3. Scroll down to the **Artifacts** section
4. Click on `file-parts` to download a ZIP containing the 10 split files

---

## 🛠️ Configuration

To change the file being downloaded:
- Edit the URL in [`download_and_split.py`](./download_and_split.py):
  ```python
  url = "https://example.com/path/to/file.zip"  # Replace this
📎 Dependencies
Python 3.10+

requests library (auto-installed in GitHub Actions)

🧩 File Output Example
After the script runs, you’ll get files like:

python
Copy
Edit
downloaded_file.zip.part1
downloaded_file.zip.part2
...
downloaded_file.zip.part10
These will be bundled and available as a downloadable artifact.

