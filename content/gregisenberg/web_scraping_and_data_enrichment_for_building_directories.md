---
title: Web scraping and data enrichment for building directories
videoId: 6rAHkSyzfNA
---

From: [[gregisenberg]] <br/> 
Frey, an "online directory King", teaches how to [[building_a_cash_flowing_online_directory | build an online directory]] that can generate between $2,000 and $10,000 a month in passive income, requiring only about 15 minutes of work per week <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. His first directory, built in October 2022, has been monetized for 18 months, is Evergreen and location-based, and generated around $2,300 in revenue in a recent month <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. While AI tools can be recommended for certain parts, they are not strictly necessary to get started <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

The process of [[starting_an_online_directory | starting an online directory]] includes [[finding_and_validating_niche_ideas_for_directories | finding and validating a niche]], optimizing it for [[using_seo_and_keyword_research_for_directory_success | SEO]], gathering and cleaning data, enriching it, and then implementing it on a content management system (CMS) like WordPress <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

## Getting Data for Directories

The primary method for acquiring data for directories is web scraping <a class="yt-timestamp" data-t="00:27:41">[00:27:41]</a>.

### Web Scraping Tools
Frey uses OutsScraper, specifically its Google Map scraper <a class="yt-timestamp" data-t="00:27:47">[00:27:47]</a>. Before scraping, it's recommended to go to Google Maps and identify actual Google categories for the niche, as this makes scraping much easier <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>. For example, for "dog parks near me," a dedicated "dog park" category exists <a class="yt-timestamp" data-t="00:28:19">[00:28:19]</a>.

If a specific Google category doesn't exist, a general query can be used, but this will result in significantly more data, much of which will be "junk" <a class="yt-timestamp" data-t="00:29:04">[00:29:04]</a>. Frey prefers [[creating_online_directories_using_apis | creating Nationwide directories]] to take advantage of all search volume <a class="yt-timestamp" data-t="00:32:24">[00:32:24]</a>.

### Cleaning Junk Data
When a plain query results in a large amount of irrelevant data (e.g., businesses with "dog" mentioned in reviews but not actual dog parks), several strategies can be employed for cleaning:
*   Delete listings without addresses <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>.
*   Remove entries with no reviews or only one review <a class="yt-timestamp" data-t="00:30:18">[00:30:18]</a>.
*   While [[using_ai_for_data_enrichment_and_lead_generation | AI tools]] like ChatGPT or Claude can help parse data, a solid prompt is essential <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>. Frey suggests manually removing large irrelevant entries first to prevent AI from discarding valuable listings <a class="yt-timestamp" data-t="00:31:14">[00:31:14]</a>.

### Key Parameters to Scrape
When configuring the scraper, essential parameters to include are:
*   Name <a class="yt-timestamp" data-t="00:32:45">[00:32:45]</a>
*   Phone number (especially for indoor parks) <a class="yt-timestamp" data-t="00:32:47">[00:32:47]</a>
*   Address (Street, Postal Code, State) <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>
*   Reviews <a class="yt-timestamp" data-t="00:32:53">[00:32:53]</a>
*   Street view <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>
*   Working hours <a class="yt-timestamp" data-t="00:33:02">[00:33:02]</a>
*   Location link (crucial for later data enrichment) <a class="yt-timestamp" data-t="00:33:06">[00:33:06]</a>

## Data Enrichment

Data enrichment is a critical step to make a directory more useful and comprehensive than existing competitors <a class="yt-timestamp" data-t="00:35:22">[00:35:22]</a>.

### Identifying Desired Features
To enrich data, Frey analyzes Google Map reviews for recurring tags and features that users mention. For dog parks, common desired features include:
*   Water fountains for dogs <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a>
*   Shade <a class="yt-timestamp" data-t="00:36:55">[00:36:55]</a>
*   Benches <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>
*   Dog bags <a class="yt-timestamp" data-t="00:37:02">[00:37:02]</a>
*   Trash cans <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>
*   Specific types like "indoor dog park" or "off-leash dog park" <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>

These features align with the "fragmented search intent" found during [[keyword_research_for_directories | keyword research]], where users are looking for specific types of amenities <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.

### Manual vs. Automated Enrichment
Manually enriching data for thousands of listings is "God awful" and "extremely tedious" <a class="yt-timestamp" data-t="00:38:20">[00:38:20]</a>. Frey's first directory only had about 130 listings, making manual enrichment feasible <a class="yt-timestamp" data-t="00:39:41">[00:39:41]</a>.

For larger datasets, [[using_ai_for_data_enrichment_and_lead_generation | AI automation]] is key <a class="yt-timestamp" data-t="00:39:49">[00:39:49]</a>. Frey is developing a tool that uses the location ID/Google URL to automate data enrichment by reading reviews and extracting information on specific features (e.g., "does this dog park have shade?") <a class="yt-timestamp" data-t="00:38:32">[00:38:32]</a>. This saves immense time compared to manual entry <a class="yt-timestamp" data-t="00:39:35">[00:39:35]</a>.

### Benefits of Detailed Enrichment
Detailed data enrichment is what differentiates a new directory from dominant competitors, making it more useful and encouraging repeat visits <a class="yt-timestamp" data-t="00:41:21">[00:41:21]</a>. For example, providing information on whether a dog park has dog bags or water fountains solves a real problem for users who otherwise would need to search reviews or call the park <a class="yt-timestamp" data-t="00:41:33">[00:41:33]</a>.

## Implementation on a CMS

After data is cleaned and enriched, it can be formatted onto a CMS like WordPress <a class="yt-timestamp" data-t="00:42:11">[00:42:11]</a>. While WordPress might seem "dumb" or basic for modern builds, it's effective <a class="yt-timestamp" data-t="00:42:38">[00:42:38]</a>. Other CMS options like Framer or Bolt.new are also viable <a class="yt-timestamp" data-t="00:42:24">[00:42:24]</a>.

This detailed data, especially with comprehensive features, forms the backbone of a static pillar page directory, which is highly effective for [[using_seo_and_keyword_research_for_directory_success | SEO]] by targeting high-volume location-based keywords <a class="yt-timestamp" data-t="00:43:41">[00:43:41]</a>.

The initial steps of [[finding_and_validating_niche_ideas_for_directories | finding an idea]], validating it, and gathering/parsing data are consistent regardless of whether one aims to [[building_a_cash_flowing_online_directory | build a large or small directory]] <a class="yt-timestamp" data-t="00:53:37">[00:53:37]</a>.