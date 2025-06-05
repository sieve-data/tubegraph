---
title: Introduction to Reactive Forms in Angular
videoId: JeeUY6WaXiA
---

From: [[fireship]] <br/> 

Reactive forms in Angular 6 provide a powerful way to manage form input [00:00:04]. They are built upon a reactive approach, treating the form as a real-time stream using [[Basics of Angular Components | RxJS]] [00:01:50]. Understanding reactive forms is a highly valuable skill for any Angular developer, as most applications utilize forms [00:00:19].

This guide will cover:
*   Setting up the necessary modules and UI elements.
*   Building basic reactive forms.
*   Handling nested forms.
*   Creating dynamic forms with arrays.
*   Implementing form validation.
*   [[submitting_reactive_forms_to_a_backend_database | Submitting form data to a backend database]].

## Getting Started

To begin, you'll need an Angular 6 project [00:00:37].

### Installing Angular Material
Angular Material provides useful UI elements for form validation [00:00:41]. It can be installed by running `ng add @angular/material` [00:00:46]. Angular Material offers a variety of form elements, which can be explored in its documentation [00:01:22].

### Importing Modules
The `ReactiveFormsModule` is not included by default and must be imported from `@angular/forms` [00:01:01]. Additionally, various modules from Angular Material are imported to handle different form fields [00:01:09]. All these modules are then added to the `imports` section of the Angular module, granting access to their components and services [00:01:14].

## Building Basic Reactive Forms

The foundational concepts for building reactive forms are `FormGroup` and `FormBuilder` [00:02:01].

*   **`FormGroup`**: This class is used to tie different form controls together into a single, unified form [00:02:08].
*   **`FormBuilder`**: A service that simplifies the process of building forms [00:02:16].

### TypeScript Setup
1.  **Declare `FormGroup`**: A variable should be declared with the type `FormGroup` [00:02:22].
2.  **Inject `FormBuilder`**: Add the `FormBuilder` service to the component's constructor [00:02:30].
3.  **Define Form Model**: During `ngOnInit` (part of the [[Lifecycle of Angular Components | component lifecycle]]), create a data model using `formBuilder.group()` [00:02:35]. This model acts as a schema, defining the default values and validation rules for the form's fields [00:02:39]. For example, `formBuilder.group({ email: '' })` sets an empty string as the default value for an email field [00:02:46].

### Observing Form Value Changes
The `FormGroup` has a `valueChanges` method that returns an observable [00:03:07]. By subscribing to this observable, you can receive the form's value every time it changes, allowing for real-time updates and debugging (e.g., via `console.log`) [00:03:09].

### Connecting to HTML
To connect the `FormGroup` from TypeScript to the HTML markup:
1.  **Bind `formGroup`**: The `formGroup` attribute in the HTML `<form>` tag is bound to the `FormGroup` instance defined in TypeScript [00:03:20].
2.  **Display Form Value**: The entire form's value can be displayed in HTML using `myForm.value | json` [00:03:32].
3.  **Bind `formControlName`**: Within the form, individual HTML inputs (often with Angular Material's `matInput` [[Angular Directives and Usage | directive]]) are linked to their corresponding form controls in the `FormGroup` using the `formControlName` attribute [00:03:47].

## Nested Forms

Nested forms allow for better organization of complex forms by creating sub-groups within a parent form [00:04:17]. This results in a nested object structure in the form's value [00:04:27].

### TypeScript Setup for Nested Forms
1.  **Create Reusable `FormGroup`**: Define a `FormGroup` schema for the nested section (e.g., a phone number `FormGroup`) [00:04:40].
2.  **Nest within Parent `FormGroup`**: Include instances of the reusable `FormGroup` within the parent `FormGroup`'s schema [00:04:52].

### Connecting Nested Forms to HTML
Instead of `formControlName` for the nested group, use `formControlGroup` on a container element (like a `<div>`) [00:05:08]. Inside this container, individual inputs use `formControlName` as usual [00:05:19].

## Dynamic Forms with FormArray

`FormArray` allows for the dynamic addition and removal of form fields, which is ideal for scenarios where the number of inputs is not fixed (e.g., multiple phone numbers) [00:05:40]. When using `FormArray`, the form's value will be a nested array of objects [00:05:57].

### TypeScript Setup for FormArray
1.  **Import `FormArray`**: Import `FormArray` from `@angular/forms` [00:06:08].
2.  **Define `FormArray` Property**: Set a property on the form (e.g., `phones`) as a `FormArray` that starts with an empty array [00:06:15].
3.  **Create a Getter**: A getter method is highly recommended to easily retrieve the `FormArray` instance from the main form [00:06:23]. This getter should return the `FormArray` type [00:06:37].
4.  **Add Field Method**: Implement a function (e.g., `addPhone`) that, when triggered, creates a new `FormGroup` and `push`es it into the `FormArray` using the getter [00:06:43].
5.  **Delete Field Method**: Implement a function (e.g., `deletePhone`) that uses the `removeAt` method of the `FormArray`, passing the index of the item to be removed [00:07:02].

### Connecting FormArray to HTML
1.  **Bind `formArrayName`**: Bind the `formArrayName` attribute to the `FormArray` property on a container element [00:07:19].
2.  **Loop with `*ngFor`**: Use `*ngFor` to iterate over the `FormArray`'s controls, keeping track of the `index` [00:07:23].
3.  **Bind `formGroupName`**: Inside the loop, each item is a `FormGroup`, so bind `formGroupName` to the current `index` [00:07:39].
4.  **Add/Delete Buttons**: Create buttons (e.g., with `(click)` event [[Binding Properties and Events in Angular | binding]]) to trigger the `addPhone` and `deletePhone` methods [00:07:57]. The delete button should be inside the `*ngFor` loop and pass the `index` as an argument [00:08:08].

## Form Validation

Reactive forms track various states that can be used for validation and styling [00:08:30]:

*   **`valid`**: The form or control passes all validation rules [00:08:35].
*   **`dirty`**: The user has interacted with and changed the input value [00:08:39].
*   **`touched`**: The user has entered a form field and then left it [00:08:42].

Angular applies [[Angular Directives and Usage | CSS classes]] for each of these states, allowing for conditional styling [00:08:54].

### TypeScript Setup for Validation
1.  **Import `Validators`**: Import `Validators` from `@angular/forms` [00:09:42].
2.  **Apply Validators**: For each form property in the `FormGroup` schema, pass an array of validators as the second item in its configuration [00:09:52].
    *   **Built-in Validators**:
        *   `Validators.required`: Ensures a field is not empty [00:10:10].
        *   `Validators.email`: Validates email format [00:10:12].
        *   `Validators.pattern`: Allows custom regular expressions for validation (e.g., for password complexity) [00:10:19].
        *   `Validators.min`/`Validators.max`: Validates minimum and maximum numeric values [00:10:30]. (Do not confuse with `minLength` for strings [00:10:39]).
3.  **Pro Tip: Create Getters for Fields**: Define getter methods for individual form fields (e.g., `email`, `password`) in TypeScript [00:11:03]. This significantly cleans up the HTML logic when showing error messages [00:11:09].

### Connecting Validation to HTML
1.  **Conditional Error Messages**: Use Angular Material's `mat-error` component along with `*ngIf` to conditionally display error messages [00:11:19].
    *   Combine state checks: `*ngIf="email.invalid && email.touched"` ensures the error message only appears if the field is invalid and the user has interacted with it [00:11:28].
2.  **Hints**: Use Angular Material's hint elements to provide guidance for complex fields, like password requirements [00:11:44].
3.  **Specific Error Messages**: For fields with multiple validators, use `*ngIf` with specific error checks (e.g., `age.hasError('min')`, `age.hasError('max')`) to show different messages based on the type of validation error [00:12:06].
4.  **Disable Submit Button**: To prevent submission of invalid data, bind the `disabled` attribute of the submit button to the form's `invalid` state: `[disabled]="myForm.invalid"` [00:12:48]. This is a common and important practice [00:12:57].

## Submitting Forms to a Backend Database

This section demonstrates submitting form data to Cloud Firestore, but the principles apply to any backend [00:13:03].

### TypeScript Setup for Submission
1.  **Import Database Service**: Import your database service (e.g., `AngularFirestore` from `angularfire2`) [00:13:42].
2.  **Manage States**: Introduce state variables like `loading` and `success` to manage the UI during submission [00:13:50].
3.  **Create Submission Event Handler**: Implement an asynchronous method (e.g., `onSubmit`) that triggers when the form is submitted [00:13:59].
    *   Set `loading` to `true` [00:14:07].
    *   Get the current form value using `myForm.value` [00:14:12].
    *   Use a `try-catch` block to handle potential backend errors [00:14:17].
    *   Inside `try`, `await` the database operation (e.g., `firestore.collection('contacts').add(formValue)`) [00:14:22].
    *   If successful, set `success` to `true` [00:14:31].
    *   In `catch`, log any errors [00:14:35].
    *   Finally, set `loading` back to `false` [00:14:40].

### Connecting Submission to HTML
1.  **Hide Form on Success**: Use the `[hidden]` [[Binding Properties and Events in Angular | attribute binding]] to hide the form once it's successfully submitted: `[hidden]="success"` [00:14:47].
2.  **Bind Submit Event**: Bind the `(ngSubmit)` event of the form to your submission handler method (e.g., `(ngSubmit)="onSubmit()"`) [00:14:55].
3.  **Success Notification**: Add a conditional message (e.g., using `*ngIf="success"`) to inform the user that their data has been saved [00:15:05].