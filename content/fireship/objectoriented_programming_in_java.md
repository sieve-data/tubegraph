---
title: Objectoriented programming in Java
videoId: m4-HM_sCvtQ
---

From: [[fireship]] <br/> 

Java is designed for writing verbose, [[objectoriented_and_functional_programming_in_java | object-oriented]] code [00:00:03]. The language forces developers into [[objectoriented_and_functional_programming_in_java | object-oriented programming]] [00:01:35].

## Core Concepts

To understand [[objectoriented_and_functional_programming_in_java | object-oriented programming]] in Java, it is recommended to read [[programming_concepts_and_paradigm | design patterns]] thoroughly [00:01:37].

### Boilerplate

When writing a basic "Hello World" program in Java, developers encounter a significant amount of [[java_as_a_boilerplate_driven_language | boilerplate]] code compared to languages like Python [00:01:47]. This is considered a feature, not a design flaw [00:01:50].

A common first step in Java development is to write a single, large class [00:01:55]. If this becomes problematic, the next step is to break it down into a hierarchy of deeply nested subclasses, which can make future refactoring difficult [00:01:57].

### Basic Program Structure
To say "Hello World" in Java, the following structure is used:
```java
public class YourClassName {
    public static void main(String[] args) {
        System.out.println("Hello world");
    }
}
```
This structure involves creating a class, and within it, the `public static void main(String[] args)` method [00:01:33], [00:01:42].