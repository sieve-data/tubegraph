---
title: Using Google Maps and Firestore for app development
videoId: MYHVyl-juUk
---

From: [[fireship]] <br/> 

Geolocation is a critical feature in modern applications, exemplified by companies like Uber, which relies on real-time geolocation queries and device GPS tracking for its core functionality <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This article outlines how to build such features using [[flutter_app_integration_with_firebase | Flutter]], [[creating_responsive_uis_with_flutter_and_google_maps | Google Maps]], and [[working_with_firebase_firestore_and_realtime_updates | Firestore]], often with less than 200 lines of code <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

The [[building_realtime_geolocation_apps_with_flutter | building realtime geolocation apps with Flutter]] capabilities discussed here are significantly powered by the [[managing_geolocation_data_in_firestore_with_geo_flutter_fire | Geo Flutter Fire]] library, authored by Darshan Goda, which handles geo queries <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Core Application Features

A demonstration application built with these technologies includes:
*   **Device GPS Tracking**: The ability to track the user's current location <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Real-time Geolocation Queries**: Querying a cloud database (Firestore) for data based on geographical location <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
*   **Adding Geo Points**: Users can add new geographical points to [[working_with_firebase_firestore_and_realtime_updates | Firestore]] based on their device's current location <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Reactive Map Markers**: Map markers update instantly in response to events in the database, allowing multiple users to listen to the same stream of geolocation data <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Setting Up the Development Environment

Before starting, ensure [[flutter_app_integration_with_firebase | Flutter]] and [[flutter_app_integration_with_firebase | Firebase]] are properly installed and configured <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Google Maps API Key
A [[creating_responsive_uis_with_flutter_and_google_maps | Google Maps API key]] is required, obtained from the Google Cloud Platform (GCP) project associated with your [[flutter_app_integration_with_firebase | Firebase]] project <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This key must be integrated into your Flutter project:
*   **Android**: Add the API key as metadata in the `AndroidManifest.xml` file within the `<application>` tag <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **iOS**: Add the API key in the `AppDelegate.m` file <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

### Dependencies
Key dependencies for geolocation applications include:
*   `firebase_core` <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>
*   `cloud_firestore` <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
*   `rxdart` (for complex stream management) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
*   `geo_flutter_fire` <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
*   `location` <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   `google_maps_flutter` (note: this package is relatively new and may experience breaking changes) <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>

### Permissions
To track user location, permissions must be requested:
*   **Android**: Add a `<uses-permission>` tag for `ACCESS_FINE_LOCATION` in `AndroidManifest.xml` <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   **iOS**: Add specific key-value pairs (e.g., `NSLocationWhenInUseUsageDescription`) to `Info.plist` <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## Building the Map Interface with Flutter

A responsive, full-screen map is typically achieved using a `Stack` widget in Flutter <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. The `GoogleMap` widget is placed at the bottom, allowing other controls (like sliders or buttons) to be overlaid <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### GoogleMap Configuration
*   **Initial Camera Position**: Set with `CameraPosition`, defining a latitude and longitude for the map's center and an initial zoom level <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **`onMapCreated`**: A lifecycle hook where the `GoogleMapController` is set up. This controller is vital for interacting with the map, such as setting markers or zooming <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Location Tracking**: Set `myLocationEnabled` to `true` to display the user's location as a blue dot <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Camera Tracking**: Enable `trackCameraPosition` to continuously get the current center point of the camera <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

### Adding UI Controls
`Positioned` widgets within the `Stack` can place elements like buttons or sliders at specific corners <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. A `FlatButton` with an icon can trigger actions, such as adding a new marker based on the camera's current position <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

## Tracking User Location

The `location` plugin can retrieve the user's current location either as a `Future` (one-time fetch) or a `Stream` (real-time updates) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. The `GoogleMapController` can then be used to `animateCamera` to the user's current position <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

## Storing Geolocation Data in Firestore

To store geolocation data in [[working_with_firebase_firestore_and_realtime_updates | Firestore]], a collection (e.g., `locations`) is used, where each document contains a `position` field <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. This `position` field has two key components:
*   **`geohash`**: A string encoding a bounding box, crucial for efficiently querying data within a certain radius <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **`geopoint`**: The actual latitude and longitude coordinates <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

The [[managing_geolocation_data_in_firestore_with_geo_flutter_fire | Geo Flutter Fire]] library automatically creates this data structure <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. A `GeoFirePoint` is a special data structure that calculates the `geohash` and can compute distances between points <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

To add a new geo point:
1.  Get the user's current location using the `location` service <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
2.  Create a `GeoFirePoint` from the latitude and longitude <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
3.  Add a document to the specified [[working_with_firebase_firestore_and_realtime_updates | Firestore]] collection, setting the `position` field to the `point data` provided by `GeoFirePoint` <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

> [!TIP] Android Emulator GPS Spoofing
> When developing on Android, you can go into the emulator settings to send custom GPS locations to simulate movement and test the app's behavior <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

## Querying Geolocation Data and Real-time Updates

The ability to query data within a certain radius and display it reactively on the map is a core feature.

### Radius-Based Queries
*   **Rx Behavior Subject**: The query's radius can be managed using an `Rx Behavior Subject`, an observable that always holds a current value and can be pushed new values <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Stream Management**: The geo query itself is a stream of documents from the [[working_with_firebase_firestore_and_realtime_updates | Firestore]] database <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   **Subscription Handling**: It's crucial to manage the stream subscription to prevent memory leaks by canceling it when the widget is disposed <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### Reactive Map Marker Updates
When [[working_with_firebase_firestore_and_realtime_updates | Firestore]] emits a change (the entire list of documents), the app loops over them to update the markers on the map <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. The geolocation data from the Firestore document is used for the marker's position <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. [[managing_geolocation_data_in_firestore_with_geo_flutter_fire | Geo Flutter Fire]] also provides the distance of each point from the query's center point, which can be displayed in the marker's info window <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### Constructing the Query
1.  **Center Point**: The query starts from a `GeoFirePoint` based on the user's current location <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
2.  **Listening to Radius and Database**: The subscription is dependent on two streams: the `radius` value and the `Firestore` documents <a class="yt-timestamp" data-t="00:09:59">[00:10:00]</a>.
3.  **`switchMap`**: `rxdart`'s `switchMap` operator is useful here, allowing the app to switch from observing the `radius` stream to observing a stream of `Firestore` documents whenever the radius changes <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
4.  **`geoFireCollection.within`**: This method from [[managing_geolocation_data_in_firestore_with_geo_flutter_fire | Geo Flutter Fire]] is used to perform the query, requiring the `center point`, `radius`, and the `property` in the document containing the geolocation data <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
5.  **`strict mode`**: Recommended to ensure only points strictly within the defined radius are included, as geohashes are square-shaped and can sometimes include points slightly outside the circular radius <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

When the user adjusts a slider control, the `onChanged` event triggers an update to the `radius behavior subject`, which then causes the query to re-evaluate and update the map <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

By combining [[flutter_app_integration_with_firebase | Flutter]], [[creating_responsive_uis_with_flutter_and_google_maps | Google Maps]], and [[working_with_firebase_firestore_and_realtime_updates | Firestore]] with the [[managing_geolocation_data_in_firestore_with_geo_flutter_fire | Geo Flutter Fire]] library, a real-time geolocation application can be built efficiently for both iOS and Android <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.