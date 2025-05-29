---
title: Integrating Cloudflare D1 with Nextjs
videoId: VuuAAjkLRZs
---

From: [[swarajmakesstuff]] <br/> 

This article details the process of integrating [[Using Drizzle ORM with Cloudflare D1 | Drizzle ORM]] with Cloudflare D1 within a Next.js project. Cloudflare D1 is a fast, serverless SQL database provided by Cloudflare <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Prerequisites and Caveats

To bind your D1 database directly to [[Handling API routes in Nextjs app router | Next.js API routes]] or server actions, you need to use [[Deploying Nextjs Projects with Cloudflare Pages | Cloudflare Pages]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. If you are integrating D1 into an existing Next.js project, it's recommended to deploy it via Cloudflare Pages by connecting through GitHub <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Project Setup

The initial setup involves installing Next.js, Drizzle, and Cloudflare D1 <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

### Initialize Next.js Project with Cloudflare Pages

To create a new Next.js project integrated with Cloudflare Pages, use the Cloudflare Pages command <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>:

```bash
npx create-cloudflare@latest drizzle-D1-demo --framework next --deploy false
```

This command creates a project named `drizzle-D1-demo` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The `--deploy false` flag prevents immediate deployment.

### Setting Up Wrangler

[[Setting Up Cloudflare D1 and Wrangler for Local Development | Wrangler]] is Cloudflare's CLI tool and is essential for interacting with D1 <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

1.  **Install Wrangler**:
    If you don't have Wrangler installed globally, run:

    ```bash
    npm install -g wrangler
    # or
    pnpm add -g wrangler
    ```

    <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>

2.  **Verify Installation**:
    Check the Wrangler version:

    ```bash
    npx wrangler version
    ```

    <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>

3.  **Authenticate Wrangler**:
    Connect Wrangler to your Cloudflare account, which will prompt for permissions:

    ```bash
    npx wrangler whoami
    ```

    <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>

### Creating a D1 Database

Once Wrangler is set up, create your D1 database:

```bash
npx wrangler D1 create drizzle-demo-DB --migrations-directory=drizzle
```

<a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>
This command creates a D1 database named `drizzle-demo-DB` and specifies `drizzle` as the directory for migrations.

## Drizzle ORM Integration

### Install Drizzle

Install Drizzle ORM and Drizzle Kit in your project:

```bash
pnpm add drizzle-orm drizzle-kit
```

<a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>

### Database Configuration (`app/server/db.ts`)

Create a `db.ts` file (e.g., `app/server/db.ts`) to configure your Drizzle database instance:

```typescript
// app/server/db.ts
import { D1 } from '@cloudflare/workers-types';
import { drizzle } from 'drizzle-orm/d1';
import * as schema from './schema';

declare global {
  namespace NodeJS {
    interface ProcessEnv {
      DB: D1; // This ensures process.env.DB is typed as D1
    }
  }
}

export const db = drizzle(process.env.DB, { schema });
```

<a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>
<a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>
<a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>

To ensure type safety for the `D1` database binding, you need to extend `process.env`.
Run the following command to generate types for your Cloudflare environment:

```bash
pnpm cf-types
```

<a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>
Then, create a `globals.d.ts` file (e.g., `globals.d.ts` or `app/globals.d.ts`) to extend `process.env`:

```typescript
// globals.d.ts
import { D1Database } from '@cloudflare/workers-types';

declare global {
  namespace NodeJS {
    interface ProcessEnv {
      DB: D1Database;
    }
  }
}
```

<a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>

### Define Database Schema (`app/server/schema.ts`)

Create a `schema.ts` file (e.g., `app/server/schema.ts`) to define your database tables using Drizzle's schema helpers:

```typescript
// app/server/schema.ts
import { sql } from 'drizzle-orm';
import { sqliteTable, text, integer } from 'drizzle-orm/sqlite-core';

export const todoTable = sqliteTable('todos', {
  id: integer('id', { mode: 'number' }).primaryKey({ autoIncrement: true }),
  title: text('title').notNull(),
  description: text('description'),
  completed: integer('completed', { mode: 'boolean' }).default(false).notNull(),
  createdAt: text('created_at').default(sql`CURRENT_TIMESTAMP`).notNull(),
  updatedAt: text('updated_at').default(sql`CURRENT_TIMESTAMP`).notNull(),
});
```

<a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>
<a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>
<a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>
<a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>

### Drizzle Configuration (`drizzle.config.ts`)

Create a `drizzle.config.ts` file at the root of your project. This configuration handles both local development and production environments.

For local development, Wrangler uses `miniflare` to create a local SQLite database, so Drizzle needs to point to this local file <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. For production, it connects to the remote D1 database.

```typescript
// drizzle.config.ts
import type { Config } from 'drizzle-kit';
import { readFileSync } from 'fs';
import path from 'path';

function getLocalD1DatabasePath() {
  const wranglerTomlPath = path.join(process.cwd(), 'wrangler.toml');
  const wranglerToml = readFileSync(wranglerTomlPath, 'utf-8');
  const d1DatabaseMatch = wranglerToml.match(/database_id\s*=\s*"(.*?)"/);
  const databaseId = d1DatabaseMatch ? d1DatabaseMatch[1] : null;

  if (!databaseId) {
    throw new Error('D1 database_id not found in wrangler.toml');
  }

  // Path to the local D1 database file created by miniflare
  const localDbPath = path.join(process.cwd(), '.wrangler', 'state', 'v3', 'd1', databaseId, 'db.sqlite');
  return localDbPath;
}

export default {
  schema: './app/server/schema.ts',
  out: './drizzle', // Migration files will be stored here
  driver: 'd1-http',
  dbCredentials: {
    accountId: process.env.CLOUDFLARE_ACCOUNT_ID!,
    databaseId: process.env.CLOUDFLARE_D1_DATABASE_ID!,
    token: process.env.CLOUDFLARE_D1_API_TOKEN!,
  },
  // Environment-specific configuration for local vs. production
  // This is typically handled by environment variables or separate configurations
  // The 'd1-http' driver can connect to local or remote based on env.
  // For local migrations, Drizzle Kit itself will use the local SQLite file.
  // The `dbCredentials` are primarily for production.
  // Drizzle Kit's `migrate` command needs a `url` for local operations.
  // This is implicitly handled by the `npx wrangler D1 migrations run --local` command.
} satisfies Config;
```

<a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>
<a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>
<a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>

### Add Drizzle Scripts to `package.json`

Add the following scripts to your `package.json` for managing migrations and the Drizzle Studio:

```json
{
  "scripts": {
    "db:generate": "drizzle-kit generate:sqlite --schema=./app/server/schema.ts",
    "db:migrate-local": "npx wrangler D1 migrations run drizzle-demo-DB --local",
    "db:migrate-remote": "npx wrangler D1 migrations run drizzle-demo-DB --remote",
    "db:studio": "drizzle-kit studio"
  }
}
```

<a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>

## Running Migrations and Drizzle Studio

### Generate Migrations

Generate your SQL migration file based on your `schema.ts`:

```bash
pnpm db:generate
```

<a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>
This creates a new migration file under the `drizzle` directory <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. Ensure your schema file path is correct in the script <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

### Migrate Locally

Apply migrations to your local D1 database:

```bash
pnpm db:migrate-local
```

<a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>
This command ensures your local D1 database (`.wrangler/state/v3/d1/<database_id>/db.sqlite`) reflects your schema <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

### Drizzle Studio

To inspect your local database using Drizzle Studio:

```bash
pnpm db:studio
```

<a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>
Note that Drizzle Studio for local D1 databases relies on `better-sqlite3`, so you might need to install it if you encounter issues <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

## Production Deployment

For production, you need to configure environment variables for Cloudflare D1.

### Required Environment Variables

You'll need `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_D1_DATABASE_ID`, and `CLOUDFLARE_D1_API_TOKEN` <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

1.  **Get Database ID**:
    Navigate to your Cloudflare dashboard, go to "D1" under "Workers & Pages", and click on your database name (`drizzle-demo-DB`). The Database ID will be visible there <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.

2.  **Get Account ID**:
    In the Cloudflare dashboard, navigate to "Workers & Pages". Your Account ID will be displayed on the overview page <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.

3.  **Create API Token**:
    *   Go to your Cloudflare dashboard.
    *   Click "My Profile" in the top-right corner <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
    *   Select "API Tokens" <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.
    *   Click "Create Token" <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
    *   Choose "Create Custom Token" <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
    *   Give it a name (e.g., "Drizzle D1 Token").
    *   Add permissions: "Account" -> "Workers Scripts" -> "Edit" and "Account" -> "Cloudflare D1" -> "Edit" <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
    *   Select your account under "Include resources" <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
    *   Continue to summary and create the token. Copy the generated token immediately as it won't be shown again <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.

Set these values as environment variables in your Cloudflare Pages project settings, or as secrets if [[Using Drizzle ORM with Cloudflare D1 | deploying Next.js projects with Cloudflare Pages]] <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

Once configured, you can apply migrations to your remote D1 database:

```bash
pnpm db:migrate-remote
```

This completes the integration of Cloudflare D1 with your Next.js application using Drizzle ORM.