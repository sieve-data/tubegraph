---
title: Spread syntax for objects and arrays
videoId: Mus_vwhTCq0
---

From: [[fireship]] <br/> 

The spread syntax (`...`) in [[Modern JavaScript array methods | modern JavaScript]] provides a concise and efficient way to work with objects and arrays, particularly when combining or creating new data structures without mutating original ones <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.

## Objects

When combining or updating properties of objects, traditional methods can be verbose and lead to mutation of the original object <a class="yt-timestamp" data-t="06:29:31">[06:29:31]</a>.

*   **Problem with direct assignment**: Directly redefining properties one by one on an existing object is verbose and mutates the original object <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>. This is undesirable if you want to maintain immutability, such as representing progressive states of an object (e.g., a Pokémon leveling up) <a class="yt-timestamp" data-t="06:39:00">[06:39:00]</a>.
*   **`Object.assign`**: A better alternative is `Object.assign()`, which merges properties from source objects into a target object. It can be used to combine objects or update a single property, merging from left to right <a class="yt-timestamp" data-t="06:46:04">[06:46:04]</a>.

    ```javascript
    // Example: Combining objects
    const pokemon = { name: 'Pikachu' };
    const stats = { hp: 35, attack: 55 };
    const leveledUpPokemon = Object.assign({}, pokemon, stats);

    // Example: Updating a single property
    const updatedPokemon = Object.assign({}, pokemon, { level: 2 });
    ```
*   **Spread Syntax for Objects**: The spread syntax offers a more concise approach for creating new objects from existing ones <a class="yt-timestamp" data-t="07:00:20">[07:00:20]</a>. By creating a new object and placing existing objects within it using three dots (`...`), a new object is composed from left to right <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>. Properties farthest to the right will have priority if there are overlaps <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>.

    ```javascript
    const pokemon = { name: 'Pikachu' };
    const stats = { hp: 35, attack: 55 };

    // Combine objects
    const leveledUpPokemon = { ...pokemon, ...stats };

    // Update a single property
    const updatedPokemon = { ...pokemon, level: 2 };
    ```

    The spread syntax for objects is primarily syntactic sugar that enhances code readability and maintainability <a class="yt-timestamp" data-t="07:15:00">[07:15:00]</a>.

## Arrays

The spread syntax can also be applied to arrays for adding or combining elements in a more concise way than traditional methods like `push` or `shift` <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>.

*   **Old-school `push`**: Traditionally, to add multiple items to an array, one would use `array.push()` for each item <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>.
*   **Spread Syntax for Arrays**: This allows you to reduce multiple lines of code into a single line <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>.
    *   **Appending (like `push`)**: By placing the spread syntax (`...`) of the original array at the beginning of a new array literal, new items are appended to the end <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>.

        ```javascript
        const originalArray = ['apple', 'banana'];
        const newArray = [...originalArray, 'cherry', 'date'];
        // newArray is ['apple', 'banana', 'cherry', 'date']
        ```
    *   **Prepending (like `unshift`)**: By placing the spread syntax of the original array at the end of a new array literal, new items are prepended to the beginning <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>.

        ```javascript
        const originalArray = ['apple', 'banana'];
        const newArray = ['cherry', 'date', ...originalArray];
        // newArray is ['cherry', 'date', 'apple', 'banana']
        ```
    *   **Splicing in the middle**: The spread syntax offers flexibility to insert elements anywhere within an array <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>.

        ```javascript
        const originalArray = ['apple', 'banana', 'date'];
        const newArray = ['item1', ...originalArray.slice(0, 1), 'item2', ...originalArray.slice(1)];
        // or
        const newArray2 = [...originalArray.slice(0, 1), 'inserted', ...originalArray.slice(1)];
        // newArray2 is ['apple', 'inserted', 'banana', 'date']
        ```

*   **Trailing Commas**: In [[Modern JavaScript array methods | modern JavaScript]], trailing commas (e.g., `['a', 'b',]`) are now allowed and are considered good practice. They can reduce the number of lines that appear as changed in Git commits when adding new items to the end of a list <a class="yt-timestamp" data-t="08:04:00">[08:04:00]</a>.