---
title: Using the Provider Package in Flutter
videoId: vFxk_KJCqgk
---

From: [[fireship]] <br/> 

One of the most challenging aspects of [[building_mobile_app_components_with_flutter | building an interactive app]] is controlling the flow of data <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. While Flutter and Firebase offer tools for reactive, real-time data, effective [[state_management_with_flutter_and_firebase | state management]] remains a common debate among developers <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The Provider library can significantly reduce code complexity for apps with complex data flow needs, especially when dealing with Firebase authentication <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Challenges with Data Flow in Flutter and Firebase

Working with Firebase and Flutter presents several challenges, particularly concerning streams for user authentication and Firestore data <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>:

*   **Boilerplate Code**: Manually managing streams in `StatefulWidget`s requires substantial boilerplate, including setting up stream subscriptions and disposing of them in the `dispose` lifecycle hook <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>, <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Lack of Type Safety**: Firestore returns data as dynamic maps <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. If the database returns null or unexpected data types, widgets expecting specific types (e.g., a `Text` widget expecting a string) will fail at runtime due to Dart's strict type checking <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **Nested StreamBuilders**: When multiple streams are needed simultaneously, or when one stream depends on another (e.g., Firestore document reads depending on the authenticated user), it often leads to deeply nested `StreamBuilder` widgets <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   **Prop Drilling**: Accessing data from deeply nested widgets typically requires passing properties down through all intermediate children, leading to cumbersome "prop drilling" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

## Desired Values for State Management

When choosing a [[state_management_with_flutter_and_firebase | state management]] solution, key values include <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>:

*   **Separation of Concerns**: A clear distinction between business logic (data retrieval) and presentation logic (UI display) <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Business logic should not be embedded directly in the widget tree <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Easy Data Sharing**: The ability to easily share data throughout the widget tree, avoiding manual stream listening in multiple `StatefulWidget`s <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **Avoid Boilerplate**: Solutions that minimize configuration and prioritize simple conventions <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## How Provider Solves These Problems

The Provider package for Flutter excels at meeting these needs <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. It acts as syntactic sugar for `InheritedWidget` and other low-level Flutter building blocks like `StreamBuilder` and `ChangeNotifier` <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. It allows you to expose a value or stream and then access that value in any descendant widget <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

### Setting Up Provider for Authentication

To observe the current user throughout the application, especially with Firebase authentication <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>:

1.  **MultiProvider**: Wrap the root of your application (e.g., `MaterialApp`) in a `MultiProvider`. This is convenient for setting up and sharing multiple streams or values without nesting widgets <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
2.  **StreamProvider**: Set up a `StreamProvider` typed to `FirebaseUser` and pass it the stream containing the authentication data <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
3.  **Accessing User Data**: Within any stateless widget, you can access the user directly inside the `build` method by calling `Provider.of<FirebaseUser>(context)` <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. This allows treating the `FirebaseUser` as if it were a synchronous value <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
4.  **Conditional UI**: Determine if the user is logged in by checking if the user object is null <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. Dart 2.3 allows using conditional logic directly in widget lists (e.g., using the spread syntax for partial lists) to render different UI based on login status <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

```dart
// Example using MultiProvider
MultiProvider(
  providers: [
    StreamProvider<FirebaseUser>.value(
      stream: FirebaseAuth.instance.onAuthStateChanged,
    ),
    // ... other providers
  ],
  child: MaterialApp(
    // ...
  ),
);

// Accessing user in a widget
class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final user = Provider.of<FirebaseUser>(context);
    if (user != null) {
      return Text('Welcome, ${user.displayName}');
    } else {
      return Text('Please log in');
    }
  }
}
```

This setup provides a fully functioning authentication system where the app automatically reacts to user login/logout events without manual `StreamBuilder`s <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

### Handling Firestore Data with Provider

While user authentication is straightforward, Firestore data, returned as dynamic maps, requires additional handling to ensure type safety <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

#### Data Models (Dart Classes)

To deserialize Firestore data into actual Dart classes:

1.  **Define Classes**: Create immutable Dart classes that define the shape of your data (e.g., `Superhero`, `Weapon`) <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
2.  **Benefits**:
    *   **Intellisense**: Provides code completion when working with data models <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
    *   **Type Safety**: Ensures appropriate default values and data types, preventing runtime failures <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
    *   **Single Source of Truth**: Centralizes data schema management <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
3.  **Constructors**:
    *   `fromMap` constructor: Takes a map (e.g., from Firestore or JSON) and sets properties on the class, optionally using `??` to set default values <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
    *   `fromFirestore` constructor: A more specialized constructor that takes a `DocumentSnapshot`, providing access to the document ID which isn't automatically included in the return data <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

#### Database Service

Create a plain, stateless Dart class responsible for the business logic of retrieving and deserializing items from the database <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

*   **Methods for Data Retrieval**:
    *   **Single Document**: Expose methods that return a typed instance of your data model (e.g., `getSuperhero` returns `Superhero`) <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
    *   **Streams**: Use the `map` operator on a Firestore stream to map the snapshot data to an instance of your custom class (e.g., `Stream<Superhero>`) <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
    *   **Collections (Lists)**: For lists of documents, map each item in the list of snapshots down to the desired instance (e.g., `Stream<List<Weapon>>`) <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **Separation**: This service keeps all database-related business logic out of the widget tree <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. It can also handle database writes <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

### Combining Streams with Provider

With the database service and data models set up, Provider's true power emerges <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

*   **Related Streams**: The authenticated user, already accessible via Provider, can be easily used to create related streams by passing the user ID as an argument to your database service methods <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   **Distributed StreamProviders**: You can use `StreamProvider` elsewhere in the widget tree, which is highly beneficial for apps broken into many small UI components <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **Simplified Data Access**: Data can be used in all these widgets without manual property passing or creating additional `StreamBuilder`s or subscriptions <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. The data is simply available.

By leveraging Provider, developers can build robust and maintainable Flutter applications with complex data flows, especially when integrated with Firebase.