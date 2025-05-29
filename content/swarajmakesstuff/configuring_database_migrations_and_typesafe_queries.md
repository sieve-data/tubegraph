---
title: Configuring Database Migrations and Typesafe Queries
videoId: VuuAAjkLRZs
---

From: [[swarajmakesstuff]] <br/> 

This guide outlines the process of integrating Next.js with [[using_drizzle_orm_with_cloudflare_d1 | Drizzle ORM]] and [[using_drizzle_orm_with_cloudflare_d1 | Cloudflare D1]] for database management, focusing on migrations and typesafe queries <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. [[using_drizzle_orm_with_cloudflare_d1 | Cloudflare D1]] is described as a very fast SQL database <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Initial Setup and Caveats

To bind a [[using_drizzle_orm_with_cloudflare_d1 | Cloudflare D1]] database directly with Next.js using server actions or API routes, it's necessary to use Cloudflare Pages <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. The demonstration proceeds by installing Next.js using Cloudflare Pages as a pre-demo <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### Step 1: Initialize Next.js Project with Cloudflare Pages

First, grab the command from Cloudflare Pages to initialize the project <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. An example project name used is `drizzle D1 demo` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

```bash
# Example command (replace with actual Cloudflare Pages command)
npx create-next-app --template @cloudflare/nextjs drizzle-D1-demo
```

It's recommended to connect your project to GitHub via the Cloudflare Pages dashboard for deployment, rather than deploying directly from the initial setup command, as existing projects might not easily connect to GitHub <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Step 2: Set Up [[setting_up_cloudflare_d1_and_wrangler_for_local_development | Wrangler]]

Before creating a [[using_drizzle_orm_with_cloudflare_d1 | Cloudflare D1]] database, ensure [[setting_up_cloudflare_d1_and_wrangler_for_local_development | Wrangler]] is set up <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. If not installed, run `npm install wrangler` <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

To verify [[setting_up_cloudflare_d1_and_wrangler_for_local_development | Wrangler]] installation and authenticate:
```bash
npx wrangler version <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>
npx wrangler who am I <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>
```
These commands ensure [[setting_up_cloudflare_d1_and_wrangler_for_local_development | Wrangler]] is connected to your Cloudflare account with necessary permissions <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

### Step 3: Create [[using_drizzle_orm_with_cloudflare_d1 | Cloudflare D1]] Database

Create a [[using_drizzle_orm_with_cloudflare_d1 | D1]] database using [[setting_up_cloudflare_d1_and_wrangler_for_local_development | Wrangler]] <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>:
```bash
npx wrangler D1 create drizzle-demo-DB --migrations-directory=drizzle <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>
```
The `--migrations-directory=drizzle` flag points to the `drizzle` folder where migration files will be stored <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### Step 4: Install [[using_drizzle_orm_with_cloudflare_d1 | Drizzle ORM]] and Drizzle Kit

Install [[using_drizzle_orm_with_cloudflare_d1 | Drizzle ORM]] and Drizzle Kit <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>:
```bash
pnpm add drizzle-orm drizzle-kit <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>
```

### Step 5: Configure Database Connection (`db.ts`)

Create a database connection file, e.g., `app/server/db.ts` <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
Import `D1` from `drizzle-orm/cloudflare-d1` and pass it to [[using_drizzle_orm_with_cloudflare_d1 | Drizzle ORM]] <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

For typesafety, generate types for your [[using_drizzle_orm_with_cloudflare_d1 | D1]] database bindings <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. This command is typically found in `env.d.ts` after Cloudflare project setup <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
```bash
npx @cloudflare/nextjs-init <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>
```
This generates `CF` types <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. To make `process.env` typesafe, create `globals.d.ts` <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
```typescript
// globals.d.ts
declare global {
  namespace NodeJS {
    interface ProcessEnv {
      DB: D1Database; // This extends process.env to include DB as D1Database
    }
  }
}
```
Now, `process.env.DB` will be typesafe <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

```typescript
// app/server/db.ts
import { drizzle } from 'drizzle-orm/cloudflare-d1';
import * as schema from './schema'; // Import your schema

export const db = drizzle(process.env.DB, { schema }); <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a><a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>
```

### Step 6: Define Database Schema (`schema.ts`)

Create a schema file, e.g., `app/server/schema.ts` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
Define your tables and columns using [[using_drizzle_orm_with_cloudflare_d1 | Drizzle ORM]] functions.

Example `todoTable` schema:
```typescript
// app/server/schema.ts
import { sql } from 'drizzle-orm';
import { integer, text, sqliteTable, boolean } from 'drizzle-orm/sqlite-core';

export const todoTable = sqliteTable('todos', {
  id: integer('id').primaryKey({ autoIncrement: true }), <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a><a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>
  title: text('title').notNull(),
  completed: boolean('completed').default(false), <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>
  createdAt: text('created_at').default(sql`CURRENT_TIMESTAMP`).notNull(), <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>
  updatedAt: text('updated_at').default(sql`CURRENT_TIMESTAMP`).notNull().$onUpdate(() => sql`CURRENT_TIMESTAMP`), <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>
});
```

### Step 7: Configure Drizzle for Local and Remote Development

When developing locally, [[setting_up_cloudflare_d1_and_wrangler_for_local_development | Wrangler]] and Cloudflare use MiniFlare to create an SQLite database on your local machine, rather than querying a remote database <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. To manage this properly with [[using_drizzle_orm_with_cloudflare_d1 | Drizzle ORM]], configure `drizzle.config.ts`.

Create a helper function to get the local [[using_drizzle_orm_with_cloudflare_d1 | D1]] database path <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>:
```typescript
// drizzle.config.ts (or a helper file)
import { Config } from 'drizzle-kit';
import path from 'path';
import fs from 'fs';

function getLocalD1DatabasePath() {
  const wranglerTomlPath = path.resolve(process.cwd(), 'wrangler.toml');
  if (fs.existsSync(wranglerTomlPath)) {
    const wranglerConfig = fs.readFileSync(wranglerTomlPath, 'utf-8');
    const dbNameMatch = wranglerConfig.match(/database_name = "(.*?)"/);
    if (dbNameMatch && dbNameMatch[1]) {
      const dbDir = path.resolve(process.cwd(), '.wrangler', 'state', 'v3', 'd1');
      const dbPath = path.join(dbDir, dbNameMatch[1] + '.sqlite');
      return dbPath;
    }
  }
  return undefined;
}

export default {
  schema: './app/server/schema.ts',
  out: './drizzle',
  dialect: 'sqlite',
  dbCredentials: process.env.NODE_ENV === 'production' ? {
    accountId: process.env.CLOUDFLARE_ACCOUNT_ID!, <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>
    databaseId: process.env.CLOUDFLARE_D1_DATABASE_ID!,
    token: process.env.CLOUDFLARE_D1_API_TOKEN!,
  } : {
    url: getLocalD1DatabasePath() || './.wrangler/state/v3/d1/drizzle-demo-DB.sqlite', // Default local path if not found
  },
} satisfies Config;
```
For remote (production) environment, the configuration will use `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_D1_DATABASE_ID`, and `CLOUDFLARE_D1_API_TOKEN` <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. The local environment will use the `url` pointing to the SQLite file created by MiniFlare <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. The local database path is found inside the `.wrangler` folder <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

### Step 8: Add Drizzle Scripts to `package.json`

Add scripts to your `package.json` for managing migrations <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>:
```json
// package.json
"scripts": {
  "db:generate": "drizzle-kit generate:sqlite --config drizzle.config.ts", <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>
  "db:studio": "drizzle-kit studio --config drizzle.config.ts", <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>
  "db:migrate:local": "drizzle-kit migrate:sqlite --config drizzle.config.ts --url ./.wrangler/state/v3/d1/drizzle-demo-DB.sqlite", <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>
  "db:migrate:remote": "drizzle-kit migrate:sqlite --config drizzle.config.ts", <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
}
```

### Step 9: Generate and Run Migrations

1.  **Generate SQL migration file:**
    ```bash
    pnpm db:generate <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>
    ```
    This command will create a new migration file under the `drizzle` folder based on your schema changes <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. Ensure your schema file is correctly located (e.g., `src/app/server/schema.ts` if moved from `app`) <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

2.  **Run local migrations:**
    ```bash
    pnpm db:migrate:local <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>
    ```
    This applies the generated migrations to your local [[using_drizzle_orm_with_cloudflare_d1 | D1]] SQLite database <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

### Step 10: Check Database Schema Locally with Drizzle Studio

To view your local database schema, use Drizzle Studio <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>:
```bash
pnpm db:studio <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>
```
Note that Drizzle Studio for local [[using_drizzle_orm_with_cloudflare_d1 | D1]] databases requires `better-sqlite3` as it's interacting with a local SQLite file, not [[using_drizzle_orm_with_cloudflare_d1 | Cloudflare D1]] directly <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

### Step 11: Set Up Production Environment Variables

For production migrations, you need `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_D1_DATABASE_ID`, and `CLOUDFLARE_D1_API_TOKEN` <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

1.  **Database ID:** This can be copied from your `wrangler.toml` file or the Cloudflare dashboard <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.

2.  **API Token:**
    *   Log in to your Cloudflare account <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
    *   Go to "My Profile" > "API Tokens" <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
    *   Create a custom token <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.
    *   Add "Account" permissions: "[[using_drizzle_orm_with_cloudflare_d1 | D1]]" (Edit) and "Cloudflare Pages" (Edit) <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
    *   Select specific accounts if desired <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
    *   Copy the generated token <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.

3.  **Account ID:**
    *   Go to Cloudflare Pages or Workers & Pages <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
    *   Click on "Overview" to find your Account ID <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.

Set these as environment variables in your deployment environment. Once configured, you can run `pnpm db:migrate:remote` to apply migrations to your production [[using_drizzle_orm_with_cloudflare_d1 | D1]] database. You can also view your production database via the Cloudflare D1 Dashboard <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.