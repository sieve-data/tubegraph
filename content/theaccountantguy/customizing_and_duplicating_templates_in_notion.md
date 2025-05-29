---
title: Customizing and duplicating templates in Notion
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

Notion templates can be duplicated and customized to generate documents in bulk, such as purchase orders, by integrating with external tools like PDFoutput.com <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Template Structure for Customization

A Notion template, like a purchase order, includes relevant details such as the purchase order number, date, supplier, and buyer name <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. For customization, specific items that need to be replaced by data are placed inside curly braces `{}` <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. These placeholders, such as `{purchase order number}`, `{date field}`, `{supplier name}`, and `{buyer name}`, will be automatically populated from a Notion database <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

The corresponding Notion database must contain properties (columns) with the *exact same naming convention* as the placeholders in the template <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>, for example, "purchase order number," "date field," "supplier name," and "buyer name" <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This precise naming enables automatic mapping between the template and the database <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. If the naming is incorrect, manual mapping will be required <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### Customization Flexibility
Once a template is duplicated into your Notion workspace, you have full control to edit, modify, or make any changes to it <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. The key rule for [[customizing Notion templates]] for data population is to ensure that any dynamic information you want to pull from a database remains enclosed in curly braces, following the exact same naming as your database properties <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

## Duplicating Templates into Notion

To use pre-defined templates for bulk PDF generation (e.g., [[customizing purchase order templates in Notion]]), you typically follow these steps:

1.  **Log in to PDFoutput.com** <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
2.  **Navigate to the Template Section** <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    *   This section usually lists predefined templates <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
3.  **Search for the desired template**, such as "purchase order" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
4.  **Access the Template and Database Links**: The search result will typically provide links to both the associated Notion database and the Notion template <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Click on both <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
5.  **Duplicate the Template and Database**:
    *   For each opened Notion link (template and database), click on the "Start with this template" option <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   When prompted for duplication, select your Notion workspace and click "Add to private" <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
    *   This will add the database and template to your Notion workspace <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
    *   Repeat the duplication process for both the database and the template <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
6.  **Connect to PDFoutput.com**: Once duplicated, return to PDFoutput.com and connect to your newly duplicated Notion database and template <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. You may need to grant access by selecting your workspace, specific pages (database and template), and then clicking "Allow access" <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

This process enables [[customizing Notion templates for specific needs]], by allowing you to take an existing structure and adapt it to your unique data and formatting requirements. If using relation properties in your database, ensure access is also given to those related databases during the connection process <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.