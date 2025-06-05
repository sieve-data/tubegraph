---
title: Introduction to Stripe Payments and 3D Secure
videoId: 1XKRxeo9414
---

From: [[fireship]] <br/> 

2019 was a significant year for online payment handling, particularly due to the rollout of strong customer authentication by banks in the EU starting in September <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This means EU customers might need to log into their bank's website to authorize a payment before it's processed <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This process is commonly known as [[handling_3d_secure_authentication_for_eu_customers | 3D Secure authentication]] <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

Stripe offers two main strategies for accepting one-time payments that are fully compatible with the 3D Secure process <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>:
1.  [[using_stripe_checkout_for_onetime_payments | Stripe Checkout]] <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>: An easier option with limited customization, requiring zero backend code for implementation <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
2.  [[using_payment_intents_api_with_stripe_elements | Stripe Elements with the Payment Intents API]] <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>: A more complex approach that offers full control over the payment flow and user experience <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

To get started with either method, a Stripe account is required, along with a Node.js backend (such as Firebase Cloud Functions) <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## [[using_stripe_checkout_for_onetime_payments | Using Stripe Checkout]]

[[using_stripe_checkout_for_onetime_payments | Stripe Checkout]] is an easy way to accept payments, handling the entire UI coding, credit card validation, and payment processing within its own checkout page <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. It also handles the [[handling_3d_secure_authentication_for_eu_customers | 3D Secure authentication]] process for European customers <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. If a user doesn't complete the authentication, the payment won't go through <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

After a payment is complete, Stripe can redirect the user to a specified success URL, including the session ID for retrieval <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. A separate URL can be set for unsuccessful or canceled payments <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Fulfilling Purchases with Webhooks

To programmatically fulfill a purchase after receiving a payment, Stripe Checkout utilizes webhooks <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. When the checkout process is successful, Stripe sends a webhook with data to a backend server <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This requires a server accessible over HTTP, such as Firebase Cloud Functions <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. The webhook data contains information about the payment intent, which can be used to update a database or send emails to the user <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### Client-Only Integration

The easiest way to use [[using_stripe_checkout_for_onetime_payments | Stripe Checkout]] is with a client-only integration, which requires creating product details and SKUs in the Stripe dashboard <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. A limitation of this approach is that pricing is static and cannot be calculated dynamically <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. For dynamic pricing or discounts, generating checkout sessions on a server is necessary <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

To implement:
*   **Stripe SDK Initialization**: Include `stripe.js` via a script tag in the HTML head to ensure the latest version and allow background fraud detection <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Initialize the Stripe SDK with the publishable key from the Stripe dashboard <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Redirect to Checkout**: Use `stripe.redirectToCheckout` within an async function to initiate the checkout process <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. This function takes multiple items, quantities, and redirect URLs for success and cancellation <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Amount Handling**: Amounts in Stripe are based on the currency's lowest denomination (e.g., cents for USD), so amounts displayed in the frontend UI should be divided by 100 <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### Backend Setup for Webhooks

For a full-stack payment solution with webhooks:
1.  **Initialize Firebase Cloud Functions**: Use `firebase init functions` (TypeScript recommended) <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
2.  **Install Dependencies**: Install `express`, `cors`, and the `stripe` SDK, along with their TypeScript types <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
3.  **Initialize Stripe SDK on Backend**: Import and initialize Stripe with the secret API key (ideally stored as an environment variable) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
4.  **Create Webhook Endpoint**: Set up an Express.js POST endpoint for the webhook <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
5.  **Validate Webhook Signature**: To ensure [[security_measures_in_frontend_and_backend | security]], validate that the webhook originated from Stripe by checking the `stripe-signature` header and using `stripe.webhooks.constructEvent` with an endpoint secret <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. The endpoint secret is obtained when creating a new webhook in the Stripe dashboard <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
6.  **Handle Event Types**: Use a switch statement to handle different webhook types (e.g., `payment_intent.succeeded` or `payment_intent.payment_failed`) to implement business logic like updating a database or sending emails <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

## [[using_payment_intents_api_with_stripe_elements | Using Payment Intents API with Stripe Elements]]

While [[using_stripe_checkout_for_onetime_payments | Stripe Checkout]] offers limited customization, [[using_payment_intents_api_with_stripe_elements | the Payment Intents API combined with Stripe Elements]] provides full control over the user experience and handles the [[handling_3d_secure_authentication_for_eu_customers | 3D Secure authentication]] process directly within the app's page, so the user never leaves the application <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

Here are the five steps involved in this approach:
1.  **Create a Payment Intent on the Backend**: When a user signals an intention to pay, make a request to your backend to create a Payment Intent object using the Stripe SDK <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. This intent takes an amount, currency, and optional parameters <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
2.  **Request the Payment Intent on the Frontend**: Make a request to the backend endpoint to retrieve the Payment Intent object <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. The returned Payment Intent contains an important value called the `client_secret` <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
3.  **Collect User Credit Card Information**: Stripe Elements provides pre-built widgets to validate credit card details on the frontend. Mount the Stripe card element onto a DOM element in your application <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
4.  **Process the Payment**: Call `stripe.handleCardPayment` on the frontend, passing the `client_secret` received from the backend and the card element where the user entered their details <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. This function processes the payment on Stripe's servers and returns an updated Payment Intent <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
5.  **Fulfill the Purchase**: Once the payment is processed, show a confirmation to the user in the UI <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. The purchase should then be fulfilled by running a webhook, similar to the process used with [[using_stripe_checkout_for_onetime_payments | Stripe Checkout]] <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.