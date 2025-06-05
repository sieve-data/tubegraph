---
title: Continuous Deployment using Firebase
videoId: eB0nUzAI7M8
---

From: [[fireship]] <br/> 

Continuous Deployment (CD) is the process of automatically pushing new code changes out to customers once the code has been merged into the codebase <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>. It is a distinct phase from Continuous Integration (CI), which focuses on merging new code into the codebase <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>.

## Integrating Firebase for Continuous Deployment

To demonstrate continuous deployment, a third-party host like [[Introduction to Firebase and benefits | Firebase]] can be integrated <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>. A helpful guide for these steps is available on Fireship IO <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.

### Local Setup for Firebase Hosting

Setting up hosting locally with [[Setting up and managing Firebase projects | Firebase]] is straightforward by running `firebase init hosting` <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>. Code can then be pushed to a [[Deploying and hosting applications with Firebase | Firebase]] hosting account using `firebase deploy` <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>. This works locally because the system is authenticated into the [[Setting up and managing Firebase projects | Firebase]] account <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a>.

### Authenticating a Remote CI Server

To enable a remote CI server to deploy to [[Setting up and managing Firebase projects | Firebase]], a secret token must be shared with GitHub <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>.

1.  **Obtain the Token**: Run `firebase login:ci` to get a token string, which acts as an API key or username/password combination <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>. This value should be kept secret <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.
2.  **Store as GitHub Secret**: Copy the token value <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>. In your GitHub repository, navigate to "Settings" then "Secrets" and add a new secret <a class="yt-timestamp" data-t="06:53:00">[06:53:00]</a>. Name it `FIREBASE_TOKEN` (all caps) and paste the token value <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>. GitHub encrypts this value for secure access from the CI server, allowing secure authentication with [[Setting up and managing Firebase projects | Firebase]] from a GitHub Actions workflow <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>.

## GitHub Actions Workflow for Continuous Deployment

A new YAML file, for example, `deploy.yaml`, is created in the `.github/workflows` directory <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>.

### Workflow Configuration

*   **Trigger Event**: Unlike CI, this workflow is triggered on a `push` event to the `master` branch, meaning it runs when code is pushed directly or a pull request is merged <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>.
*   **Job Definition**: The deployment job is similar to a CI job:
    *   **Environment**: Runs on Ubuntu <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.
    *   **Steps**:
        *   `actions/checkout@v2`: Retrieves the source code into the virtual machine <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>.
        *   `actions/setup-node@v2`: Sets up Node.js for running commands <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>.
        *   `npm ci`: Installs all dependencies <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>.
        *   `npm run build`: Builds the application <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>.
        *   **Deployment**: Uses a third-party action, `firebase-action`, to handle the setup of the [[Setting up and managing Firebase projects | Firebase]] CLI on the server <a class="yt-timestamp" data-t="07:38:00">[07:38:00]</a>. It's configured to run `firebase deploy --only hosting` <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>.
        *   **Authentication**: The `FIREBASE_TOKEN` secret is accessed securely using `secrets.FIREBASE_TOKEN` to authenticate the deployment <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a>.

```yaml
# Example deploy.yaml structure
name: Deploy to Firebase Hosting

on:
  push:
    branches:
      - master

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
        with:
          node-version: '14' # Or your desired node version
      - name: Install dependencies
        run: npm ci
      - name: Build application
        run: npm run build
      - name: Deploy to Firebase
        uses: w9jds/firebase-action@master
        with:
          args: deploy --only hosting
        env:
          FIREBASE_TOKEN: ${{ secrets.FIREBASE_TOKEN }}
```

### Execution and Verification

Once the workflow is committed to the `master` branch <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>, merging a pull request will automatically trigger the build and [[Deploying and hosting applications with Firebase | deployment of the code to Firebase]] <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>. The changes should then be automatically reflected on the live website <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>.