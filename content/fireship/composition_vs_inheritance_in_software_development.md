---
title: Composition vs Inheritance in software development
videoId: fsVL_xrYO0w
---

From: [[fireship]] <br/> 
[[design_techniques_in_app_development | Design techniques]] like composition and inheritance are fundamental in software development, particularly for code reusability <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. While opinions on which is better can be strong, there's no single "correct" answer, as each approach involves trade-offs depending on the situation <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

## Inheritance
Inheritance is a concept where a class (child class) derives properties and methods from another class (parent or base class) <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. Child classes can then override or extend this inherited functionality with their own custom behaviors <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

### Inheritance Example in TypeScript
Consider a `Human` class with a `name` property and a `sayHi` method <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

```typescript
class Human {
  constructor(public name: string) {}
  sayHi() {
    return `Hello, my name is ${this.name}`;
  }
}
```
<a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>

To create a `SuperHuman` character that has all human abilities plus something extra, you can use inheritance <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. In TypeScript, this is done with the `extends` keyword <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. The `super()` call in the constructor executes the parent class's constructor, initializing inherited properties like `name` <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

```typescript
class SuperHuman extends Human {
  constructor(name: string) {
    super(name); // Call parent class constructor
  }
  superPower() {
    return `${this.name} has super powers!`;
  }
}

const regularHuman = new Human("Alice");
console.log(regularHuman.sayHi()); // Output: Hello, my name is Alice
const superHuman = new SuperHuman("Bob");
console.log(superHuman.sayHi());    // Output: Hello, my name is Bob
console.log(superHuman.superPower()); // Output: Bob has super powers!
```
<a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>

### Pros and Cons of Inheritance
*   **Pros**: Can be effective in the right scenarios <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Cons**: Avoid creating deeply nested class hierarchies, as this can make debugging very difficult when issues arise in the middle of the hierarchy <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

## Composition
Composition offers an alternative to inheritance <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. Instead of building from a large base class, composition breaks down interfaces and logic into many smaller, independent pieces <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. These smaller pieces are then combined to build larger functions or objects, allowing for flexible aggregation of behaviors <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

### Composition Example in TypeScript (Mixins)
One way to apply composition is by concatenating objects, often referred to as the [[understanding_creational_patterns | Mixin pattern]] <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. This involves decoupling properties or behaviors into smaller objects or functions that return objects, which can then be merged together to form a final composite function or object <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

While the raw Mixin pattern might sacrifice some ergonomics of class-based [[Object Oriented Programming with TypeScript | Object-Oriented Programming]], TypeScript provides flexibility to use mixins in a class-based format <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

This approach uses small "behavior classes" that define individual behaviors rather than trying to encapsulate everything in a single class <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. These classes focus on *what something does* rather than *what something is* <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

```typescript
// Helper function from TypeScript Docs to apply mixins
function applyMixins(derivedCtor: any, constructors: any[]) {
  constructors.forEach((baseCtor) => {
    Object.getOwnPropertyNames(baseCtor.prototype).forEach((name) => {
      Object.defineProperty(
        derivedCtor.prototype,
        name,
        Object.getOwnPropertyDescriptor(baseCtor.prototype, name) ||
          Object.create(null)
      );
    });
  });
}

// Behavior classes
class SayHi {
  sayHi() {
    return "Hello!";
  }
}

class SuperPower {
  superPower() {
    return "I have super powers!";
  }
}

// Combine behaviors using 'implements' and applyMixins
class Superhero implements SayHi, SuperPower {
  // Required boilerplate: manually declare the methods from the mixins
  sayHi!: () => string;
  superPower!: () => string;

  constructor(public name: string) {}
}

applyMixins(Superhero, [SayHi, SuperPower]);

const hero = new Superhero("Captain Code");
console.log(hero.sayHi());       // Output: Hello!
console.log(hero.superPower());  // Output: I have super powers!
```
<a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>

In this example, the `Superhero` class `implements` the `SayHi` and `SuperPower` classes <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. The `implements` keyword means you're concerned only with the *interface* of the classes, not their underlying code <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. The `applyMixins` function then takes these interfaces and applies their code to the `Superhero` class <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

## Hot Dog Analogy
The debate between composition and inheritance can be humorously illustrated with the question, "Is a hot dog a sandwich?" <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>:
*   **Inheritance View**: If you use inheritance, a hot dog would have to inherit from a base "sandwich" class, meaning it *is* a sandwich <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **Composition View**: If you use composition, you simply pull in the components: a hot dog and a bun. Therefore, it is *not* a sandwich, but a distinct combination of elements <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.