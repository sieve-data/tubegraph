---
title: Nesting and Dynamic Form Arrays
videoId: JeeUY6WaXiA
---

From: [[fireship]] <br/> 

Understanding how to structure complex forms is crucial for Angular developers. This article explores two powerful techniques for organizing and managing form fields: nested forms and dynamic form arrays <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. These concepts allow for more organized and maintainable code, especially when dealing with variable numbers of inputs.

## Nested Forms

Nested forms allow you to group related form controls into reusable sub-forms within a larger parent form <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This approach helps keep forms organized, especially when dealing with complex data structures like multiple phone numbers <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### TypeScript Implementation

The fundamental building blocks for reactive forms are `FormGroup` and `FormBuilder` <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   `FormGroup` is used to tie different form controls together into a single, unified form <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   `FormBuilder` is a service that simplifies the process of creating forms <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

To create a nested form:
1.  **Define a reusable form group**: Use `FormBuilder.group()` to define the schema for the nested data, for example, a phone number with `area` and `prefix` fields <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
    ```typescript
    phoneSchema = this.fb.group({
      area: '',
      prefix: '',
      // ... other phone fields
    });
    ```
2.  **Nest the schema in the parent form**: You can then include this reusable `phoneSchema` multiple times within your main form's definition <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
    ```typescript
    myForm: FormGroup;

    constructor(private fb: FormBuilder) {}

    ngOnInit() {
      this.myForm = this.fb.group({
        email: '',
        homePhone: this.phoneSchema, // Nested form group
        cellPhone: this.phoneSchema  // Another instance of the nested form group
      });
    }
    ```

### HTML Structure

When rendering a nested form in HTML:
*   Bind the main form to your `FormGroup` using `[formGroup]="myForm"` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   For the nested sections, instead of `formControlName`, use `formGroupName` on a container element (like a `div`) to connect it to the corresponding nested `FormGroup` in your TypeScript <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   Inside the `formGroupName` context, you can then use `formControlName` for the individual inputs of that nested group <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

```html
<form [formGroup]="myForm">
  <div formGroupName="cellPhone">
    <input formControlName="area">
    <input formControlName="prefix">
  </div>
  <div formGroupName="homePhone">
    <input formControlName="area">
    <input formControlName="prefix">
  </div>
</form>
```

This method is effective for a fixed number of nested groups, but it becomes unmaintainable if the user needs to dynamically add an arbitrary number of fields <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Dynamic Form Arrays (FormArray)

For scenarios where users need to add or remove an unlimited number of fields, such as multiple phone numbers or addresses, Angular provides `FormArray` <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This allows for [[form_validation_and_dynamic_fields | dynamic form fields]] to be added and removed from the form as needed <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. The data structure for a `FormArray` is a nested array of objects <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

### TypeScript Implementation

1.  **Import `FormArray`**: Begin by importing `FormArray` from `@angular/forms` <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

2.  **Initialize the `FormArray`**: In your `FormGroup` definition, set up a property as a `FormArray`, initially empty <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

    ```typescript
    import { FormGroup, FormBuilder, FormArray } from '@angular/forms';

    export class MyFormComponent implements OnInit {
      myForm: FormGroup;

      constructor(private fb: FormBuilder) {}

      ngOnInit() {
        this.myForm = this.fb.group({
          name: '',
          emails: this.fb.array([]) // Initialize as an empty FormArray
        });
      }
    }
    ```

3.  **Create a Getter for the `FormArray`**: A getter is highly recommended to easily access the `FormArray` instance in both TypeScript and HTML, making your code cleaner <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

    ```typescript
    get emails(): FormArray {
      return this.myForm.get('emails') as FormArray;
    }
    ```

4.  **Add a New Field to the `FormArray`**: Create a method to add a new `FormGroup` (representing a single item, e.g., an email field) to the `FormArray`.

    ```typescript
    addEmail() {
      const emailFormGroup = this.fb.group({
        address: ''
      });
      this.emails.push(emailFormGroup); // Use the getter to push a new form group
    }
    ```

5.  **Remove a Field from the `FormArray`**: To delete a field, you can use the `removeAt()` method of `FormArray`, passing the index of the item to be removed <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

    ```typescript
    deleteEmail(index: number) {
      this.emails.removeAt(index);
    }
    ```

### HTML Structure

The HTML for a `FormArray` involves looping over the array's controls:

1.  **Bind the `FormArray` name**: On the container for your dynamic fields, use `formArrayName` to bind to the `FormArray` property defined in TypeScript <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

2.  **Loop with `ngFor`**: Use `*ngFor` to iterate over `formArray.controls`. It's crucial to also track the `index` for each item, as this will be used for binding and deletion <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

3.  **Bind individual `FormGroup`**: Inside the loop, each item is a `FormGroup`, so you'll use `formGroupName` bound to the current `index` of the loop <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

4.  **Individual `formControlName`**: Within each dynamic `FormGroup`, use `formControlName` for the actual input fields, just like in a regular form <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

5.  **Add/Delete Buttons**:
    *   Place an "Add" button outside the loop that triggers the `addEmail()` method <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
    *   Place a "Delete" button inside the loop for each item that triggers the `deleteEmail()` method, passing the `index` of that item <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

```html
<form [formGroup]="myForm">
  <div formArrayName="emails">
    <div *ngFor="let email of emails.controls; let i = index">
      <div [formGroupName]="i">
        <input formControlName="address" placeholder="Email Address">
        <button (click)="deleteEmail(i)">Delete</button>
      </div>
    </div>
  </div>
  <button (click)="addEmail()">Add Email</button>
</form>
```

By combining these techniques, you can build [[introduction_to_reactive_forms_in_angular | reactive forms]] that are both well-organized and highly adaptable to user input <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.