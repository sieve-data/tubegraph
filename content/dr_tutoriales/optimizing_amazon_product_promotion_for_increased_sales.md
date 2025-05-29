---
title: Optimizing Amazon Product Promotion for Increased Sales
videoId: EtOxBh6IodY
---

From: [[dr_tutoriales]] <br/> 

This guide details how to effectively [[Promoting products through websites and social media | promote Amazon products]] on a WordPress website, allowing users to [[generating_commissions_from_amazon_affiliates | make money]] through the [[Generating Revenue through Amazon Affiliate Program | Amazon Affiliates program]] without requiring an API key <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. An API key is typically needed after making three affiliate sales <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, but this method bypasses that requirement <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Plugin Installation and Setup

To begin [[advertising_amazon_products_with_wordpress_plugins | advertising Amazon products]] on your WordPress site:

1.  Navigate to your WordPress dashboard <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
2.  Go to the "Plugins" section on the left-hand menu and click "Add New" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
3.  In the search bar, look for "Amazon Philip" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
4.  Install the "Droxypin and Affiliation Weed Amazon" plugin <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This is a free and useful plugin <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
5.  After installation, click "Activate" <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Once activated, the plugin will appear in your left menu <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

## Plugin Configuration

### Amazon Settings

First, configure the Amazon settings to ensure sales are attributed correctly:

1.  Access the plugin's settings and go to the "Amazon" section <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
2.  Enter your Amazon Affiliate ID (also known as a [[Using Keywords and Tracking IDs for Amazon Affiliate Marketing | Tracking ID]]) so that all purchased products are assigned to your account <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
3.  Select your country <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
4.  To find your Amazon Affiliate ID: Log in to your Amazon affiliate page, go to "Account settings," then "Manage Tracking IDs" <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. You can use multiple [[Using Keywords and Tracking IDs for Amazon Affiliate Marketing | tracking IDs]] for different product categories or webpages <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### General Settings

Adjust these general settings for optimal display:

1.  Go to the "General" part of the plugin settings <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
2.  Specify the number of products to show per page <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. For example, setting it to eight is recommended to avoid saturating the page <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
3.  The dropdown options mentioned are typically for the Pro version of the plugin <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
4.  Customize the text for the "buy" button. While it defaults to English, you can change it to "Buy it now," "Buy," or any other desired call to action <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. A clear, concise message like "BUY" in capital letters can lead to more direct sales <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
5.  Most other advanced changes are for the Pro version <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
6.  Remember to "Save settings" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Methods for Displaying Amazon Products

The plugin provides several codes to [[customizing_amazon_product_displays_on_wordpress | display Amazon products]] on your website, each serving a different purpose:

### 1. Search Bar (`[wpas_search]`)

This code allows you to embed an Amazon search bar on your website <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Code**: `[wpas_search]` <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>
*   **Functionality**: When a user enters a product query (e.g., "Samsung tablet"), a dropdown will appear showing relevant Amazon products <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
*   **Benefit**: Users can directly search for products on your site, and any purchase made through these searches will be linked to your affiliate ID <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. The width of the search results can be adjusted based on your WordPress theme's sidebar settings <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### 2. Automatically Promoted Products (`[wpas_bestseller]`)

This code automatically displays Amazon products based on algorithms <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>, Google algorithms <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>, and popular sales/recommendations <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Code**: `[wpas_bestseller]` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
*   **Functionality**: Amazon promotes products it believes will interest your audience <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
*   **Consideration**: While you earn commission on purchases, you don't choose which specific products are displayed. This means a technology-focused page might show unrelated items like books or water bottles <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. It's useful but requires careful implementation <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### 3. Specific Products by ASIN Code (`[wpas_products number="ASIN_CODE"]`)

This is highly useful for promoting specific products that you choose <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   **Code**: `[wpas_products number="ASIN_CODE"]` <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>
*   **ASIN Code**: The ASIN (Amazon Standard Identification Number) is a unique 10-character alphanumeric identifier for products on Amazon. You can find it in the product's URL or details page <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. For example, for an iPad, the ASIN might appear as part of `B08J72...` in the URL <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
*   **Functionality**: Simply copy the ASIN and paste it into the shortcode <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **Benefit**: You have full control over the specific products promoted, ensuring relevance to your content <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Multiple Products**: You can display multiple products in a row by separating their ASINs with commas within the `number=""` attribute <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. This creates a dropdown-style display of chosen products <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.

### 4. Products by Keyword (`[wpas_products keyword="KEYWORD"]`)

This code allows you to display products based on a specified keyword or phrase <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
*   **Code**: `[wpas_products keyword="KEYWORD"]` <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>
*   **Keyword Formatting**: If your keyword phrase includes spaces (e.g., "cheap tablets"), replace the spaces with a plus sign (`+`) (e.g., `cheap+tablets`) <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Functionality**: The plugin will deploy products from Amazon that match the provided keyword <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.
*   **Benefit**: Useful for displaying a range of products related to a general topic on your website <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

## Customizing Product Display

To further [[customizing_amazon_product_displays_on_wordpress | optimize your product displays]] and improve user trust and engagement, you can customize the appearance:

*   **Button Styling**: You can change the "buy" button's color and width to match Amazon's familiar yellow style <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. This helps people feel more familiar and confident clicking on your products <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.
*   **Applying Custom CSS**: Go to "Customize" or "Personalize" in your WordPress theme settings. Locate the "Additional CSS" section <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. You can paste custom CSS code here (often provided by the plugin documentation or tutorials) to style the product displays, such as changing button colors or increasing product box width <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. A yellow "buy" button, similar to Amazon's, can inspire more confidence in users <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.

By following these steps, you can effectively [[creating_amazon_affiliate_links | create Amazon affiliate links]] and [[methods_for_obtaining_amazon_affiliate_links | promote Amazon products]] on your WordPress site, driving traffic to Amazon through your unique affiliate ID, and ultimately, [[generating_commissions_from_amazon_affiliates | generating commissions]] from sales. This approach leverages the [[benefits_of_amazon_affiliates_program | Amazon Affiliates program]] to [[Generating Revenue through Amazon Affiliate Program | generate revenue]] efficiently.