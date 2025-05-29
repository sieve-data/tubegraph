---
title: Setting Up Cloudflare D1 and Wrangler for Local Development
videoId: VuuAAjkLRZs
---

From: [[swarajmakesstuff]] <br/> 

This guide outlines the process of integrating [[integrating_cloudflare_d1_with_nextjs | Next.js]] with Cloudflare D1, a fast SQL database, and Drizzle ORM for local development.

## Prerequisites <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>

Before proceeding, ensure you have Cloudflare Wrangler set up. If not, install it globally:
```bash
npm install -g wrangler <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>
```
You can verify your Wrangler installation by running:
```bash
npx wrangler version <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>
```
To connect Wrangler to your Cloudflare account and grant necessary permissions, use:
```bash
npx wrangler who am I <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>
```

## Initializing a Project with Cloudflare Pages <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>

When binding a D1 database directly with [[integrating_cloudflare_d1_with_nextjs | Next.js]] server actions or API routes, you need to use [[deploying_nextjs_projects_with_cloudflare_pages | Cloudflare Pages]] for deployment <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

To start a new project, use the command provided by [[deploying_nextjs_projects_with_cloudflare_pages | Cloudflare Pages]] <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. For example, to create a project named `drizzle-D1-demo`:
```bash
# Example command (replace with actual Cloudflare Pages init command)
# npx create-next-app --template cloudflare-pages drizzle-D1-demo
```
During setup, you can opt out of ESLint if desired <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

> [!CAUTION] GitHub Integration Caveat <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
> As of the recording, deploying a project directly from the command line does not allow connecting it to GitHub automatically. It's recommended to go to the [[deploying_nextjs_projects_with_cloudflare_pages | Cloudflare Pages]] dashboard and connect your project via GitHub there after initialization <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

Navigate into your newly created project directory:
```bash
cd drizzle-D1-demo <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>
```

## Setting up Cloudflare D1 Database <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>

Create your D1 database using Wrangler:
```bash
npx wrangler d1 create drizzle-demo-DB <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>
```
When creating the database, specify the migrations directory, which will be named `drizzle`:
```bash
npx wrangler d1 create drizzle-demo-DB --migrations-dir=drizzle <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>
```

## Integrating Drizzle ORM <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>

Install Drizzle ORM and Drizzle Kit:
```bash
pnpm add drizzle-orm drizzle-kit <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>
```

### Database and Schema Files <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>

Create the following files under `src/app/server/`:
*   `src/app/server/db.ts`
*   `src/app/server/schema.ts`

**`src/app/server/db.ts`**:
Set up the Drizzle database connection. You'll need to import `drizzle` from `drizzle-orm/cloudflare-d1` and pass the D1 binding:

```typescript
// src/app/server/db.ts
import { drizzle } from 'drizzle-orm/cloudflare-d1';
import { D1Database } from '@cloudflare/workers-types'; // For type safety
import * as schema from './schema'; // Import your schema

// Declare global type for process.env.DB
declare global {
  namespace NodeJS {
    interface ProcessEnv {
      DB: D1Database;
    }
  }
}

export const db = drizzle(process.env.DB, { schema }); <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>
```

### Generating Types for D1 Binding <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>

To ensure type safety for `process.env.DB`, generate the necessary types. Run the command found in `env.d.ts` (usually `pnpm cf-types` or `npx -- cf-typegen`):
```bash
pnpm cf-types <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>
```
This command generates the `CFEnv` type definition, which includes `D1Database`.

Create `globals.d.ts` to extend `process.env` with these types:
```typescript
// globals.d.ts
/// <reference types="@cloudflare/workers-types" />

import { CFEnv } from './.wrangler/types'; // Path might vary based on your setup

declare global {
  namespace NodeJS {
    interface ProcessEnv extends CFEnv {}
  }
}
```

Now, `process.env.DB` will be correctly typed as `D1Database` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Defining Your Schema <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>

Define your database schema in `src/app/server/schema.ts`. Here's an example `todoTable`:

```typescript
// src/app/server/schema.ts
import { sqliteTable, text, integer } from 'drizzle-orm/sqlite-core'; <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>

export const todoTable = sqliteTable('todos', { <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>
  id: integer('id').primaryKey({ autoIncrement: true }), <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>
  title: text('title').notNull(),
  description: text('description'),
  completed: integer('completed', { mode: 'boolean' }).default(false).notNull(), <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>
  createdAt: text('created_at').default('CURRENT_TIMESTAMP').notNull(), <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>
  updatedAt: text('updated_at')
    .default('CURRENT_TIMESTAMP')
    .notNull()
    .$onUpdate(() => new Date().toISOString()), <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>
});
```

## Configuring Drizzle for Local and Remote <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>

For local development, Wrangler/Cloudflare Pages uses `mini-flare` to create a local SQLite database, avoiding remote queries <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. Drizzle needs to be configured to handle both local and remote environments for migrations and querying.

Create a `drizzle.config.ts` file in your project root:

```typescript
// drizzle.config.ts
import type { Config } from 'drizzle-kit';
import path from 'path';
import fs from 'fs';

// Function to get local D1 database path from .wrangler/state/v3/d1
function getLocalD1DatabasePath() {
  const wranglerStatePath = path.join(process.cwd(), '.wrangler', 'state', 'v3', 'd1'); <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>
  if (fs.existsSync(wranglerStatePath)) {
    const files = fs.readdirSync(wranglerStatePath);
    const dbFile = files.find(file => file.endsWith('.sqlite'));
    if (dbFile) {
      return path.join(wranglerStatePath, dbFile);
    }
  }
  return undefined;
}

const config: Config = {
  schema: './src/app/server/schema.ts', // Path to your schema file <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>
  out: './drizzle', // Migrations output directory <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>
  dialect: 'sqlite',
  dbCredentials: process.env.NODE_ENV === 'production' ? {
    accountId: process.env.CLOUDFLARE_ACCOUNT_ID!, <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>
    databaseId: process.env.CLOUDFLARE_D1_DATABASE_ID!, <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>
    token: process.env.CLOUDFLARE_D1_API_TOKEN!, <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>
  } : {
    url: getLocalD1DatabasePath() || 'file:./local.sqlite', // Fallback for local <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>
  },
  migrations: {
    table: 'migrations',
    schema: true,
  }
};

export default config;
```

### Add Drizzle Scripts to `package.json` <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>

Add the following scripts to your `package.json` for managing migrations:

```json
{
  "scripts": {
    "db:generate": "drizzle-kit generate:sqlite", <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>
    "db:migrate:local": "drizzle-kit migrate:sqlite", <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>
    "db:migrate:remote": "drizzle-kit migrate:sqlite --config drizzle.config.ts", <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
    "db:studio:local": "drizzle-kit studio --verbose" <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>
  }
}
```
Note: `db:migrate:remote` requires Cloudflare credentials to be set up as environment variables.

## Performing Local Migrations and Studio <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>

### Generating Migrations <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>

After defining your schema, generate the migration SQL file:
```bash
pnpm db:generate <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>
```
This will create migration files in the `drizzle` directory.

### Running Local Migrations <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>

Apply the migrations to your local D1 database:
```bash
pnpm db:migrate:local <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>
```
This command will create or update the SQLite database file in `.wrangler/state/v3/d1/` <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

### Accessing Drizzle Studio Locally <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>

To view your local database via Drizzle Studio:
```bash
pnpm db:studio:local <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>
```
> [!NOTE] `better-sqlite3` Requirement <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>
> Drizzle Studio requires `better-sqlite3` to interact with the local SQLite database. Ensure it's installed as a development dependency if you plan to use `db:studio:local`. It is not required for just querying from your application.

## Setting Up for Production/Remote <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>

For production deployments and remote migrations, you need to provide Cloudflare credentials.

### Required Environment Variables <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>

Set the following environment variables (e.g., in a `.env.production` file or directly in your CI/CD settings):
*   `CLOUDFLARE_ACCOUNT_ID`
*   `CLOUDFLARE_D1_DATABASE_ID`
*   `CLOUDFLARE_D1_API_TOKEN`

### Obtaining Credentials

1.  **Database ID**: You can find your database ID in the Cloudflare D1 dashboard <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
2.  **Account ID**: Your account ID is available in the Cloudflare Pages dashboard under "Overview" or "Account Home" <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
3.  **API Token**:
    *   Log in to your Cloudflare account <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
    *   Go to the top corner, click "My profile," then "API Tokens" <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
    *   Click "Create Token" <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
    *   Choose a custom token.
    *   Add permissions: At minimum, you'll need "Account" > "Cloudflare D1" > "Edit" and "Account" > "Workers R2 Storage" > "Edit" <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
    *   Select specific accounts if desired <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
    *   Continue to summary and create the token <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
    *   Copy the generated token and set it as `CLOUDFLARE_D1_API_TOKEN` <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.

### Verifying Production Setup <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>

You can verify your production database by navigating to D1 databases in your Cloudflare dashboard and selecting your `drizzle-demo-DB` <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.