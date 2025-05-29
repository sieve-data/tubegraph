---
title: Challenges and near collapse during COVID
videoId: IIPKMixTMfE
---

From: [[lennyspodcast]] <br/> 

During the COVID-19 pandemic, Notion faced one of its "bleakest" challenges, nearly leading to the company's collapse <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Infrastructure Scaling Crisis
For an extended period, Notion operated on a single instance of a PostgreSQL database, reflecting a philosophy of avoiding premature optimization <a class="yt-timestamp" data-t="00:49:42">[00:49:42]</a>. As the user base rapidly expanded during COVID, the company kept scaling up to larger and larger machines to accommodate the growth <a class="yt-timestamp" data-t="00:49:54">[00:49:54]</a>.

However, Notion eventually began "running out of even the largest instance" available for PostgreSQL <a class="yt-timestamp" data-t="00:49:59">[00:49:59]</a>. This created a "Doomsday Clock," indicating that the company would soon run out of space to store all user data, potentially leading to a complete shutdown of Notion <a class="yt-timestamp" data-t="00:50:07">[00:50:07]</a>.

> "There's a Doomsday Clock that when we're going to truly run out this space to store everything in Notion and Notion got completely shut down." <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a>

The situation was critical, with the company mere "weeks" away from hitting the limit <a class="yt-timestamp" data-t="00:50:24">[00:50:24]</a>. As the database approached its capacity, system behavior became sporadic and unpredictable <a class="yt-timestamp" data-t="00:50:30">[00:50:30]</a>.

## Resolution
To address this existential threat, Notion halted the development of all new features, with almost every engineer dedicating their efforts to solving the infrastructure problem <a class="yt-timestamp" data-t="00:50:14">[00:50:14]</a>. The solution involved "sharding" the database <a class="yt-timestamp" data-t="00:50:39">[00:50:39]</a>. This extensive effort took between three and six months to complete <a class="yt-timestamp" data-t="00:50:57">[00:50:57]</a>.

The experience served as a key learning moment: while premature optimization should be avoided, it's crucial to plan ahead for future scaling needs <a class="yt-timestamp" data-t="00:50:45">[00:50:45]</a>. The rapid growth during COVID was both "a blessing and a curse" for the company <a class="yt-timestamp" data-t="00:51:07">[00:51:07]</a>.