---
title: Implementing GPS tracking and geolocation queries
videoId: MYHVyl-juUk
---

From: [[fireship]] <br/> 

Geolocation is a critical feature for many modern applications, exemplified by companies like Uber, which achieved a valuation of over 100 billion dollars with real-time geolocation at its core <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This article outlines how to build a real-time geolocation application with features such as device GPS tracking and real-time geolocation queries to a cloud database, using tools like [[Flutter]], [[Google Maps and Firestore for app development | Google Maps]], and [[Working with Firebase Firestore and realtime updates | Firestore]] <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Core Application Features

The demonstrated application allows users to:
*   Track their device's GPS location <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   Add new geolocation points to [[Working with Firebase Firestore and realtime updates | Firestore]] based on the device's current location <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   Query for "safe points" within a specified radius of a center point, often the user's device location <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   Update map markers in real-time by reacting to database events <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This enables multiple users to see the same real-time geolocation data updates, similar to how Uber displays drivers <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

The application's UI features a full-screen [[Google Maps and Firestore for app development | Google Map]], a slider to control the query radius, and a button to add new geo points <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Key Technologies and Dependencies

This application leverages the following:
*   [[Flutter]] for cross-platform app development <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   [[Google Maps and Firestore for app development | Google Maps]] for map rendering <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   [[Working with Firebase Firestore and realtime updates | Firebase Firestore]] for cloud data storage and [[RealTime Database Implementation | real-time updates]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   [[Managing geolocation data in Firestore with Geo Flutter Fire | Geo Flutter Fire]] library for powering geo queries <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   `location` plugin for device GPS tracking <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   `rxdart` for complex stream management <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Setup and Configuration

Before building the app, ensure:
*   `FlutterFire` is installed and configured in your project <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   A [[Google Maps and Firestore for app development | Google Maps]] API key is obtained from your Google Cloud Platform (GCP) project, which is automatically created with a [[Working with Firebase Firestore and realtime updates | Firebase]] project <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

#### Dependencies (`pubspec.yaml`)
Add the following to your `pubspec.yaml` file <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>:
*   `firebase_core`
*   `cloud_firestore`
*   `rxdart`
*   `geo_flutter_fire`
*   `location`
*   `google_maps_flutter` (Note: This package is very new and may have breaking changes <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>).

#### Android Configuration
*   **Permissions:** In `android/app/src/main/AndroidManifest.xml`, request location permission by adding `<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>` <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **API Key:** Add the Google Maps API key as metadata within the `<application>` tag <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

#### iOS Configuration
*   **API Key:** In `ios/Runner/AppDelegate.m`, add your Google Maps API key <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   **Permissions:** In `ios/Runner/Info.plist`, add key-value pairs to obtain user location permission <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

## Building the Map and UI

The application starts with a `MaterialScaffold` containing a `StatefulWidget` (e.g., `FireMapWidget`) that encapsulates all state and logic <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Responsive Map Layout
To create a full-screen, responsive map, use a `Stack` widget. This allows the [[Google Maps and Firestore for app development | Google Map]] to be at the bottom, with controls overlaid on top <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

```dart
Stack(
  children: [
    GoogleMap(...), // Map widget
    Positioned(...), // Controls like buttons or sliders
  ],
)
```

### GoogleMap Widget
The `GoogleMap` widget requires an `initialCameraPosition` with a `LatLng` target and a `zoom` level <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **`onMapCreated`:** This lifecycle hook is crucial for setting up the `mapController`, which enables interaction with the map, such as setting markers or zooming <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **`myLocationEnabled`:** Set to `true` to display the user's location on the map <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **`cameraTracking`:** Enable to continuously get the current center point of the camera <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

### Adding Markers to the Map
A `Positioned` widget can place a button (e.g., a `FlatButton` with an icon) in the bottom-right corner <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. When pressed, this button triggers an `addMarker` event handler.

The `addMarker` method creates a `Marker` object:
*   **`position`:** Obtained from the `mapController.cameraPosition` to place the marker at the map's center <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **`icon`:** Can be customized <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **`infoWindowText`:** Displayed when the user clicks the marker <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
Finally, `mapController.addMarker` adds the marker to the map <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## GPS Tracking: User's Location
The `location` plugin allows easy access to the user's GPS position, either as a `Future` or a `Stream` <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   Initialize an instance of `Location` <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **`animateToUser` method:** An asynchronous function that uses `await location.getLocation()` to get the current location and then `mapController.animateCamera` to move the map camera to the user's position <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. For [[RealTime Database Implementation | real-time updates]], `location.onLocationChanged` can be used <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## [[Managing geolocation data in Firestore with Geo Flutter Fire | Managing Geolocation Data in Firestore]] with Geo Flutter Fire

To store and query location data efficiently, [[Working with Firebase Firestore and realtime updates | Firestore]] documents will contain a `position` field. This field includes a `geoHash` and a `geoPoint` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. The [[Managing geolocation data in Firestore with Geo Flutter Fire | Geo Flutter Fire]] library automatically creates this structure, including the `geoHash` <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

### What is a GeoHash?
A `geoHash` is an algorithm that encodes a bounding box on the surface of a sphere (like Earth) into a string <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. This string is crucial for performing efficient geo-spatial queries within a certain radius in [[Working with Firebase Firestore and realtime updates | Firestore]] <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

### Adding Geo Points to Firestore
An `addGeoPoint` method is created to save location data to [[Working with Firebase Firestore and realtime updates | Firestore]] <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
1.  Get the user's current location using the `location` service <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
2.  Create a `GeoFirePoint` based on the latitude and longitude. A `GeoFirePoint` is a special data structure responsible for calculating the `geoHash` and distances between points <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
3.  Make a reference to the desired [[Working with Firebase Firestore and realtime updates | Firestore]] collection (e.g., `locations`) <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
4.  Add a new document to the collection, setting the `position` field to the `pointData` provided by `GeoFirePoint` <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

> **Tip:** When working on Android, you can send custom GPS locations to the emulator settings to simulate movement and test the app's real-time features <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

## Geolocation Queries and Real-time Updates

The application allows users to query for documents within a changeable radius, using a `BehaviorSubject` from `rxdart` to manage the radius value <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. A `Slider` widget allows the user to dynamically change this radius <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### Updating Markers Reactively
When the [[Working with Firebase Firestore and realtime updates | Firestore]] query emits changes, the entire list of documents is received <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. The application loops over these documents to update the markers on the map:
*   The `geolocation` data from the [[Working with Firebase Firestore and realtime updates | Firestore]] document is used for the marker's position <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   [[Managing geolocation data in Firestore with Geo Flutter Fire | Geo Flutter Fire]] can provide the actual distance of a point from the query's center, which can be displayed in the marker's info window <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### Setting Up the Geo Query
The geo query is dependent on two streams: the `radius` value and the [[Working with Firebase Firestore and realtime updates | Firestore]] documents within that radius <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
1.  **Initial Setup:** Get the user's current location to set the initial `GeoFirePoint` as the center of the query <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
2.  **`rxdart` `switchMap`:** Use `rx.switchMap` on the `radius` `BehaviorSubject`. This allows switching to a new observable stream of database documents whenever the radius changes <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
3.  **`geoFireCollection.within`:** This method performs the actual geo query:
    *   `center`: The `GeoFirePoint` representing the query's center <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
    *   `radius`: The current radius value <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
    *   `field`: The name of the document field containing the `geolocation` data (e.g., "position") <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
    *   `strictMode`: Recommended to ensure only points strictly within the radius are included, as geo hashes are square-shaped <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
4.  **Listen and Update:** Call `listen` on the resulting stream to receive document updates in real-time and trigger the `updateMarkers` method <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

### Managing Subscriptions
To prevent memory leaks, ensure that the `StreamSubscription` created by listening to the query is cancelled when the widget is disposed. This is done by overriding the `dispose` method in the `StatefulWidget` and calling `subscription.cancel()` <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

By combining these components, a full-featured [[Building realtime geolocation apps with Flutter | real-time geolocation app]] can be built in a remarkably short amount of time <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.