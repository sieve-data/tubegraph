---
title: Customizing Amazon Product Displays on WordPress
videoId: EtOxBh6IodY
---

From: [[dr_tutoriales]] <br/> 

This article details how to [[advertising_amazon_products_with_wordpress_plugins | advertise Amazon products]] on a WordPress website, focusing on [[installing_amazon_affiliate_plugins_on_wordpress_without_api | installing and using a free plugin]] that doesn't require the Amazon API code, which typically needs three affiliate sales to obtain <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. The tutorial explains how to display products in various customizable ways to facilitate [[generating_commissions_from_amazon_affiliates | generating commissions from Amazon affiliates]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Plugin Installation and Setup

To begin, navigate to your WordPress dashboard <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
1.  Go to the "Plugins" section on the left menu <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
2.  Click "Add New" <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
3.  Search for "Amazon Philip" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
4.  Download and install the "Droxypin and Affiliation Weed Amazon" plugin <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This is a free plugin that doesn't require the API <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
5.  After installation, click "Activate" <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

Once activated, the plugin will appear in the left menu <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### Configuring Your Amazon Affiliate ID

To ensure sales are assigned to your account, you must enter your Amazon Affiliate ID <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
1.  Go to the "Amazon" section within the newly installed plugin settings <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
2.  Enter your Amazon ID and select your country <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

If you don't know your ID:
*   Go to your Amazon page <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   Navigate to "Account settings" <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   Select "Manage IDs follow up" <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. Here, you can enter multiple [[using_keywords_and_tracking_ids_for_amazon_affiliate_marketing | Tracking IDs]] for different web pages or product categories <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. This helps in [[using_keywords_and_tracking_ids_for_amazon_affiliate_marketing | tracking product performance]] <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

## General Display Settings

Within the plugin's "General" settings, you can customize various characteristics of how [[advertising_amazon_products_with_wordpress_plugins | Amazon products are advertised]] <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **Initial Products Shown**: This allows you to edit how many initial products are displayed <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Products Per Page**: You can set the number of products to show per page, for example, eight <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The goal is not to saturate the viewer <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **"Buy" Button Text**: By default, the button text appears in English. You can change it to "Buy," "Buy it now," "Subscribe," or any other desired text <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. Using a clear and concise message like "BUY" is recommended for direct sales <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

Many other advanced customization options are available in the Pro version <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Remember to save settings after making changes <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

## Displaying Products with Shortcodes

The plugin uses specific shortcodes to promote Amazon products on your WordPress site <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. These shortcodes allow for different display functionalities without needing an API <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### 1. Amazon Product Search Bar
This shortcode allows users to search for Amazon products directly on your website <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Shortcode**: `[WPAS_Search]` <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>
*   **Functionality**: When implemented, it creates a search bar. Users can type a product name (e.g., "Samsung tablet"), and a dropdown menu will appear displaying relevant Amazon products <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. The number of products displayed will adhere to your "products per page" setting <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Clicking on a product redirects directly to Amazon with your affiliate ID <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### 2. Automated Product Display
This shortcode allows Amazon to automatically display products based on its algorithms, factoring in sales volume, recommendations, and perceived user interest <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Shortcode**: `[WPAS_Products_Auto]` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
*   **Functionality**: Products like speakers or phone holders might appear <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. While this generates affiliate commissions, you do not choose which products are shown <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This can be beneficial but might show products unrelated to your website's niche <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

### 3. Specific Product Display using ASIN
This method involves displaying specific Amazon products using their ASIN (Amazon Standard Identification Number) code <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. This is useful for [[optimizing_amazon_product_promotion_for_increased_sales | optimizing Amazon product promotion]] by showcasing specific products.
*   **Shortcode (Single Product)**: `[WPAS_Products product_id="ASIN_CODE"]` <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
*   **Finding ASIN**: The ASIN code is usually found in the product's URL on Amazon or under product details <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. For example, for an iPad, the ASIN might look like `B08J72...` <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
*   **Shortcode (Multiple Products)**: You can display multiple products in a dropdown format by separating their ASIN codes with commas <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
    *   Example: `[WPAS_Products product_id="ASIN1,ASIN2,ASIN3"]` <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>
*   **Functionality**: This allows you to curate product displays, such as a list of "best eight for less than a hundred euros" <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. When a user clicks, they are directed to Amazon with your [[using_amazon_affiliate_account | Amazon affiliate ID]] <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This creates a powerful browsing experience where users can view many products vertically <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

### 4. Keyword-Based Product Display
This shortcode allows you to display products based on specific keywords <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. This is another method for [[optimizing_amazon_product_promotion_for_increased_sales | optimizing Amazon product promotion]].
*   **Shortcode**: `[WPAS_Products_Keyword keyword="your+keyword"]` <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>
*   **Keyword Formatting**: If your keyword has a space (e.g., "cheap tablets"), replace the space with a plus symbol (`+`) <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. For example, "cheap tablets" becomes "cheap+tablets" <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
*   **Functionality**: This will display a selection of products from Amazon that match the specified keyword <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. The number of products displayed will align with your configured settings <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.

## Styling and Appearance with Additional CSS

To customize the visual style of your Amazon product displays, such as changing the "Buy" button color and width, you can use additional CSS <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.
1.  Go to "Customize" in your WordPress dashboard <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
2.  Find the "Additional CSS" section <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
3.  Paste the provided CSS code (usually found in the video description or comments) into this section <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. This allows you to match Amazon's familiar yellow "Buy" button color, which can inspire more confidence in buyers compared to other colors like green <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

This customization ensures that your [[advertising_amazon_products_with_wordpress_plugins | advertised Amazon products]] align with your desired aesthetic and potentially [[optimizing_amazon_product_promotion_for_increased_sales | optimize sales]] <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.