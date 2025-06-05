---
title: Functional programming languages and their features
videoId: pEfrdAtAmqk
---

From: [[fireship]] <br/> 

Functional programming languages represent a paradigm where developers seek an alternative to "big, heavy object-oriented languages" by focusing on a "better way" to structure code <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This approach forms a significant tier within the programming language landscape <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Core Concepts of Functional Programming

Instead of relying on classes, inheritance, and complex design patterns, the primary abstraction in functional programming is the [[functions_and_closures_in_javascript | function]] <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. Key characteristics include:
*   **Immutability:** Variables are designed to be immutable <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **No Side Effects:** Functions aim to have no side effects, meaning they don't modify state outside their scope <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Monads:** A concept that helps manage side effects and composition, described simply as "a monoid in the category of n-functors" <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **Higher-Order Functions:** Functions that can take other functions as arguments or return them as results, pioneered by languages like Lisp <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

Despite these limitations, it is possible to build almost anything with functional programming, though it doesn't represent the majority of production code <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

## Notable Functional Programming Languages

### Haskell
Haskell is the most renowned purely functional language <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. It was inspired by the Miranda language and named after mathematician Haskell Curry <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. Variables in Haskell are immutable, and functions are designed to have no side effects <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. Haskell also influenced the polymorphic type system used by other statically typed functional languages <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

### F-sharp (F#)
Developed by Microsoft, F# is described as a functional "sister language" to [[c_sharp_in_object_oriented_and_functional_programming | C#]] <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. Unlike Haskell, F# is not purely functional; it also supports imperative and [[c_sharp_in_object_oriented_and_functional_programming | object-oriented programming]], making it more accessible to developers from other paradigms <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Scala
Scala is presented as an alternative to Java for developers seeking a more modern approach <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. Like F#, Scala supports both [[objectoriented_and_functional_programming_in_java | object-oriented and functional programming]] paradigms <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. It runs on the Java Virtual Machine (JVM) and is statically typed <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### Clojure
Clojure is another JVM language that stands out as both functional and dynamic <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Its dynamic nature makes it well-suited for rapid development, though with a trade-off in type safety compared to statically typed languages <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. It was also inspired by Lisp <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

### OCaml
OCaml is a functional language used extensively at Facebook <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. It pioneered the polymorphic type system, which has been adopted by other statically typed functional languages like Haskell <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

### Elixir
Elixir features a "very nice Ruby-like syntax" and is capable of building high-performance, real-time web applications <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### Elm
Elm is a purely functional language that compiles to [[state_of_javascript_in_modern_development | JavaScript]] <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. It is used to build front-end user interfaces and is notable for its ability to produce UIs with "zero runtime errors" <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

### Erlang
Erlang is a concurrent functional programming language that has historically powered the entire telecom industry and remains in use today <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

### Lisp
Invented in 1958, Lisp pioneered many ideas now commonplace in computer science, including dynamic typing, higher-order functions, recursion, and the Read-Eval-Print Loop (REPL) <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. It inspired several other languages, including Racket, Scheme, [[functions_and_closures_in_javascript | Clojure]], and to some extent, [[javascript_language_quirks | JavaScript]] <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.