---
title: Form Validation and Dynamic Fields
videoId: JeeUY6WaXiA
---

From: [[fireship]] <br/> 

This article explores how to implement dynamic form fields and robust validation using Angular Reactive Forms. The concepts are demonstrated through building various forms, progressing from absolute basics to advanced topics like dynamic fields, validation, and backend submission. Understanding reactive forms is a valuable skill, as forms are integral to almost all applications <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Setup and Core Concepts

To begin using reactive forms effectively in Angular 6, certain modules and tools are essential:

*   **Angular Material**: This library provides UI elements for forms and simplifies form validation. It can be installed by running `ng add @angular/material` <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **Reactive Forms Module**: This module is not included by default and must be imported from `@angular/forms` <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

The two fundamental building blocks of reactive forms are `FormGroup` and `FormBuilder`:

*   **`FormGroup`**: This class is used to tie different form controls together into a single, unified form <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **`FormBuilder`**: This is a service that simplifies the process of building forms <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

In the TypeScript of a component, you typically declare a variable of type `FormGroup` <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a> and inject the `FormBuilder` service into the component's constructor <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. A data model, acting as a schema for the form's values and validation rules, is then created using `formBuilder.group()` <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>, <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

Forms are reactive real-time streams; the `FormGroup`'s `valueChanges` method returns an observable that emits the form's value every time it changes <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>, <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

In the HTML, the `formGroup` attribute is bound to the `FormGroup` defined in TypeScript <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Individual HTML inputs are connected to the reactive form using the `formControlName` attribute, referencing the corresponding attribute in the TypeScript definition <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Nesting and Dynamic Form Arrays

To maintain organized and DRY (Don't Repeat Yourself) forms, especially for complex structures, nesting and dynamic arrays are vital.

### Nested Forms

Nested forms involve having a parent `FormGroup` with multiple nested form groups inside it, allowing for a structured data model where related fields are grouped together <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>, <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

In TypeScript, a reusable `FormGroup` can be created for the nested schema (e.g., phone numbers), and then this schema can be nested multiple times within the parent `FormGroup` using `formBuilder.group()` <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>, <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

In HTML, when dealing with a nested group, instead of `formControlName`, you set up a container (e.g., a `div`) and pass it the `formControlGroup` name. Inside this container, you can then add inputs using `formControlName` for the individual fields within that nested group <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>, <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Form Arrays

[[Nesting and Dynamic Form Arrays]] become necessary when users need to dynamically add or remove multiple instances of a form field (e.g., adding multiple phone numbers). Instead of nested objects, a `FormArray` creates a nested array of objects <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

To use `FormArray`, it must be imported from `@angular/forms` <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. A property on the form is set up as a `FormArray` that starts with an empty array <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

**Dynamic Operations**:
*   **Adding Fields**: A function (e.g., `addPhone`) defines a new `formBuilder.group()` schema and then uses a getter to retrieve the `FormArray` from the reactive form, calling `push()` on it with the new form group <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **Deleting Fields**: When looping over form array elements, their index can be obtained. The `FormArray.removeAt(index)` method can then be called to remove an item from the reactive form <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

In HTML, the `formArrayName` attribute is used with the array property. An `ngFor` loop iterates over the `FormArray`'s controls, and each item in the loop (which is a `FormGroup`) is passed its index as the `formGroupName` <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Buttons can then trigger the `addPhone` and `deletePhone` methods <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

## Form Validation and Feedback

[[Form State Management and Validation Feedback]] is crucial for guiding user input and preventing bad data from being submitted. Reactive forms track various states:

*   **`valid`**: The form or control passes all validation rules <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **`dirty`**: The user has typed into the form or control <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **`touched`**: The user has entered and then left a form field <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

These states apply to both the entire `FormGroup` and individual controls, and Angular applies CSS classes for each state, allowing for styling based on form state <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>, <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. Angular Material often handles much of the visual feedback out of the box <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### Built-in Validators

Angular provides a set of built-in validators, which cover a majority of validation use cases. These are imported from `@angular/forms` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

In the TypeScript, for each form property, validators are passed as a second item in an array alongside the default value <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. Examples include:

*   `Validators.required` <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>
*   `Validators.email` (for proper email format) <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>
*   `Validators.pattern` (for regular expressions, e.g., password complexity) <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>
*   `Validators.min` and `Validators.max` (for numeric ranges) <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>, <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>
*   `Validators.minLength` (for string length) <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>

> **Pro Tip**: Set up getters for various form fields in TypeScript. This cleans up the HTML when implementing logic for showing different error messages <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>, <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

### Displaying Validation Feedback

In HTML, the `mat-error` component from Angular Material, combined with `ngIf`, can conditionally show error messages. For example, an error message can be displayed if a field is `invalid` and has been `touched` <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>, <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.

Different error messages can be displayed based on the specific type of validation error by checking `control.hasError('validatorName')` <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Hints can also be provided for more complex values, like password requirements <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

A common [[Submitting Reactive Forms to a Backend Database | UI technique]] is to disable the submit button until the entire form is completely valid. This is easily achieved by binding the `disabled` attribute of the button to the `form.invalid` state of the `FormGroup` <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>, <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

## Submitting Forms to a Backend Database

After validation, the next step is often to submit the form data to a backend database. This example uses Cloud Firestore, but the principles apply to any backend <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>, <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

### TypeScript Logic for Submission

1.  **Import necessary services**: For Firestore, import `AngularFirestore` <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
2.  **Manage submission state**: Use boolean flags like `loading` and `success` to track the submission process, both initially `false` <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
3.  **Create an event handler**: This method is triggered when the form is submitted (e.g., `submitHandler`) <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.
4.  **Submission steps**:
    *   Set `loading` to `true` <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   Get the current form value using `myForm.value` <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   Use a `try-catch` block to handle potential backend errors <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.
    *   `await` the database operation (e.g., `firestore.collection('contacts').add(formValue)`) <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.
    *   If successful, set `success` to `true` <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
    *   If there are errors, log them to the console <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.
    *   Finally, set `loading` back to `false` <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.

### HTML for Submission Feedback

*   **Conditional display**: The form can be hidden once successfully submitted by binding the `hidden` attribute to the `success` state <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.
*   **Submission event**: The form's `ngSubmit` event is bound to the `submitHandler` method <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Success notification**: A message can be displayed to the user confirming successful submission <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.