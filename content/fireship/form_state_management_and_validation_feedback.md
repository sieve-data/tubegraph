---
title: Form State Management and Validation Feedback
videoId: JeeUY6WaXiA
---

From: [[fireship]] <br/> 

Effective [[Introduction to Reactive Forms in Angular | reactive forms]] in Angular involve managing their state and providing clear validation feedback to the user <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Understanding the different states a form can be in and how to implement validation rules is crucial for building robust applications <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Understanding Form States

Reactive forms and their individual controls can exist in several states, each indicating a specific interaction or validity status <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>:

*   **Valid**: The form or control passes all defined validation rules <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Dirty**: The user has interacted with and changed the value of the form or control <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **Touched**: The user has focused on a form field and then moved out of it (blurred) <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

These states can apply to the entire form group or to each individual control within the form <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. Angular automatically applies CSS classes corresponding to these states, allowing for dynamic styling based on the form's condition <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

## Implementing Validation Rules

To implement validation, the `Validators` module needs to be imported from `@angular/forms` <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. Angular provides a suite of built-in validators that cover most common use cases <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

Validation rules are defined as the second item in an array when setting up a form control's default value <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

### Built-in Validators

Commonly used built-in validators include:

*   **`Validators.required`**: Ensures a field has a value <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **`Validators.email`**: Validates that the input is in a proper email format <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
*   **`Validators.pattern`**: Allows validation against a regular expression for specific format requirements (e.g., a password requiring one letter and one number) <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
*   **`Validators.min` / `Validators.max`**: Used for validating numeric values within a specified range (e.g., an age range) <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **`Validators.minLength` / `Validators.maxLength`**: Used for validating string length <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

Synchronous validators are typically used, but asynchronous validators can also be implemented for more complex scenarios, though they are a topic for further discussion <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

## Displaying Validation Feedback

Angular Material greatly simplifies the process of displaying validation feedback, often providing automatic error messages out of the box <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### Conditional Error Messages

Error messages can be conditionally displayed in the HTML using `*ngIf` in conjunction with `mat-error` components <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. For example, an error message for an email field can be shown if the email is invalid and has been `touched` <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

```html
<mat-error *ngIf="email.invalid && email.touched">
  Your email does not look right.
</mat-error>
```
<a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>

### Dynamic Error Messages for Different Validation Types

For fields with multiple validators, different error messages can be displayed based on the specific validation error that occurred <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. This is achieved by checking specific error properties of the form control, such as `hasError('min')` or `hasError('max')` <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.

```html
<mat-error *ngIf="age.hasError('min')">
  Your actual age is too young to use this app
</mat-error>
<mat-error *ngIf="age.hasError('max')">
  Your actual age is too old to use this app
</mat-error>
```
<a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>

Hints can also be provided for more complex values, such as password requirements <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

### Using Getters for Cleaner HTML

To keep the HTML concise and readable, it is highly recommended to set up getter methods for each form control in the TypeScript file <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. This allows for simpler access to form control states in the template (e.g., `email.invalid` instead of `myform.get('email').invalid`) <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

## Controlling Submit Button State

A common and important technique is to disable the submit button until the form is entirely valid, preventing the submission of incomplete or incorrect data to the backend database <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. This is easily achieved by binding the `disabled` attribute of the button to the form's `invalid` state <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>:

```html
<button [disabled]="myform.invalid">Submit</button>
```
<a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>

This integration of form state management and validation feedback is crucial for building user-friendly and robust [[Introduction to Reactive Forms in Angular | reactive forms]] that prevent submission of bad data to the backend <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>, ultimately leading to better [[Security Measures in Frontend and Backend | security]] and data integrity. The process of [[Submitting Reactive Forms to a Backend Database | submitting form data to a backend database]] is then performed after validation is complete <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.