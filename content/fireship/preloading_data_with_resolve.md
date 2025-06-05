---
title: Preloading Data with Resolve
videoId: Np3ULAMqwNo
---

From: [[fireship]] <br/> 

The Angular Router provides a powerful `Resolve` interface that allows you to preload data for a route before the component is even activated <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. This ensures that all necessary data is available when the component loads, leading to a smoother user experience and cleaner component code.

## Why Use Resolve?

Previously, data might have been fetched directly within a component, often by subscribing to route parameter changes and then fetching data based on those parameters <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. While functional, this approach can lead to duplicated code if the same data needs to be preloaded on multiple different components <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. The `Resolve` interface offers a reusable solution to this problem <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

## Generating a Resolver

A resolver is essentially an Angular service that implements the `Resolve` interface <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. You can generate one using the Angular CLI:

```bash
ng generate guard preload
```
<a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>

Although generated as a "guard", you will implement the `Resolve` interface instead of `CanActivate` <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

## Implementing the Resolve Interface

The `Resolve` interface requires a `resolve` method that returns the actual data to be preloaded. This data can be a primitive value, an `Observable`, or a [[using_promises_for_asynchronous_operations | Promise]] <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. Typically, when fetching from an external API, it will return an `Observable` <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

```typescript
import { Injectable } from '@angular/core';
import { Resolve, ActivatedRouteSnapshot } from '@angular/router';
import { AngularFirestore } from '@angular/fire/firestore';
import { Observable } from 'rxjs';
import { first } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class PreloadGuard implements Resolve<any> { // You can strong type 'any'
  constructor(private afs: AngularFirestore) {}

  resolve(route: ActivatedRouteSnapshot): Observable<any> {
    const animalName = route.paramMap.get('name'); // Access URL parameter
    return this.afs.collection('animals').doc(animalName).valueChanges().pipe(
      first() // Essential for real-time streams like Firebase to complete
    );
  }
}
```
<a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>
<a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>
<a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>
<a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>
<a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>

It's crucial to `pipe` the `first()` operator when dealing with real-time data streams (e.g., from [[optimizing_performance_with_virtual_scroll_and_firebase | Firebase]]) to ensure the `Observable` completes <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. The `ActivatedRouteSnapshot` provides access to route information, including dynamic URL parameters <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

## Configuring the Router

To apply the resolver to a route, add the `resolve` property to the route configuration in your `app-routing.module.ts`:

```typescript
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AnimalDetailComponent } from './animal-detail/animal-detail.component';
import { PreloadGuard } from './preload.guard'; // Import your resolver

const routes: Routes = [
  {
    path: 'animals',
    children: [
      {
        path: ':name',
        component: AnimalDetailComponent,
        resolve: {
          animal: PreloadGuard // 'animal' is the key to access data in the component
        }
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```
<a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>

The key assigned to `PreloadGuard` (e.g., `animal`) will be used to retrieve the preloaded data in the component.

## Accessing Preloaded Data in the Component

Once the resolver is configured, the preloaded data becomes available on the `ActivatedRoute`'s `data` property in your component. You can access it like this:

```typescript
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-animal-detail',
  templateUrl: './animal-detail.component.html',
  styleUrls: ['./animal-detail.component.scss']
})
export class AnimalDetailComponent implements OnInit {
  animal: any;

  constructor(private route: ActivatedRoute) { }

  ngOnInit(): void {
    // Access the preloaded data using the key defined in the router config
    this.route.data.subscribe(data => {
      this.animal = data.animal;
    });
  }
}
```
<a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>
<a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>

This approach allows for cleaner component code, as the data fetching logic is isolated and made reusable across multiple routes <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.