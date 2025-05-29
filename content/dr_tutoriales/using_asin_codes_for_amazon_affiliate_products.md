---
title: Using ASIN codes for Amazon affiliate products
videoId: EtOxBh6IodY
---

From: [[dr_tutoriales]] <br/> 

The ASIN (Amazon Standard Identification Number) code is a unique identifier for products sold on Amazon. When using specific [[WordPress Plugins for Amazon Affiliates | WordPress plugins]] for [[Amazon Affiliate Program Basics | Amazon affiliate marketing]], ASIN codes are crucial for directly promoting individual products on your website without requiring the Amazon API key <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This allows you to promote products and earn commissions even if you haven't yet achieved the three affiliate sales required to obtain an API code <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## How to Find ASIN Codes

The ASIN code for an [[amazon_affiliate_program_basics | Amazon]] product can be found in the product's URL <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. For example, in an Amazon product URL, you might see a segment like `B08J72XXXX` – this "B0" followed by numbers and letters is the ASIN code <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

## Promoting Products Using ASIN Codes

With the "Droxypin and Affiliation Weed Amazon" plugin installed on [[setting_up_wordpress_to_promote_amazon_products | WordPress]], you can use shortcodes with ASINs to display specific products <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Before displaying products, ensure your [[amazon_affiliate_program_basics | Amazon]] affiliate ID is entered in the plugin settings so that sales are assigned to your account <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Displaying a Single Product

To promote a single [[amazon_affiliate_program_basics | Amazon]] product, use the `WPAS_Products` shortcode followed by the product's ASIN code <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>:

```
[WPAS_Products ASIN_CODE_HERE]
```

Replace `ASIN_CODE_HERE` with the actual ASIN of the product you wish to display <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. When a user clicks on the product display, they will be redirected to Amazon with your [[amazon_affiliate_program_basics | affiliate ID]] embedded in the link <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

### Displaying Multiple Products as a Dropdown

You can also display multiple products in a dropdown list by using the same `WPAS_Products` shortcode and separating each ASIN code with a comma <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>:

```
[WPAS_Products ASIN_CODE_1, ASIN_CODE_2, ASIN_CODE_3]
```

This method is highly useful for creating comprehensive product lists or recommendations, allowing visitors to easily browse through multiple items you are recommending <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.

### Customizing Product Display

The plugin allows for customization of product display elements, such as the number of products shown per page (e.g., eight products per page) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>, and the text on the "buy" button (e.g., "Buy" instead of "Buy Now") <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. The visual style, including the color of the buy button and product display width, can be further customized by adding custom CSS code within your [[setting_up_wordpress_to_promote_amazon_products | WordPress]] theme's "Additional CSS" section <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. This ensures the product display aligns with your website's design and creates a familiar experience for users, like Amazon's characteristic yellow button <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.