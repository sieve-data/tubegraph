---
title: Using Payment Intents API with Stripe Elements
videoId: 1XKRxeo9414
---

From: [[fireship]] <br/> 

While [[using_stripe_checkout_for_onetime_payments | Stripe Checkout]] offers a straightforward way to process payments with minimal backend code, it provides limited options for customizing the user experience <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. For greater control over the payment flow and user interface, developers can combine the Payment Intents API with Stripe Elements <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This approach also seamlessly handles the [[introduction_to_stripe_payments_and_3d_secure | 3D Secure]] authentication process when necessary, ensuring the user remains within your application's page <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

## Prerequisites
To get started with Stripe payments, you will need:
*   A Stripe account <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   A Node.js backend, such as [[flutter_app_integration_with_firebase | Firebase Cloud Functions]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## How it Works
This method involves more code compared to [[using_stripe_checkout_for_onetime_payments | Stripe Checkout]] <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. The payment process occurs within your application's page, where users enter their card details. If [[introduction_to_stripe_payments_and_3d_secure | 3D Secure]] is required (e.g., for EU customers), Stripe automatically initiates the authentication process, allowing the user to complete it without leaving your app <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

The implementation can be broken down into five key steps:

### 1. Create a Payment Intent on the Backend
When a user indicates an intention to pay, your frontend makes a request to your backend to create a `PaymentIntent` object <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. This object is created using the Stripe SDK on your backend and typically requires an amount and currency, along with other optional parameters <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

```typescript
// Example backend code (conceptual)
// Initialize Stripe with your secret key (ideally from environment variables)
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

// Endpoint to create a Payment Intent
app.post('/create-payment-intent', async (req, res) => {
  const { amount, currency } = req.body;
  try {
    const paymentIntent = await stripe.paymentIntents.create({
      amount: amount, // in cents/lowest denomination
      currency: currency,
      // Add other optional parameters as needed
    });
    res.json({ clientSecret: paymentIntent.client_secret });
  } catch (e) {
    res.status(500).send({ error: e.message });
  }
});
```

### 2. Initialize Stripe SDK and Fetch Client Secret
On the frontend, you initialize the Stripe SDK by including `stripe.js` in your HTML document <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. It's recommended to include `stripe.js` via a script tag in the head of your `index.html` to ensure you always have the latest version and allow Stripe to perform background fraud detection <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

After initializing the Stripe SDK with your publishable key <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>, you'll make a request to your backend endpoint to obtain the `client_secret` for the `PaymentIntent` <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. This `client_secret` is crucial for client-side operations. It's important to create only one `PaymentIntent` per user session <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

```javascript
// Example frontend code (conceptual, Svelte in video)
import { onMount } from 'svelte';
import { writable } from 'svelte/store';

const paymentIntent = writable(null);
let stripe;

onMount(async () => {
  stripe = Stripe('YOUR_PUBLISHABLE_KEY'); // Initialize Stripe with your publishable key

  const response = await fetch('/create-payment-intent', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ amount: 1999, currency: 'usd' }), // Example amount
  });
  const data = await response.json();
  paymentIntent.set(data.clientSecret);
});
```

### 3. Collect Credit Card Information with Stripe Elements
Stripe Elements provides pre-built, customizable UI components that securely collect credit card details and validate them on the frontend <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. You can mount these elements onto a DOM element in your application <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

```javascript
// Example frontend code (conceptual)
let cardElement; // Reference to the Stripe Card Element

onMount(() => {
  const elements = stripe.elements();
  cardElement = elements.create('card');
  cardElement.mount('#card-element'); // Mounts the card element to a div with id 'card-element'
});
```

### 4. Process the Payment on Stripe's Server
Once the user has entered their card details, you call `stripe.handleCardPayment()` on the frontend <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. This method takes the `client_secret` obtained from your backend and the card element containing the user's details <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. The actual payment processing occurs on Stripe's servers, not your own <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

This function returns an updated `PaymentIntent` object with any charges added <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. If [[introduction_to_stripe_payments_and_3d_secure | 3D Secure]] authentication is required, Stripe will automatically display the necessary prompt to the user <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

```javascript
// Example frontend code (conceptual)
async function handleSubmit() {
  const { paymentIntent, error } = await stripe.handleCardPayment(
    $paymentIntent, // The client_secret from the paymentIntent store
    {
      payment_method_data: {
        card: cardElement,
      },
    }
  );

  if (error) {
    // Show error to your customer (e.g., insufficient funds)
    console.error(error.message);
  } else if (paymentIntent.status === 'succeeded') {
    // Payment succeeded!
    console.log('Payment succeeded:', paymentIntent);
    // You can show a confirmation in the UI here <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>
  }
}
```

### 5. Fulfill the Purchase with a Webhook
After the payment succeeds, you should fulfill the purchase by using a webhook <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. Stripe can send a webhook to a URL you specify (e.g., an [[flutter_app_integration_with_firebase | Firebase Cloud Function]]) when the `payment_intent.succeeded` event occurs <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. Your backend function will receive this webhook, validate its authenticity using the Stripe signature header and endpoint secret <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>, and then implement logic to update your database, send an email, or deliver the product <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

You can set up webhooks in the Stripe dashboard, specifying the URL of your backend and the events you want to listen for, such as `payment_intent.succeeded` or `payment_intent.payment_failed` <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

This comprehensive approach provides full control over the user experience and is essential for dynamic pricing, discounts, or complex payment flows that require a high degree of customization <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.