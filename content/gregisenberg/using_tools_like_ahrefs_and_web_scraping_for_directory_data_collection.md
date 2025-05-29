---
title: Using tools like Ahrefs and web scraping for directory data collection
videoId: 6rAHkSyzfNA
---

From: [[gregisenberg]] <br/> 

Building a profitable online directory requires strategic use of tools for idea generation, validation, and comprehensive data collection and enrichment. Frey, an online directory expert, outlines his process for creating directories capable of generating significant passive income <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Identifying Profitable Niches with Ahrefs

Frey emphasizes starting with niche identification using Ahrefs, a comprehensive SEO tool <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

### Keyword Research Strategy
His primary method involves searching for "near me" queries in Ahrefs' Keyword Explorer <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. This reveals a list of local queries with substantial search volume <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
Key metrics to look for include:
*   **High monthly search volume** <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>
*   **Low keyword difficulty** <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a> (Frey considers anything under 20 as "pretty easy," though notes it can be misleading <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>)
*   **Monthly searches in the 30,000 to 100,000 range** as a "sweet spot" <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.

### Niche Selection Criteria
Frey advises avoiding certain types of niches:
*   **Seasonal niches:** Such as "pumpkin patches near me," as monetization would only be effective for a short period <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
*   **Niches with difficult-to-obtain data:** For example, "earthquake near me," where reliable data sources are hard to secure <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
*   **Big branded keywords:** Like "Taco Bell near me," because established brands likely already have robust, updated directories <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. Branded searches also tend to be "one-dimensional" in user intent <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

Instead, look for niches with **fragmented or "multi-dimensional" search intent** <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. For example, "dog parks near me" branches into specific searches like "indoor dog park," "offleash dog park," or parks with specific amenities like water fountains or shade <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. This fragmentation indicates users aren't fully satisfied with existing search results and are looking for more curated information <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

## Competitive and Problem Validation
Before collecting data, it's crucial to validate the idea and assess the competition.
*   **Google Search:** Perform competitive research by searching keywords like "Dog Park Los Angeles" to identify existing directories <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. Evaluate if you can build something superior to what currently ranks <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>. Websites with basic information but high traffic (like `nyabone.com` for dog parks, getting 21,000 monthly visitors while only showing name and address) signal a strong opportunity for improvement <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
*   **Reddit (Social Listening):** Use Reddit to confirm if the chosen niche presents a problem worth solving <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>. Searching for terms like "Dog Park Los Angeles Reddit" reveals forums where people discuss challenges and specific needs related to finding information <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>. This can provide "social signals" confirming a demand for curated information and specific features <a class="yt-timestamp" data-t="00:25:42">[00:25:42]</a>.

## Data Collection through Web Scraping

Frey uses web scraping tools to gather the necessary data for directories <a class="yt-timestamp" data-t="00:27:41">[00:27:41]</a>.

### Choosing a Scraper
He specifically uses `outscraper` and its Google Map Scraper <a class="yt-timestamp" data-t="00:27:49">[00:27:49]</a>.

### Scraping Strategy
1.  **Identify Google Categories:** Before scraping, search on Google Maps for your niche (e.g., "Dog Park Los Angeles") to see if a dedicated Google Category exists (e.g., "dog park") <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>.
2.  **Exact Match vs. Plain Query:**
    *   If a category exists, use the "exact match" option in the scraper. This yields cleaner, more relevant data <a class="yt-timestamp" data-t="00:28:45">[00:28:45]</a>.
    *   If no category exists, use a "plain query" (e.g., "off leash dog parks"). This will result in much more data, including a lot of "junk," requiring more extensive cleaning <a class="yt-timestamp" data-t="00:28:58">[00:29:09]</a>.
3.  **Nationwide Scope:** Frey recommends scraping nationwide to leverage all available search volume <a class="yt-timestamp" data-t="00:32:24">[00:32:24]</a>.
4.  **Parameter Selection:** Select essential data points for scraping, such as name, phone number, address, postal code, state, reviews, street view, working hours, and especially the **location link/ID** (crucial for future data enrichment) <a class="yt-timestamp" data-t="00:32:38">[00:32:38]</a>.

### Data Cleaning and Parsing
When dealing with "junk data" from plain queries, several methods can be used:
*   **Manual Deletion:** Remove listings without addresses or those with very few reviews (e.g., less than 10 reviews) <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>.
*   **AI Tools:** [[Using AI in online directory creation and growth | Utilizing tools like ChatGPT]] or Claude can assist in parsing and cleaning data, though manual initial filtering of obvious irrelevant entries (like Walmart if scraping for dog parks) is recommended to prevent losing "good quality listings" <a class="yt-timestamp" data-t="00:30:28">[00:30:28]</a>.

## Data Enrichment for Enhanced Value

Data enrichment is key to making a directory more useful than existing solutions and capitalizing on fragmented search intent <a class="yt-timestamp" data-t="00:35:22">[00:35:22]</a>.

### Identifying Features
Analyze Google Maps reviews for the niche to identify common tags and desired features <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. For dog parks, this might include "shade," "parking," "water," "benches," and "dog bags" <a class="yt-timestamp" data-t="00:36:22">[00:36:22]</a>.

### Manual vs. Automated Enrichment
*   **Manual (initial method):** Manually create columns in a spreadsheet for each feature (e.g., "Water," "Shade") and populate them <a class="yt-timestamp" data-t="00:37:30">[00:37:30]</a>. This is tedious, especially for large datasets <a class="yt-timestamp" data-t="00:38:20">[00:38:20]</a>.
*   **Automated (Frey's current development):** Frey is building a tool that uses the Google location ID/URL to automatically read reviews and extract feature information (e.g., determining if a dog park has shade) <a class="yt-timestamp" data-t="00:38:32">[00:38:32]</a>. This significantly reduces manual effort <a class="yt-timestamp" data-t="00:39:32">[00:39:32]</a>.

Enriched data allows the directory to provide specific details that address user needs, making it more valuable than generic map services or basic existing directories <a class="yt-timestamp" data-t="00:41:46">[00:41:46]</a>. This detailed information is what drives users back to the website <a class="yt-timestamp" data-t="00:41:55">[00:41:55]</a>.

By mastering [[Utilizing tools like Ahrefs and Particle for market research | Ahrefs for market research]] and [[Utilizing Apify for Data Scraping | web scraping for data collection and enrichment]], creators can lay a strong foundation for a successful online directory. These initial steps — finding and validating an idea, and meticulously gathering and parsing data — are critical regardless of the project's scale <a class="yt-timestamp" data-t="00:53:37">[00:53:37]</a>.