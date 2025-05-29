---
title: Technological infrastructure of payment systems
videoId: akO8qAx4xjY
---

From: [[acquiredfm]] <br/> 

The evolution of payment systems has been a long and complex journey, moving from physical exchanges to sophisticated digital networks. Visa, alongside Mastercard, has played a pivotal role in developing the underlying [[Technological Innovations in Payment Systems | technological innovations]] that enable global commerce today <a class="yt-timestamp" data-t="00:01:00">[01:00:00]</a>.

## Early Payment Methods: Cash and Checks

Historically, transferring money was challenging. The primary options were cash or checks <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>. Checks, while functional, presented several issues:
*   **Discounted Value** Before the Federal Reserve's creation in the 1910s, parties cashing checks didn't receive the full face value due to costs associated with mailing and travel <a class="yt-timestamp" data-t="01:19:10">[01:19:10]</a>. This concept of a "discount" due to expense and risk in processing checks was an early form of transaction fees <a class="yt-timestamp" data-t="01:54:02">[01:54:02]</a>.
*   **Slow Processing** In the 1800s and early 1900s, checks traveled by methods like the Pony Express, making transactions incredibly slow <a class="yt-timestamp" data-t="01:22:20">[01:22:20]</a>.
*   **Manual Settlement** Banks would manually reconcile individual checks, a "crazy system of individual couriers" <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>. A centralized Automated Clearing House (ACH) for checks wasn't developed in the US until the 1970s <a class="yt-timestamp" data-t="01:30:08">[01:30:08]</a>.

Merchants and customers often resorted to credit accounts or charge accounts to manage payments for regular customers <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. These were initially ledger-based, evolving into cards usable across brand branches (e.g., Standard Oil's unsolicited cards in 1939) <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

## The Birth of BankAmericard and Early Infrastructure

When Bank of America launched BankAmericard in 1958, it marked the first time a bank entered the charge card market at scale <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. Initially, the system was "closed-loop," meaning all transaction parties (consumer, merchant, and their banks) were Bank of America customers <a class="yt-timestamp" data-t="01:46:50">[01:46:50]</a>. There was no distinction between issuing and merchant (acquiring) banks within their system <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

With the expansion of BankAmericard licenses to other banks across the country in 1966, the system transitioned to an "open-loop" model, necessitating a new [[Technological Innovations in Payment Systems | network]] and operational services for transaction settlement, known as interchange <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a> <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.

Initially, this involved banks manually mailing "sales drafts" (effectively invoices) to other banks to collect funds, charging a discount fee for the service, similar to early check processing <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. This process was "ludicrously expensive" and "chaos" <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.

## Visa's Core Technological Innovations

Dee Hock, the founder of Visa, envisioned a "transcendental organization" linking diverse institutions globally <a class="yt-timestamp" data-t="01:09:17">[01:09:17]</a>. He recognized that the "necessary technology had been discovered" <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>, but it needed to be built and implemented. Visa's transformation from a fragmented, manual system to a global digital network relied on three major technological pieces:

### 1. Transaction Authorization: BASE

Prior to digital authorization, merchants used "floor limits." Transactions below a certain amount ($50-$100) were approved at the cashier's discretion, accepting a certain amount of fraud <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>. Above the limit, the cashier would call their merchant bank, which would then call the cardholder's issuing bank to verify credit <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>. This process took up to 20 minutes and didn't work outside business hours <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>.

In 1971, Dee Hock initiated the BankAmericard Authorization System Experimental (BASE) project to automate this <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. After initial attempts at joint ventures and RFPs failed, Visa decided to build it in-house <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. This involved:
*   Building a nationwide and then worldwide telecom network <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.
*   Installing computer systems in member banks <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.
*   Establishing a new centralized data center for Visa in San Mateo, California (Sano campus), which remains its headquarters today <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a> <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.
*   Innovating [[Cloud infrastructure and enterprise enablement | data center infrastructure]]: Visa's team pioneered running concurrent, shared operations across multiple data centers, a practice that became industry standard <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.

This project, completed in nine months, created Visanet, eliminating bank-to-bank phone calls for authorizations <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a> <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.

### 2. Settlement Digitization: BASE II (Automated Clearing House)

The next challenge was automating transaction settlement, which still involved extensive paper and manual processes <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. Visa built its own internal Automated Clearing House (ACH) system, known as BASE II, for electronic settlement <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. This development occurred concurrently with the Federal Reserve building its own ACH system for checks in San Francisco during the 1970s <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

BASE II, also completed in less than a year, reduced average settlement times from a week to overnight batch processing <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>. This saved banks approximately $15 million in labor and postage costs in its first year <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>.

### 3. Point of Sale Digitization

The final step was to digitize the point of transaction itself, requiring both machine-readable cards and digital point-of-sale (POS) terminals <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
*   **Magnetic Stripe** Visa standardized on the magnetic stripe technology for cards <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.
*   **POS Terminals** Visa issued specifications for POS terminals, leading to companies like Verifone mass-producing inexpensive devices <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>. To incentivize adoption, Visa offered merchants a discount on transaction fees for digital transactions <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.
*   **Network Expansion** Visa also built a telecom network to connect all merchants globally. For its pilot program in the 1980s, Visa famously rented unused network capacity from CompuServe (an early internet service provider) during off-peak hours to send digital transactions <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.

This full digitization significantly reduced fraud, cutting chargebacks by 82% during the pilot phase <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>.

## The Modern Payment Landscape

With these technological foundations, Visa transformed into a fully digital entity with "essentially zero marginal cost" <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>. Today, Visa processes $14 trillion in volume annually, with over 190 billion transactions, equating to 8,600 transactions per second <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a> <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. It boasts 99.999% uptime across its six global data centers, a testament to its robust [[Cloud infrastructure and enterprise enablement | cloud infrastructure and enterprise enablement]] <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a> <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.

Key aspects of the modern system:
*   **Authorization Flow** The process remains largely the same: merchant runs card, checks with their bank, which checks with Visanet, which checks with the issuer's bank, and the response flows back, all within milliseconds <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.
*   **Data Minimization** The transaction payload size remains "infinitesimally small," a legacy of its 1970s architecture <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>. Visa itself doesn't store personal identity information (e.g., social security numbers), only card numbers, as banks prefer to control customer data <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a> <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.
*   **Tokenization** Technologies like Apple Pay utilize tokenization, where a unique token representing the card is sent instead of the actual card number. This enhances security and allows for new proprietary services <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. Visa now has more digital tokens than card credentials on its network <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

Despite the complexities and the ongoing debate around interchange fees, the [[Evolution of the Payments Landscape | technological infrastructure of payment systems]] built by Visa and its partners has been instrumental in enabling the scale of modern commerce, particularly e-commerce <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.