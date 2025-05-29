---
title: Lambda function with event schedulers
videoId: wOdpDEkw_us
---

From: [[swarajmakesstuff]] <br/> 

This article details how to implement a scheduling feature using [[aws_eventbridge_schedulers | AWS EventBridge Schedulers]] and Lambda functions to post content to social media at a specific time <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. The system allows users to schedule posts days or even months in advance <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## System Overview and Precision

The scheduling system works by allowing a user to type content and select a future time for it to be posted <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. When the selected time arrives, the content is automatically posted to the chosen social media platform <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

It's important to note that this method is not completely precise; there might be a delay of approximately 30 seconds to 2 minutes <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. For millisecond-precise timing, AWS Step Functions would be required <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. However, for a quick setup with less complexity, the new [[aws_eventbridge_schedulers | AWS EventBridge Schedulers]] feature is suitable <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### How it Works

The core architecture involves three main components <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>:
1.  An [[aws_eventbridge_schedulers | event scheduler]] is created <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
2.  At the particular scheduled time, this scheduler invokes an AWS Lambda function <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
3.  The Lambda function then sends a request to the user's server, which executes the actual posting function <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. The Lambda function itself performs minimal logic, primarily hitting a specified URL <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Setting Up the Scheduler

Setting up the [[aws_eventbridge_schedulers | event scheduler]] involves several steps, typically orchestrated using CDK for initial deployment and SDK for dynamic scheduler creation based on user input <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

### 1. Create a Lambda Function

First, you need to create a Lambda function that will be invoked by the scheduler <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   Define the runtime and handler <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   The Lambda function's code will simply hit a specified URL <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
*   Ensure the Lambda code is built into a JS file before deployment for proper execution <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### 2. Create a Policy and IAM Role

Next, create a [[policy_and_iam_roles_for_scheduler | policy]] that grants permission to invoke this specific Lambda function <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   The [[policy_and_iam_roles_for_scheduler | policy]] explicitly states that it has permission to invoke the particular Lambda ARN <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   Create an [[policy_and_iam_roles_for_scheduler | IAM role]] and attach this policy to it <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This role will then be assigned to the scheduler, giving the scheduler the necessary permissions to invoke the Lambda <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   The role created for the scheduler should be `scheduler.amazonaws.com` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

### 3. Obtain ARNs

To create schedulers dynamically using the SDK, you will need the Amazon Resource Names (ARNs) of both:
*   Your Lambda function <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>
*   Your [[policy_and_iam_roles_for_scheduler | IAM role]] for the scheduler <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>
These can be obtained by logging them during the CDK deployment using `cdk.CfnOutput` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. These are one-time deployments that do not need to be re-created for each schedule <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Creating a Dynamic One-Time Event Scheduler

To create a [[dynamic_onetime_event_schedulers | dynamic onetime event scheduler]] based on user input:
1.  Install the scheduler SDK <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
2.  Create a scheduler instance using the SDK <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
3.  The `createSchedule` function takes several parameters <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>:
    *   **Time:** The specific time for the event to occur <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. Ensure the time format is converted to the proper UTC format that AWS expects <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
    *   **Scheduler Name:** A unique name for each individual schedule <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. Using a post ID or similar unique identifier is recommended (e.g., `post schedule post/post_ID`) <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
    *   **URL:** The target URL that the Lambda function will hit <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
    *   **Target ARN:** The ARN of the Lambda function (the target) <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
    *   **Role ARN:** The ARN of the [[policy_and_iam_roles_for_scheduler | IAM role]] created for the scheduler <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
    *   **Input/Payload:** Any data (e.g., content to post) that needs to be passed to the Lambda function <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
    *   **Action of Completion:** Set to `DELETE` so the scheduler is automatically deleted after it executes the Lambda function <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. This is crucial because there is a limit of 1 million schedulers per account (though more can be requested from Amazon) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Deleting them once they've served their purpose prevents hitting this limit <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Reoccurring Schedulers
In addition to [[dynamic_onetime_event_schedulers | one-time event schedulers]] (which execute and then get deleted), it's also possible to create reoccurring schedules that run at regular intervals <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Detailed information on this can be found in supplementary blog posts <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.