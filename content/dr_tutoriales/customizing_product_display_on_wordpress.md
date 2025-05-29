---
title: Customizing product display on WordPress
videoId: EtOxBh6IodY
---

From: [[dr_tutoriales]] <br/> 

This article describes how to [[installing_amazon_affiliate_plugin_without_api_for_wordpress | install a plugin]] and use it in WordPress to advertise Amazon products without needing the Amazon API code <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The API code is typically required after three affiliate sales <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This method allows users to make money with Amazon affiliates even without those initial sales <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Plugin Installation and Basic Setup

To begin [[setting_up_wordpress_to_promote_amazon_products | promoting Amazon products]] on a WordPress website, navigate to the "Plugins" section in the left menu and select "Add New" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Search for "Amazon Philip" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, and download the plugin called "Droxypin and Affiliation Weed Amazon" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This free plugin does not require the API <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. After downloading, click "Activate" <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Configuring Amazon ID

Once activated, a new section for the plugin appears in the left menu <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
1.  Go to the "Amazon" section within the plugin settings <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
2.  Enter your Amazon ID and select your country <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. This ensures that any purchased products are assigned to your affiliate account <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
3.  To find your Amazon ID, go to your Amazon affiliate page and navigate to "Account settings" <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
4.  Within "Account settings," select "manage IDs follow up" <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. Here, you can enter or find various tracking IDs for different web pages or product categories <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### General Settings

Under the "General" section of the plugin settings, you can edit certain characteristics of the Amazon products being advertised <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **Initial Products Displayed**: You can specify how many initial products are shown <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Products per Page**: Determine the number of products to display per page (e.g., eight) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. The goal is not to saturate the viewer <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **Buy Button Text**: Customize the text on the "buy" button <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. While the default is in English, you can change it to "buy it now," "buy," or any other desired text <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

After making changes, click "Save settings" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Displaying Amazon Products with Codes

The plugin uses specific codes to display products on your WordPress site <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

### 1. Amazon Search Bar (WPAS\_Search)

This code creates a search bar on your website, allowing visitors to search for Amazon products <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Code**: `[WPAS_Search]` <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>
*   **Functionality**: When a product (e.g., "Samsung tablet") is entered into the search bar, a dropdown menu appears with Amazon products matching the search, along with reviews <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. Purchases made through these links will be linked to your affiliate ID <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
*   **Display**: The number of products appearing (e.g., eight) is determined by the general settings <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

### 2. Automated Product Display (WPAS\_Product)

This code allows Amazon to automatically display products based on its algorithms and Google's algorithms <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Code**: `[WPAS_Product]` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
*   **Functionality**: It shows products that are highly sold or well-recommended on Amazon, believing they will interest your visitors <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Consideration**: While you earn a commission if a product is purchased, you do not choose which products are shown <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This means unrelated products (e.g., books, water bottles) might appear on a themed website (e.g., technology) <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

### 3. Specific Product Display (WPAS\_Products with ASIN)

This is a powerful option for displaying specific products by using their ASIN (Amazon Standard Identification Number) code <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   **Code**: `[WPAS_Products asin="ASIN_CODE_HERE"]` <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>
*   **Finding ASIN**: The ASIN code is typically found in the URL of the Amazon product page (e.g., `B08J72...`) <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Implementation**: Copy the ASIN code from Amazon and paste it into the shortcode on your WordPress page <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. This will display the chosen product, promoted with your affiliate ID <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   **Multiple Products**: To display several products in a row, include multiple ASIN codes separated by commas within the same shortcode <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
    *   **Example**: `[WPAS_Products asin="ASIN1,ASIN2,ASIN3"]` <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>
    *   This creates a dropdown or inline display of selected products, allowing users to browse <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.

### 4. Keyword-based Product Display (WPAS\_Products with keywords)

This code allows you to display products based on specified keywords <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
*   **Code**: `[WPAS_Products keywords="KEYWORD_HERE"]` <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>
*   **Using Spaces**: If your keyword phrase includes spaces (e.g., "cheap tablets"), replace the spaces with a plus (+) symbol (e.g., "cheap+tablets") <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Functionality**: This will display Amazon products related to the entered keywords <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>. The number of products displayed will match what was set in the general settings <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.

## Customizing Button Style with CSS

To change the appearance of the "buy" button, such as its width or color, you can use Additional CSS <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
1.  Go to the "Customize" section in WordPress <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
2.  Navigate to "Additional CSS" <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
3.  Paste the provided CSS code into this section <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. This code will be made available in the video description or first comment <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
4.  Using the yellow color, like Amazon's, helps users feel familiar and builds confidence in the products <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

This comprehensive approach allows for flexible [[creating_amazon_affiliate_links | Amazon affiliate link creation]] and [[using_amazon_web_bar_for_affiliate_links | product display]] on your WordPress site, helping you to make money without needing the Amazon API.