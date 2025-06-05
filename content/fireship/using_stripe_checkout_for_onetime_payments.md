---
title: Using Stripe Checkout for Onetime Payments
videoId: 1XKRxeo9414
---

From: [[fireship]] <br/> 

2019 marked a significant year for online payments, as banks in the EU began implementing strong customer authentication (SCA) in September <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This requires EU customers to authorize payments by logging into their bank's website <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Stripe offers two strategies for accepting payments, both fully compatible with this [[handling_3d_secure_authentication_for_eu_customers | 3D Secure]] process <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This article focuses on handling one-time payments using Stripe Checkout <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Stripe Checkout Overview

Stripe Checkout is presented as an easy way to get paid for one-time payments <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
It offers several key benefits:
*   **Zero Back-End Code** It can be implemented with zero back-end code for basic functionality <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   **Limited Customization** While easy, it has limited options for customization <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Fully Handled by Stripe** Stripe handles the entire checkout UI, credit card validation, and payment processing <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   **[[handling_3d_secure_authentication_for_eu_customers | 3D Secure]] Compatible** It automatically handles the [[handling_3d_secure_authentication_for_eu_customers | 3D Secure]] authentication process for customers in Europe, ensuring payments only go through if authorized by the user's bank <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **Redirects** Upon payment completion, Stripe can redirect the user to a specified success URL (including a session ID), or to a separate URL for unsuccessful payments or cancellations <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

## Fulfilling Purchases with Webhooks

After receiving a payment, you need to fulfill the purchase <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. While manual fulfillment via the Stripe dashboard is an option, programmatic fulfillment is achieved using webhooks <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. When the checkout process is successfully completed, Stripe sends a webhook with data to your back-end server <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This server needs to be accessible via HTTP, making Firebase Cloud Functions a suitable use case <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. The webhook data, specifically the payment intent, can then be used to update your database or send emails to the user <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

## Setting up Stripe Checkout (Client-Only Integration)

For a simple use case, a client-only integration of Stripe Checkout can be used <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Prerequisites
*   **Stripe Account**: You'll need a Stripe account <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Node.js Backend**: Some form of Node.js backend (e.g., Firebase Cloud Functions) is needed for webhooks <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   **API Keys**: In the Stripe dashboard, ensure development mode is active. Your publishable key is safe for front-end use, but the secret key must *never* be used in front-end code <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Steps for Client-Only Integration

1.  **Create Product & SKU**: Go to the Stripe dashboard's products tab to create details for the product you want to sell, and then add a SKU <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This approach has a limitation: pricing is static and based on values entered in the dashboard <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. For dynamic pricing or per-user discounts, generating checkout sessions on a server is required <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
2.  **Include Stripe.js**: Instead of NPM, include a script tag for `stripe.js` in your `index.html` file (e.g., in the `<head>`) <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. This ensures you always have the latest version and allows Stripe to perform background fraud detection <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
3.  **Initialize Stripe SDK**: In your front-end component (e.g., a Svelte product component), initialize the Stripe SDK by passing your publishable key <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. This key identifies your Stripe account <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
    *   *Note on Amounts*: When working with amounts in Stripe, they are based on a currency's lowest denomination (e.g., 1999 for $19.99 USD). You'll likely divide by 100 for display in your UI <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
4.  **Redirect to Checkout**: Set up an async function to call `stripe.redirectToCheckout` <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
    *   You can add multiple `items` to the checkout process and set quantities <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   Specify `success_url` and `cancel_url` for redirects <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
    *   Handle potential errors if Stripe cannot redirect the user <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
5.  **Trigger UI**: Create a UI element, such as a button, that fires this async function when clicked <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
6.  **Verify Payments**: Once a payment is submitted, you can see it on the Stripe dashboard to process refunds, view risk evaluations, and download invoices <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

## Backend Webhook Setup

To programmatically fulfill purchases, you'll need a backend to receive Stripe webhooks.

1.  **Initialize Backend Project**: Initialize your backend project (e.g., `firebase init functions` for Firebase Cloud Functions) <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
2.  **Install Dependencies**: Install necessary packages like Express.js, CORS, and the Stripe SDK, along with their TypeScript types for intellisense <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
3.  **Initialize Stripe SDK on Backend**: Import and initialize the Stripe SDK by passing your secret API key. It's recommended to store this as an environment variable (e.g., in your Firebase project) rather than hard-coding it <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
4.  **Create Webhook Endpoint**: Create an Express.js POST endpoint for your webhook (e.g., `/payments/webhook`) <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
5.  **Validate Webhook**: Crucially, validate that the webhook originated from Stripe using the `stripe-signature` header and an endpoint secret <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. The Stripe SDK's `webhooks.constructEvent` method can be used for this <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
6.  **Create Webhook in Stripe Dashboard**: Go to the Stripe dashboard to create a new webhook <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
    *   Set the URL to your deployed Firebase function (e.g., `your-main-functions-url/payments/webhook`) <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
    *   Select `payment_intent.succeeded` as the event to listen to, and optionally `payment_intent.payment_failed` <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
    *   After creation, grab the secret code for this webhook and store it as a Firebase environment variable <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
7.  **Implement Logic**: Use a switch statement to handle different webhook event types <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. For `payment_intent.succeeded`, you would typically update a Firestore database or send a confirmation email <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. For `payment_intent.payment_failed`, you might notify the customer about an open invoice <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

## Custom Payments with Payment Intents API and Stripe Elements

While Stripe Checkout is simple, its main drawback is limited customization for the user experience <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. For full control over the payment flow, including handling [[handling_3d_secure_authentication_for_eu_customers | 3D Secure authentication]] within your app, the [[using_payment_intents_api_with_stripe_elements | Payment Intents API]] combined with [[using_payment_intents_api_with_stripe_elements | Stripe Elements]] is a more complex but flexible approach <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. This allows users to enter card details directly in your app, with Stripe automatically prompting for [[handling_3d_secure_authentication_for_eu_customers | 3D Secure]] if needed, without leaving your application <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.