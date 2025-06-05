---
title: Building a peertopeer video chat app
videoId: WmR9IMUD_CY
---

From: [[fireship]] <br/> 

[[introduction_to_webrtc | WebRTC]] is an API that enables real-time exchange of audio and video streams directly between browsers, entirely within the browser itself <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It's ideal for creating video conferencing applications that allow users to establish a peer-to-peer connection without needing a third-party server or native app for media transmission <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## How WebRTC Works

The process involves two main phases: [[signaling_process_and_stp_in_webrtc | signaling]] and [[signaling_process_and_stp_in_webrtc | Interactive Connectivity Establishment (ICE)]].

### Signaling Process

The [[signaling_process_and_stp_in_webrtc | signaling]] process facilitates the secure exchange of connection data between two parties without ever touching the actual media being transmitted <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

1.  **Offer Creation**: The first peer creates an "offer" to connect to another peer <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This generates an Session Description Protocol (SDP) object, which describes the peer-to-peer connection, including details like video codec and timing <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
2.  **Data Exchange**: This SDP data is saved to a server where the second peer can read it <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
3.  **Answer Creation**: The second peer responds by creating an SDP "answer" and also writes it to the server <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Interactive Connectivity Establishment (ICE)

Most devices operate behind firewalls and dynamic IP addresses due to Network Address Translation (NAT), which complicates direct peer-to-peer connections <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. [[signaling_process_and_stp_in_webrtc | ICE]] is a standard that helps clients find their public-facing IP addresses <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

1.  **ICE Candidate Generation**: Both peers generate a list of ICE candidates, which are IP address and port pairs that can be used to connect <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
2.  **STUN Server Interaction**: [[introduction_to_webrtc | WebRTC]] uses STUN (Session Traversal Utilities for NAT) servers to discover these public IP addresses <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Free STUN server options are available from reliable sources like Google <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
3.  **Candidate Exchange**: Each peer saves their ICE candidates in a database for the other peer to read <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
4.  **Connection Establishment**: An algorithm automatically determines the best candidate pair, at which point real-time media can begin flowing between the peers <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Building the App with Vanilla JavaScript and Firebase

A peer-to-peer video calling app can be built using vanilla JavaScript and [[setting_up_firebase_for_signaling_in_video_chat_apps | Firebase]] as the [[signaling_process_and_stp_in_webrtc | signaling]] server <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. [[setting_up_firebase_for_signaling_in_video_chat_apps | Firebase]] is a suitable choice because it simplifies real-time database updates compared to traditional databases requiring WebSockets <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

### Initial Setup

1.  **Project Initialization**: Start a vanilla JavaScript project, for example, using `Vite` (`npm init vite@latest` for a simple build tool) <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
2.  **[[setting_up_firebase_for_signaling_in_video_chat_apps | Firebase]] Installation**: Install [[setting_up_firebase_for_signaling_in_video_chat_apps | Firebase]] which provides the Firestore database for the backend [[signaling_process_and_stp_in_webrtc | signaling]] server <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
3.  **Firestore Configuration**: Initialize Firestore in test mode from the [[setting_up_firebase_for_signaling_in_video_chat_apps | Firebase]] console, then create a web project and obtain its credentials to initialize the [[setting_up_firebase_for_signaling_in_video_chat_apps | Firebase]] app in `main.js` <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

### Global State Management

Key global state variables include:
*   **`RTCPeerConnection`**: This object manages the [[introduction_to_webrtc | WebRTC]] negotiation process, emitting events for database updates and media stream additions <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. It uses STUN servers (like Google's free options) to generate ICE candidates <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **`localStream`**: The video stream from the local user's webcam <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   **`remoteStream`**: The video stream from the remote user's webcam <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

HTML elements for video feeds and UI buttons are accessed using imperative DOM APIs like `document.getElementById` <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

### Managing Media Streams

1.  **Accessing Webcam**: A button click event handler uses `navigator.mediaDevices.getUserMedia({ video: true, audio: true })` to get permission and access the user's webcam, resolving to a `MediaStream` object for `localStream` <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. The `remoteStream` is initially an empty `MediaStream` <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
2.  **Adding Tracks to Peer Connection**: Tracks from the `localStream` are added to the `RTCPeerConnection` using `peerConnection.addTrack()` <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
3.  **Listening for Remote Tracks**: The `RTCPeerConnection`'s `ontrack` event is listened to, and incoming tracks are added to the `remoteStream` <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
4.  **Displaying Video Feeds**: Both `localStream` and `remoteStream` are applied to their respective video elements in the DOM by setting their `srcObject` property <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

### Signaling with Firestore

The `RTCPeerConnection` handles the complex peer-to-peer networking, while the majority of the developer's work involves [[signaling_process_and_stp_in_webrtc | signaling]] data between users via Firestore <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

#### Creating an Offer

1.  **Call Document**: A "call" document in Firestore manages the offer and answer <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. Sub-collections for `offerCandidates` and `answerCandidates` store ICE candidates <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
2.  **Generate Offer**: The `peerConnection.createOffer()` method is awaited to get an offer description <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
3.  **Set Local Description**: This offer is set as the local description on the peer connection using `peerConnection.setLocalDescription()` <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This action automatically starts generating ICE candidates <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
4.  **Save SDP**: The SDP value from the offer description is converted to a plain JavaScript object and saved to the call document in Firestore <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
5.  **Listen for ICE Candidates (Offer Side)**: An `onicecandidate` event listener is set up on the peer connection. When a candidate is generated, its data is written as JSON to the `offerCandidates` sub-collection in Firestore <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
6.  **Listen for Answer**: The caller listens to changes on their call document in Firestore using `onSnapshot` to receive the answer from the remote user <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. If an answer exists and a remote description isn't already set, it's set as the remote description on the local peer connection <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
7.  **Listen for ICE Candidates (Answer Side)**: The caller also listens to updates on the `answerCandidates` collection. New documents added to this collection (representing remote ICE candidates) are created as local ICE candidates and added to the peer connection <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

#### Answering a Call

1.  **Reference Call Document**: The answering user references the same call document in Firestore using the unique ID generated by the caller <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
2.  **Listen for ICE Candidates (Answer Side)**: An `onicecandidate` event listener is set up on the answering peer connection to write generated candidates to the `answerCandidates` collection <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
3.  **Fetch Offer Data**: The call document is fetched from the database to retrieve the offer data <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
4.  **Set Remote Description**: The retrieved offer data is used to set the remote description on the answering peer connection <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
5.  **Generate and Set Local Answer**: An answer is generated locally using `peerConnection.createAnswer()` and then set as the local description <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
6.  **Update Call Document**: This answer is converted to a plain object and updated on the call document in Firestore, making it available for the calling user <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
7.  **Listen for ICE Candidates (Offer Side)**: The answering peer also listens to the `offerCandidates` collection. Newly added offer ICE candidates are created locally and added to the peer connection <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

This [[signaling_process_and_stp_in_webrtc | signaling]] process, combined with [[introduction_to_webrtc | WebRTC]]'s handling of peer-to-peer networking and media streaming, provides the foundation for a real-time video chat feature <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.