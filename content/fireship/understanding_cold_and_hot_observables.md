---
title: Understanding Cold and Hot Observables
videoId: 2LCo926NFLI
---

From: [[fireship]] <br/> 

The concept of [[hot_vs_cold_observables | hot versus cold observables]] is a fundamental aspect of ReactiveX, which has transformed how modern developers approach app development by treating all data as a stream unfolding over time <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Cold Observables

A cold observable is characterized by its data being created inside of it <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This means the underlying data is not created until something subscribes to the observable <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

Consider an observable that generates a random number internally <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. If two different subscribers subscribe to this cold observable, they will each receive a different random number <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. This occurs because the random number is generated anew for each subscription <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## Hot Observables

An observable can be made hot by defining its value outside of the observable itself <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

For example, if a random number is set outside the observable and then passed in as a variable, both subscribers will receive the exact same random number <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This shared data source makes the observable hot <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Making a Cold Observable Hot with `publish()` and `connect()`

It's also possible to make a cold observable hot without separating the data from the observable <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

1.  Place the data generation (e.g., random number) back inside the observable <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
2.  Create a new hot observable by calling `publish()` on the cold observable <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
3.  This setup ensures that the observable will only emit data once a corresponding `connect()` method is called <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
4.  Subscribers can be set up, but no data will be emitted until `connect()` is invoked on the hot observable <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
5.  Calling `connect()` triggers the subscriptions to emit data, which is then shared among all subscribers <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. This can be verified by observing that all subscribers receive the same shared value <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

This method, related to [[using_subjects_and_multicasting_in_rxjs | multicasting]] (specifically `multicast`), allows values to be sent to multiple subscribers without redundant side effects, which is highly beneficial for data sources with many subscribers <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.