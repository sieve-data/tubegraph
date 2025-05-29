---
title: Mapping Notion Database Elements to Templates
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[personalizing_templates_with_notion_data | personalize templates with Notion data]] by mapping elements from a Notion database to placeholders in a template, enabling the bulk generation of documents like professional invoices <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process is crucial for [[connecting_notion_databases_and_templates_for_pdf_creation | connecting Notion databases and templates for PDF creation]] and [[using_templates_in_notion_for_pdf_generation | using templates in Notion for PDF generation]].

## Template and Database Preparation

To successfully map Notion database elements to a template, both the template and the database must be set up correctly:

### Template Structure
In the template, any element intended to be replaced by data from the Notion database must be enclosed in curly braces, e.g., `{{client name}}`, `{{client company}}`, `{{client address}}` <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

### Database Structure
The Notion database should contain properties with information corresponding to the placeholders in the template <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. For every element in the template (inside curly braces), there should be a corresponding property in the database <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

> [!TIP]
> To ensure [[automatically_mapping_database_properties_to_template_elements | automatically mapping database properties to template elements]], use the exact same name for the placeholder in the template (within curly braces) and the corresponding property in the Notion database <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. For example, if your template has `{{invoice number}}`, your database property should also be named "Invoice Number" <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

## The Mapping Process

After [[connecting_notion_databases_and_templates | connecting Notion databases and templates]] within the PDF Output portal <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>, the software initiates the mapping process <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

### Automatic Mapping
The software automatically reflects all database properties on the left side of the interface <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. Each property is then automatically mapped to its corresponding element on the template side <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. This automatic mapping occurs seamlessly when the property names in the database precisely match the placeholder names in the template <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### Manual Mapping
If the names in the template and database do not match exactly, the elements will not be automatically mapped <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. In such cases, a gray icon will appear, allowing you to manually click and search for the correct corresponding element to map it <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Manual mapping is required for any elements where names differ <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

## Generating Documents
Once all elements are correctly mapped, you can proceed to generate PDF documents <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. The system will create a separate PDF document for each row (entry) in your Notion database, using the specified template and populating it with the mapped data <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. For example, three rows in a professional invoice database would generate three distinct invoice PDFs <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

## Important Considerations for Mapping

### Template Customization
The template used for PDF generation is entirely customizable <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. You can modify its layout and content to fit your specific requirements. The key is to ensure that any data you want to pull from the database is placed within curly braces and that the name inside the braces matches the database property <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

### Relational Properties
If your Notion database includes relational properties—meaning some elements in your primary database are connected to another separate database—you must also connect that secondary database during the setup process <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. This ensures that all necessary data for the template can be accessed and mapped smoothly <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
For more details on [[mapping_and_managing_data_fields_between_notion_database_and_pdf_templates | mapping and managing data fields between Notion database and PDF templates]], especially for specific use cases like [[mapping_database_elements_to_invoice_templates | mapping database elements to invoice templates]], refer to the respective guides.