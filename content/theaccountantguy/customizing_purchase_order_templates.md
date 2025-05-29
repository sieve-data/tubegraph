---
title: Customizing purchase order templates
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

This article details how to customize and utilize a purchase order tracker template, particularly focusing on the Notion database and the PDF generation process via PDF output.com.

## Purchase Order Tracker Database Customization

The purchase order tracker template features a database designed to manage purchase order information <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Key customizable fields include:
*   Purchase order number <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   Order date and expected delivery date <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
*   Terms and conditions <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   Company name and address <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   Supplier name <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   Notes <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>

### Customizing Item Details and Calculations

The template includes specific columns for item descriptions, quantities, and unit prices <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Adding More Items**: To add more description, quantity, or unit price fields, simply duplicate existing columns <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. After duplicating, input the item description, quantity, and unit price <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Subtotal Calculation**: The subtotal automatically computes the sum of the unit price and quantity for all descriptions <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. If additional description/quantity columns are added, the subtotal formula must be updated to include the new values <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Total Amount**: The total amount is calculated by including shipping costs and a percentage tax rate <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Purchase Order Summary Metrics

The template provides an automated purchase order summary at the top of the database <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>:
*   **Total Purchase**: This is the summation of all purchases recorded in the database <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Units Ordered**: Calculated from the quantity columns of all descriptions <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. Ensure formulas are updated if more quantity columns are added <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Average Order Value**: Computed by dividing the total purchases by the units ordered <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Client Summary

A client summary section displays total purchases, total quantities ordered, and average order value for each client <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### General Customization Assistance
For further customization of the template, users can reach out to notionformyuse@gmail.com for assistance <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Generating and Customizing Purchase Order PDFs

PDF documents for purchase orders can be generated using PDF output.com <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Template and Currency Selection
*   **Template Selection**: Upon logging in to PDF output.com, users can select the "purchase AO template" from a dropdown menu <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Currency Selection**: The desired currency for the PDF can be chosen from the interface <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. If a currency is not available, it can be requested through a dedicated window <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. The currency can be changed instantly, updating the displayed values <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Requesting New Templates
Users can request specific templates if they are not available in the dropdown list <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

### PDF Generation Modes
*   **Single PDF Mode**: This mode allows generating PDF documents one by one <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Once all information is filled, clicking "download PDF" generates the document <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   **Bulk Export Mode**: For exporting multiple documents simultaneously, the bulk export mode can be used <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. Users fill in all details, add multiple rows as needed, and can then download individual documents or all documents at once by clicking "download all PDF" <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Future Notion Integration
Future updates plan to include a Notion database integration, allowing direct export of PDFs by reading information from a Notion database <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. [[Generating purchase order PDFs using Notion | This integration will streamline the process of creating purchase order PDFs directly from Notion data]] <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

### Feedback
Users can provide feedback via the feedback window on PDF output.com to help improve the product <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.