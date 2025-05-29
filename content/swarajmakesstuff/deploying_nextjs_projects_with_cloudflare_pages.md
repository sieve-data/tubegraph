---
title: Deploying Nextjs Projects with Cloudflare Pages
videoId: VuuAAjkLRZs
---

From: [[swarajmakesstuff]] <br/> 

This guide outlines the process of deploying Next.js projects, specifically when [[integrating_cloudflare_d1_with_nextjs | integrating Cloudflare D1 with Next.js]] using Drizzle ORM, by leveraging Cloudflare Pages <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Why Cloudflare Pages for Next.js and D1?
To bind a [[using_drizzle_orm_with_cloudflare_d1 | Cloudflare D1 database]] directly with Next.js server actions or API routes, you need to use Cloudflare Pages <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Initial Project Setup
You can begin by installing Next.js through Cloudflare Pages commands <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, for example, by grabbing the command from Cloudflare Pages' documentation <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Deployment Workflow Considerations

### Connecting GitHub Repository
When deploying a Next.js application to Cloudflare Pages, there's a specific workflow recommended for linking with GitHub:
*   It's generally advised to initiate the connection from the Cloudflare Pages dashboard by linking it to your GitHub repository <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   Directly deploying from a local setup might not allow for connecting your GitHub repository to an already deployed Cloudflare Pages project <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This means if you deploy directly without linking GitHub first, you might not be able to connect it later <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Configuring for Production
For a deployed Next.js application to interact with your [[using_drizzle_orm_with_cloudflare_d1 | remote D1 database]], you need to configure Drizzle ORM with specific environment variables for production <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

The necessary values include:
*   `Cloudflare D1 Account ID` <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>
*   `Cloudflare D1 Database ID` <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>
*   `Cloudflare D1 API Token` <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>

### Retrieving Production Values

1.  **Database ID**: This ID is obtained when you create your D1 database using Wrangler <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
2.  **API Token**:
    *   Log into your Cloudflare account <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
    *   Go to "My Profile" in the top corner <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
    *   Navigate to "API Tokens" <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.
    *   Create a custom token, ensuring it has "Account" permissions for "Workers Script" and "Worker Routes" <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>, <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
    *   Copy the generated token for your environment variables <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
3.  **Account ID**:
    *   Go back to the main Cloudflare dashboard <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
    *   Navigate to "Workers & Pages" <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
    *   Your Account ID can be found on the overview page <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>, <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.

Once these values are set in your Cloudflare Pages environment, your application will be ready to interact with the production D1 database <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.