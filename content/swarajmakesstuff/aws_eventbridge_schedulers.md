---
title: AWS EventBridge schedulers
videoId: wOdpDEkw_us
---

From: [[swarajmakesstuff]] <br/> 

AWS EventBridge Schedulers provide a way to schedule actions, such as posting to social media at a specific time <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. This service allows users to schedule events far into the future, such as 10 days or even a month away <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## How Scheduling Works
A user types in content and selects a time for it to be posted <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. At the chosen time, the content is automatically posted to the specified social media <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. The system internally creates a schedule that triggers a URL at the precise time <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Precision
EventBridge schedulers are not completely precise; there can be a delay of approximately 30 seconds to 2 minutes <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. For millisecond-precise timing with AWS, [[server_components_without_a_server | Step Functions]] should be used <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. However, for quick implementation without excessive complexity, EventBridge schedulers are a suitable choice <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Architecture
The scheduling process involves an [[dynamic_onetime_event_schedulers | EventBridge scheduler]] that invokes a [[lambda_function_with_event_schedulers | Lambda function]] at a particular time <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. This [[lambda_function_with_event_schedulers | Lambda function]] then sends a request to the user's server, which executes the desired function <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. The [[lambda_function_with_event_schedulers | Lambda function]]'s primary role is simply to hit a specified URL <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

## Types of Event Schedulers
There are two main types of [[dynamic_onetime_event_schedulers | EventBridge schedulers]] in AWS CDK <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>:
*   **One-time event scheduler**: Executes once and then is deleted <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Reoccurring scheduler**: Occurs at regular intervals <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

It is best practice to delete [[dynamic_onetime_event_schedulers | one-time schedulers]] after they execute, as there is a limit of 1 million schedulers per instance, although more can be requested from Amazon <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Implementation Steps
Creating a scheduler involves several AWS components and configurations:

### 1. Create a Lambda Function
First, a [[lambda_function_with_event_schedulers | Lambda function]] needs to be created, which will be invoked by the scheduler <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   Assign the runtime and handler <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   The [[lambda_function_with_event_schedulers | Lambda function]]'s code typically just hits a URL <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
*   Before deployment, build the Lambda function code to a JS file for proper execution <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### 2. Create an IAM Policy and Role
Next, create a [[policy_and_iam_roles_for_scheduler | policy]] that grants permission to invoke the specific [[lambda_function_with_event_schedulers | Lambda function]] <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   This [[policy_and_iam_roles_for_scheduler | policy]] is then assigned to an [[policy_and_iam_roles_for_scheduler | IAM rule]] <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   The [[policy_and_iam_roles_for_scheduler | IAM rule]] is given to the scheduler, providing it with the necessary permissions to invoke the [[lambda_function_with_event_schedulers | Lambda function]] <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The rule for the scheduler is `scheduler.amazonaws.com` <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   The [[policy_and_iam_roles_for_scheduler | policy]] directly assigns the ARN of the [[lambda_function_with_event_schedulers | Lambda function]] <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

### 3. Deploying Infrastructure (CDK)
The [[lambda_function_with_event_schedulers | Lambda function]] and [[policy_and_iam_roles_for_scheduler | IAM rule]] are generally one-time deployments, which can be handled using AWS CDK (Cloud Development Kit) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   To get the ARNs (Amazon Resource Names) of the deployed [[lambda_function_with_event_schedulers | Lambda function]] and the scheduler [[policy_and_iam_roles_for_scheduler | IAM rule]], use `cd.CNF.out` to log these values during deployment <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. These ARNs are then copied for use in the SDK <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

### 4. Creating Schedules (SDK)
To create schedulers dynamically based on user input, the AWS SDK for scheduler is used <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   Install the scheduler SDK <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   Create a schedule instance, providing the desired time, a unique scheduler name, and the target URL <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Key parameters for creating a schedule**:
    *   `Arn of Lambda function` (target ARN) <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>
    *   `Arn of IAM Rule` (for your scheduler) <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>
    *   `Input/Payload`: Data passed to the [[lambda_function_with_event_schedulers | Lambda function]] <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
    *   `Action on completion`: Set to `delete` for [[dynamic_onetime_event_schedulers | one-time schedulers]] <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
    *   `Scheduler expression`: Time in the format AWS requires, often converted to UTC <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
    *   `Unique name`: Each schedule must have a unique name <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. For example, `post schedule/post ID` can be used to ensure uniqueness for posts <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   Execute `scheduler.createScheduler` with the configured input to create the schedule <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.