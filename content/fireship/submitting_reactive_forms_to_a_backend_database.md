---
title: Submitting Reactive Forms to a Backend Database
videoId: JeeUY6WaXiA
---

From: [[fireship]] <br/> 

Submitting [[introduction_to_reactive_forms_in_angular | reactive forms]] data to a [[implementing_backend_logic_with_webhooks | back-end database]] is a crucial step in many web applications <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This process integrates the [[front_end_and_back_end_development | front end]] [[introduction_to_reactive_forms_in_angular | reactive form]] with a [[implementing_backend_logic_with_webhooks | backend]] service, such as Cloud Firestore, to persist user input <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. This technique enables the building of full-stack [[introduction_to_reactive_forms_in_angular | reactive forms]] in Angular 6 <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

## Prerequisites

To follow along with an example using [[building_serverless_backends_with_firebase_and_flutter | Firebase]], ensure you have:
*   AngularFire 2 installed <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   A [[building_serverless_backends_with_firebase_and_flutter | Firebase]] project set up <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.

While Cloud Firestore is used as an example, the principles discussed can be adapted for any [[implementing_backend_logic_with_webhooks | backend]] system <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

## TypeScript Implementation

The TypeScript file manages the form's state and the submission logic <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

### Imports

Import necessary modules into your component's TypeScript file:
*   `AngularFirestore` for [[building_serverless_backends_with_firebase_and_flutter | database]] interaction <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.
*   `tap` and `first` operators from RxJS for handling asynchronous operations <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.

### Form State Management

Declare state variables to manage the submission process:
*   `loading`: A boolean indicating if the submission is in progress, initially `false` <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
*   `success`: A boolean indicating if the submission was successful, initially `false` <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

### Submit Handler Method

Create an event handler method (e.g., `submitHandler`), which will be triggered when the user clicks the submit button on the form <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>:

1.  **Set Loading State**: Immediately set the `loading` state to `true` to indicate that the submission has begun <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.
2.  **Retrieve Form Value**: Grab the current value from the [[introduction_to_reactive_forms_in_angular | reactive form]] by calling `myform.value` <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.
3.  **Error Handling**: Implement a `try-catch` block to catch any potential errors that might occur on the [[implementing_backend_logic_with_webhooks | backend]] during the submission <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
4.  **Database Operation**:
    *   Inside the `try` block, use `await` with `angularFirestore.collection('contacts').add(formValue)` to add the form data to your [[implementing_backend_logic_with_webhooks | database]] <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.
    *   After the operation successfully completes, set the `success` state to `true` <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
    *   If an error occurs in the `catch` block, log the error to the console <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
5.  **Reset Loading State**: After the operation (success or error), set the `loading` state back to `false` <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.

## HTML Markup

The HTML markup connects the form to the TypeScript logic and provides [[form_state_management_and_validation_feedback | user feedback]]:

1.  **Hide Form on Success**: Use the `[hidden]` attribute bound to the `success` state to hide the form once it has been successfully submitted <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.
2.  **Bind Submit Event**: Crucially, bind the `(ngSubmit)` event on your form element to the `submitHandler` method defined in your TypeScript <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>. This sends the data to the [[implementing_backend_logic_with_webhooks | database]] <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
3.  **Success Notification**: Add a success notification message that is conditionally displayed based on the `success` state, informing the user that their data has been saved in the [[implementing_backend_logic_with_webhooks | backend]] <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.
4.  **Disable Submit Button**: As part of [[form_validation_and_dynamic_fields | form validation]], disable the submit button until the form is completely valid by binding the `disabled` attribute to the `form.invalid` state <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. This prevents users from submitting invalid data to your [[implementing_backend_logic_with_webhooks | backend database]] <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.