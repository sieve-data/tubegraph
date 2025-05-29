---
title: Notions early years and challenges
videoId: IIPKMixTMfE
---

From: [[lennyspodcast]] <br/> 

Notion, co-founded by Ivan Zhao, describes its initial three to four years, starting in 2013 <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>, as the "Lost Years" <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This period was marked by significant [[overcoming_and_learning_from_failures | challenges]] as the company sought to define its product and achieve market fit <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

## The Shifting Product Vision: From Developer Tool to Productivity Suite

Initially, Notion pursued a vision where "everybody can make and create their software" <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This led to building a developer tool intended to be so easy that more people could create software <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
<a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>:
> "the first version to take okay everybody can make and create their software so let's just build a developer tool that's so easy that more people can do that."

After a couple of years, the team realized that "most people just don't care" about creating software; they simply want to get their jobs done <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This led to a crucial realization:
<a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>:
> "actually let's hide our vision which is everybody can create their software in the form factor that people do care so what kind of tool do people use every day productiv software."

It took Notion two years to pivot to building a productivity tool <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Ivan Zhao uses an analogy to describe this strategic shift:
<a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>:
> "We call the sugar called the broccoli. People don't want to eat the broccoli, but people like sugar, so give them the sugar that hides your broccoli inside of it."

This meant creating a product that appeared as a familiar productivity suite but secretly contained the no-code developer power that was Notion's original intent <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. The first version of Notion was more about what Ivan wanted than what people wanted <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.

### Balancing Vision and User Needs

Building a product or business requires a balance between serving user needs (getting users and revenue) and building for values (what you want the world to have) <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>.
<a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>:
> "too much of yourself then there's no users, you're just doing art project... and too much for a business you're building a commodity."

Finding this "sweet spot" is crucial for creating something durable and with a right to exist <a class="yt-timestamp" data-t="00:41:02">[00:41:02]</a>.

## Technical and Financial Setbacks

During the "Lost Years," Notion faced severe technical hurdles. After spending two years building the developer tool, the team realized they were building on the wrong technical foundation <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. They had bet on Web Components, a competing technology to React, which proved unstable <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>. This necessitated rebuilding the entire codebase to avoid running out of time and money <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
<a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>:
> "so that's instead reset a c-base reset a company so we can build on our worther do techn technology Foundation."

### Staying Solvent

To survive these long, unproductive years, Notion had to be extremely lean <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>. Ivan's mother helped kickstart the company and later loaned them money to bridge financial gaps <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. At one point, the five-person team was laid off, leaving only Ivan and his co-founder Simon to rebuild <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. They even moved to Japan and traveled the world, making money by subleasing their San Francisco apartment and office, allowing them to continue coding daily <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.

## Finding Product-Market Fit: A Gradual Realization

Notion's product-market fit wasn't a sudden "boom" but a gradual realization <a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a>. Ivan describes it as:
<a class="yt-timestamp" data-t="00:25:28">[00:25:28]</a>:
> "It just kind of like oh good we have people who care about this thing we make now oh good people are um reach out to us or paying us."

A humorous "sign of product-market fit" was when a venture capitalist firm sent dog food to their non-public office address as a gift, signaling significant interest <a class="yt-timestamp" data-t="00:26:33">[00:26:33]</a>.

## Crisis during COVID-19: Scaling Infrastructure

A significant crisis occurred during the COVID-19 pandemic when Notion's infrastructure struggled to scale <a class="yt-timestamp" data-t="00:49:32">[00:49:32]</a>. For a long time, Notion ran on a single PostgreSQL database instance, continuously upgrading to larger machines <a class="yt-timestamp" data-t="00:49:42">[00:49:42]</a>. However, they were running out of space on even the largest available instances, facing a "Doomsday Clock" before the database would be completely full <a class="yt-timestamp" data-t="00:49:57">[00:49:57]</a>. This would have shut Notion down completely <a class="yt-timestamp" data-t="00:50:07">[00:50:07]</a>.
<a class="yt-timestamp" data-t="00:50:10">[00:50:10]</a>:
> "We stop building any new features. All hands on deck. Almost every engineer in the company trying to solve that problem."

The solution was to implement database sharding, a complex process to distribute data across multiple databases <a class="yt-timestamp" data-t="00:50:39">[00:50:39]</a>. This was a "close call," with only weeks to spare before the system would fail <a class="yt-timestamp" data-t="00:50:19">[00:50:19]</a>.

## Challenges of Building a Horizontal Product

Building a horizontal product like Notion, which aims to be a "Lego for software" <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>, presents unique [[challenges_and_strategies_for_creating_successful_startups | challenges]] and joys <a class="yt-timestamp" data-t="00:51:45">[00:51:45]</a>.
<a class="yt-timestamp" data-t="00:52:04">[00:52:04]</a>:
> "Lego for software doesn't exist. And Lego is a horizontal thing, so that's the thing we want to build. We always want to do that so we did not start to optimize for business, but we're optimized for that vision."

### Lego Bricks vs. Lego Boxes

A key learning was the importance of segmentation <a class="yt-timestamp" data-t="00:52:20">[00:52:20]</a>. While hardcore Notion users enjoy the "Lego bricks" (individual, flexible components), most people, especially enterprise customers, prefer "Lego boxes"—ready-made solutions tailored to their specific needs <a class="yt-timestamp" data-t="00:52:31">[00:52:31]</a>.
<a class="yt-timestamp" data-t="00:52:43">[00:52:43]</a>:
> "there's this term took me a while to learn it's called Solutions. You need to be a solution for Enterprise customer."

Initially, Notion was too focused on the "Lego brick" mindset <a class="yt-timestamp" data-t="00:53:08">[00:53:08]</a>. While vertical software naturally comes bundled, horizontal products need to create their own "walls" and clear positioning in customers' minds <a class="yt-timestamp" data-t="00:53:30">[00:53:30]</a>. However, it's crucial to continue building the underlying "bricks" <a class="yt-timestamp" data-t="00:54:14">[00:54:14]</a>.

Notion, for example, is used for project management, docs, and CRM, despite not being designed explicitly for those purposes <a class="yt-timestamp" data-t="00:54:41">[00:54:41]</a>. This is because it provides the relational database "bricks" that allow users to build these solutions themselves <a class="yt-timestamp" data-t="00:55:06">[00:55:06]</a>.

### Finding the First Use Case

For horizontal tools, finding an initial use case that resonates broadly is key <a class="yt-timestamp" data-t="00:56:18">[00:56:18]</a>. Notion stumbled upon "document notes" as a widely used, simple entry point <a class="yt-timestamp" data-t="00:56:49">[00:56:49]</a>. This "B2C2B" strategy meant consumers used Notion for personal note-taking, realized its deeper capabilities (relational database, task management), and then brought it into their workplaces <a class="yt-timestamp" data-t="00:57:03">[00:57:03]</a>. This provided a large top-of-funnel for Notion's growth into more verticalized enterprise use cases <a class="yt-timestamp" data-t="00:57:38">[00:57:38]</a>.

### The Impact of AI

The rise of large language models (LLMs) has been a "gift" for Notion <a class="yt-timestamp" data-t="00:58:19">[00:58:19]</a>. Since AI thrives on data, and Notion consolidates various information types, it has a significant advantage <a class="yt-timestamp" data-t="00:58:57">[00:58:57]</a>. Notion's AI writer product and AI Q&A/connectors leverage this <a class="yt-timestamp" data-t="00:59:07">[00:59:07]</a>.

Even more fascinating, AI is proving to be excellent at "piecing things together" <a class="yt-timestamp" data-t="00:59:54">[00:59:54]</a>. This addresses one of the biggest weaknesses of the "Lego" approach: not everyone can build a Lego set from scratch <a class="yt-timestamp" data-t="00:59:42">[00:59:42]</a>. An AI coding agent on top of Notion's Lego blocks can create custom knowledge software or customer agents for various vertical use cases <a class="yt-timestamp" data-t="01:00:08">[01:00:08]</a>.

## Key Lessons for Founders

*   **Don't be afraid to reset:** Courage is essential, even if it means abandoning momentum or sunk costs <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>. Progress can be achieved through better abstractions that compound faster <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>.
*   **Balance personal vision with market needs:** While it's important to build something you believe in and want to exist, it must also resonate with users <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>, <a class="yt-timestamp" data-t="00:38:45">[00:38:45]</a>.
*   **Embrace [[The significance of beginners mind in entrepreneurship | lean operations]]:** Notion remained profitable by keeping the team small and efficient, leveraging the mindset of building better systems and tools internally <a class="yt-timestamp" data-t="00:31:08">[00:31:08]</a>. The "small bus" metaphor emphasizes that a smaller, more talented team is easier to maneuver and accelerate <a class="yt-timestamp" data-t="00:33:40">[00:33:40]</a>. This lean approach was ingrained through the tough "Lost Years" <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>.
*   **Understand market cycles:** Markets operate in cycles of "bundling" and "unbundling" <a class="yt-timestamp" data-t="01:00:46">[01:00:46]</a>. Recognizing whether the current trend favors vertical or horizontal solutions helps determine the right product approach <a class="yt-timestamp" data-t="01:02:20">[01:02:20]</a>, <a class="yt-timestamp" data-t="01:02:35">[01:02:35]</a>. Currently, with AI and macro trends, the market is shifting towards more bundling <a class="yt-timestamp" data-t="01:02:20">[01:02:20]</a>.
*   **Steal from outside tech:** Look beyond tech and business to history, literature, and other industries for patterns, shapes, and tradeoffs <a class="yt-timestamp" data-t="01:06:29">[01:06:29]</a>. This can provide fresh perspectives and lead to more interesting solutions <a class="yt-timestamp" data-t="01:07:04">[01:07:04]</a>.
*   **Prioritize craft and values:** Building a product should feel like a craft, applying values to technical know-how to make clever tradeoffs and create something new and useful <a class="yt-timestamp" data-t="00:37:38">[00:37:38]</a>. Building according to one's values creates a more durable and fulfilling energy source <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.
*   **Listen to customer feedback:** Product launches, even if not immediately successful, can provide crucial feedback to realign with core values and vision <a class="yt-timestamp" data-t="00:48:01">[00:48:01]</a>.
*   **Prioritize rest:** When feeling overwhelmed, simply getting sleep can provide a daily personal and physical reset <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.