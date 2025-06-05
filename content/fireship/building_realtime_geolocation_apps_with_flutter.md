---
title: Building realtime geolocation apps with Flutter
videoId: MYHVyl-juUk
---

From: [[fireship]] <br/> 

Geolocation is a critical feature in many modern applications, exemplified by companies like Uber, which has a core feature of real-time geolocation and a valuation exceeding 100 billion dollars <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This article outlines how to build essential features for a geolocation app, such as device GPS tracking and real-time geolocation queries to a cloud database, using less than 200 lines of code <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Key Technologies Used
The application is built using:
*   [[crossplatform_app_development_with_flutter | Flutter]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   [[using_google_maps_and_firestore_for_app_development | Google Maps]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>
*   [[using_google_maps_and_firestore_for_app_development | Firestore]] <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>
*   Geo Flutter Fire library (authored by Darshan Goda) <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>

## App Overview
The demonstration app features a full-screen Google Map <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. It includes a slider in the left corner and a button in the right corner <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   Moving the slider zooms out the camera and increases the range of the geo query <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   The app finds "safe points" within a certain radius of a center point, which is often the user's device location via GPS <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   A button allows adding new geo points to Firestore based on the device's current location <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   Markers on the map update by reacting to events in the database, allowing multiple users to see the same real-time geolocation data, similar to Uber <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Setup and Dependencies

### Prerequisites
1.  **FlutterFire Installation**: Refer to the official documentation or the Google OAuth Water video for installation steps <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
2.  **Google Maps API Key**: Obtain a Google Maps API key from your Google Cloud Platform (GCP) project, which is created when you set up a Firebase project <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Project Dependencies
Add the following to your `pubspec.yaml` file <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>:
*   `firebase_core`
*   `cloud_firestore`
*   `rxdart` (for complex stream management) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
*   `geo_flutter_fire` <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
*   `location` <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   `google_maps_flutter` (note: this package is new and may have breaking changes) <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>

### Platform-Specific Configuration
*   **Android**:
    *   In `android/app/src/main/AndroidManifest.xml`, add the `ACCESS_FINE_LOCATION` permission tag to track user location <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
    *   Add metadata for the Google Maps API key within the `<application>` tag <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **iOS**:
    *   In `ios/Runner/AppDelegate.m`, add your API key <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
    *   In `ios/Runner/Info.plist`, add key-value pairs to obtain user location permission <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## [[building_mobile_app_components_with_flutter | Building the App]]

### Basic UI Structure
The app starts with a `MaterialApp` scaffold and a stateful widget named `FireMap` to encapsulate logic and state <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### [[creating_responsive_uis_with_flutter_and_google_maps | Responsive Map Layout]]
To create a perfectly centered full-screen map, use a `Stack` widget. This allows the map to be at the bottom, with controls overlaid on top <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   Add the `GoogleMap` widget as the first child in the `Stack` <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   Set an `initialCameraPosition` with a `LatLng` target and a zoom level <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   Implement `onMapCreated` to set up the `GoogleMapController`, which is essential for interacting with the map (e.g., setting markers, zooming) <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   Enable `myLocationEnabled` to track the user's location and `cameraTracking` to get the current center point of the camera <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. You can also change the `mapType` (e.g., to satellite imagery) <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### Adding Markers
A `Positioned` widget within the `Stack` can place a button in the bottom right corner <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Define a `FlatButton` with an icon <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   When pressed, this button triggers an `addMarker` event handler <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   The `addMarker` method creates a `Marker` object. Its position is obtained from `mapController.cameraPosition` <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   Customize the marker icon and add `infoWindow` text that displays when clicked <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   Call `mapController.addMarker` with `MarkerOptions` to add it to the map <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### [[implementing_gps_tracking_and_geolocation_queries | Tracking User Location]]
The `location` plugin makes it easy to track the user's position as either a `Future` or a `Stream` <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   Create an instance of `Location` at the top of the stateful widget <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   Implement `animateToUser` as an `async` function.
    *   Get the current location using `await location.getLocation()` <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
    *   Use `mapController.animateCamera` to move the camera to the user's position <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
    *   `location.onLocationChanged` can be used to listen to real-time streams <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
*   The user's current position will appear as a small blue dot on the map <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

## [[managing_geolocation_data_in_firestore_with_geo_flutter_fire | Saving Geolocation Data in Firestore]]
Geolocation data is stored in a `locations` collection in Firestore <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. Each document has a `position` field containing a `geo_hash` and a `geo_point` <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. Geo Flutter Fire handles the creation of this data structure and calculates the geohash value, which is crucial for querying Firestore within a certain radius <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

### Adding Geo Points
*   Set up instances for `Firestore` and `GeoFireClient` in the stateful widget <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   Create an `addGeoPoint` method. This method:
    *   Retrieves the user's current location using the `location` service <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
    *   Sets up a `GeoFirePoint` based on the latitude and longitude. A `GeoFirePoint` calculates the geohash and can determine distances between points <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
    *   Makes a reference to the Firestore collection and adds a document, setting the `position` field to the `GeoFirePoint` data <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   Replace the `addMarker` call on the button with `addGeoPoint` <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Tip**: On Android, you can send custom GPS locations to the emulator to simulate movement and observe different geo hashes being added <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

## Querying Geolocation Data Reactively

### State Management for Queries
*   **Radius**: Define an `Rx.BehaviorSubject` for the query radius. This is an observable that stores the current value and allows new values to be pushed to it <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Geo Query Stream**: Set up a stream for documents from the Firestore database <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Subscription**: Keep track of the subscription to prevent memory leaks by cancelling it when the widget is disposed <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

### User Interface for Query Control
*   Add a `Slider` widget to the `Stack` to allow the user to change the radius value <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   Set `min` and `max` values for the slider <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   The slider's `value` property should get the current value from the `radius` BehaviorSubject <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
*   The `onChanged` event will trigger an update to the query when the user slides it <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

### Updating Markers from Query Results
*   Implement `updateMarkers` method. When Firestore emits a change, it provides the entire list of documents <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   Loop over these documents to update the markers on the map <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   Use the [[managing_geolocation_data_in_firestore_with_geo_flutter_fire | geolocation data]] from the Firestore document for the marker's position <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   Geo Flutter Fire provides the distance of the position from the query center point, which can be displayed in the info window <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### Initializing and Reacting to Queries
*   Create a `startQuery` method.
    *   Get the user's current location to serve as the initial center point <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
    *   Make a reference to the `locations` collection in Firestore <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
    *   Set up a `GeoFirePoint` based on the user's location <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
    *   The subscription is dependent on two streams: the `radius` value and the Firestore documents <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
    *   Use `switchMap` from `rxdart` on the `radius` stream to switch to an observable of the database documents <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
    *   Perform the query using `geoFireClient.collection.within()`, passing the `centerPoint`, `radius`, and the field name containing the [[managing_geolocation_data_in_firestore_with_geo_flutter_fire | geolocation data]] <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
    *   Enable `strict mode` to ensure only points within the defined radius are included <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
    *   Call `listen` on the stream and run the `updateMarkers` method <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
*   In the `onChanged` callback of the slider, call `setState` and add the new value to the `radius` BehaviorSubject to update the query <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. Optionally, map zoom values to the slider's radius for a more polished experience <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   Call `startQuery` when the map is created <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Memory Management**: Override the `dispose` method and cancel the subscription when the widget is destroyed to prevent memory leaks <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

This approach enables [[state_management_with_flutter_and_firebase | building serverless backends with Firebase and Flutter]] for real-time geolocation, [[implementing_gps_tracking_and_geolocation_queries | implementing GPS tracking and geolocation queries]], and managing data efficiently.

## Conclusion
Building a real-time geolocation app that [[crossplatform_app_development_with_flutter | runs on both iOS and Android]] can be achieved rapidly, even in under ten minutes, by leveraging Flutter, Google Maps, Firebase, and Geo Flutter Fire <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.