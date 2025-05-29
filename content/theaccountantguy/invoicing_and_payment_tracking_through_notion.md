---
title: Invoicing and payment tracking through Notion
videoId: 96mB_cSpyoI
---

From: [[theaccountantguy]] <br/> 

Notion Books Freelancers OS is a comprehensive dashboard designed to help freelancers manage their entire finances, including income and expense details, and client management [00:00:09].

## Finance Section
The Finance section allows users to track their income and expenses [00:00:12]. It is crucial to classify income, especially client-related income, as "client" for accurate tracking within the system [00:01:44]. Users can also create their own income classifications [00:01:58]. Any income transactions booked and classified under "client" in the finance setup will automatically reflect in the client portal [00:02:45].

To add new income:
1.  Click "New income" [00:02:03].
2.  Specify the income name (e.g., "Client income") [00:02:12].
3.  Click on "Classification" and select "Client" (or create a new classification) [00:02:19].

For a detailed understanding of the finance system, a tutorial video is available within the Notion setup [00:01:30].

## Client Management Dashboard
The client management dashboard, accessed by clicking "Client" in the navigation bar, offers a portal for managing client-related activities [00:00:59]. It includes sections for:
*   [[tracking_invoice_payments_in_notion | Invoicing details]] [00:03:37]
*   Client details [00:03:39]
*   Project details [00:03:42]
*   Services section [00:03:45]

Additionally, it contains a "Tools" section with Resources, Contacts, Goals, and a Calendar for meeting schedules [00:03:52].

A "workflow" section at the bottom of the client dashboard displays all income classified under "client," providing a filtered view of client-related earnings [00:04:25].

### Client Details
Clients are organized into a pipeline with three stages:
*   Lead: Potential clients [00:05:22].
*   Negotiation: Clients in the discussion phase [00:05:27].
*   Client: Current active clients [00:05:32].

To add a new client:
1.  Click the "New" option under the desired pipeline category [00:05:39].
2.  Enter the client's name [00:05:51].
3.  The "Invoice amount" automatically reflects the total invoices raised against this client from the invoicing section [00:05:58].
4.  The "Contract value" is manually entered by the user and represents the total contract value [00:07:04].
5.  A percentage shows the portion of the contract value that has been invoiced (e.g., $2,000 invoiced out of a $12,000 contract value is 17%) [00:07:22].

Clicking on a client's entry opens a window to add more details, such as company, contact, email, position, stage, and website [00:07:42]. It also displays work-related details, including associated invoices and their status (e.g., Draft) [00:08:11]. Clients can be easily dragged and dropped between pipeline categories to update their status [00:09:14].

### Project Details
Projects track the work being performed for a client, often dividing a larger contract into manageable tasks [00:10:10]. Projects are categorized by priority: Low, Medium, and High [00:10:33].

To add a new project:
1.  Click "New" under the desired priority category [00:10:41].
2.  Specify the project name and value [00:10:51].
3.  Assign a completion date, which can be a single date or a date range (start and end dates) [00:11:30].
4.  Update the project's status (e.g., Not Started, In Progress, Completed) [00:12:18].

Project completion is calculated based on either:
*   **Hourly basis**: By specifying estimated hours and booking actual hours (e.g., 7 actual hours out of 10 estimated hours results in 70% completion) [00:14:45].
*   **Invoicing basis**: By comparing the total invoiced amount for the project against the total project value (e.g., $3,000 invoiced out of a $6,000 project value results in 50% completion) [00:15:06].

Projects are linked to specific clients and can be associated with multiple services [00:16:38].

### Services Section
Services are linked to projects, with each project potentially having multiple services [00:17:48]. Services are classified by status: Not Started, In Progress, or Completed [00:18:01].

To add a new service:
1.  Click "New" under the desired status category [00:18:13].
2.  Specify the service name [00:18:21].
3.  Add "Service pricing," choosing between "hourly basis" (e.g., $10/hour) or "fixed flat rate fees" (e.g., $2,000) [00:18:27].
4.  Enter the "Service rate" accordingly [00:18:46].

Service entries can also include service duration, pricing type, status, and in future updates, team members [00:19:37]. Each service also shows the client it's provided to, the associated project, and the total service value [00:20:11].

## Invoicing Section
The [[tracking_invoice_payments_in_notion | invoicing]] section tracks the status of invoices, which are categorized as:
*   **Draft**: Invoices that are still being prepared [00:21:23].
*   **Sent**: Invoices that have been issued to the client [00:21:27].
*   **Paid**: Invoices for which payment has been received [00:21:29].

The section displays the total [[tracking_invoice_payments_in_notion | invoice amount]] for each status category [00:21:33]. Users can also view the number of invoices in each category by changing the display option to "count unique values" [00:21:46].

To add a new invoice:
1.  Click "New" under the desired status category (e.g., "Sent") [00:22:07].
2.  Enter the "Invoice number" (e.g., "Invoice 0003") [00:22:15].
3.  Set a "Due date" for the invoice [00:22:34].
4.  The "Invoice amount" will be automatically populated from the workflow section below [00:22:27].

### Workflow Section (Linking Income to Invoices)
The "Workflow" section at the bottom of the client dashboard is crucial for linking income to invoices, clients, projects, and services [00:23:08]. This section pulls income details directly from the finance view, specifically filtering for client-assigned income [00:23:18].

For each income entry, there are columns to assign:
*   **Invoice**: Link the income to a specific invoice by selecting an existing one or creating a new one directly from this field [00:23:39]. Once an invoice is selected, its amount automatically updates in the main invoicing section [00:23:57]. New invoices created here will automatically appear in the main invoicing section under "Draft" status [00:26:06].
*   **Client**: Assign the income to a specific client [00:24:37]. This updates the client's total invoice value [00:24:47].
*   **Project**: Link the income to a specific project [00:25:15].
*   **Service**: Assign the income to a specific service [00:25:23].

This bidirectional functionality allows users to either add all details (clients, projects, services, invoices) at the top first, or to create new entries directly from the workflow section, which then populate the respective main sections [00:25:38].

### Tracking Payment Modes
Users can track the payment mode for each income entry in the workflow (e.g., "Bank" once payment is received) [00:27:10]. Removing the payment mode (leaving it blank) indicates that the money has not yet been received, which then updates calculations in the finance view [00:27:26].

## Tools Section
The "Tools" section provides additional functionalities to streamline business operations:

*   **Resources**: A curated view for storing useful resources categorized as checklists, guides, strategies, or tips [00:28:59]. Users can add resource names, categories (e.g., Taxes, Budgeting, Investments, Savings), and external links [00:29:37]. Each resource can also contain detailed notes or to-do lists using Notion's `/` command [00:30:09].

*   **Contacts**: A catalog to store contact details of people used for different services (e.g., Finance, Services, Legal) [00:31:30]. Users can add contact names, designations, phone numbers, addresses, email IDs, and company names [00:31:57]. Custom categories for contacts can also be created or edited [00:32:31].

*   **Goals**: A section to set and track personal or business goals, classified under categories like Health, Wealth, and Relationship [00:33:06]. For each goal, users specify a target number and track their progress, with a completion percentage automatically calculated (e.g., losing 3 pounds out of a 10-pound target is 30% complete) [00:33:41].

*   **Calendar**: Displays all scheduled meetings for the month, providing a quick overview of business engagements [00:34:26]. To add a meeting, users specify a title, agenda, assign clients or contacts, select a meeting medium (e.g., Google Meet, Skype), and attach reference documents or links [00:34:44]. Meetings can also be assigned a priority (low, medium, high) [00:36:04]. The calendar view can be switched between monthly and weekly layouts [00:36:27].

This comprehensive Notion setup allows freelancers to [[tracking_personal_finances_in_notion | track personal finances]], [[bookkeeping_in_notion | manage bookkeeping]], [[using_notion_as_an_expense_tracker | track expenses]], [[budgeting_and_tracking_expenses_in_notion | budget]], [[debt_payment_tracking_using_notion | track debt payments]], and manage credit card overviews [00:00:14]. The system aims to provide a complete solution for managing a freelancing business [00:37:44].