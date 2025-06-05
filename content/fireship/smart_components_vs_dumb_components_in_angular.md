---
title: Smart Components vs Dumb Components in Angular
videoId: 23o0evRtrFI
---

From: [[fireship]] <br/> 

The concept of smart components versus dumb components (also known as stateful versus stateless, or container versus presentational components) is crucial for Angular developers to create predictable and maintainable code bases <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>. This approach promotes a clear separation of concerns within an application <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Defining the Roles

### Smart Components (Container / Stateful)
A smart component is typically a page or a container that manages the overall functionality of a section of the application <a class="yt-timestamp" data-t="12:44:00">[12:44:00]</a>.
Their primary responsibilities include:
*   Controlling how different parts of the application work <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>.
*   Synchronizing the state of the application <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.
*   Fetching data, for example, from a database or API <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>.

### Dumb Components (Presentational / Stateless)
In contrast, a dumb component is solely focused on presentation logic and displaying data <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>.
Their primary characteristics are:
*   They are isolated <a class="yt-timestamp" data-t="13:00:00">[13:00:00]</a>.
*   They receive data as inputs and emit events for interactions <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.
*   They typically don't manage their own state or fetch data <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>.

## Benefits of Separation
As an application grows in complexity, this separation makes it easier to understand and rationalize what is happening within the codebase <a class="yt-timestamp" data-t="13:11:00">[13:11:00]</a>. The parent component (smart component) can focus on low-level concerns like state management and data retrieval, while the child component (dumb component) only worries about how to display the data it receives <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>.

## Practical Example

Consider a scenario where a `home` component displays a list of `boat` items.
*   The `home` component would act as the smart component. It would be responsible for fetching the boat data, potentially asynchronously using the [[lifecycle_of_angular_components | `ngOnInit` lifecycle hook]] and [[Binding Properties and Events in Angular | async pipe]] <a class="yt-timestamp" data-t="13:17:00">[13:17:00]</a>.
*   A separate `boat` component would be the dumb component. Its only concern would be to take the boat data (received as an input from the `home` component) and present it in the user interface <a class="yt-timestamp" data-t="13:19:00">[13:19:00]</a>. This allows the `home` component to extract the presentation logic into its own isolated component <a class="yt-timestamp" data-t="12:54:00">[12:54:00]</a>.