---
title: Policy and IAM roles for scheduler
videoId: wOdpDEkw_us
---

From: [[swarajmakesstuff]] <br/> 

To enable a scheduler to invoke a [[Lambda function with event schedulers | Lambda function]], specific policies and IAM (Identity and Access Management) roles are required to grant the necessary permissions <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. This setup ensures secure and authorized execution of the [[Lambda function with event schedulers | Lambda function]] by the scheduler <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.

## Core Components

The process involves establishing a chain of trust and permission:
1.  **Lambda Function**: The target of the invocation <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.
2.  **Policy**: Defines the specific permissions, primarily to invoke the Lambda function <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>.
3.  **IAM Role**: An entity that assumes permissions via an attached policy. This role is then assigned to the scheduler <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.

## Steps for Configuration

### 1. Create the Lambda Function

First, define your [[Lambda function with event schedulers | Lambda function]]. This function will be the target of the scheduler <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.
For the example, the Lambda function's code is located in a directory named `Lambda` and the handler is `invokeScheduler.Handler` <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>. It's crucial to build the code into a JS file before deploying for proper execution <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.

### 2. Define the Policy

A policy must be created that explicitly grants permission to invoke the specific Lambda function <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>. This policy directly assigns the ARN (Amazon Resource Name) of the Lambda function as the resource it has permission to invoke <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>.

### 3. Create and Assign the IAM Role

Create an IAM role that will be assumed by the scheduler <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>. This role should have a trust policy allowing `scheduler.amazonaws.com` to assume it <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.
Once the role is created, attach the previously defined policy to this IAM role <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>. This grants the role, and by extension the scheduler, the permission to invoke the Lambda function <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>.

### 4. Configure the Scheduler with ARNs

When creating the [[AWS EventBridge schedulers | EventBridge scheduler]], you will need two key ARNs:
*   The **ARN of your Lambda function** (`targetArn`) <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>, <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.
*   The **ARN of your IAM role** (`roleArn`) <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>, <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>.

> [!TIP] Obtaining ARNs
> During deployment (e.g., using CDK), you can log these ARN values using `cd.CNF out` to easily retrieve them <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>. These ARNs are then used when creating the scheduler via the SDK based on user input <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

The scheduler configuration will also specify:
*   The unique name for the schedule <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>, <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>.
*   The URL that the Lambda function will hit <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>.
*   The input payload for the Lambda function <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>.
*   The action to take upon completion, such as `DELETE`, which is recommended for [[Dynamic onetime event schedulers | one-time schedulers]] to manage the limit of 1 million schedulers per instance <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>, <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
*   The scheduler expression and time zone (e.g., UTC) <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>.

## Implementation Notes

The initial setup of the Lambda function, policy, and IAM role can be done as a one-time deployment using tools like CDK (Cloud Development Kit) <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>. After this initial deployment, the creation of individual schedulers based on user input is handled programmatically using the AWS SDK <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.