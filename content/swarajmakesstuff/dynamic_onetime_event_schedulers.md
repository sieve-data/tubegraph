---
title: Dynamic onetime event schedulers
videoId: wOdpDEkw_us
---

From: [[swarajmakesstuff]] <br/> 

This article explores the implementation of dynamic onetime event schedulers, primarily focusing on their application in automating social media posts and the underlying AWS technologies.

## Scheduling Functionality
The scheduling system allows users to type content and select a specific time for it to be posted to social media platforms <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>, <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>, <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. While the demonstration primarily shows scheduling up to 10 days in advance for testing, the system is capable of scheduling posts for any time in the future, including months away <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Precision
It's important to note that this scheduling mechanism is not entirely precise <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. There can be an approximate delay ranging from 30 seconds to 2 minutes <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. For millisecond-precise timing with AWS, [[Lambda function with event schedulers | Step Functions]] would be required <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>, <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. However, for quicker implementation and less complexity, [[AWS EventBridge schedulers | EventBridge schedulers]] offer a suitable alternative <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>, <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## How it Works (AWS Implementation)
The system leverages [[AWS EventBridge schedulers | AWS EventBridge schedulers]] to manage event timing <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

The workflow is as follows:
1.  An [[AWS EventBridge schedulers | event scheduler]] is created <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
2.  At the specified time, the [[AWS EventBridge schedulers | event scheduler]] invokes an [[Lambda function with event schedulers | AWS Lambda function]] <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>, <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>, <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
3.  The [[Lambda function with event schedulers | Lambda function]] sends a request to the main server, which then executes the desired function (e.g., posting to social media) <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>, <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
4.  The [[Lambda function with event schedulers | Lambda function]] itself is lightweight, primarily designed to hit a specified URL <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>, <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>, <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

## Types of Schedulers
There are two main types of [[AWS EventBridge schedulers | event schedulers]]:
*   **Reoccurring Schedulers**: These execute at regular intervals <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>, <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   **Onetime Schedulers**: These execute once and are then deleted <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
    *   This article focuses on the implementation of single-time event schedulers due to a limit of 1 million schedulers per instance <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>, <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>, <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Deleting a scheduler after its execution optimizes resource usage <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>, <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## Creating a Onetime Scheduler
To implement a dynamic onetime scheduler, several AWS components are required:

### 1. [[Lambda function with event schedulers | Lambda Function]] Creation
*   First, create the [[Lambda function with event schedulers | Lambda function]] that will be invoked by the scheduler <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>, <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   This function needs to be built into a JS file before deployment for proper execution by [[Lambda function with event schedulers | Lambda]] <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>, <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>, <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>, <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### 2. [[Policy and IAM roles for scheduler | Policy and IAM Role]] Setup
*   A [[Policy and IAM roles for scheduler | policy]] must be created that grants permission to invoke the specific [[Lambda function with event schedulers | Lambda function]] <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>, <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>, <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>, <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>, <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   This [[Policy and IAM roles for scheduler | policy]] is then assigned to an [[Policy and IAM roles for scheduler | IAM role]] <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>, <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>, <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>, <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>, <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   The [[Policy and IAM roles for scheduler | IAM role]] provides the necessary permissions for the scheduler to invoke the [[Lambda function with event schedulers | Lambda function]] <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>, <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>, <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>, <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

### 3. Scheduler Configuration
To create the scheduler, two key ARN (Amazon Resource Name) values are required:
*   The ARN of the [[Lambda function with event schedulers | Lambda function]] <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>, <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>, <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   The ARN of the [[Policy and IAM roles for scheduler | IAM role]] <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>, <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

These ARNs can be retrieved using `cdk.cnf.out` during [[CDK and SDK implementation | CDK deployment]] <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>, <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>, <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

### [[CDK and SDK implementation | CDK and SDK Implementation]]
The overall process involves a combination of [[CDK and SDK implementation | CDK]] for one-time infrastructure setup and [[CDK and SDK implementation | SDK]] for dynamic scheduler creation based on user input <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>, <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>, <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>, <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>, <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

*   **[[CDK and SDK implementation | CDK]]**: Used to deploy the [[Lambda function with event schedulers | Lambda function]] and [[Policy and IAM roles for scheduler | IAM roles]] once <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>, <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>, <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>, <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>, <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **[[CDK and SDK implementation | SDK]]**: Used to dynamically create schedules based on user input <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>, <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>, <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>, <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

When creating a schedule via [[CDK and SDK implementation | SDK]]:
*   It requires the target time, a unique scheduler name, and the URL <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>, <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   The scheduler provides a payload to the [[Lambda function with event schedulers | Lambda function]] <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>, <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>, <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   It uses the [[Lambda function with event schedulers | Lambda function]] ARN (target ARN) and the [[Policy and IAM roles for scheduler | IAM role]] ARN <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>, <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>, <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>, <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   The `action of completion` is set to `delete` to automatically remove the scheduler after execution <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>, <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
*   The scheduler expression must follow AWS's required format, with time converted to UTC <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>, <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>, <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>, <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>, <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   Each scheduler must have a unique name <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>, <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>, <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>, <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>, typically incorporating a unique post ID <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>, <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   The scheduler is initiated using `scheduler.createScheduler` <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>, <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.