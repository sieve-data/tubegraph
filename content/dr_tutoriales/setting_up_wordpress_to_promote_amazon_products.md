---
title: Setting up WordPress to promote Amazon products
videoId: EtOxBh6IodY
---

From: [[dr_tutoriales]] <br/> 

This article outlines how to set up WordPress to promote Amazon products using a free plugin, bypassing the typical requirement for an Amazon API code, which is usually needed after achieving three affiliate sales <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This method allows users to display Amazon products without needing the API <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Installing the Plugin

To begin, navigate to your WordPress page <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>:
1.  Go to the "Plugins" section in the left-hand menu <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
2.  Click "Add New" <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
3.  Search for "Amazon Philip" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
4.  Download and install the "Droxypin and Affiliation Weed Amazon" plugin <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This is a free plugin and does not require the API <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
5.  After installation, click "Activate" <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Configuring the Plugin

Once activated, the plugin will appear in your left-hand WordPress menu <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### Amazon ID Settings

1.  Go to the "Amazon" section within the plugin's settings <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
2.  Enter your Amazon Affiliate ID (also known as a Tracking ID) to ensure that product purchases are assigned to your account <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
3.  Enter the country you are from <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
    *   **How to find your Amazon Affiliate ID:** Visit the Amazon Associates page, go to "Account Settings" <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, and then "Manage Tracking IDs" <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. You can manage multiple tracking IDs for different web pages or product categories <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### General Settings

Navigate to the "General" section of the plugin settings <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
1.  **Products per page:** You can specify how many products are shown per page <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. For example, eight products are recommended to avoid saturating the page <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
2.  **Dropdown options:** Options for dropdowns are typically for the Pro version <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
3.  **Buy button text:** You can customize the text for the "Buy" button <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. While it defaults to English, you can change it to "Buy," "Buy it now," or any other desired text <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. Using a clear, concise message like "BUY" in capital letters can encourage direct sales <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
4.  After making changes, click "Save settings" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. Most other advanced changes are for the Pro version of the plugin <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

## Promoting Amazon Products with Shortcodes

The plugin uses specific codes (shortcodes) to display products on your WordPress site.

### 1. Product Search Bar

This shortcode allows users to search for Amazon products directly on your website:
*   **Shortcode:** `[wpas_search]` <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>
*   **Functionality:** Displays an Amazon search bar <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. When a user types a product (e.g., "Samsung tablet"), a dropdown menu appears showing relevant Amazon products <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. The number of products displayed will match the "products per page" setting (e.g., eight) <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   **Benefits:** Directly links to Amazon with your affiliate ID <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### 2. Automatic Product Promotion

This shortcode allows Amazon to automatically display products based on algorithms (e.g., Google's) that predict user interest.
*   **Shortcode:** `[wpas_show_products]` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
*   **Functionality:** Automatically displays products that are highly sold or well-recommended on Amazon <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Consideration:** You don't choose which specific products are shown <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This can be good, but it might show products unrelated to your website's niche (e.g., books on a technology review site) <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

### 3. Displaying Specific Products by ASIN

This shortcode allows you to display individual Amazon products using their ASIN (Amazon Standard Identification Number) code.
*   **Shortcode:** `[wpas_products]` followed by the ASIN <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   **Functionality:** Displays a specific product chosen by you <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **How to find ASIN:** The ASIN code is usually found in the URL of the Amazon product page (e.g., `B08J72...`) <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>, <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
*   **Example:** If the ASIN is `B08J72`, the shortcode would be `[wpas_products B08J72]` <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

### 4. Displaying Multiple Specific Products by ASIN

You can display multiple products in a row by using the same `[wpas_products]` shortcode and separating the ASINs with commas. This creates a powerful scrolling display of products <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
*   **Shortcode Example:** `[wpas_products ASIN1,ASIN2,ASIN3]` <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>
*   **Benefit:** Allows users to browse through many products you are recommending <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

### 5. Displaying Products by Keyword

This shortcode allows you to display products based on specific keywords.
*   **Shortcode:** `[wpas_keyword]` followed by the keyword <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
*   **Functionality:** Displays products from Amazon related to the entered keyword <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
*   **Important:** If your keyword has spaces, replace them with a plus (`+`) symbol (e.g., "cheap+tablets") <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Example:** `[wpas_keyword cheap+tablets]` <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
*   **Benefit:** Useful for displaying a range of products relevant to a broader topic <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

## Customizing Product Display with CSS

To customize the appearance of the product displays, such as the width and the "Buy" button color, you can add custom CSS.
1.  Go to the "Customize" section of your WordPress site <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
2.  Add the provided CSS code (usually found in the video description or first comment) to the "Additional CSS" section <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
3.  **Benefit:** Customizing the button color to Amazon's familiar yellow can build trust and encourage purchases <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

This [[installing_amazon_affiliate_plugin_without_api_for_wordpress | method provides a comprehensive way to promote Amazon products]] on a WordPress site, offering various display options and customization, without needing the API, making it a great [[benefits_of_amazon_affiliate_marketing | benefit for new Amazon affiliates]].
For more information on [[creating_an_amazon_affiliates_account | creating an Amazon affiliates account]] or [[creating_amazon_affiliate_links | creating Amazon affiliate links]], refer to other resources. For [[how_to_use_social_media_for_amazon_affiliates | using social media for Amazon affiliates]], [[customizing_product_display_on_wordpress | customizing product display on WordPress]], [[using_amazon_web_bar_for_affiliate_links | using the Amazon Web Bar for affiliate links]], or other [[wordpress_plugins_for_amazon_affiliates | WordPress plugins for Amazon affiliates]], explore related tutorials. Overall, this is a very effective way of [[using_amazon_affiliate_plugins_to_make_money | using Amazon affiliate plugins to make money]].