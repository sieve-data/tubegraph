---
title: Streambased state management with BehaviorSubject
videoId: 3tm-R7ymwhc
---

From: [[fireship]] <br/> 

Streambased state management, particularly using `BehaviorSubject` from RxDart, is a favored method for managing global state in Flutter applications <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>. This approach allows for business logic to be developed independently of the widget tree, simplifying testing and reasoning about the application's data flow <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>.

## What is a BehaviorSubject?

A `BehaviorSubject` is a special type of stream available in [[Using Subjects and Multicasting in RxJS | RxDart]] <a class="yt-timestamp" data-t="06:16:00">[06:16:00]</a>. It is highly useful for state management due to several key features <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>:
*   It always retains a current value that can be read by Flutter's build methods <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>.
*   It can be treated as a stream, allowing new values to be added to it <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>.
*   By default, it is a broadcast stream, enabling multiple widgets to listen to the same stream simultaneously <a class="yt-timestamp" data-t="06:39:00">[06:39:00]</a>.

## Implementing the Counter Service

To implement streambased state management with `BehaviorSubject`, a custom class can be created. For example, a `CounterService` class might look like this <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>:

```dart
class CounterService {
  final _counterSubject = BehaviorSubject<int>.seeded(0); // Starts at 0
  
  // Expose the stream
  Stream<int> get counterStream => _counterSubject.stream;
  
  // Get the current value synchronously
  int get currentCount => _counterSubject.value;
  
  // Method to mutate (increment) the BehaviorSubject
  void increment() {
    _counterSubject.add(_counterSubject.value + 1);
  }
}
```
This structure creates a custom API for widgets to consume, completely decoupling the business logic from the UI <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>.

## Consuming State with StreamBuilder

The `StreamBuilder` widget is used to consume the `BehaviorSubject` stream and rebuild the UI when new values are emitted <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>. The `StreamBuilder` is passed the stream from the `BehaviorSubject`, causing the widget to rebuild every time a new value is added to the subject <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>.

An example `HomePage` widget using `StreamBuilder` might look like this:

```dart
class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: StreamBuilder<int>(
        stream: counterService.counterStream, // Assuming counterService is globally accessible
        builder: (context, snapshot) {
          // Access the current count from the snapshot
          final count = snapshot.data ?? 0; // Provide a default value
          return Text('Count: $count');
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          counterService.increment(); // Call the increment method
        },
        child: Icon(Icons.add),
      ),
    );
  }
}
```

Key benefits of using `StreamBuilder` include:
*   **Efficient UI updates:** It allows for the `StreamBuilder` to be nested deeper in the widget tree, repainting less of the UI compared to other methods <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>.
*   **Automatic Unsubscription:** The `StreamBuilder` automatically unsubscribes from the stream when the widget is disposed, preventing memory leaks without manual stream cancellation <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>.
*   **Decoupled State:** The data itself is completely decoupled from the `StreamBuilder`, meaning the logic to update the data does not need to rebuild whenever the stream value changes <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>.

## Managing Dependencies with GetIt

While a `BehaviorSubject` service can be instantiated in the global namespace <a class="yt-timestamp" data-t="07:18:00">[07:18:00]</a>, it is preferable to manage it as a true singleton using a dependency injection library like `get_it` <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>.

To set up `get_it`:
1.  Import the `get_it` library <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.
2.  Instantiate `get_it` globally <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>.
3.  Register the `CounterService` as a singleton in the `main` function <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>:

```dart
// main.dart
import 'package:get_it/get_it.dart';

final GetIt getIt = GetIt.instance;

void main() {
  getIt.registerSingleton<CounterService>(CounterService());
  runApp(MyApp());
}
```

Now, the `CounterService` state can be accessed in any widget using `getIt<CounterService>()` <a class="yt-timestamp" data-t="08:37:00">[08:37:00]</a>. This approach makes the state easier to mock for integration tests and ensures that the `CounterService` class is instantiated only once <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>.