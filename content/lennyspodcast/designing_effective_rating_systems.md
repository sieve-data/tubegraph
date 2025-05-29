---
title: Designing Effective Rating Systems
videoId: BVzTfsUMaK8
---

From: [[lennyspodcast]] <br/> 

Rating systems are crucial for online marketplaces, as they enable the platform to gather information about matches made and feed that data back into the system to improve future interactions. They are part of the core [[integrating_customer_feedback_loops_in_product_development | feedback loops]] that help marketplaces function effectively <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

## Role of Rating Systems in Marketplaces

Marketplaces sell the "taking away of friction" in transactions, such as finding a place to stay or a driver <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. Data science is central to building successful marketplaces by helping with three key problems <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>:
1.  **Finding matches**: Connecting buyers and sellers <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
2.  **Making matches**: Assisting users in selecting the best partner from available options <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
3.  **Learning about matches**: Collecting and using data from completed transactions to improve future interactions <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

Rating systems fall under "learning about matches" <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. This includes both active data collection (e.g., five-star ratings) <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a> and passive data collection (e.g., whether a booking was left early) <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. This feedback loop allows marketplaces to better find and make potential matches in the future <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

## Challenges in Designing Rating Systems

Despite innovation, platforms are still largely using the same fundamental tools for rating systems as pioneers like eBay and Amazon did decades ago <a class="yt-timestamp" data-t="01:02:36">[01:02:36]</a>. No one has "really nailed" rating system design <a class="yt-timestamp" data-t="01:02:31">[01:02:31]</a>.

Key challenges include:

### Rating Inflation
A common phenomenon is "rating inflation," where the median rating on marketplaces tends to increase over time <a class="yt-timestamp" data-t="01:02:50">[01:02:50]</a>. Reasons for this include:
*   **Reciprocity**: Users may feel compelled to leave positive ratings, especially if there's direct interaction <a class="yt-timestamp" data-t="01:03:20">[01:03:20]</a>.
*   **Norming**: As ratings increase, a four-star rating might be perceived as "screwing this person over," even if it was considered good initially <a class="yt-timestamp" data-t="01:03:36">[01:03:36]</a>.

### Averaging Ratings
A common default is to simply average ratings, but this can have significant "distributional consequences" on who benefits or loses in the marketplace <a class="yt-timestamp" data-t="01:04:41">[01:04:41]</a>.
*   **Established vs. New Participants**: For established participants with many reviews (e.g., a restaurant with 10,000 Yelp reviews), a new review has little impact <a class="yt-timestamp" data-t="01:05:05">[01:05:05]</a>. However, for new participants, a single negative first review can be devastating, potentially leading to an 8% hit on immediate expected revenue or even exit from the platform <a class="yt-timestamp" data-t="01:05:16">[01:05:16]</a>.

### The Sound of Silence
There is significant information in ratings that are *not* left <a class="yt-timestamp" data-t="01:07:45">[01:07:45]</a>. Users are often more inclined to simply not leave a review than to leave a bad one <a class="yt-timestamp" data-t="01:08:23">[01:08:23]</a>. This "lack of a response" can be highly predictive of a seller's downstream performance <a class="yt-timestamp" data-t="01:08:18">[01:08:18]</a>.

## Advice for Designing Rating Systems

### 1. Renorming Meaning of Labels
Consider approaches that "renorm" the meaning of rating labels <a class="yt-timestamp" data-t="01:03:51">[01:03:51]</a>.
*   Instead of just "poor to excellent," define the top rating as "exceeded expectations" <a class="yt-timestamp" data-t="01:04:02">[01:04:02]</a>.
*   Ask users to compare their experience to past highly-rated experiences or to their expectations <a class="yt-timestamp" data-t="01:04:06">[01:04:06]</a>. It's easier for people to say "that was good but didn't exceed my expectations" than to "ding this person and give them four stars" <a class="yt-timestamp" data-t="01:04:23">[01:04:23]</a>.

### 2. Addressing Distributional Fairness
Be mindful of the distributional consequences of averaging ratings, particularly for new participants <a class="yt-timestamp" data-t="01:05:50">[01:05:50]</a>.
*   **Implement a "prior belief"**: Instead of just averaging a new participant's ratings, average them with a prior belief about typical performance <a class="yt-timestamp" data-t="01:06:01">[01:06:01]</a>. This can help pull up the rating of a new participant who might have gotten unlucky with an early negative review, giving them a better chance to succeed <a class="yt-timestamp" data-t="01:06:13">[01:06:13]</a>.
*   **Delay showing ratings**: Some platforms don't show ratings until a participant has accumulated a few, to mitigate the impact of early negative reviews <a class="yt-timestamp" data-t="01:05:42">[01:05:42]</a>.

### 3. Double-Blind Reviews
A system where neither party sees the other's review until both have submitted theirs can encourage more honesty and accuracy, and can also significantly increase the review rate, providing more data <a class="yt-timestamp" data-t="01:07:20">[01:07:20]</a>.

### 4. Importance of Learning
Rating systems are crucial for understanding what happened with matches <a class="yt-timestamp" data-t="01:06:47">[01:06:47]</a>. They provide insights into who wins and who loses within the market and have social implications <a class="yt-timestamp" data-t="01:07:04">[01:07:04]</a>. The collected data is invaluable for data scientists to understand and improve marketplace dynamics <a class="yt-timestamp" data-t="01:06:54">[01:06:54]</a>.