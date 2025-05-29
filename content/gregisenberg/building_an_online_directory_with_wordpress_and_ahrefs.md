---
title: Building an online directory with WordPress and Ahrefs
videoId: 6rAHkSyzfNA
---

From: [[gregisenberg]] <br/> 

Frey, an online directory expert, teaches how to build an online directory that can generate anywhere between $2,000 to $10,000 a month in passive income with minimal weekly maintenance [00:00:08]. This article focuses on a simplified, static directory model, which Frey considers a great starting point for aspiring creators [00:02:19].

## Frey's Approach to Online Directories
Frey's first directory website, built in October 2022, has been monetized for 18 months, requires about 15 minutes a month to maintain, and generated approximately $2,300 in revenue in a recent month [00:01:59]. He specializes in evergreen, location-based directories because they require less frequent data updates [00:12:24].

## Finding and Validating Niche Ideas
The process begins with finding and validating a niche idea, which ensures the directory solves a genuine problem [00:02:45].

### Using [[using_ai_and_seo_for_online_directories | Ahrefs]] for Idea Generation
Frey uses [[using_ai_and_seo_for_online_directories | Ahrefs]] to find niche ideas:
*   **Keyword Explorer:** Type "near me" into the Keyword Explorer to find a list of local queries with high search volume [00:12:43].
*   **Targeting Keywords:** Look for keywords with high monthly search volume and relatively low keyword difficulty [00:13:08]. Frey's sweet spot is typically 30,000 to 100,000 monthly searches [00:13:20].
*   **Ideal Keyword Difficulty:** Anything under 20 is generally considered easy to rank for [00:16:48]. However, keyword difficulty can be misleading due to competition or dominant backlinks [00:16:55]. For experienced builders, 40-50 can also be possible [00:17:44]. Programmatic directories have even ranked for keywords with difficulty 70 [00:17:53].

### What to Avoid
Frey recommends avoiding certain types of niches [00:13:34]:
*   **Seasonal Niches:** Websites like "pumpkin patches near me" are highly seasonal, making monetization inconsistent [00:13:40].
*   **Difficult-to-Get Data:** Niches where data is hard to acquire or constantly changing, such as "earthquake near me" [00:14:02].
*   **Branded Keywords:** Queries like "Taco Bell near me" are often too one-dimensional. Big brands likely already have established directories, and user search intent is often very specific, offering less opportunity for rich content [00:14:21].

### Example: Dog Parks Near Me
A good example of a multi-dimensional niche is "dog parks near me," which gets 73,000 monthly searches and has a keyword difficulty of 27/100 [00:15:22]. This niche exhibits "fragmentation in search intent," meaning users are looking for specific types of dog parks (e.g., indoor, off-leash, with water fountains, shade, or benches) [00:15:40]. This provides opportunities to enrich the directory with detailed features [00:16:00].

### Competitive Research and Social Listening
After identifying a potential niche, it's crucial to perform competitive research and social listening to confirm the problem is worth solving [00:26:00].
1.  **Google Search:** Search for "[Niche] [City]" (e.g., "Dog Park Los Angeles") to identify existing directories on the first page [00:18:27]. Analyze competitors to determine if you can build something better [00:19:04].
    *   **Identifying Weak Competitors:** An example, "Nyabone," showed a basic directory with only names and addresses, yet it received 21,000 monthly visitors [00:19:50]. This indicates a clear opportunity to improve the offering by adding more useful information [00:20:16].
2.  **Reddit for Social Validation:** Search Reddit for "[Niche] [City]" (e.g., "Dog Park Los Angeles Reddit") to find forums where people discuss problems or seek information related to the niche [00:23:35].
    *   **Confirming User Needs:** Reddit discussions can reveal unmet needs or specific features users are looking for (e.g., a six-year-old Reddit post showing a Google Map of dog parks with a user wishing for descriptions, photos, and details about amenities like shade or benches) [00:24:53]. This confirms that Google Maps isn't satisfying all user needs, creating an opportunity for a specialized directory [00:21:11].

## Data Acquisition and [[Using SEO and web scraping tools for directory data enrichment | Data Enrichment]]

### Web Scraping for Data Collection
Frey uses web scraping tools, specifically OutScraper, to acquire data from Google Maps [00:27:45].
*   **Google Map Scraper:**
    *   **Category Identification:** First, go to Google Maps and type in your niche (e.g., "Dog Park Los Angeles") to see if there's a dedicated Google category (like "dog park") [00:28:05]. Scraping with an exact match category is much easier and yields cleaner data [00:28:45].
    *   **Plain Query:** If no exact category exists, use a plain query (e.g., "off leash dog parks"). This will yield more data but also more "junk" [00:29:02].
    *   **Nationwide Directories:** Frey prefers to create nationwide directories to leverage all available search volume [00:32:24].
    *   **Parameters:** Select essential data points such as name, phone number, address, postal code, state, reviews, street view, working hours, and location link (important for data enrichment) [00:32:38].
*   **Handling Junk Data:** For plain queries, manually filter out irrelevant listings (e.g., those without addresses, or with very few reviews) [00:30:05]. AI tools like ChatGPT or Claude can assist, but manual review is often preferred to avoid losing valuable listings [00:30:32].

### [[Using SEO and web scraping tools for directory data enrichment | Data Enrichment]] for Enhanced Usefulness
[[Using SEO and web scraping tools for directory data enrichment | Data enrichment]] involves adding specific features to the directory data that address user needs and differentiate it from competitors [00:35:22].
*   **Identifying Features:**
    *   **[[using_ai_and_seo_for_online_directories | Ahrefs]] Keywords:** Revisit the fragmented keywords found earlier (e.g., "indoor dog park," "off-leash dog park") [00:35:44].
    *   **Google Maps Reviews:** Analyze user reviews on Google Maps listings for recurring mentions of features or amenities (e.g., "shade," "parking," "water," "benches," "dog bags," "trash cans") [00:36:00].
*   **Implementation:**
    *   **Manual Enrichment (Tedious):** Early directories were manually enriched by creating columns for each feature (e.g., "Water," "Shade") and filling them out [00:37:20]. This is extremely tedious for large datasets [00:38:20].
    *   **Automated Enrichment (AI):** Frey is developing a tool that uses the Google URL (Location ID) to read reviews and automatically identify features like "shade" or "benches," marking them as "true" or "false" [00:38:32]. This significantly automates the process and allows for deeper, more specific information to be included, which sets the directory apart [00:40:07].

## Implementation: The Static Pillar Page Directory on WordPress

### Choosing a CMS
While other CMS options like Framer and Bolt.new are emerging, WordPress with a basic theme (like Elementor Pro) can be used effectively for a simple, static directory build [00:42:16].

### The Static Pillar Page Concept
This directory format is a "level one" build, a "slept-on format" that works well for SEO by consolidating comprehensive content on a single, long page [00:43:30]. This approach leverages the "pillar page" SEO principle, where one page broadly covers a topic and links to more detailed content [00:43:59].

### Structure of a Static Pillar Page
*   **Header (H1):** Include your main keyword (e.g., "Dog Parks") [00:44:27].
*   **Table of Contents:** A table of contents allows users to navigate the long page easily [00:44:32].
*   **City-Specific Sections:** Target city-specific keywords (e.g., "Dog Park Long Beach," "Dog Parks Los Angeles") with individual sections [00:44:35].
*   **Listing Details:** For each listing, include:
    *   A nice photo [00:44:47].
    *   [[Using SEO and web scraping tools for directory data enrichment | Enriched data]] (features identified during enrichment) [00:44:50].
    *   Basic information: address, phone number, hours [00:44:53].
    *   Map embeds [00:44:55].
    *   Optional: Reviews [00:44:57].
*   **SEO Advantage:** This format targets the highest search volume keywords, which are often location-based (e.g., "dog friendly restaurant New York," "pet friendly hotels in Dallas") [00:45:13]. Even programmatic directories see location pages as their most trafficked pages [00:45:30]. By putting all this content on one page, it captures broad keyword clusters; Frey's first directory's state pages ranked for 1,300 keywords [00:47:16].

### [[Monetizing online directories | Monetization]] and Future Potential
*   **[[Monetizing online directories through ads and affiliate marketing | Display Ads]]:** The long nature of pillar pages allows for many ad placements, making display ads a good passive income source [00:46:27]. AdSense can be a very passive form of income, potentially generating $5,000-$7,000 a month for a simple static directory [00:11:12], [00:05:37].
*   **Internal Linking:** A simple internal linking strategy, like linking to different states to view dog parks, encourages user engagement and further reinforces SEO [00:46:56].
*   **Foundation for Larger Ideas:** A successful directory can serve as a foundation for a much bigger idea. Traffic can be funneled into a SaaS product (e.g., a directory for farms and CSAs advertising their SaaS) [00:11:45], or even a consumer product [00:49:03].
*   **[[Monetizing online directories through ads and affiliate marketing | Affiliate Marketing]]:** For niches like pet care, affiliate plays (e.g., BarkBox's affiliate program) can be integrated [00:50:57].
*   **Lead Magnets:** Collecting email lists or data on dog owners through lead magnets can be valuable [00:51:04].

This simple, "dumb" static directory format is inspiring because it allows for a "brute force" approach to [[starting_an_online_directory | starting an online directory]] and can generate enough [[generating_passive_income_through_online_directories | passive income]] to cover bills or free up time for other ventures [00:48:05].