---
title: Building websites with Webflow
videoId: t96lvP5l3zE
---

From: [[gregisenberg]] <br/> 

Webflow is a powerful visual web development platform that allows users to design, build, and launch responsive websites without writing code <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a>. It functions similarly to design tools like Framer and Figma, but uniquely enables actual website construction directly within the interface <a class="yt-timestamp" data-t="00:33:28">[00:33:28]</a>. Webflow facilitates the creation of sophisticated, SEO-rich platforms and websites, especially when combined with AI and automation tools <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Core Capabilities and Design Flexibility

Webflow offers significant design flexibility, allowing users to design from scratch or utilize pre-built components <a class="yt-timestamp" data-t="00:33:57">[00:33:57]</a>. Resources like Flowbase, Relume, and Flowponents provide a wealth of Webflow components that can be copied and pasted directly into a project <a class="yt-timestamp" data-t="00:33:40">[00:33:40]</a>. This feature makes it easy to build visually without worrying about intricate design details <a class="yt-timestamp" data-t="00:34:24">[00:34:24]</a>.

## Content Management System (CMS)

A crucial feature of Webflow is its integrated Content Management System (CMS), which allows users to create custom "collections" for dynamic content <a class="yt-timestamp" data-t="00:34:34">[00:34:34]</a>. For example, a travel directory might have collections for "restaurants," "malls," or "hotels" <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>. These collections essentially act as catalogs for listings within specific categories <a class="yt-timestamp" data-t="00:34:59">[00:34:59]</a>. Each element on a Webflow template page (e.g., name, address, URL) can be dynamically connected to specific data fields in the CMS <a class="yt-timestamp" data-t="00:54:30">[00:54:30]</a>.

To integrate with external tools like Zapier, a Webflow collection must be published for Zapier to detect it <a class="yt-timestamp" data-t="01:11:08">[01:11:08]</a>.

## Integration with AI and Automation (Zapier, Claude, Appify)

Webflow's power is amplified when integrated with AI and automation tools:
*   **Zapier**: Acts as the central orchestrator, connecting Webflow with other platforms <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. It enables automated workflows, such as taking a place ID from a Google Sheet and generating an entire page in Webflow <a class="yt-timestamp" data-t="00:44:06">[00:44:06]</a>.
*   **Appify**: A platform for data scraping, including Google Maps business data <a class="yt-timestamp" data-t="00:49:09">[00:49:09]</a>. Appify can extract detailed information about a place (address, city, images, popular times, reviews) using its unique Place ID <a class="yt-timestamp" data-t="00:37:52">[00:37:52]</a>.
*   **Claude (or other LLMs)**: An AI language model used to process and repurpose the scraped data <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>. Users can feed raw data from Appify to Claude and instruct it to format content, generate descriptions, or even calculate scores based on information like reviews <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. This allows for automated content generation tailored to specific needs and formats required by Webflow's CMS <a class="yt-timestamp" data-t="00:53:50">[00:53:50]</a>. Claude can also be prompted to generate content in specific languages, like Canadian French <a class="yt-timestamp" data-t="00:56:22">[00:56:22]</a>.

The overall workflow involves:
1.  **Data Input**: Starting with a simple input, like a Place ID in a Google Sheet <a class="yt-timestamp" data-t="00:45:19">[00:45:19]</a>.
2.  **Data Scraping**: Zapier triggers Appify to scrape detailed data from Google Maps using the Place ID <a class="yt-timestamp" data-t="00:47:02">[00:47:02]</a>.
3.  **Data Processing**: A Python code step in Zapier processes the Appify output (which is initially broken down) into a single JSON string, making it easier for Claude to consume <a class="yt-timestamp" data-t="00:52:18">[00:52:18]</a>.
4.  **Content Generation**: Claude receives the JSON data and, based on specific prompts, generates structured content (e.g., place name, URL, best time to visit, scores) <a class="yt-timestamp" data-t="00:53:50">[00:53:50]</a>. The use of mini-prompts wrapped in asterisks helps Claude break down its output into individual, digestible strings for Webflow <a class="yt-timestamp" data-t="00:58:01">[00:58:01]</a>.
5.  **Webflow Integration**: Another Python step in Zapier breaks Claude's single text block output into individual strings <a class="yt-timestamp" data-t="01:07:38">[01:07:38]</a>. These strings are then mapped to the corresponding fields in Webflow's CMS, automatically populating new pages <a class="yt-timestamp" data-t="01:08:49">[01:08:49]</a>.

This automated process allows for the mass creation of website pages with minimal manual effort <a class="yt-timestamp" data-t="00:45:31">[00:45:31]</a>.

## Real-World Examples

The speaker demonstrates this process with two personal projects:
*   **Guilty Chef**: A recipe directory website that generates thousands of recipes using AI, with each page automatically created and optimized with schema <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. It achieved over 100,000 monthly traffic within seven to eight months with almost zero time investment <a class="yt-timestamp" data-t="01:11:53">[01:11:53]</a>.
*   **BestDubai.com**: A travel directory for Dubai, built in just a few weeks using the same process <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>. This site leverages AI to generate scores for locations based on reviews and even created a Chrome extension to scrape up-to-date menu and pricing information from delivery services like Deliveroo and Talabat <a class="yt-timestamp" data-t="00:30:56">[00:30:56]</a>. Within 30 days, it started ranking highly on Google for specific search terms <a class="yt-timestamp" data-t="00:27:08">[00:27:08]</a>.

## SEO Benefits

This approach to building with Webflow, combined with AI, offers significant SEO advantages:
*   **Schema Markup**: AI (like Claude) can automatically write schema markup for content (e.g., recipe schema for recipe sites) <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Schema helps Google understand website content more effectively, leading to rich snippets and higher rankings <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. Even large websites often fail to implement schema properly <a class="yt-timestamp" data-t="00:53:53">[00:53:53]</a>.
*   **Automated Content Creation**: The ability to generate thousands of unique, high-quality pages with minimal effort drastically increases a site's search footprint <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   **AI Engine Indexing**: Content generated this way not only ranks on Google but is also indexed by AI engines like ChatGPT and Claude <a class="yt-timestamp" data-t="01:17:01">[01:17:01]</a>. This means that when users ask AI engines for information, the Webflow site can be cited as the primary source, driving additional traffic <a class="yt-timestamp" data-t="01:17:11">[01:17:11]</a>.
*   **Backlinks**: By embedding a reference (e.g., `ref=yourname`) in external links on the Webflow site, users can track traffic coming from their platform <a class="yt-timestamp" data-t="01:49:24">[01:49:24]</a>. This can proactively lead to partnership opportunities with external businesses as they observe traffic originating from the Webflow site <a class="yt-timestamp" data-t="01:50:15">[01:50:15]</a>.
*   **Localized Content**: Building directories for specific geographies and languages (e.g., a Montreal directory in Canadian French) can be highly effective, as it caters to underserved niches and local search trends <a class="yt-timestamp" data-t="00:56:56">[00:56:56]</a>.