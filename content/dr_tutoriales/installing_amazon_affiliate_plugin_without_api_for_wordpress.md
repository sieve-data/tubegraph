---
title: Installing Amazon affiliate plugin without API for WordPress
videoId: EtOxBh6IodY
---

From: [[dr_tutoriales]] <br/> 

This tutorial explains how to install and configure a free WordPress plugin to advertise Amazon products and [[using_amazon_affiliate_plugins_to_make_money | make money with affiliates]] without requiring the Amazon API code <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The Amazon API code is typically needed after making three affiliate sales <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This method bypasses that requirement <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Plugin Installation <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>

To begin, navigate to your WordPress dashboard <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>:

1.  Go to the "Plugins" section in the left-hand menu <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
2.  Click on "Add New" <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
3.  Search for "Amazon Philip" or specifically "Droxypin and Affiliation Weed Amazon" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
4.  Install the free plugin <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
5.  Once downloaded, click to "Activate" the plugin <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Plugin Configuration

After activation, a new menu item for the plugin will appear on the left <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### Amazon Settings <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>

1.  Navigate to the "Amazon" section within the plugin settings <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
2.  Enter your [[creating_an_amazon_affiliates_account | Amazon Affiliate ID]] so that sales are attributed to your account <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
3.  Select your country <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

    > If you don't know how to find your [[creating_an_amazon_affiliates_account | Amazon Affiliate ID]]:
    > 1.  Go to the Amazon page <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    > 2.  Access "Account settings" <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
    > 3.  Go to "Manage IDs" <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. Here you can find your existing IDs or create new ones for different websites or product categories <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### General Settings <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>

In the "General" section, you can customize how Amazon products are displayed <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>:

1.  **Initial Products Shown:** You can edit the number of initial products shown <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  **Products Per Page:** Configure how many products appear per page (e.g., eight products is recommended to avoid saturating the viewer) <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
3.  **Dropdown Options:** Most dropdown options are for the Pro version <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
4.  **Buy Button Text:** Change the default "Buy" button text to anything you prefer (e.g., "Buy Now," "Buy") <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. A clear, concise message in capital letters is suggested for direct sales <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
5.  **Save Settings:** Click "Save Settings" to apply your changes <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Promoting Products Using Codes <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>

The plugin uses specific codes to display Amazon products on your WordPress site. These codes are entered where you want the products to appear <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

### 1. Amazon Search Bar (WPAS\_Search) <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>

*   **Code:** `[wpas_search]` <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>
*   **Functionality:** This code displays a search bar on your website, allowing visitors to search for Amazon products directly from your page <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. When a user enters a product (e.g., "Samsung tablet"), a dropdown list of matching Amazon products with reviews will appear <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. If a product is purchased, your [[creating_an_amazon_affiliates_account | affiliate ID]] is automatically applied <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### 2. Automatic Product Recommendations (WPAS\_Popular) <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>

*   **Code:** `[wpas_popular]` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
*   **Functionality:** This code instructs Amazon to automatically display products based on its algorithms (e.g., Google's algorithms), showing items that are highly sold or well-recommended <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Consideration:** While you receive commission for purchases <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>, you do not control which specific products are shown <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This means a technology-themed website, for example, might display books or water bottles <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

### 3. Specific Product by [[using_asin_codes_for_amazon_affiliate_products | ASIN]] (WPAS\_Products) <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>

*   **Code:** `[wpas_products]` followed by the product's [[using_asin_codes_for_amazon_affiliate_products | ASIN]] code <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Functionality:** This allows you to display a specific Amazon product using its [[using_asin_codes_for_amazon_affiliate_products | ASIN]] code <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   **Finding the [[using_asin_codes_for_amazon_affiliate_products | ASIN]]:** The [[using_asin_codes_for_amazon_affiliate_products | ASIN]] code can be found in the product's URL on Amazon, typically starting with "B0" <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Multiple Products:** You can display multiple products in a row by separating their [[using_asin_codes_for_amazon_affiliate_products | ASIN]] codes with commas <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. This creates a powerful dropdown list of recommended products <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.

### 4. Products by Keyword (WPAS\_Products) <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>

*   **Code:** `[wpas_products keyword="your+keywords"]` <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>
*   **Functionality:** This code allows you to display products based on specific keywords <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.
*   **Important:** When using multiple words in a keyword, replace spaces with the "+" symbol (e.g., "cheap+tablets" for "cheap tablets") <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. The plugin will display products matching the keyword provided by Amazon <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. The number of products shown will match your settings in the general configuration <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.

## Customizing Product Display (CSS) <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>

To match the look and feel of Amazon and inspire trust, you can customize the appearance of the product displays, such as the width and the "Buy" button color <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

1.  Go to "Customize" in your WordPress dashboard <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
2.  Navigate to "Additional CSS" <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
3.  Paste the provided CSS code (usually found in the video description or comments) <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. This code will make the buy button yellow and adjust the width, making it more familiar to users who are accustomed to Amazon's visual style <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.