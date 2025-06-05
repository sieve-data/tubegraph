---
title: Dealing with accidental data loss and database issues
videoId: OoQLoKHhohg
---

From: [[fireship]] <br/> 

Software engineers may encounter various challenges, including accidental data loss and database-related problems <a class="yt-timestamp" data-t="00:33:43">[00:33:43]</a>.

## Cloud Billing Alerts

When working with cloud services like [[aws_storage_and_databases | AWS]], one of the worst messages a software engineer can receive is a cloud billing alert indicating a budget has been exceeded, potentially by millions of dollars <a class="yt-timestamp" data-t="01:50:49">[01:50:49]</a>. This can happen due to clicking the wrong button or accidentally creating an infinite loop <a class="yt-timestamp" data-t="01:59:04">[01:59:04]</a>. A simple solution suggested is to stop using [[aws_storage_and_databases | AWS]] and pretend nothing happened, or claim the account was hacked <a class="yt-timestamp" data-t="02:03:77">[02:03:77]</a>. Many individuals have faced similar issues by forgetting to turn off an EC2 instance <a class="yt-timestamp" data-t="02:16:34">[02:16:34]</a>.

## Accidentally Dropping Production Databases

A dreaded and [[lessons_learned_from_catastrophic_software_failures | catastrophic]] event for a developer is learning that a production database, along with all of the company's data worth [[consequences_of_software_glitches_in_financial_systems | billions of dollars]], has been accidentally dropped <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. This often occurs due to the simple mistake of dropping the production (prod) database instead of the development (dev) database <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.

### Mitigation and Consequences

When such an event occurs, it is terrifying <a class="yt-timestamp" data-t="02:31:681">[02:31:681]</a>. However, having backups that can restore the database to its original state is crucial <a class="yt-timestamp" data-t="02:32:46">[02:32:46]</a>. If backups are not available, it may be time to seek new employment <a class="yt-timestamp" data-t="02:36:44">[02:36:44]</a>.

### Ease of Accidental Deletion and SQL Injection

Dropping a database is remarkably easy and can be achieved with a single line of code <a class="yt-timestamp" data-t="02:41:40">[02:41:40]</a>. This knowledge can also be used, for instance, by weaponizing SQL injection against systems like speed cameras <a class="yt-timestamp" data-t="02:44:811">[02:44:811]</a>.