---
title: Methods for finding and validating niche ideas
videoId: 6rAHkSyzfNA
---

From: [[gregisenberg]] <br/> 

Frey, an online directory expert, shares his strategies for [[identifying_niche_markets_and_opportunities | finding]] and [[methods_for_validating_startup_ideas_without_building_them | validating ideas]] for online directories that can generate significant passive income [00:00:20]. His first directory, built in October 2022, has been monetized for 18 months, takes about 15 minutes a month to maintain, and generated around $2,300 in revenue last month [00:01:27], [00:01:59], [00:02:03], [00:02:04], [00:02:12].

The core process involves finding an idea, validating it, gathering and cleaning data, and implementing it on a content management system (CMS) [00:02:45], [00:02:59], [00:03:08], [00:03:15].

## Finding Niche Ideas

Frey's preferred method for [[identifying_niche_markets_and_opportunities | finding ideas]] is by using Ahrefs' Keyword Explorer [00:12:40], [00:12:43].

### Using Ahrefs
*   **Search "Near Me"**: Type "near me" into Ahrefs' Keyword Explorer to discover a long list of local queries with high search volume [00:12:43], [00:12:50].
*   **Identify Opportunities**: Look for keywords with high monthly search volume and low keyword difficulty [00:13:08], [00:13:10]. Frey's "sweet spot" for monthly searches is between 30,000 and 100,000 [00:13:20], [00:13:23].
*   **Optimal Keyword Difficulty**: Anything under 20 is generally considered easy to rank for [00:16:48], [00:16:51], although this metric can sometimes be misleading due to competition or dominant backlinks [00:16:55], [00:17:18], [00:17:21], [00:17:27]. However, with expertise, ranking for keywords with a difficulty of 40-50 is also possible [00:17:44], [00:17:47].

### Niches to Avoid
Frey advises against specific types of niches based on his experience [00:13:34], [00:13:37]:
*   **Seasonal Niches**: Avoid niches that are highly seasonal, such as "pumpkin patches near me," as they only monetize well for a short period [00:13:40], [00:13:51], [00:13:56].
*   **Difficult-to-Obtain Data Niches**: Niches where data is hard to acquire, like "earthquake near me," should be avoided [00:14:02], [00:14:07], [00:14:12].
*   **Big Branded Keywords**: Stay away from highly branded keywords like "Taco Bell near me" because major brands likely already have effective directories and the search intent is too one-dimensional [00:14:21], [00:14:26], [00:14:28], [00:14:47].

### Ideal Niche Characteristics
An ideal niche has fragmented or multi-dimensional search intent, meaning people are looking for specific types of results within the niche [00:14:52], [00:15:47], [00:15:49]. For example, "dog parks near me" is good because people search for "indoor dog park," "off-leash dog park," or "dog water park," indicating a need for detailed information beyond just a location [00:15:10], [00:15:40], [00:15:52], [00:15:57]. This allows for data enrichment to provide additional utility, like details on water fountains, benches, or shade [00:16:00], [00:16:03], [00:16:05], [00:16:16], [00:16:19].

## Validating Niche Ideas

After identifying a potential niche, it's crucial to validate the idea to ensure it solves a real problem [00:03:02], [00:03:04].

### Competitive Research (Google Search)
*   **Analyze Existing Directories**: Search for "[Niche] + [City]" (e.g., "Dog Park Los Angeles") to find existing directories on the first page of Google [00:18:25], [00:18:29], [00:18:31], [00:18:38].
*   **Identify Improvement Opportunities**: Evaluate if you can build a better directory than what currently exists [00:19:04], [00:19:07]. For example, a basic directory like Nyabone, which only lists names and addresses but gets 21,000 monthly visitors, signals a significant opportunity for improvement by adding more useful features [00:19:37], [00:19:50], [00:20:04], [00:20:07], [00:20:16], [00:20:25]. Even more established directories like BringFido, while better, might still lack specific details users seek (e.g., dog bags, water fountains) [00:22:49], [00:22:51], [00:22:53], [00:22:57], [00:23:01], [00:41:46].

### Social Listening (Reddit)
*   **Confirm Problem Existence**: Use Reddit to verify if people are actively discussing and struggling with the problem your directory aims to solve [00:23:35], [00:23:38], [00:23:42].
*   **Search Reddit**: Search for "[Niche] + [City] Reddit" (e.g., "Dog Park Los Angeles Reddit") [00:23:44], [00:23:49].
*   **Analyze Discussions**: Skim through forums and comments for discussions indicating unmet needs, people looking for information elsewhere, or even manual attempts by users to curate information [00:23:54], [00:24:01], [00:24:08], [00:24:21].
*   **Example**: A Reddit post from six years ago where someone shared Google Map pins of dog parks, with comments expressing a desire for more detailed descriptions and photos, serves as a strong social signal for curation and hyper-specific features [00:24:47], [00:24:55], [00:24:58], [00:25:03], [00:25:22], [00:25:26], [00:25:40], [00:25:44].

## Data Acquisition and Enrichment

Once a niche is validated, the next step is to acquire and enrich the data for the directory [00:26:03], [00:26:06], [00:26:09], [00:35:22].

### Data Acquisition
*   **Web Scraping Tools**: Use web scraping tools like Outscraper's Google Map Scraper [00:27:41], [00:27:45], [00:27:49], [00:27:55].
*   **Google Map Categories**: Prioritize scraping based on exact Google Map categories (e.g., "dog park") for cleaner data [00:28:14], [00:28:19], [00:28:27], [00:28:45], [00:28:47], [00:34:48].
*   **Plain Queries**: If an exact category isn't available, use a plain query (e.g., "off leash dog parks"), but expect more "junk" data [00:28:52], [00:28:58], [00:29:02], [00:29:11].
*   **Essential Data Points**: Collect basic information such as name, phone number, address, postal code, state, reviews, street view, working hours, and location links [00:32:38], [00:32:40], [00:33:02], [00:33:06], [00:33:08].
*   **Nationwide Scope**: Frey prefers to create nationwide directories to leverage all available search volume [00:32:24], [00:32:27].

### Data Cleaning and Enrichment
*   **Initial Cleaning**: For junk data from plain queries, manually remove listings without addresses or those with very few reviews [00:29:53], [00:30:05], [00:30:07], [00:30:11], [00:30:14].
*   **Leveraging AI for Cleaning**: [[AI_tools_for_validating_and_developing_startup_ideas | AI tools]] like ChatGPT (or "Cloe") can help parse and clean data with a solid prompt, though manual initial filtering can prevent removal of good quality listings [00:30:28], [00:30:32], [00:30:47], [00:30:50], [00:31:14], [00:31:31], [00:31:38].
*   **Enriching Data**: This involves adding features that address the multi-dimensional search intent identified earlier [00:35:22], [00:35:28], [00:35:30].
    *   **Manual Enrichment**: Go through Google Maps reviews for individual listings to identify common features and tags (e.g., "shade," "parking," "water," "benches," "dog bags," "trash cans") [00:35:57], [00:36:00], [00:36:08], [00:36:10], [00:36:13], [00:36:15], [00:36:22], [00:36:31], [00:36:34], [00:36:39], [00:36:41], [00:36:47], [00:36:49], [00:37:02], [00:37:05], [00:37:09], [00:37:20], [00:37:24], [00:37:30], [00:37:33]. This process can be tedious for large datasets [00:38:24], [00:38:26].
    *   **Automated Enrichment**: Frey is developing a tool that uses the location ID from Google Maps URLs to automate data enrichment by analyzing reviews for specific keywords (e.g., "shade," "benches") and marking properties as true/false [00:38:32], [00:38:36], [00:38:47], [00:39:01], [00:39:06], [00:39:08], [00:39:12], [00:40:07], [00:40:12], [00:40:15], [00:40:18], [00:40:21], [00:40:28], [00:40:30], [00:40:32], [00:40:35]. This level of detail [[niche_selection_and_audience_targeting | sets a directory apart]] and brings users back [00:41:51], [00:41:53], [00:41:55].

## Building the Directory

While WordPress with basic themes like Elementor Pro can be used [00:42:15], [00:42:20], [00:42:52], [00:43:06], any CMS works, including Framer or Bolt.new [00:42:24], [00:42:26], [00:42:32], [00:42:57], [00:43:01].

### Static Pillar Page Directory Format
Frey advocates for a "static pillar page directory" — a single, comprehensive, long page [00:43:30], [00:43:33], [00:43:44], [00:43:48], [00:44:04], [00:44:07].
*   **Structure**: Includes a header with the main keyword, a table of contents, and sections targeting city-specific keywords (e.g., "Dog Park Long Beach") [00:44:27], [00:44:29], [00:44:32], [00:44:35], [00:44:36].
*   **Content**: Each section includes a listing's photo, enriched data (features), basic information (address, phone, hours), and an embedded map [00:44:47], [00:44:50], [00:44:53], [00:44:55], [00:44:57].
*   **SEO Advantages**: This format leverages high-volume location-based keywords and helps rank for numerous related keywords (e.g., one state page ranking for 1,300 keywords) [00:45:13], [00:45:16], [00:45:18], [00:45:20], [00:45:33], [00:45:36], [00:46:16], [00:46:18], [00:47:16], [00:47:19], [00:47:21].
*   **Monetization**: It's well-suited for display ad monetization due to its length, allowing for many ad placements [00:46:27], [00:46:30], [00:46:33], [00:46:36], [00:46:37], [00:46:40].
*   **Internal Linking**: A simple internal linking strategy can be implemented by listing different states or locations, allowing users to navigate through the directory [00:46:53], [00:46:56], [00:46:58], [00:47:01].

## Conclusion

Building a directory, even a simple one, can generate substantial passive income ("mailbox money") [00:48:22], [00:48:26], [00:48:28], [00:48:32], [00:48:34], [00:48:37], [00:48:40]. This provides a foundation for larger ventures, like developing a SaaS product or a consumer product based on the collected traffic and data, showcasing the [[opportunities_in_niche_mobile_app_markets | potential of niche markets]] and [[niche_publishing_strategies | niche publishing strategies]] [00:48:55], [00:48:57], [00:49:00], [00:49:03], [00:49:06], [00:49:12], [00:49:15], [00:49:19], [00:49:54], [00:50:05], [00:50:08], [00:50:10]. The initial steps of finding and validating the idea, as well as getting and parsing data, are fundamental regardless of the scale of the project [00:53:37], [00:53:41], [00:53:43], [00:53:46], [00:53:50], [00:53:52].