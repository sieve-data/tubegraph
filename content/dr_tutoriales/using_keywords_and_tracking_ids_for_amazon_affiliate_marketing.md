---
title: Using Keywords and Tracking IDs for Amazon Affiliate Marketing
videoId: EtOxBh6IodY
---

From: [[dr_tutoriales]] <br/> 

This article outlines how to promote Amazon products on a WordPress website using a specific plugin, focusing on the importance of Amazon Affiliate IDs and the utility of keywords in product promotion, all without requiring an Amazon API key <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>. This method helps users advertise products and [[generating_revenue_through_amazon_affiliate_program | make money with affiliates]] even if they haven't achieved the three affiliate sales typically required to obtain an API code <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>.

## Plugin Installation and Setup

To begin [[optimizing_amazon_product_promotion_for_increased_sales | promoting Amazon products]] on a WordPress site, a specific plugin can be used <a class="yt-timestamp" data-t="01:03:03">[01:03:03]</a>.
1.  Navigate to the "Plugins" section in the left-hand menu of your WordPress dashboard <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a>.
2.  Click "Add New" <a class="yt-timestamp" data-t="01:17:91">[01:17:91]</a>.
3.  Search for "Amazon Philip" <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.
4.  Download and install the free plugin named "Droxypin and Affiliation Weed Amazon" <a class="yt-timestamp" data-t="01:29:43">[01:29:43]</a>.
5.  Activate the plugin <a class="yt-timestamp" data-t="01:50:50">[01:50:50]</a>.

Once activated, the plugin creates a new menu item on the left, allowing access to its configurations <a class="yt-timestamp" data-t="01:54:38">[01:54:38]</a>.

## Configuring Your Amazon Affiliate ID

To ensure that sales are assigned to your [[using_amazon_affiliate_account | Amazon affiliate account]], it's crucial to enter your Amazon Affiliate ID within the plugin settings <a class="yt-timestamp" data-t="02:14:48">[02:14:48]</a>.
1.  In the plugin settings, go to the "Amazon" section <a class="yt-timestamp" data-t="02:11:09">[02:11:09]</a>.
2.  Enter your Amazon ID and specify your country <a class="yt-timestamp" data-t="02:28:38">[02:28:38]</a>.

### Locating Your Amazon Affiliate ID
If you do not know how to find your ID, follow these steps <a class="yt-timestamp" data-t="02:34:65">[02:34:65]</a>:
1.  Go to the Amazon Associates page <a class="yt-timestamp" data-t="02:37:65">[02:37:65]</a>.
2.  Navigate to "Account Settings" <a class="yt-timestamp" data-t="02:58:34">[02:58:34]</a>.
3.  Select "Manage Tracking IDs" <a class="yt-timestamp" data-t="03:02:18">[03:02:18]</a>.
4.  Here, you can enter or find various tracking IDs to monitor sales across different web pages or product categories <a class="yt-timestamp" data-t="03:07:31">[03:07:31]</a>.

## General Plugin Settings

Within the "General" section of the plugin, you can customize how Amazon products are displayed <a class="yt-timestamp" data-t="03:41:48">[03:41:48]</a>.
*   **Initial Products Displayed**: Configure how many initial Amazon products are shown <a class="yt-timestamp" data-t="03:51:30">[03:51:30]</a>.
*   **Products Per Page**: Set the number of products displayed per page (e.g., eight products is recommended to avoid saturating the viewer) <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.
*   **Buy Button Text**: Customize the text for the "buy" button (e.g., "Buy," "Buy it now," "Subscribe") to be clear and concise <a class="yt-timestamp" data-t="04:35:05">[04:35:05]</a>.

After making changes, remember to click "Save settings" <a class="yt-timestamp" data-t="05:07:14">[05:07:14]</a>.

## Methods for Promoting Amazon Products with the Plugin

The plugin utilizes shortcodes to display Amazon products, offering different [[methods_for_obtaining_amazon_affiliate_links | methods for obtaining Amazon affiliate links]].

### 1. Search Bar for Amazon Products (WPAS_Search)
This shortcode creates an Amazon search bar on your website <a class="yt-timestamp" data-t="05:26:30">[05:26:30]</a>.
*   **Code**: `[wpas_search]` <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>
*   **Functionality**: Allows users to search for any Amazon product directly on your site <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>.
*   **Result**: Displays product listings from Amazon based on the search query, including reviews, which are linked to your affiliate ID if purchased <a class="yt-timestamp" data-t="06:37:78">[06:37:78]</a>.

### 2. Automatically Recommended Products (WPAS_Recommend)
This shortcode allows Amazon's algorithms to display automatically recommended products <a class="yt-timestamp" data-t="07:07:07">[07:07:07]</a>.
*   **Code**: `[wpas_recommend]` <a class="yt-timestamp" data-t="07:00:26">[07:00:26]</a>
*   **Functionality**: Amazon selects products based on factors like high sales, good ratings, and user recommendations, or previous search interests <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>.
*   **Consideration**: While commissions are earned if purchased, you do not choose which specific products are displayed, meaning unrelated items might appear <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>.

### 3. Displaying Specific Products by ASIN (WPAS_Products)
This method allows you to display individual Amazon products using their unique ASIN (Amazon Standard Identification Number) code <a class="yt-timestamp" data-t="09:32:93">[09:32:93]</a>.
*   **Code**: `[wpas_products ASIN_CODE]` <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>
*   **Locating ASIN**: The ASIN code can typically be found in the product's URL on Amazon's website <a class="yt-timestamp" data-t="09:42:36">[09:42:36]</a>.
*   **Functionality**: Ensures that only the specific product(s) you choose are promoted on your site <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>.
*   **Multiple Products**: You can list several ASIN codes separated by commas within the `[wpas_products]` shortcode to display multiple items, even as a dropdown list <a class="yt-timestamp" data-t="11:27:66">[11:27:66]</a>.
    *   **Example**: `[wpas_products ASIN1, ASIN2, ASIN3]` <a class="yt-timestamp" data-t="11:47:00">[11:47:00]</a>

### 4. Displaying Products by Keywords (WPAS_Keywords)
This is a powerful method for [[creating_amazon_affiliate_links | creating Amazon affiliate links]] by dynamically displaying products based on specific keywords you define <a class="yt-timestamp" data-t="12:46:42">[12:46:42]</a>.
*   **Code**: `[wpas_keywords "your+keyword"]` <a class="yt-timestamp" data-t="12:43:08">[12:43:08]</a>
*   **Keyword Spacing**: When using multiple words in a keyword phrase, replace spaces with the plus (`+`) symbol <a class="yt-timestamp" data-t="13:03:00">[13:03:00]</a>.
    *   **Example**: For "cheap tablets," the code would be `[wpas_keywords "cheap+tablets"]` <a class="yt-timestamp" data-t="13:15:39">[13:15:39]</a>.
*   **Functionality**: The plugin fetches and displays relevant products from Amazon based on the specified keyword(s) <a class="yt-timestamp" data-t="13:26:00">[13:26:00]</a>. This is highly useful for targeting specific product categories on your website <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a>.
*   **Display**: Products are displayed in the quantity chosen in the general settings (e.g., three by three grid) <a class="yt-timestamp" data-t="13:46:27">[13:46:27]</a>.

## Customizing Product Display Style

To enhance the visual appeal and trustworthiness of the displayed Amazon products, you can customize the styling of the "buy" button.
1.  Navigate to "Customize" in your WordPress dashboard <a class="yt-timestamp" data-t="14:10:40">[14:10:40]</a>.
2.  Go to "Additional CSS" <a class="yt-timestamp" data-t="14:13:00">[14:13:00]</a>.
3.  Paste custom CSS code (often provided by the plugin documentation or similar tutorials) to change elements like button color and width to match Amazon's familiar yellow button <a class="yt-timestamp" data-t="14:33:00">[14:33:00]</a>. This fosters familiarity and trust with users <a class="yt-timestamp" data-t="14:36:00">[14:36:00]</a>.