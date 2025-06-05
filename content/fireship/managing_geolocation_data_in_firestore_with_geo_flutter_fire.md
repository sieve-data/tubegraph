---
title: Managing geolocation data in Firestore with Geo Flutter Fire
videoId: MYHVyl-juUk
---

From: [[fireship]] <br/> 

Geolocation is a crucial feature in many modern applications, exemplified by companies like Uber, whose core feature is real-time geolocation <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This article explores how to manage geolocation data in Firestore using the `geo_flutter_fire` library in Flutter, enabling features such as device GPS tracking and real-time geolocation queries <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The demonstrated process allows for the creation of a real-time geolocation app in under 200 lines of code <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, [[building_realtime_geolocation_apps_with_flutter | building real-time geolocation apps with Flutter]] by [[using_google_maps_and_firestore_for_app_development | using Google Maps and Firestore for app development]].

The `geo_flutter_fire` library is authored by Darshan Goda, who also wrote most of the code for the example project <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Application Overview

The example application features a full-screen Google Map with a slider in the left corner and a button in the right <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This layout can be simply arranged using a Stack in Flutter <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

Key functionalities include:
*   **Zoom and Query Range**: Moving the slider zooms out the camera and increases the range of the geo query <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Finding Geo Points**: The app finds all geo points within a certain radius of a center point, which is often the user's device location via GPS <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Adding Geo Points**: A button allows adding new geo points to Firestore based on the device's current location <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Real-time Updates**: Markers on the map update by reacting to events in the database, allowing multiple users to listen to the same stream of geolocation data and see updates instantly <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This is similar to how the Uber app displays drivers moving in real time <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Project Setup

Before starting, ensure FlutterFire is installed <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. A Firebase project also provides a GCP project to obtain a Google Maps API key <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Dependencies
The following dependencies are used:
*   `firebase_core` <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>
*   `cloud_firestore` <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
*   `rxdart` (for complex stream [[state_management_with_flutter_and_firebase | management]] and [[managing_state_in_flutter_applications | managing state in Flutter applications]]) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
*   `geo_flutter_fire` <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
*   `location` <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   `google_maps_flutter` (note: this package is very new and may have breaking changes) <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>

### Platform-Specific Configuration
*   **Android**:
    *   In `android/app/src/main/AndroidManifest.xml`, request `ACCESS_FINE_LOCATION` permission for user location tracking <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
    *   Add metadata for the Google Maps API key within the `<application>` tag <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **iOS**:
    *   In `ios/Runner/AppDelegate.m`, add the Google Maps API key <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
    *   In `ios/Runner/Info.plist`, add key-value pairs to obtain user location permission <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## Building the Map and UI

The app starts with a `MaterialApp` and `Scaffold`, with the main UI encapsulated in a stateful widget called `FireMap` <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

### Google Map Widget
To create a responsive, centered map that takes up the entire screen, a `Stack` widget is recommended. The `GoogleMap` widget is placed as the first widget in the stack, allowing other controls to be overlaid <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

*   `GoogleMap` requires an `initialCameraPosition` (latitude, longitude, and zoom level) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   The `onMapCreated` lifecycle hook is used to set up the `GoogleMapController`, which is essential for interacting with the map (e.g., setting markers, zooming) <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   Other options include `myLocationEnabled: true` to track the user's location, changing `mapType` (e.g., satellite imagery), and enabling `cameraTracking` to get the current center point <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

### Adding UI Controls
*   **Add Marker Button**: A `Positioned` widget in the `Stack` can place a `FlatButton` with an icon in the bottom right corner <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
    *   When pressed, an `addMarker` method is triggered <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
    *   The marker's position is obtained from the `mapController.cameraPosition` <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
    *   Markers can have custom icons and info window text <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
    *   Markers are added using `mapController.addMarker()` <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Tracking User Location

The `location` plugin is used to track the user's actual position <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

*   An instance of the `Location` service is set up in the stateful widget <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   An `animateToUser` method (async) gets the user's location using `await location.getLocation()` <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   The camera can then be animated to this position using `mapController.animateCamera` <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   `onLocationChanged` can be used to listen to real-time location streams <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## Saving Geolocation Data to Firestore

Geolocation data is stored in a Firestore collection (e.g., `locations`). Each document in this collection has a `position` field containing a `geohash` and a `geopoint` <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. `geo_flutter_fire` automatically creates this data structure, including the `geohash` value <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Geohashes are essential for querying Firestore for data within a certain radius <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

### Adding Geo Points
An `addGeoPoint` method is responsible for saving location data:
1.  Initialize `Firestore` and `GeoFireClient` instances <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
2.  Get the user's current location using the `location` service <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
3.  Create a `GeoFirePoint` from the latitude and longitude. A `GeoFirePoint` is a special data structure for calculating geohashes and distances <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
4.  Reference the Firestore collection (e.g., `firestore.collection('locations')`) <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
5.  Add a document to Firestore, setting the `position` field to the `GeoFirePoint`'s data <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

The `addGeoPoint` method can be linked to a UI button. To test different geo points when device location is static, one can use Android emulator settings to send custom GPS locations <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

## Querying Geolocation Data from Firestore Reactively

The `geo_flutter_fire` library facilitates reactive queries based on a radius, which can be changed by the user.

### State Management for Queries
*   `BehaviorSubject<double> radius` from [[advanced_data_management_techniques_in_flutter_apps | RxDart]] is used to manage the query radius. It's an observable that always has a current value <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   A `Stream<List<DocumentSnapshot>> geoQuery` holds the stream of documents from Firestore <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   A `StreamSubscription` is maintained to prevent memory leaks by cancelling it when the widget is disposed <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

### UI Slider for Radius
A `Slider` widget is added to the UI to allow users to change the `radius` value <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   The slider's `value` is bound to the `radius.value` <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
*   The `onChanged` event listener pushes new values to the `radius` subject, which triggers the query update <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### Updating Map Markers
When `firestore` emits changes, the entire list of documents is received. The app loops over them to update markers on the map <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   The geolocation data from the Firestore document is used for the marker's position <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   `geo_flutter_fire` can provide the distance of each position from the query center point, which can be displayed as info window text <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### Initializing and Listening to the Query
The `_startQuery` method sets up the geo query:
1.  Get the user's current location <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
2.  Make a reference to the `locations` collection in Firestore <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
3.  Set up a `GeoFirePoint` based on the user's location to serve as the query `centerPoint` <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
4.  The subscription depends on two streams:
    *   The `radius` value <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
    *   The real-time values of documents from the database <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
5.  [[state_management_with_flutter_and_firebase | RxDart]]'s `switchMap` operator is used on the `radius` stream to switch to an observable of the documents <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
6.  The query itself is made using `geoFireCollection.within()`, passing in the `centerPoint`, `radius`, and the document property containing the geolocation data (`position`) <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
7.  `strictMode: true` is recommended to ensure only points truly within the radius are included, as geohashes are square-shaped <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
8.  Finally, `listen` is called on the stream to execute the `updateMarkers` method when changes occur <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

The `_startQuery` method is called when the map is created (`onMapCreated`). It is also crucial to override the `dispose` method in the stateful widget to cancel the subscription, preventing memory leaks <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

This setup allows for a reactive real-time geolocation application running on both iOS and Android <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.