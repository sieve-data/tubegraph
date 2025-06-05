---
title: Creating responsive UIs with Flutter and Google Maps
videoId: MYHVyl-juUk
---

From: [[fireship]] <br/> 

Creating responsive user interfaces with [[crossplatform_app_development_with_flutter | Flutter]] and [[using_google_maps_and_firestore_for_app_development | Google Maps]] is essential for applications requiring real-time geolocation features, similar to those found in high-valued tech companies like Uber [00:00:09]. Such applications require dynamic UIs that update based on device GPS tracking and real-time database queries [00:00:19].

## Core Components and Tools

Applications that leverage real-time geolocation with [[crossplatform_app_development_with_flutter | Flutter]] typically integrate several key tools:
*   **[[crossplatform_app_development_with_flutter | Flutter]]**: For [[crossplatform_app_development_with_flutter | crossplatform app development]] [00:00:26].
*   **[[using_google_maps_and_firestore_for_app_development | Google Maps]]**: To display interactive maps and locations [00:00:27].
*   **Firestore**: A cloud database for storing and querying geolocation data [00:00:28].
*   **[[managing_geolocation_data_in_firestore_with_geo_flutter_fire | Geo Flutter Fire]]**: A library that powers geo queries on Firestore [00:00:40].
*   **RxDart**: For handling complex stream management, especially for reactive UI updates [00:02:01].
*   **Location package**: For tracking the user's device position [00:02:05].

## Setting up the UI

A responsive [[crossplatform_app_development_with_flutter | Flutter]] UI for a map-based application can be arranged simply using a `Stack` widget [00:00:53]. This allows for layering elements, with the map at the bottom and other controls overlaid on top [00:03:16].

### Initial Map Setup

1.  **Scaffold and Stateful Widget**: The app starts with a `MaterialApp` and `Scaffold`, encapsulating all state and logic within a `StatefulWidget` [00:02:57].
2.  **GoogleMap Widget**: The `GoogleMap` widget is added as the first child in the `Stack` [00:03:21].
    *   It requires an `initialCameraPosition`, which includes a `latitude`, `longitude`, and `zoom` level to center the map [00:03:25].
    *   The `onMapCreated` lifecycle hook is used to set up the `mapController`, which is crucial for programmatically interacting with the map, such as setting markers or zooming [00:03:41].
    *   Additional map properties can be configured, such as `myLocationEnabled` to track the user's location, `mapType` for satellite imagery, or `cameraTracking` to get the current center point of the camera [00:04:03].

### Overlaying Controls

Interactive elements like buttons and sliders can be positioned over the map using the `Positioned` widget within the `Stack` [00:03:28].

1.  **Add Geo Point Button**: A `FlatButton` can be placed in the bottom right corner using `Positioned` properties [00:04:22].
    *   When pressed, this button triggers an `addGeoPoint` event handler [00:04:38].
    *   The `addGeoPoint` method utilizes the device's current location to create a new `GeoFirePoint` and saves it to Firestore [00:07:07]. This demonstrates real-time data addition from the UI [00:07:38].
2.  **Radius Slider**: A `Slider` widget allows users to change the radius for geo queries [00:00:48].
    *   It has `min` and `max` values [00:08:50].
    *   Its current value is obtained from an Rx `BehaviorSubject` [00:08:55].
    *   The `onChanged` event of the slider updates this `BehaviorSubject`, which in turn triggers a new geo query [00:09:04]. This enables the UI to control the scope of data displayed [00:11:00].

## Real-time UI Updates

A key aspect of a responsive geolocation UI is its ability to update in real-time as data changes in the database or as the user interacts with controls.

### Tracking User Location
The [[crossplatform_app_development_with_flutter | Flutter]] `location` plugin can be used to track the user's actual position, either as a `Future` or a real-time `Stream` [00:05:19]. A method like `animateToUser` can programmatically animate the map camera to the user's current location [00:05:33].

### Reactive Marker Updates
Markers on the map can be updated reactively based on events from the database [00:01:17].
1.  **Firestore Data Structure**: Geolocation data in Firestore documents should include a `position` field with a `geohash` and `geopoint` [00:09:12]. [[managing_geolocation_data_in_firestore_with_geo_flutter_fire | Geo Flutter Fire]] simplifies the creation of this data structure [00:06:17].
2.  **Geo Query Stream**: The `geoQuery` is a stream of documents from the Firestore database [00:08:28].
    *   The query is dependent on a radius value, managed by an Rx `BehaviorSubject` [00:08:10].
    *   Using RxDart's `switchMap` on the radius stream allows switching to an observable of documents from the database based on the updated radius [00:10:10].
    *   The `geoFireCollection.within` method is used to query for documents within a specified radius from a `centerPoint` [00:10:18]. Strict mode is recommended to ensure only points within the radius are included [00:10:28].
3.  **Updating Markers**: Anytime there's a change in the Firestore data, the `listen` method on the stream runs an `updateMarkers` method [00:10:40].
    *   This method loops over the received documents, takes their geolocation data, and updates or adds new markers to the map [00:09:14].
    *   Information like the distance from the query center point can be displayed in the marker's info window [00:09:31].
4.  **Subscription Management**: To prevent memory leaks, it is crucial to cancel the query subscription in the `dispose` method of the `StatefulWidget` [00:11:11].

This reactive approach ensures that the UI (markers on the map) reflects the real-time state of the database, allowing multiple users to view the same dynamic geolocation data simultaneously, much like in an Uber app [00:01:26].