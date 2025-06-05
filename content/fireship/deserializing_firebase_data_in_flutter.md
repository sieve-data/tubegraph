---
title: Deserializing Firebase data in Flutter
videoId: vFxk_KJCqgk
---

From: [[fireship]] <br/> 

When [[flutter_app_integration_with_firebase | integrating Flutter apps with Firebase]], one of the challenges is managing the flow of data, particularly when dealing with [[using_firebase_databases_and_data_modeling_techniques | Firebase databases]] like Firestore <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Firestore always returns data as a map, which can lead to issues with type safety and runtime errors in Dart <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

## The Problem with Dynamic Maps

Directly using dynamic maps from Firestore within the widget tree presents several problems:
*   **No Type Safety** Data accessed from a map using bracket notation (e.g., `data['title']`) is dynamic <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. If the database returns `null` or an unexpected type, the widget (like a `Text` widget expecting a string) will fail because Dart performs runtime type checking <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   **Boilerplate** Manually managing stream subscriptions in stateful widgets adds significant boilerplate code for initialization, data updates with `setState`, and disposal <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Lack of Intellisense** Dynamic maps don't provide intellisense, making development less efficient and more error-prone <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

While a `StreamBuilder` widget can help by automatically subscribing and unsubscribing from streams, it still doesn't provide type safety for the data payload <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Developers often use null-aware operators (e.g., `??`) to provide default values and ensure proper types <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Solution: Data Models (Classes)

To address the lack of type safety and improve code quality, it's recommended to define Dart classes that explicitly represent the shape of your data <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

### Benefits of Data Models
*   **Intellisense**: Provides auto-completion and type hints when working with data objects <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Type Safety**: Ensures that appropriate default values and data types are used, preventing runtime errors <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   **Single Source of Truth**: Establishes a clear schema for your data that matches what's in Firestore <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

### Creating Constructors for Deserialization
Data models should include constructors to deserialize data from a map or a Firestore document snapshot.

*   **`fromMap` Constructor**: This constructor takes a `Map` as an argument and sets the values as properties on the class <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. It's flexible, allowing deserialization from regular JSON or other data sources <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. Null-aware operators (`??`) can be used to set default values <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

*   **`fromFirestore` Constructor**: A more specialized constructor can take a `DocumentSnapshot` as an argument <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. This allows access to the document ID, which isn't automatically included in the return data of a map <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. However, this makes the constructor less versatile for non-Firestore data sources <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

## Database Service Layer

To further improve code organization and separation of concerns, it's recommended to define a dedicated database service class <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This class is responsible for the business logic of retrieving items from the database and deserializing them into the appropriate Dart classes <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

Key characteristics of a database service:
*   **Stateless**: The class itself should be stateless <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Expose Methods**: It should focus on exposing methods that return typed data <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Stream Mapping**: For real-time data streams, the `.map` operator can be used on a stream to convert raw snapshots into instances of your data models <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. This means that instead of a dynamic map, your widgets receive a strongly-typed class instance <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   **Centralized Logic**: This approach pulls all business logic related to working with the database out of your widget tree <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

### Example: Retrieving a Single Document
To get a single hero document typed to a `Superhero` class, the service can make a reference to the collection with a document ID and then return a `Superhero` instance using its `fromMap` constructor with the snapshot data <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. For a real-time stream, the `map` operator can be used to convert the stream of snapshots to a stream of `Superhero` instances <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

### Example: Retrieving a List of Documents
For a list of documents (e.g., weapon documents), the process involves mapping a list of snapshots, then mapping each individual item in that list down to the desired `Weapon` instance <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

This structured approach to [[data_modeling_in_firestore_chat_applications | data modeling]] and deserialization makes working with data in your widgets much more user-friendly, providing intellisense and confidence in data types at runtime <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

## Sharing Deserialized Data

Once data is properly deserialized into typed Dart objects by the database service, it can be easily shared throughout the widget tree using state management solutions. For example, the Provider package allows you to expose these typed streams and then access the values in any descendant widget as if they were synchronous values, without needing additional `StreamBuilder` widgets or manual subscriptions <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. This is particularly useful when composing multiple streams, such as a Firebase user with related data from the database <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.