---
title: CDK and SDK implementation
videoId: wOdpDEkw_us
---

From: [[swarajmakesstuff]] <br/> 

This article details the implementation of event scheduling using AWS Cloud Development Kit (CDK) and Software Development Kit (SDK), specifically focusing on AWS EventBridge Schedulers for managing one-time events.

## Overview of Event Scheduling <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>

The system allows users to schedule posts by selecting a time, including up to 10 days or even a month into the future <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. At the scheduled time, the content is posted to the user's social media <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

While the scheduling is generally effective, it's important to note that it's not completely precise; there can be a delay of approximately 30 seconds to 2 minutes <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. For millisecond-precise timing, AWS Step Functions would be required <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. However, for quick implementation without significant complexity, AWS EventBridge Schedulers are utilized <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### Workflow <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>

The scheduling process involves the following steps:
1.  An event scheduler is created <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
2.  This scheduler invokes an AWS Lambda function at a specific time <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
3.  The Lambda function, which runs on AWS, sends a request to the server URL <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
4.  The server then executes the desired function <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. The Lambda function itself is simple, primarily just hitting the specified URL <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Types of Event Schedulers <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>

In CDK, there are two types of event schedulers:
*   **Reoccurring Schedulers**: These execute at regular intervals <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   **One-Time Schedulers**: These execute once and are then deleted <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. The focus here is on single-time event schedulers that execute and are subsequently deleted <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. This deletion is important because there is a limit of 1 million schedulers per instance, though more can be requested from Amazon <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Deleting them after execution ensures efficient resource management <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## Implementation Steps

### Prerequisites for Scheduler Creation <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>

To create an event scheduler, the following AWS components are required:
1.  **Lambda Function**: This function will be invoked by the scheduler <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
2.  **Policy**: A policy must be created that grants permission to invoke the specific Lambda function <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
3.  **IAM Role**: This policy is then assigned to an IAM role <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
4.  **Scheduler Assignment**: The IAM role is assigned to the scheduler, giving it permission to invoke the Lambda function <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
5.  **ARNs**: The scheduler requires the Amazon Resource Name (ARN) of the Lambda function and the ARN of the IAM role <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

### CDK Implementation for Initial Setup <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>

CDK is used for the one-time deployment of the foundational AWS resources, while the SDK is used for creating schedulers dynamically based on user input <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

#### Creating the Lambda Function with CDK <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>
The Lambda function is defined by specifying its runtime, handler, and the code directory <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. The Lambda function itself is straightforward, its primary job being to hit a given URL <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. It's crucial to build the Lambda code to a JavaScript (JS) file before deploying for proper execution <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

#### Creating the IAM Role and Policy with CDK <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>
A rule is created specifically for the EventBridge scheduler (`scheduler.amazonaws.com`) <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. A policy is then created to grant permission to invoke the Lambda function, referencing the Lambda function's ARN directly <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. This policy is then attached to the scheduler role <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

To obtain the ARNs of the scheduler role and the Lambda function, they can be logged during the CDK deployment using `cd.CNF.out` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. These ARNs are then used in the SDK implementation.

### SDK Implementation for Dynamic Scheduler Creation <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>

After installing the SDK for the scheduler <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>, an instance of the scheduler client can be created.

#### Creating a Schedule <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>
The `createSchedule` function is used, which takes parameters such as the scheduled time, a unique scheduler name, and the target URL <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

The payload for the scheduler includes:
*   **Target ARN**: The ARN of the Lambda function to be invoked <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Role ARN**: The ARN of the IAM role assigned to the scheduler <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   **Input/Payload**: Any data to be passed to the Lambda function <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **`ActionAfterCompletion`**: Set to `DELETE` for one-time schedulers, ensuring they are removed after execution <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   **Scheduler Expression**: The time expression must be in the specific format required by AWS <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>, and the time zone should be converted to UTC <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Unique Name**: Each schedule must have a unique name <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This is typically achieved by incorporating a unique identifier like a post ID (e.g., `post schedule for post/{post_id}`) <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

Finally, the `scheduler.createScheduler` method is called with the prepared input to create the scheduler <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. Once created, it will hit the specified URL when ready <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

This detailed process enables [[dynamic_onetime_event_schedulers | dynamic onetime event schedulers]] for various applications such as [[apertures_platform_features_and_functionality | Apertures platform features and functionality]] or [[building_in_public_for_developers | building in public for developers]].