---
title: Mapping database elements to invoice templates
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

## Overview

This article outlines how to generate professional invoices directly from a Notion database using the PDF Output tool <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The process involves [[mapping_database_properties_to_template_placeholders | mapping Notion database elements to template placeholders]] within an invoice template to create professional PDF documents <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Invoice Template Design

An invoice template includes sections like "from" and "to" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Key details such as client name, client company, client address, city, state, and zip are designated as placeholder text enclosed in curly braces <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Any element within the template placed in curly braces will be replaced by data from a connected database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

> All placeholder text elements in the template must be placed inside curly braces `{}` <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

This [[customizing_invoice_templates_using_placeholders | customizable invoice template]] is then used to generate PDF documents <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Notion Database Setup

The Notion database contains corresponding elements such as client name, amount, bank name, client address, and client company <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. For every row of information in the database, the data will populate the template and generate a PDF <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. It's crucial that the placeholder element names in the template match the column names in the database for automatic mapping <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

## Using PDF Output for Generation

To begin, log into PDF Output <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. First, certain steps within the "help" section (accessible by clicking "H") must be completed to enable API keys for the setup <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Connecting Database and Template

1.  Define a connection name (e.g., "Invoice Generation") <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  Select the specific database, such as "professional invoice database" <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
3.  Select the corresponding template, such as "professional invoice template" <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
4.  Click "next" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Automatic Mapping and Customization

PDF Output loads all elements and values from both the database and the template, and [[automatically_mapping_database_properties_to_template_elements | automatically maps each database property to its corresponding template element]] <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. For example, "client address" from the database is connected to the "client address" placeholder in the template <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. Other elements like "item one," "terms," and "amount three" are also automatically mapped <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

If any mapping is not automatic (appearing in gray), you can manually click on the element and search for the correct value to establish the connection <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### Generating and Downloading Invoices

After mapping, click "export" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. In the Notion database, a "PDF status" column will automatically tick as each PDF file is generated <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

You can then:
*   **Preview Sample:** Click "preview sample" to view the generated PDF, which shows all elements from the database accurately replaced in the template <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Download All:** Click "download all" to download all generated PDF files <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

The output provides clean, professional invoices, with all database information accurately populated into the template <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. This enables [[using_templates_to_generate_pdf_invoices | using templates to generate PDF invoices]] efficiently.

## Key Takeaways

The PDF Output site allows users to connect their Notion database and Notion template to generate PDF documents <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Remember to:
*   Place all placeholder text elements inside curly braces in your template <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   Use the same names for these elements in your database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   Follow the instructions in the "help" section of PDF Output for initial setup <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

This process enables efficient [[customizing_and_mapping_database_elements_for_pdf_output | customizing and mapping database elements for PDF output]] directly from Notion.