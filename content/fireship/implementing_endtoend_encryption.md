---
title: Implementing endtoend encryption
videoId: J5x3OMXjgMc
---

From: [[fireship]] <br/> 

[[implementing_cryptographic_concepts_in_blockchain_development | End-to-end encryption]] can be implemented in a decentralized chat application built with Gun.js <a class="yt-timestamp" data-t="01:12:56">[01:12:56]</a>. While it is possible to encrypt data, it requires a different mental model than traditional centralized systems <a class="yt-timestamp" data-t="03:04:95">[03:04:95]</a>.

## Mechanism

In the demonstrated chat application, [[implementing_cryptographic_concepts_in_blockchain_development | end-to-end encryption]] is implemented for message text <a class="yt-timestamp" data-t="09:02:96">[09:02:96]</a>. The value stored in the database is encrypted, and decryption requires the corresponding key <a class="yt-timestamp" data-t="09:05:85">[09:05:85]</a>.

To encrypt a message, the `SEA.encrypt` method is used, taking the message text and an encryption key as arguments <a class="yt-timestamp" data-t="10:09:47">[10:09:47]</a>. When querying messages, the same key used for encryption is applied to decrypt the messages for display in the UI <a class="yt-timestamp" data-t="09:13:67">[09:13:67]</a>, <a class="yt-timestamp" data-t="10:13:67">[10:13:67]</a>.

## Security Considerations

While the demo implements [[implementing_cryptographic_concepts_in_blockchain_development | end-to-end encryption]], it hardcodes the encryption key directly in the source code <a class="yt-timestamp" data-t="09:14:41">[09:14:41]</a>. This approach means the data is not truly secure, as anyone could find the key <a class="yt-timestamp" data-t="09:16:71">[09:16:71]</a>. For actual security, the encryption key should be a secret shared between the two communicating users to effectively encrypt and decrypt messages <a class="yt-timestamp" data-t="09:18:96">[09:18:96]</a>.