---
title: Working with functions and arrays in TypeScript
videoId: ahCwqrYpIuM
---

From: [[fireship]] <br/> 

## Functions

Strong typing [[functions_and_closures_in_javascript | functions]] in TypeScript involves specifying types for both their arguments and return values <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### Argument Type Annotation
To strong type function arguments, append a colon and the desired type after the argument name, similar to variable annotation <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. This ensures that only values of the specified type can be passed to the function <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. For example, a function expecting numbers for its arguments will produce a compiler error if strings are passed instead <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

```typescript
function power(x: number, y: number) {
  // ...
}
```

### Return Value Type Annotation
A function's return value can be explicitly typed by adding a colon and the type after the parentheses and before the curly braces of the function body <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. If the function's implicit return type (e.g., a `number` from `Math` operations) does not match the explicitly annotated return type (e.g., `string`), TypeScript will show an error <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

```typescript
function power(x: number, y: number): number {
  return Math.pow(x, y);
}

function powerToString(x: number, y: number): string {
  return Math.pow(x, y).toString(); // Corrected to match return type
}
```

### Void Return Type
For [[functions_and_closures_in_javascript | functions]] that do not return a value, or primarily produce side effects, their return type can be annotated as `void` <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. This is common for event listeners or functions that modify state without explicit return <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

```typescript
function logMessage(message: string): void {
  console.log(message);
}
```

### Optional Function Arguments
Function arguments can be made optional by placing a question mark (`?`) after the argument name and before its type annotation <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

## Arrays

TypeScript provides ways to strong type arrays to ensure they only contain elements of a specific type <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.

### Strong Typing Arrays
To declare an array that holds only numbers, for example, you can specify `number[]` <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Trying to add a value of a different type to such an array will result in an error <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

```typescript
const numbers: number[] = [];
numbers.push(1);
// numbers.push("two"); // Error: Argument of type 'string' is not assignable to parameter of type 'number'.
```

### Arrays of Objects with Interfaces
This type annotation is particularly useful when working with arrays of objects. By using [[typescript_interfaces_and_custom_types | interfaces]] to define the shape of the objects within the array, you can get Intellisense and auto-completion when iterating over them <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

```typescript
interface Person {
  firstName: string;
  lastName: string;
}

const people: Person[] = [
  { firstName: "John", lastName: "Doe" },
  { firstName: "Jane", lastName: "Smith" }
];
```

## Tuples

TypeScript introduces tuples, which are a data structure similar to arrays but with a fixed length where each item in the array has its own specific type <a class="yt-timestamp" data-t="00:09:59">[00:10:06]</a>.

```typescript
type MyList = [string, number, boolean];
const item: MyList = ["hello", 123, true];
```

### Optional Tuple Elements
Similar to function arguments, elements within a tuple can be made optional by appending a question mark (`?`) after their type <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. This means the compiler will not expect these values to be defined upfront <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

```typescript
type OptionalMyList = [string, number?, boolean?];
const item1: OptionalMyList = ["hello"];
const item2: OptionalMyList = ["world", 456];
const item3: OptionalMyList = ["example", 789, false];
```

## Generics

Generics allow you to use a type as a variable internally within a class or [[functions_and_closures_in_javascript | function]] <a class="yt-timestamp" data-t="00:10:32">[00:10:37]</a>. This is useful for creating flexible components that can work with various data types without sacrificing type safety <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

For example, an RxJS `Observable` class uses generics (represented by `T`) to specify the internal type of the value it observes <a class="yt-timestamp" data-t="00:10:41">[00:10:44]</a>.

```typescript
// Conceptual example of an Observable class using generics
class Observable<T> {
  private value: T;
  // ...
}

// Later, you can specify the actual type
const numberObservable: Observable<number> = new Observable<number>();
const personObservable: Observable<Person> = new Observable<Person>();
```

TypeScript can also implicitly infer the generic type if a value is provided during initialization <a class="yt-timestamp" data-t="00:11:03">[00:11:06]</a>. While creating generics can be complex, you will more often use existing generics in libraries <a class="yt-timestamp" data-t="00:11:11">[00:11:12]</a>.