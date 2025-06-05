---
title: Prototype pattern
videoId: tv-_1er1mWI
---

From: [[fireship]] <br/> 

The Prototype pattern is described as a "fancy word for clone" <a class="yt-timestamp" data-t="02:26:01">[02:26:01]</a>. It provides an alternative approach to traditional class-based inheritance in object-oriented programming <a class="yt-timestamp" data-t="02:40:48">[02:40:48]</a>.

## How it Works

Instead of inheriting functionality from a class, the Prototype pattern dictates that functionality comes from an object that has already been created <a class="yt-timestamp" data-t="02:44:26">[02:44:26]</a>. This approach creates a "flat prototype chain," which simplifies sharing functionality between objects <a class="yt-timestamp" data-t="02:47:04">[02:47:04]</a>. It is particularly useful in dynamic languages like [[JavaScript language quirks | JavaScript]] <a class="yt-timestamp" data-t="02:51:56">[02:51:56]</a>.

## Prototypal Inheritance in JavaScript

[[JavaScript language quirks | JavaScript]] supports prototypal inheritance natively <a class="yt-timestamp" data-t="02:54:19">[02:54:19]</a>.

### Creating Objects with Prototypes

To create a new object based on an existing prototype object, you can use `Object.create()` <a class="yt-timestamp" data-t="03:02:43">[03:02:43]</a>.

For example, given a `zombie` object with an `eatBrains` method <a class="yt-timestamp" data-t="02:57:33">[02:57:33]</a>:
```javascript
const zombie = {
  eatBrains: () => console.log('nom nom nom')
};
```
A new object can be created using `Object.create()`, passing the `zombie` as its prototype <a class="yt-timestamp" data-t="03:04:14">[03:04:14]</a>. Additional properties for the new object, like `name`, can also be specified <a class="yt-timestamp" data-t="03:07:38">[03:07:38]</a>.
```javascript
const newZombie = Object.create(zombie, {
  name: { value: 'Alice' }
});
```
When `newZombie` is logged, only its `name` property will be visible, not the `eatBrains` method <a class="yt-timestamp" data-t="03:11:46">[03:11:46]</a>. However, calling `newZombie.eatBrains()` will still work because [[JavaScript language quirks | JavaScript]] traverses up the prototype chain to find methods or properties on parent objects <a class="yt-timestamp" data-t="03:17:15">[03:17:15]</a>.

### Accessing the Prototype

You can obtain the prototype of an object using the `__proto__` property <a class="yt-timestamp" data-t="03:26:06">[03:26:06]</a>. However, this is not considered a modern best practice <a class="yt-timestamp" data-t="03:29:48">[03:29:48]</a>. The recommended way to get an object's prototype is by using `Object.getPrototypeOf()` <a class="yt-timestamp" data-t="03:31:02">[03:31:02]</a>.

### Classes and Prototypes

In [[JavaScript language quirks | JavaScript]], the `prototype` property of a class refers to its constructor <a class="yt-timestamp" data-t="03:37:04">[03:37:04]</a>. While it's possible to extend a class with additional functions via its `prototype`, this is generally considered a bad practice <a class="yt-timestamp" data-t="03:42:04">[03:42:04]</a>.