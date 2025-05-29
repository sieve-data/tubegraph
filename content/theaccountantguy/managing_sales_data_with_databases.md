---
title: Managing sales data with databases
videoId: p9M2n3vwLMs
---

From: [[theaccountantguy]] <br/> 

Sales data management is crucial for understanding business performance and generating necessary documentation. This article outlines how to effectively manage sales data using dedicated databases, focusing on a Notion-based sales receipts tracker and a tool for generating PDF sales receipts.

## Introduction to Sales Receipts Tracker

A sales receipts tracker template allows businesses to keep detailed records of their sales <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This template typically includes a sales receipts database designed to store all pertinent information for tracking sales <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This approach leverages [[Using databases in Notion for financial tracking]] principles for efficient record-keeping.

## Key Features of the Sales Receipts Database

### Essential Sales Information

The core of the sales receipts database includes fundamental details for each transaction:
*   Receipt number <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   Receipt date <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   Payment method (with multiple selection options) <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   Business name and address <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>
*   Customer details, which is a [[Managing customer databases in Notion | relational property]] linked to another database containing client information <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>
*   Notes for any additional relevant information <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>

### Detailed Item Tracking

For each sale, the database allows for detailed item tracking:
*   Description of what is being sold <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>
*   Quantity of sales <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
*   Unit price <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>

The design supports adding multiple descriptions, quantities, and unit prices for various items within a single transaction row <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This enables tracking different items sold in varying quantities and unit prices within one receipt <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### Financial Calculations

The database automatically computes key financial figures:
*   **Subtotal**: Sums the total amount of individual items sold <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>
*   **Tax Rate**: Applied to the subtotal <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   **Total Amount**: Automatically computed based on subtotal and tax rate <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>

If additional columns for descriptions or quantities are added, it is important to update the formulas for the subtotal and total amount to ensure accurate computation <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## Sales Receipts Summary

A summary section at the top of the tracker provides an overview of sales performance:
*   **Total Sales**: The cumulative sales value <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
*   **Units Sold**: The total quantity of items sold <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>
*   **Average Sales Value**: Calculated by dividing total sales by units sold, providing key performance indicator (KPI) information <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>

### Client-Specific Performance

The tracker also includes a client summary that breaks down sales data by individual client:
*   Total sales for each client <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>
*   Total quantity of sales made to each client <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>
*   Average sales price for every client <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>

This summary can be customized to suit specific reporting requirements <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## Generating Sales Receipts PDF Documents

In addition to tracking, businesses often need to generate professional sales receipts. Tools like PDF output.com facilitate [[Integrating databases with PDF templates | integrating databases with PDF templates]] to create these documents <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### PDF Output.com Overview

PDF output.com is a tool designed to generate PDF documents, including sales receipts, from inputted data <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Users can select from a list of available templates <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### Single PDF Generation

To generate a single PDF sales receipt:
1.  Navigate to PDF output.com <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
2.  Select the "Sales Receipts" template from the template selection dropdown <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
3.  Fill in all required information, such as receipt number, date, payment method, business details, item descriptions, quantities, unit prices, tax rate, notes, and select the currency <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
4.  Click "Download PDF" to generate the document <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. The currency displayed on the PDF will automatically update if changed <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### Bulk PDF Export

The tool also supports bulk export of PDF documents, useful for generating multiple receipts simultaneously <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

#### Database Input for Bulk Export

In the bulk export mode, users enter all sales receipt information in a database format <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. This database structure mirrors the Notion template, including receipt number, date, payment, business details, and item specifics <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

#### Customizing Input View

Users can freely resize column widths and row heights to comfortably view and enter all details within the database <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. Rows can be added or deleted as needed <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

#### Downloading Multiple PDFs

Once all information is entered into the database:
*   Click "Download All PDF" to generate all receipts in one go <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   Alternatively, click on individual rows to download specific PDFs <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
*   The currency on the generated PDFs will reflect the selected currency option <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

For any template requests or feedback, users can utilize the "request template" or "feedback" windows on the PDF output.com website <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. For direct assistance, users can reach out via email <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.