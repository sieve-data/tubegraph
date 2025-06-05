---
title: Recent trend of ditching TypeScript for JavaScript
videoId: 5ChkQKUzDCs
---

From: [[fireship]] <br/> 

The landscape of web development, particularly concerning [[state_of_javascript_in_modern_development | JavaScript]], has seen a notable shift regarding the adoption of [[introduction_to_typescript | TypeScript]]. Initially, [[introduction_to_typescript | TypeScript]] seemed to have achieved widespread victory, but recent developments suggest a more complex picture.

## The Shifting Stance on TypeScript <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>

In 2017, prominent JavaScript developer Kent C. Dodds stated he didn't use [[introduction_to_typescript | TypeScript]] and had no plans to support it <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. By 2019, he expressed concern over the "impassioned love of [[introduction_to_typescript | TypeScript]]" <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. However, by 2023, he capitulated, declaring, "[[introduction_to_typescript | TypeScript]] is one and it's only a matter of time you're using it whether you like it or not" <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This evolution highlights a good developer's willingness to adapt to new tools <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

Despite this sentiment, a significant question has emerged: Did [[introduction_to_typescript | TypeScript]] truly win? <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a> Recently, several large open-source projects have begun to [[alternatives_to_typescript_in_projects | ditch TypeScript]] in favor of vanilla JavaScript <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## History and Adoption of TypeScript <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>

[[history_and_adoption_of_typescript | TypeScript]] was first released by Microsoft in 2012, initially without much attention <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. A few years later, its adoption by the Angular 2 framework was considered controversial <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. By the early 2020s, [[introduction_to_typescript | TypeScript]] had become ubiquitous, converting many of its former critics <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## The Recent Shift: Ditching TypeScript <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>

Just as [[introduction_to_typescript | TypeScript]] reached peak saturation, major libraries like Svelte, Drizzle, and Turbo began [[alternatives_to_typescript_in_projects | removing TypeScript]] from their codebases <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. It's important to clarify that this trend applies to how these libraries are *developed*, not necessarily to end-user applications. For example, Svelte users can still use [[introduction_to_typescript | TypeScript]] within their applications <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Reasons for the Shift

Developers moving away from [[introduction_to_typescript | TypeScript]] are not ignoring the benefits it provides, such as catching runtime errors or improving code refactoring <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Instead, their decisions are based on specific [[criticisms_and_drawbacks_of_using_typescript | drawbacks]].

#### "Type Gymnastics" and Code Pollution

David Heinemeier Hansson (DHH), creator of Ruby on Rails and involved with Turbo, highlighted "type gymnastics" as a primary reason for ditching [[introduction_to_typescript | TypeScript]] in Turbo version 8 <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This refers to the code pollution caused by verbose type declarations, especially when developing libraries <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

> "The main reason they're getting rid of it is not because of the compile step but rather because it pollutes the code with quote type gymnastics." <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>

The developer notes a personal experience working on a library called SvelteFire, where "type gymnastics" are necessary to eliminate IDE squiggly lines, especially when working in strict compiler mode, leading to less elegant code <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The reaction to Turbo's change on GitHub has been a "dumpster fire," with many developers upset their [[introduction_to_typescript | TypeScript]] contributions are now "Dead on Arrival" <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

#### Productivity and No Compile Step

Svelte, another major project, is also moving away from [[introduction_to_typescript | TypeScript]] for practical reasons <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Rich Harris's post explains that Svelte 5 will no longer use [[introduction_to_typescript | TypeScript]], and SvelteKit is already written in plain vanilla JavaScript <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. The main benefit cited is the elimination of a compile step, which significantly boosts productivity for large frameworks <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

#### The Role of JSDoc

Despite moving to plain JavaScript, these projects still gain most of the benefits of [[introduction_to_typescript | TypeScript]] by utilizing JSDoc <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. JSDoc is a standard comment format used to declare types and documentation within regular JavaScript comments <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. These comments can then be used to generate type definition (`.d.ts`) files and, crucially, provide IntelliSense in code editors, allowing developers to understand code and catch bugs early, much like [[introduction_to_typescript | TypeScript]] <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## The Future of Types in JavaScript <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>

While some projects are [[alternatives_to_typescript_in_projects | ditching TypeScript]] for library development, it remains a valuable tool for building full applications with frameworks like SvelteKit or Next.js, where it integrates seamlessly <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. Achieving the same results with JSDoc in such applications would be impractical <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

The "holy war" between [[introduction_to_typescript | TypeScript]] and vanilla JavaScript may eventually conclude <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. There is currently a Stage 1 ECMAScript proposal to natively add optional type annotations to JavaScript, which could render [[introduction_to_typescript | TypeScript]] nearly obsolete <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. This development represents a significant [[future_of_javascript_with_potential_native_type_annotations | future of JavaScript with potential native type annotations]] and could fundamentally change [[trends_in_programming_languages_and_web_development | trends in programming languages and web development]].