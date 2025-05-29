---
title: Optimizing online directories with data enrichment and keyword clustering
videoId: 6rAHkSyzfNA
---

From: [[gregisenberg]] <br/> 
Frey, an "online directory King"<a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, shares his method for how to [[building_an_online_directory_using_wordpress_and_seo_techniques | build an online directory]] that can generate between $2,000 and $10,000 per month in passive income, requiring only about 15 minutes of work per week<a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. His approach emphasizes simplicity and [[seo_strategies_for_online_directories | SEO]] optimization rather than complex design or advanced [[building_an_online_directory_with_no_code_and_ai | AI tools]]<a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

Frey's first directory website, built in October 2022<a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>, has been [[monetizing_online_directories | monetized]] for 18 consecutive months<a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>, typically earning around $2,300 per month<a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. He focuses on evergreen, location-based directories that minimize the need for frequent data updates<a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

## Identifying and Validating Niche Ideas

A core part of [[finding_and_validating_niche_ideas_for_online_directories | starting an online directory]] involves identifying and [[validating_directory_ideas | validating]] a niche<a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. Frey's method focuses on finding niches that solve a problem<a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Keyword Research for Niche Validation
Frey uses Ahrefs' Keyword Explorer to find "near me" queries<a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>, looking for keywords with:
*   **High Monthly Search Volume**: His sweet spot is 30,000 to 100,000 monthly searches<a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
*   **Low Keyword Difficulty**: Ideally under 20, though 40-50 is possible with expertise<a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>. Keyword difficulty can be misleading due to competition and backlink dominance<a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.
*   **Fragmented/Multi-Dimensional Search Intent**: This means users are looking for different types or specific features within a category, allowing for deeper content and [[data_aggregation_and_summarization_for_niche_markets | data enrichment]]<a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. For example, "dog parks near me" breaks down into "indoor dog park," "off-leash dog park," or those with water fountains, benches, or shade<a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

### Niche Categories to Avoid
*   **Seasonal Niches**: Like "pumpkin patches near me," as monetization would only be good for a month<a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
*   **Difficult-to-Obtain Data Niches**: For example, "earthquake near me" would be hard to gather and maintain data for<a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
*   **Big Branded Keywords**: Such as "Taco Bell near me," because large brands likely already have updated directories, and the search intent is often one-dimensional<a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

### Competitive Research and Social Listening
Frey advises using Google to search for chosen keywords (e.g., "Dog Park Los Angeles") and analyzing existing directories<a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. The goal is to identify if he can build something better or more useful than what already exists<a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>. Even basic, unhelpful directories receiving significant traffic (like an example getting 21,000 monthly visitors while only listing names and addresses)<a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a> indicate an opportunity to improve user experience and capture traffic<a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.

Social listening, particularly on platforms like Reddit, helps to confirm that a problem is worth solving<a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>. Forums discussing challenges in finding specific types of dog parks (e.g., those with shade or benches)<a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a> provide strong social signals that users desire more curated and specific information<a class="yt-timestamp" data-t="00:25:44">[00:25:44]</a>.

## Data Acquisition and Enrichment

After validating the niche, the next step is to [[data_aggregation_and_summarization_for_niche_markets | get and enrich the data]].

### Data Acquisition
Frey uses web scraping tools, specifically OutScraper's Google Map Scraper<a class="yt-timestamp" data-t="00:27:45">[00:27:45]</a>. Before scraping, he checks Google Maps for dedicated categories for the niche (e.g., "dog park") which makes scraping much easier and cleaner<a class="yt-timestamp" data-t="00:28:14">[00:28:14]</a>. If no exact category exists, a plain query can be used, though it will yield more junk data requiring extensive cleaning<a class="yt-timestamp" data-t="00:28:52">[00:28:52]</a>.

For a nationwide directory, he keeps the default settings to capture all relevant locations<a class="yt-timestamp" data-t="00:32:24">[00:32:24]</a>. Key parameters for scraping include name, phone number, address, reviews, street view, operating hours, and crucially, the location link for future [[data_aggregation_and_summarization_for_niche_markets | data enrichment]]<a class="yt-timestamp" data-t="00:32:38">[00:32:38]</a>.

### Data Cleaning (Initial)
While exact match categories on Google Maps reduce junk, if a plain query is used, manual cleaning is often necessary<a class="yt-timestamp" data-t="00:29:27">[00:29:27]</a>. Simple methods include deleting listings without addresses or those with very few reviews (e.g., less than 10)<a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>. Although AI tools like Chat GPT or Claude can assist, Frey prefers an initial manual pass to avoid losing good quality listings<a class="yt-timestamp" data-t="00:30:43">[00:30:43]</a>.

### Data Enrichment
This is a critical step to make the directory more useful than competitors<a class="yt-timestamp" data-t="00:35:22">[00:35:22]</a>. Frey manually analyzes Google Maps reviews for common tags and features (e.g., "shade," "parking," "water," "dog bags," "benches")<a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. He then adds these as specific columns to the data sheet<a class="yt-timestamp" data-t="00:37:30">[00:37:30]</a>.

For large datasets, manual enrichment is tedious<a class="yt-timestamp" data-t="00:38:20">[00:38:20]</a>. Frey is developing a tool that automates this process by reading the Google URL for each location and extracting specific keywords from reviews to populate these feature columns<a class="yt-timestamp" data-t="00:38:32">[00:38:32]</a>. This automated [[data_aggregation_and_summarization_for_niche_markets | data enrichment]] ensures the directory offers detailed, specific information that sets it apart<a class="yt-timestamp" data-t="00:41:48">[00:41:48]</a>.

## Building and Monetizing the Directory

### Implementation on a CMS
Frey demonstrates using a basic [[building_an_online_directory_using_wordpress_and_seo_techniques | WordPress website]] for implementation, although any Content Management System (CMS) like Framer could be used<a class="yt-timestamp" data-t="00:42:16">[00:42:16]</a>.

### Static Pillar Page Directory Format
This "level one" directory build is simple but highly effective for SEO<a class="yt-timestamp" data-t="00:43:41">[00:43:41]</a>. It involves creating a single, very long, comprehensive page (a "pillar page") that targets numerous city-specific keywords<a class="yt-timestamp" data-t="00:43:48">[00:43:48]</a>.

Key elements of this format:
*   **Header One (H1)**: Uses the main keyword (e.g., "Dog Park Los Angeles")<a class="yt-timestamp" data-t="00:44:27">[00:44:27]</a>.
*   **Table of Contents**: Improves user navigation<a class="yt-timestamp" data-t="00:44:33">[00:44:33]</a>.
*   **City-Specific Sections**: Each section targets a specific city or region within the niche, listing individual entries with their enriched data (features, address, phone, hours, embedded map, optional reviews)<a class="yt-timestamp" data-t="00:44:35">[00:44:35]</a>.
*   **Internal Linking Strategy**: Simple links to different states or regions at the bottom of the page encourage users to explore more content<a class="yt-timestamp" data-t="00:46:56">[00:46:56]</a>.

### SEO Benefits of Pillar Pages
This format leverages "keyword clusters," allowing a single page to rank for hundreds or even thousands of related keywords (e.g., a state page ranking for 1,300 keywords)<a class="yt-timestamp" data-t="00:47:16">[00:47:16]</a>. The most-searched pages for successful directories are often location-based pages, not individual listings<a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>. By consolidating this high-volume, location-specific content on one page, the directory maximizes its SEO potential<a class="yt-timestamp" data-t="00:46:16">[00:46:16]</a>.

### Monetization Potential
Static pillar page directories are ideal for [[monetizing_online_directories_with_display_ads_and_affiliate_programs | display ad monetization]] like AdSense due to their long page length, allowing for many ad placements<a class="yt-timestamp" data-t="00:46:27">[00:46:27]</a>. This provides a consistent, passive income stream<a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.

Beyond ads, directories can serve as a foundation for larger ventures:
*   **Software/SaaS**: Directories can generate traffic and eyeballs in a specific niche, which can then be funneled into a related software-as-a-service (SaaS) product (e.g., a directory of farms and CSAs selling a software for farm management)<a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
*   **Affiliate Programs**: Especially in niches like pets, affiliate programs (e.g., BarkBox)<a class="yt-timestamp" data-t="00:51:51">[00:51:51]</a> can provide additional revenue.
*   **Lead Generation/Data Collection**: Collecting data via newsletters or lead magnets (e.g., dog DNA kits, as with BarkBox's acquisition)<a class="yt-timestamp" data-t="00:51:36">[00:51:36]</a> can be highly valuable.

The simplicity of this approach makes it accessible for beginners to achieve significant passive income, potentially leading to larger entrepreneurial endeavors<a class="yt-timestamp" data-t="00:48:40">[00:48:40]</a>. Despite their "boring" appearance, directories are an underrated and effective business model<a class="yt-timestamp" data-t="00:49:37">[00:49:37]</a>.