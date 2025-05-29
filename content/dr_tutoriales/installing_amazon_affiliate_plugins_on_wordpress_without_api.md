---
title: Installing Amazon Affiliate Plugins on WordPress without API
videoId: EtOxBh6IodY
---

From: [[dr_tutoriales]] <br/> 

This tutorial explains how to install and use a WordPress plugin to [[advertising_amazon_products_with_wordpress_plugins | advertise Amazon products]] without needing an API code <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. An API code is typically required after carrying out three [[generating_commissions_from_amazon_affiliates | Amazon affiliate sales]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This method allows users to start [[generating_revenue_through_amazon_affiliate_program | making money with Amazon affiliates]] immediately <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Plugin Installation

To begin, navigate to your WordPress page <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
1.  Go to the "Plugins" section in the left menu <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
2.  Click "Add New" <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
3.  Search for "Amazon Philip" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
4.  Download and install the "Droxypin and Affiliation Weed Amazon" plugin <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This is a free plugin that does not require an API <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
5.  After downloading, click "Activate" <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Once activated, the plugin will appear in the left menu <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

## Plugin Configuration

### Amazon Settings

The first step in configuring the plugin is to enter your [[using_amazon_affiliate_account | Amazon ID]] <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. This ensures that all product purchases are assigned to your account, so the sales are registered as yours <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. You will also select your country <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

#### Finding Your Amazon Affiliate ID
To find your Amazon Affiliate ID:
1.  Go to the Amazon page (specifically for affiliates) <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
2.  Navigate to "Account settings" <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
3.  Go to the "Manage tracking IDs" list <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. Here you can find your existing IDs or create new ones for different web pages or product categories (e.g., iPhone products) <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### General Settings

Under the "General" section of the plugin settings, you can edit various characteristics of the Amazon products you are [[advertising_amazon_products_with_wordpress_plugins | advertising]] <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **Initial Products Displayed**: Configure how many initial products are shown <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Products Per Page**: Set the number of products displayed per page. For example, you can set it to eight to avoid saturating your audience <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Buy Button Text**: Customize the text on the "buy" button. By default, it appears in English <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. You can change it to "buy it now," "subscribe," or any other desired text <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Pro Version Options**: Many other advanced settings are for the Pro version of the plugin <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
Once configured, click "Save settings" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Using Plugin Shortcodes to Display Products

The plugin uses shortcodes to display Amazon products on your WordPress site <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

### 1. Search Bar (WPAS Search)
The `[wpas_search]` shortcode allows you to create an Amazon product search bar on your website <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. When a user types a product (e.g., "Samsung tablet"), a dropdown menu will appear with relevant Amazon products chosen for those searches <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. Purchases made through this search bar will be linked to your [[using_amazon_affiliate_account | Amazon affiliate ID]] <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### 2. Automatic Product Display (WPAS Products_Automatic)
The `[wpas_products_automatic]` shortcode allows Amazon to automatically display products based on algorithms <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. These products are generally best-selling, well-rated, or highly recommended <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. While this generates [[generating_commissions_from_amazon_affiliates | affiliate commissions]], you do not choose which products are shown <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This can be both good and bad, as it might display products unrelated to your website's specific topic (e.g., books on a technology page) <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

### 3. Specific Product Display (WPAS Products + ASIN)
The `[wpas_products number="ASIN_CODE"]` shortcode allows you to display specific Amazon products <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   **Finding the ASIN Code**: The ASIN (Amazon Standard Identification Number) code is a unique identifier for each product <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. You can find it in the URL of the product page on Amazon, usually after `/dp/` or `/gp/product/` <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   **Usage**: Copy the ASIN code and paste it into the shortcode <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. For example, `[wpas_products number="B08J72XXXX"]` will display that specific iPad <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

### 4. Multiple Specific Products (WPAS Products + multiple ASINs)
You can display multiple specific products in a row by separating their ASIN codes with commas within the `[wpas_products]` shortcode <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
*   **Usage**: `[wpas_products number="ASIN1,ASIN2,ASIN3"]` <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. This creates a powerful dropdown list allowing users to browse various recommended products <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.

### 5. Keyword-based Product Display (WPAS Keywords)
The `[wpas_keywords]` shortcode allows you to introduce products using keywords <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
*   **Usage**: `[wpas_keywords key="your keyword here"]` <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.
*   **Spaces in Keywords**: If your keyword has a space, use a plus symbol (`+`) instead of a space (e.g., "cheap+tablets") <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. This will display a selection of products on Amazon related to that keyword <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.

## Customizing Product Display (CSS)

To [[customizing_amazon_product_displays_on_wordpress | customize the appearance of the Amazon products]] displayed by the plugin, such as the width and color of the "buy" button to match Amazon's yellow color <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>:
1.  Go to the "Customize" section of your WordPress theme <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
2.  Introduce custom CSS code where it says "Additional CSS" <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. This code will be provided in the video description or comments <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
Using Amazon's familiar yellow color for the buy button can increase user confidence <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.