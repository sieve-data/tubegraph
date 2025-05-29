---
title: Using Drizzle ORM with Cloudflare D1
videoId: VuuAAjkLRZs
---

From: [[swarajmakesstuff]] <br/> 

This guide outlines the process of integrating Next.js with Drizzle ORM and Cloudflare D1, a fast SQL database provided by Cloudflare <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Initial Setup

To begin, you need to install Next.js, Drizzle, and set up Cloudflare D1 <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

### Cloudflare Pages Requirement
A key point to note is that to bind your D1 database, you will typically need to use [[deploying_nextjs_projects_with_cloudflare_pages | Cloudflare Pages]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. If you're using Next.js directly with server actions or API routes, Cloudflare Pages is generally required for D1 integration <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The speaker initiated the Next.js installation using Cloudflare Pages as a pre-demo <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### Project Initialization
To start, grab the command from Cloudflare Pages to create your project <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. An example project name used was `drizzle-D1-demo` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Wrangler Setup
Ensure that Wrangler, the Cloudflare CLI tool, is already set up <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. If not, install it using `npm install wrangler` <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. You can check your Wrangler version with `npx wrangler version` <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a> and connect it to your account using `npx wrangler whoami` to grant necessary permissions <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

### GitHub Integration Considerations
Deploying an application directly via Wrangler might present issues with connecting to GitHub directly from an existing Cloudflare Pages project <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. It's often recommended to connect through GitHub via the Cloudflare Pages dashboard for deployment <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Creating the D1 Database

Once Wrangler is set up, you can create your D1 database.
Use the command: `npx wrangler d1 create <database-name> --migrations-directory <migrations-folder-name>` <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
For instance, `npx wrangler d1 create drizzle-demo-DB --migrations-directory drizzle` points to a `drizzle` folder for migrations <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## Installing Drizzle ORM

Install Drizzle ORM and Drizzle Kit using pnpm: `pnpm add drizzle-orm drizzle-kit` <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## Configuring Drizzle and D1 Connection

### Database Connection File (`db.ts`)
Create a file, e.g., `app/server/db.ts`, to set up the Drizzle connection <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
You'll import `D1Database` from `wrangler` and initialize Drizzle with it:
```typescript
import { D1Database } from "@cloudflare/workers-types";
import { drizzle } from "drizzle-orm/d1";
import * as schema from "./schema"; // Assuming schema.ts is in the same directory

declare global {
  namespace NodeJS {
    interface ProcessEnv {
      DB: D1Database;
    }
  }
}

export const db = drizzle(process.env.DB, { schema });
```
The `process.env.DB` must be properly type-safe <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. You can generate Cloudflare types by running `pnpm cf-types` <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### Global Types (`globals.d.ts`)
Create `globals.d.ts` to extend `process.env`, allowing direct access to environment variables like `process.env.DB` with type safety <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### Schema Definition (`schema.ts`)
Create `app/server/schema.ts` to define your database tables. An example `todoTable` is shown:
```typescript
import { sqliteTable, text, integer } from "drizzle-orm/sqlite-core";

export const todoTable = sqliteTable("todos", {
  id: integer("id", { mode: "number" }).primaryKey({ autoIncrement: true }),
  title: text("title").notNull(),
  completed: integer("completed", { mode: "boolean" }).default(false).notNull(),
  createdAt: integer("created_at", { mode: "timestamp" }).notNull().default(new Date().getTime()),
  updatedAt: integer("updated_at", { mode: "timestamp" }).notNull().$onUpdate(() => new Date().getTime()),
});
```
This schema includes auto-incrementing IDs <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>, `createdAt` with a default value <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>, and `updatedAt` that updates on change <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

## Managing Local and Remote Development

When developing locally, Wrangler or Cloudflare uses MiniFlare to create an SQLite database on your local machine, rather than querying a remote D1 database <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. To manage Drizzle migrations and queries properly for both local and remote environments, you'll need to configure Drizzle to get the correct database URL.

### Drizzle Configuration (`drizzle.config.ts`)
The `drizzle.config.ts` needs to differentiate between local and production environments:
```typescript
// Example snippet
import { getLocalD1Database } from "./utils"; // Placeholder for a utility to get local D1 path

export default {
  schema: "./src/app/server/schema.ts", // or your schema path
  out: "./drizzle", // migrations output directory
  driver: "d1-http", // or 'sqlite' for local development
  dbCredentials: {
    // For local development, get the path from .wrangler/state/v3/d1
    url: process.env.NODE_ENV === "production" ? undefined : getLocalD1Database(),
    accountId: process.env.CLOUDFLARE_ACCOUNT_ID,
    databaseId: process.env.CLOUDFLARE_D1_DATABASE_ID,
    token: process.env.CLOUDFLARE_D1_API_TOKEN,
  },
};
```
The `getLocalD1Database` utility would read the database path from the `.wrangler` folder <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. For production, it checks `CLOUDFLARE_D1_ACCOUNT_ID`, `CLOUDFLARE_D1_DATABASE_ID`, and `CLOUDFLARE_D1_API_TOKEN` <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

### Environment Variables for Production
You will need the following environment variables for production:
*   `CLOUDFLARE_D1_DATABASE_ID`: This can be found in the Cloudflare dashboard under your D1 database <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
*   `CLOUDFLARE_ACCOUNT_ID`: Go to your Cloudflare dashboard, click on "Workers & Pages", then "Overview" to find your Account ID <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   `CLOUDFLARE_D1_API_TOKEN`:
    1.  Log into your Cloudflare account <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.
    2.  Go to "My Profile" > "API Tokens" <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
    3.  Create a custom token <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
    4.  Add permissions: "Account -> Account Settings" (Read) and "Account -> D1" (Edit) are important <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
    5.  Select your specific account for resources <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
    6.  Copy the generated token <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.

## Database Migrations

Drizzle Kit helps manage database migrations.

### Scripts
Add the following scripts to your `package.json` for database operations:
*   `db:generate`: Generates SQL migration files.
*   `db:studio`: Opens Drizzle Studio for local database inspection.
*   `db:migrate:local`: Runs migrations against your local D1 database.
*   `db:migrate:remote`: Runs migrations against your remote D1 database.

```json
"scripts": {
  "db:generate": "drizzle-kit generate:sqlite --schema=src/app/server/schema.ts --out=drizzle",
  "db:studio": "drizzle-kit studio",
  "db:migrate:local": "npx wrangler d1 migrations apply drizzle-demo-DB --local",
  "db:migrate:remote": "npx wrangler d1 migrations apply drizzle-demo-DB"
}
```

### Generating Migrations
Run `pnpm db:generate` to generate the SQL migration file based on your schema <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. The output will be in the `drizzle` folder <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. Ensure your schema file path is correct, e.g., if it's under `app/server/schema.ts`, you might need to adjust the path in the script <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

### Running Local Migrations
To apply migrations to your local D1 database, use `pnpm db:migrate:local` <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. This will update the local SQLite database managed by MiniFlare.

### Checking Local Database with Drizzle Studio
You can inspect your local database using Drizzle Studio by running `pnpm db:studio` <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. Note that Drizzle Studio requires `better-sqlite3` because it connects to your local SQLite database, not directly to D1 <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

### Running Remote Migrations
To apply migrations to your deployed Cloudflare D1 database, use `pnpm db:migrate:remote` <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.