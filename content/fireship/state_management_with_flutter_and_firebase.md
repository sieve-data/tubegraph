---
title: State management with Flutter and Firebase
videoId: vFxk_KJCqgk
---

From: [[fireship]] <br/> 

Building interactive applications presents the challenge of [[Advanced data management techniques in Flutter apps | controlling the flow of data]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. While Flutter and Firebase offer tools for reactive, real-time data, effective [[Managing state in Flutter applications | state management]] remains complex <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This article explores patterns for apps with complex data flow needs, particularly when integrated with Firebase authentication <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The `provider` library can significantly reduce code complexity <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Core Principles for [[flutter_state_management_strategies | State Management]]

When approaching [[flutter_state_management_strategies | state management]] in Flutter and Firebase, several values are prioritized:
*   **Separation of Concerns**: Business logic should be distinct from presentation logic, avoiding data retrieval logic embedded within the widget tree <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Easy Data Sharing**: Data, such as a Firebase user, should be easily accessible throughout the widget tree without manually listening to streams in multiple stateful widgets <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **Avoiding Boilerplate**: Solutions should minimize extensive configuration, favoring simple conventions <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## The `provider` Package

The `provider` package for Flutter excels at meeting these needs <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. It serves as "syntactic sugar" for `InheritedWidget` and other low-level Flutter building blocks like `StreamBuilder` and `ChangeNotifier` <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. `provider` allows you to expose a value or a stream, making it accessible to any descendant widgets <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. This capability leads to profound benefits, especially when composing multiple streams, such as a Firebase user with related database data <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

## Challenges with Firebase Streams (Manual Approach)

Firebase exposes streams for both user authentication and Firestore data <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Manually managing these streams in a stateful widget can be painful <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>:
*   **Boilerplate**: Significant code is required to set up the stateful widget, stream subscription, and data properties <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   **Resource Management**: Stream subscriptions must be manually disposed of in the `dispose` lifecycle hook to prevent memory leaks and unnecessary costs <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Lack of Type Safety**: Data from the database is often dynamic (e.g., a map), requiring manual checks and risking runtime failures if the expected type is not present <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

## Improving with `StreamBuilder`

A significant improvement can be made by refactoring stream management into a `StreamBuilder` <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   `StreamBuilder` allows using a stateless widget and automatically subscribes to and cancels streams <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   It provides access to stream data within its `builder` function <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   However, type safety on the data payload is still absent, often requiring default values with `??` <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   When multiple streams are needed, especially if one depends on another (e.g., Firestore data depending on the current user), it can lead to nested `StreamBuilder`s or complex stream mapping <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   [[Local vs global state in Flutter | Deeply nested widgets]] requiring this data would still necessitate manual property passing, a problem known as "prop drilling" <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

## `provider` Solution for Firebase Streams

`provider` offers a solution similar to how themes are used in Flutter: data is set up at one point and then looked up the widget tree by its type <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Root-level Setup with `MultiProvider`

To share multiple streams or values, `MultiProvider` is used to wrap the `MaterialApp` at the root of the application <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. This avoids nested widgets <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

A `StreamProvider` can be set up to observe the current Firebase user throughout the application <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. It is typed to the `FirebaseUser` type and provided with the user authentication stream <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### Accessing Data Throughout the App

The key benefit is that the `FirebaseUser` can be treated as if it were a synchronous value anywhere in the app <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   Within a stateless widget's `build` method, the user can be accessed directly using `Provider.of<FirebaseUser>(context)` <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   This single line of code replaces the need for a `StreamBuilder` or manual stream setup <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
*   The application automatically reacts to user login/logout events, as widgets dependent on the user from the provider will re-render <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   Dart 2.3 features like conditional logic and spread syntax can be used directly in widget lists for concise conditional UI display based on user login status <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

## [[Deserializing Firebase data in Flutter | Deserializing Firebase Data]]

Firestore always returns data as a `Map`, which lacks type safety in Dart <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

### The Solution: Data Models

To address this, define Dart classes that represent the shape of your data <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Benefits**:
    *   Provides Intellisense when working with data models <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
    *   Ensures appropriate defaults and correct data types <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
    *   Creates a single source of truth for data management <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
*   **`fromMap` Constructor**: A constructor like `fromMap` takes the map from Firestore (or other JSON sources) and assigns its values to class properties, allowing for default values using `??` <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **`fromFirestore` Constructor**: A more specialized constructor like `fromFirestore` can take a `DocumentSnapshot`, providing access to the document ID, which isn't automatically included in the return data <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. This specialization, however, limits its use to only Firestore documents <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   The data model's structure should match the Firestore schema <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

## Database Service for Business Logic

To further separate concerns, define a stateless Dart class (e.g., `DatabaseService`) solely responsible for retrieving and deserializing items from the database <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   This service exposes methods that return typed data <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   For a single document, a method can reference a collection and document ID, then return a typed instance (e.g., `Superhero`) using its `fromMap` constructor on the snapshot data <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
*   To listen to a document as a real-time stream, the `map` operator on the stream is used to transform the snapshot into a typed instance <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   For lists (e.g., a query for weapon documents), the service maps each item in the returned list of snapshots to its corresponding typed instance (e.g., `Weapon`) <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   This approach keeps all business logic related to database interactions outside the widget tree <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

## Combining `provider` with Database Service

The true power of `provider` becomes apparent when combined with a database service <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   The currently authenticated user, readily available from `provider`, can be easily passed as an argument to the database service to create user-related streams (e.g., a hero document tied to a user ID) <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   A `StreamProvider` can be used elsewhere in the widget tree to expose these typed streams <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
*   This is especially useful for apps broken down into many small UI components, allowing data to be consumed across multiple widgets without manual property passing or creating additional `StreamBuilder`s or subscriptions <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. The data is simply "there and ready for you to use" <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.