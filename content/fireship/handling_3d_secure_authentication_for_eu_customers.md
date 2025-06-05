---
title: Handling 3D Secure Authentication for EU Customers
videoId: 1XKRxeo9414
---

From: [[fireship]] <br/> 

Since September 2019, banks in the EU have been rolling out strong customer authentication (SCA) [00:00:06]. This means that customers in the EU may be required to log into their bank's website to authorize a payment before it can be processed [00:00:09]. This process is known as 3D Secure. This article explores two strategies for accepting payments with Stripe that are fully compatible with the 3D Secure process [00:00:20], leveraging either [[Using Stripe Checkout for Onetime Payments | Stripe Checkout]] or the [[Using APIs and Third Party Services | Payment Intents API]] combined with Stripe Elements.

## Strategy 1: Using Stripe Checkout

[[Using Stripe Checkout for Onetime Payments | Stripe Checkout]] offers a straightforward way to accept one-time payments with minimal backend code [00:00:32]. It has limited customization options but handles the entire payment flow and [[Security Measures in Frontend and Backend | security]] measures automatically [00:00:38].

### How Stripe Checkout Handles 3D Secure

When a user clicks a purchase button, it brings up the Stripe Checkout UI [00:01:07]. This checkout flow is entirely handled by Stripe, meaning you don't need to code any of the UI yourself [00:01:11]. Stripe validates the credit card, processes the payment, and automatically handles the 3D Secure authentication process for customers in Europe [00:01:14]. If the user does not complete the authentication process by signing into their bank and authorizing the charge, the payment will not go through [00:01:23].

### Client-Only Integration

For a client-only integration of Stripe Checkout, you create product details statically in the Stripe dashboard [00:03:03]. This approach has limitations as it cannot calculate pricing dynamically [00:03:08]. To enable the checkout process, you must include `stripe.js` in the head of your document, ensuring you always have the latest version and allowing Stripe to perform background fraud detection [00:03:51].

To initialize the Stripe SDK, you pass your publishable key (safe for frontend use) [00:04:12]. To redirect the user to checkout, use `stripe.redirectToCheckout` [00:04:31]. You can add multiple items and set quantities, and it's essential to define redirect URLs for successful and cancelled payments [00:04:37].

### Fulfilling Purchases with Webhooks

After a payment is received, you need to fulfill the purchase [00:01:46]. Stripe can send a webhook to your backend server upon successful completion of the checkout process [00:02:00]. This requires a server accessible over HTTP, which is a perfect use case for [[Using APIs and Third Party Services | Firebase Cloud Functions]] [00:02:10]. The webhook will contain data about the payment intent, allowing you to implement logic to update your database or send emails [00:02:18].

To set up a webhook:
*   Initialize [[Using APIs and Third Party Services | Firebase Cloud Functions]] and install necessary SDKs (Express.js, CORS, Stripe SDK) [00:06:08].
*   Initialize Stripe with your secret API key (preferably as an environment variable, not hard-coded) [00:06:40].
*   Create a POST endpoint for the webhook [00:07:20].
*   Validate the webhook by checking for a Stripe signature header and using an endpoint secret to decode the data [00:07:24]. The `webhooks.constructEvent` method in the Stripe SDK helps with this [00:07:41].
*   In the Stripe dashboard, create a new webhook, specifying your deployed [[Using APIs and Third Party Services | Firebase Cloud Function]] URL and listening for `payment_intent.succeeded` and `payment_intent.payment_failed` events [00:07:56].
*   Grab the secret code from the Stripe dashboard for this webhook and paste it into your [[Using APIs and Third Party Services | Firebase]] project [00:08:19].
*   Use a switch statement on the webhook type to implement your business logic, such as updating a Firestore database or sending customer emails [00:08:27].

## Strategy 2: Stripe Elements and Payment Intents API

While [[Using Stripe Checkout for Onetime Payments | Stripe Checkout]] is easy, it offers limited customization [00:08:58]. For full control over the payment flow and user experience, you can combine [[Using APIs and Third Party Services | Stripe Elements]] with the [[Using APIs and Third Party Services | Payment Intents API]] [00:09:06]. This approach also handles 3D Secure authentication if necessary, keeping the user within your app's page [00:09:11].

### How Stripe Elements Handles 3D Secure

With Stripe Elements, if a payment needs to go through 3D Secure, Stripe automatically brings up that process directly within your app's page [00:09:21]. This means the user never has to leave your application to complete their payment [00:09:25].

### Five Steps for Custom Payments

1.  **Create a Payment Intent on the Backend**: When a user signifies an intention to pay, make a request to your backend to create a `PaymentIntent` object using the Stripe SDK [00:09:40]. This object takes an amount, currency, and optional parameters [00:09:50].
2.  **Request Payment Intent on the Frontend**: Your frontend code (e.g., using a Svelte `onMount` hook) makes a request to this backend endpoint to get the `PaymentIntent` [00:09:56]. The response contains an important value called the `client_secret` [00:10:18].
3.  **Collect Credit Card Information**: [[Using APIs and Third Party Services | Stripe Elements]] provides pre-built widgets to validate credit card details on the frontend [00:10:29]. You grab a DOM element and mount the Stripe card element onto it [00:10:34].
4.  **Process the Payment**: This step happens entirely on Stripe's servers [00:10:42]. You call `stripe.handleCardPayment`, passing it the `client_secret` obtained from your server and the card element where the user entered their details [00:10:47]. The return value is an updated `PaymentIntent` with any charges added [00:10:57].
5.  **Fulfill the Purchase**: Once the payment intent is updated and the charge is created, you can show a confirmation in the UI [00:11:10]. The actual fulfillment of the purchase should be handled by running a webhook, similar to the process described for [[Using Stripe Checkout for Onetime Payments | Stripe Checkout]] [00:11:14].