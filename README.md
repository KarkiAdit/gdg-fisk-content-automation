# GDG Fisk Content Handler

## 🚀 Overview
The **GDG Fisk Content Handler** is a cloud-based solution designed to simplify and automate content creation, management, and moderation for our website. It integrates **Google Cloud Functions**, **Firestore**, **Google Cloud Storage**, and third-party APIs (Google Drive and GitHub) to provide autonomous content moderation and data management without the need for a complex admin interface.

## 🛠️ Problem Statement
Building a separate admin page would be inefficient due to the independent nature of data across various pages. A lightweight, autonomous solution is needed for content management without implementing complex administrative systems.

## 💡 Solution
A new Google Cloud project (**gdg-fisk-content**) with the following services:
- **Google Drive API**: Managing and monitoring project-related content (Projects, Codelabs, Testimonials).
- **GitHub API**: Tracking organization stats (repos, commits).
- **Firestore**: Storing content and subscriber information.
- **Google Cloud Storage**: Storing images and files related to content.

## 📄 Content Creation
- **Projects**: Information in a "Projects" folder in Google Drive (each project has its own Google Doc).
- **Codelabs**: Information in a "Codelabs" folder in Google Drive (each codelab has its own Google Doc).
- **Testimonials**: Information in a "Testimonials" folder in Google Drive (each testimonial has its own Google Doc).
- **Stats**: Data fetched via GitHub API (e.g., total repositories, commits).
- **Newsletter Subscribers**: Collected via POST requests and stored in Firestore.

## 🛡️ Content Moderation
- Google Drive API monitors changes in **Projects**, **Codelabs**, and **Testimonials** folders. 
- Changes (additions, modifications, deletions) are tracked and processed by **Google Cloud Functions**.

## 📊 Additional Data
- **GitHub Stats**: Organization stats like active repositories and commits fetched using GitHub API.
- **Newsletter Subscribers**: Subscriber data stored in Firestore via HTTP POST requests.

## 🤖 Autonomous Moderation with Cloud Functions
The cloud function `gdg_content_handler` listens for notifications from Google Drive API and GitHub API. It updates Firestore with new data for **projects**, **codelabs**, **testimonials**, and other content based on these notifications.

## 🌐 Webhooks
Two webhooks:
- **Drive Service Hook**: Receives updates via Google Drive API’s `files.watch` or `changes.watch` endpoints (for monitored folders).
- **GitHub Service Hook**: Sends updates via GitHub webhooks for events (e.g., push, pull request, issue comment) related to repositories or organizations.

## 🔄 Other Considerations
- **Prompt Engineering & AI**: Content generated using **Gemini 2.0** for AI-assisted document creation.
- **Images/Files**: Stored in **Google Cloud Storage** (e.g., in a `projects` bucket) with URLs stored in Firestore for public rendering.
- **Webhook Renewal**: Periodically renewed using **Google Job Scheduling** to handle webhook expiration (7-30 days).

## ⚙️ Conclusion
This cloud solution automates content updates and moderation, stores data securely in **Google Cloud**, and ensures real-time updates via **webhooks** and **cloud functions**—all without requiring complex admin systems. 🚀
