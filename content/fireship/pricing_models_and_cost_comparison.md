---
title: Pricing Models and Cost Comparison
videoId: ucmbO2lWC2A
---

From: [[fireship]] <br/> 

Both [[features_and_pricing_of_aws_amplify | AWS Amplify]] and [[comparison_of_firebase_and_its_alternatives | Firebase]] are platforms designed to simplify app development and scale cloud infrastructure, and they both offer generous pricing models that include free tiers <a class="yt-timestamp" data-t="03:36:58">[03:36:58]</a>. Users generally do not incur costs until they achieve a significant number of active users <a class="yt-timestamp" data-t="03:41:04">[03:41:04]</a>.

## General Pricing Philosophy
Amazon's business strategy has historically driven prices to the lowest possible point, a characteristic embedded in its corporate culture <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. This is evident in AWS pricing trends; for instance, S3 storage buckets, which cost 15 cents per gigabyte ten years ago, are now priced at 2.3 cents per gigabyte, an 85% reduction over a decade <a class="yt-timestamp" data-t="03:16:08">[03:16:08]</a>. Generally, AWS services tend to be slightly cheaper than Google Cloud Platform (GCP) services <a class="yt-timestamp" data-t="03:46:04">[03:46:04]</a>.

## Service-Specific Costs

### Storage
*   **AWS**: A gigabyte of storage costs 2.3 cents <a class="yt-timestamp" data-t="03:49:09">[03:49:09]</a>.
*   **Firebase**: A gigabyte of storage costs 2.6 cents <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.

### User Authentication & Push Notifications
*   **Firebase**: Offers services like user authentication and push notifications as always free <a class="yt-timestamp" data-t="03:55:08">[03:55:08]</a>.
*   **AWS**: Charges approximately half a penny per monthly active user beyond 50,000 monthly active users <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.

### Database Operations (Real-time Data)
This is a complex area with distinct pricing models for each platform <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>.

#### Firebase (Firestore)
*   Billing is based on reads and writes to the database <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.
*   Real-time syncing of data occurs automatically, without additional charges <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.
*   For one million query or write operations:
    *   Read operations would cost 60 cents <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.
    *   Write operations would cost $1.80 <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.

#### AWS Amplify (AppSync with DynamoDB)
*   AppSync connects to a DynamoDB instance <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
*   AppSync charges $4 per 1 million query or write operations <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.
*   Additional costs may apply for the backend DynamoDB database itself <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>.
*   Billing is calculated in chunks of 5 kilobytes <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>. For example, a 100-kilobyte document equals 50 document read units <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>.
*   While direct comparisons are challenging, Firestore appears to be significantly less expensive for database operations as an app scales <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.

### Serverless Functions
*   **AWS**: Function invocations cost 20 cents per million <a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>.
*   **Firebase**: Function invocations cost 40 cents per million <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.

## Conclusion on Cost
The overall pricing between Firebase and AWS Amplify is almost equivalent, with the more economical choice depending on the specific usage patterns <a class="yt-timestamp" data-t="14:07:00">[14:07:00]</a>. AWS tends to be slightly cheaper for most services, including serverless functions, but Firebase can be significantly less expensive for database operations, especially with real-time data at scale <a class="yt-timestamp" data-t="03:46:04">[03:46:04]</a>, <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>, <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.