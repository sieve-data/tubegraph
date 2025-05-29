---
title: Using Amazon affiliate plugins to make money
videoId: EtOxBh6IodY
---

From: [[dr_tutoriales]] <br/> 

This article outlines how to install and configure a WordPress plugin to promote Amazon products and earn affiliate commissions, even without having the Amazon API code <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The Amazon API code typically requires three initial affiliate sales to be obtained <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## [[installing_amazon_affiliate_plugin_without_api_for_wordpress | Installing the Plugin]]

To begin [[setting_up_wordpress_to_promote_amazon_products | setting up WordPress to promote Amazon products]], you'll need to install a specific plugin:
1.  Navigate to your WordPress dashboard <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
2.  From the left-hand menu, go to the "Plugins" section <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
3.  Click on "Add New" <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
4.  In the search bar, look for "Amazon Philip" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
5.  Locate and download the "Droxypin and Affiliation Weed Amazon" plugin <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
6.  Install the plugin <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. It's a free plugin that doesn't require the Amazon API <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
7.  Once installed, click "Activate" <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. The plugin will then appear in your left-hand WordPress menu <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

## Plugin Configuration

### Amazon Settings
The first step in configuring the plugin is to input your Amazon Affiliate ID:
1.  From the left menu, select the newly installed plugin, then navigate to the "Amazon" section <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
2.  Enter your Amazon Affiliate ID and select your country <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>, <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This ensures that all sales generated are attributed to your account <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

#### Locating Your Amazon Affiliate ID
If you don't know your ID:
1.  Go to the Amazon Associates page <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
2.  Within your account settings, find and select "Manage Tracking IDs" <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
3.  Here, you can enter and manage multiple tracking IDs for different web pages or product categories, allowing for detailed sales tracking <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### General Settings
Next, adjust the general display characteristics of the Amazon products:
1.  Go to the "General" section of the plugin settings <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
2.  You can set the number of initial products to be displayed <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. For example, the presenter suggests eight products per page to avoid saturation <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
3.  The plugin offers "dropdown options" for the Pro version, which is not covered in this free tutorial <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
4.  Customize the text for the "buy" button. While the default is in English, you can change it to "Buy Now," "Buy," or any other desired call to action <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. The presenter recommends "Buy" in capital letters for a clear, direct message <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
5.  Most other advanced settings are part of the Pro version <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
6.  Remember to "Save settings" after making changes <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Promoting Amazon Products with Shortcodes

The plugin provides several shortcodes to display Amazon products on your WordPress site.

### 1. Search Bar (WPAS\_Search)
This shortcode creates an Amazon search bar on your website, allowing users to find products directly from your site <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Shortcode:** `[wpas_search]` <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>
*   **Functionality:** When a user searches for a product (e.g., "Samsung tablet"), a dropdown list of relevant Amazon products with reviews and ratings will appear <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. If a user buys a product through this search, the commission is linked to your affiliate ID <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### 2. Automatically Promoted Products (WPAS\_Popular)
This shortcode displays products that Amazon automatically promotes based on algorithms (Google's and Amazon's), focusing on well-sold and highly-rated items that might interest the user <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Shortcode:** `[wpas_popular]` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
*   **Functionality:** While this can display popular products and earn commissions, you do not choose which specific products are shown <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This means a technology-focused website might display books or water bottles, which may not align with its niche <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

### 3. Specific Product Display (WPAS\_Products)
This is considered very useful as it allows you to display specific products by their ASIN code <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   **Shortcode:** `[wpas_products number="YOUR_ASIN_CODE"]` <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
*   **ASIN Code:** The ASIN (Amazon Standard Identification Number) is a unique 10-character alphanumeric identifier for products on Amazon <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. You can find this code in the product's URL on Amazon's website <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Functionality:** By inputting a product's ASIN, you can precisely control which Amazon product is promoted on your page <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **Displaying Multiple Products:** You can display several specific products in a dropdown format by separating their ASIN codes with commas within the `[wpas_products]` shortcode <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. Example: `[wpas_products number="ASIN1,ASIN2,ASIN3"]` <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. This creates an organized, scrollable list of recommended products <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.

### 4. Keyword-Based Product Display (WPAS\_Keyword)
This shortcode allows you to display products based on specific keywords <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
*   **Shortcode:** `[wpas_keyword search="YOUR_KEYWORD"]`
*   **Functionality:** Instead of ASINs, you enter keywords (e.g., "tablets," "cheap tablets") <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>. The plugin will display relevant Amazon products based on those keywords <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.
*   **Spaces in Keywords:** If your keyword phrase contains spaces, replace them with a plus symbol (`+`) (e.g., "less+than+one+hundred+euros") <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.

## Customizing Product Display Style

To change the appearance of the "Buy" button (e.g., color and width) to match Amazon's familiar yellow style:
1.  Go to your WordPress **Customize** or **Personalize** section <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
2.  Locate "Additional CSS" <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
3.  Paste the provided CSS code (usually found in the video description or first comment) into this section <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. This helps create a familiar and trustworthy look for your Amazon product advertisements <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

By following these steps, you can effectively [[monetization_strategies_with_amazon_affiliates | monetize your website]] by promoting Amazon products using this free WordPress plugin, without needing the Amazon API <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This method allows for a range of display options, from dynamic search bars to curated product lists <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.