| ![People][image1] Author | ![Dropdowns][image2] Status | ![No type][image3] Notes |
| :---- | :---- | :---- |
| [Aditya Karki](mailto:adityakarki728@gmail.com) | In progress | \*\* Leave at the end \*\* |

# Background

This project aims to develop a **lightweight, mobile-responsive** website highlighting Google Devs at Fisk's vision, projects, coding practices, and culture. The website will include the following pages/logic implementation:

1. Landing Page: Showcasing the vision, goals, and impact achieved so far.  
2. Projects Page: Featuring ongoing projects.  
3. Codelabs Page: Providing technical documentation or tutorials for contributions/creative implementation about any coding domain.  
4. Work Culture Page: Highlighting our collaborative work environment.  
5. Contact Us Page: Listing our email and key contacts.  
6. Admin Logic: [AI-Driven Content Automation System](https://docs.google.com/document/d/1tUPGT8putpPJBRjOdjZVF5_r5mI7O5FfDZLyZ-qXils/edit?usp=sharing) using cloud monitoring APIs, webhooks, and Google Cloud functions.

Additionally, a consistent header and footer will be present on every page.

# Dev Tools

The following tools will be used for development, production, and deployment:

Common

1. Figma  
2. Git/Github  
3. Google Firestore (Database)

Frontend

1. Typescript  
2. Builder.io  
4. Next (Full Stack Engineering)  
5. NextUI (Frontend designing \- built on top of Tailwind and React)  
6. Framer Motion and React Hooks (Animations)  
7. Google Firestore (Database)  
8. Vercel

Backend

1. Python  
2. Google Drive API  
3. GitHub Organization API  
4. Gemini 2.0   
5. Claat  
6. Google Cloud Platform  
7. Google Drive API  
8. Google Cloud Storage (Database)  
9. Google Cloud Functions and WebHooks  
10. Google Cloud Scheduler  
11. Google Cloud SDK

# CI/CD Practices

1. Always be at the dev branch while coding.

| git checkout dev |
| :---- |

2. All changes must be reviewed before merging. The repository will have two branches: **master** (or main) and **dev**. Developers should push all changes to the dev branch first. Once the changes are reviewed (mostly by PM but anyone from the team can do it) and approved, the reviewer must merge or push them to the master (or main) branch. (\*Remember to pull both branches first to sync to the codebase.)

Code change

| git pull origin devgit add .git commit \-m "Added feature X to improve functionality Y"git checkout devgit push origin dev |
| :---- |

Code Review

| git pull origin dev && git pull origin mastergit checkout mastergit merge devgit push origin master |
| :---- |

3. Deployment will begin once the homepage is complete, using Netlify to auto-deploy changes from **google-devs-fisk/master**. As other pages may still be in progress, **dev \-\> master** merges must be handled carefully, especially after a month. Pushes to dev should now be production-ready, replacing any earlier experimental or test code.   
   Developers can try prod deployment by Netlify (\*don’t forget the prod flag).

| netlify loginnetlify deploy \--prod |
| :---- |

# UI Design

## Implementation

Create a Prism-style dark theme using **NextUI** components. Customize the mobile responsiveness using **Tailwind** classes. Any additional third-party styling/component library can be used to better the designs. **Builder.io** can be used as a smart reference to generate code from Figma design (\*everything should be consistent). Watch this [tutorial](https://cdn.builder.io/o/assets%2FYJIGb4i01jvw0SRdL5Bt%2Fba1319251a5848f9817b2f6d6e45ec81%2Fcompressed?apiKey=YJIGb4i01jvw0SRdL5Bt&token=ba1319251a5848f9817b2f6d6e45ec81&alt=media&optimized=true). Always use the [builder-mock-components](#file-structure) folder to store builder.io-generated content.

## Consistent Themes

### Page Theme

The design will feature a dark theme with glass morphic sections, incorporating color theory to ensure optimal contrast and readability for text and images.

### Page color

Dark bluish-black color (\#100425). 

### Font Family

**FigTree** (Bold, Medium, Regular), Use bold and extra bold interchangeably as needed.

## The Figma Mock

This is the completed [Figma design](https://www.figma.com/proto/sbbpFoBkWBA02VN8Xv3fif/GDG-UI-Design?node-id=1-255&p=f&t=9i3rhvRKZS9VfgLy-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1) for the website.

# Frontend Development

## Project Repo

This is the [GitHub repository](https://github.com/google-devs-fisk/google-devs-fisk) for the Frontend logic (\*see dev branch, master may be behind).

## Project Setup

The [following steps](https://docs.google.com/document/u/0/d/1zZigCvfnV_qBMIO3y69ShcxoY921ahwtRLFHgFlmz2E/edit) have already been completed. To set up the project locally, follow these instructions:

1. Clone the GitHub project locally

| git clone https://github.com/google-devs-fisk/google-devs-fisk-website.git cd google-devs-fisk-website |
| :---- |

2. Install all the dependencies

| npm install |
| :---- |

   

3. Refactor anytime for any dependency-related errors:

| rm \-rf node\_modules package-lock.json .nextnpm cache clean \--forcenpm install |
| :---- |


## Implementation

Next.js with the [App Router](https://medium.com/@kulsumansari4/next-js-app-router-routing-8d795dbe324c) uses file-based routing. All pages should be implemented by creating new folders (\*meaning routes) inside the [app](#file-structure). Add a [layout.tsx](https://github.com/KarkiAdit/your-next-tech/blob/master/src/app/layout.tsx) file where necessary to define shared layouts for the routes. Use a [loading skeleton](https://github.com/KarkiAdit/your-next-tech/blob/c58af730e9f83f1ba3aab5e948a2a02c90c8d8b4/src/app/page.tsx#L13) for a specific component fetching your page's data. 

All pages and their components must be **mobile-responsive** and **dynamic**. Builder.io generated components should be put in builder-mock-components and can be used as reference while coding (\*will not be used for prod.) Any reusable component can be added inside components. Any framer animation can be added inside animations and implemented using React Hooks in the hooks folder. Any data/component state props can be declared in types. Any page URL can be accessed from paths.ts. The Firestore client can be accessed from [db.](https://github.com/google-devs-fisk/google-devs-fisk/blob/ba116399d66f2ab0b9a890d05bed8d034aaad32a/src/actions/subscriberFormSubmit.tsx#L8)

## Data Engineering {#data-engineering}

We will implement [Incremental Static Regeneration (ISR)](https://nextjs.org/docs/pages/building-your-application/data-fetching/incremental-static-regeneration) to engineer data fetching. Data fetching will occur within [actions](#file-structure) and be passed as props to the server-side rendered component. This approach enhances performance and user experience by combining static generation with dynamic content updates.

We will establish a reasonable revalidating timeframe for ISR components to prevent stale data while minimizing unnecessary revalidations. Incorporating **lastModifiedTime** with our revalidate logic allows us to intelligently determine when to refresh data. This approach ensures users receive up-to-date information while optimizing server load and minimizing unnecessary requests.

This is a [sample implementation](https://docs.google.com/document/d/171zelLSI20BzxAOUzkymEF-KMyIfEOvHPl2E6dFhWvM/edit?usp=sharing).

## Response Definition

Refer [types folder](#file-structure) to find backend response types.

## Home Page (/)

This page should link to other pages via buttons, header, or footer links. ISR fetch to following DB docs: gdg-fisk-content/HomePageResponse (\*Remember gdg-fisk-content is our Firestore collection name.)

| Components | State variables | Additional animation functionality |
| ----- | ----- | ----- |
| Header Hero Banner Vision Projects Carousel Key Focus Domains Team Culture Testimonials Newsletter Footer | **projects** (rendered in the projects carousel) **testimonials** (rendered in the testimonial carousel)  **newsletterInfo** (used to setup newsletter form changes) *Additional variables may be needed* | Make each section animate as in the Figma prototype |

## Projects (/projects)

This page should be a single-page carousel that fills the entire viewport. Each project should be linked to associated /projects/${projectId} page (**the project info page**). ISR fetch to gdg-fisk-content/ProjectsPageResponse (\*Remember gdg-fisk-content is our Firestore collection name.)

| Components | State variables | Additional animation functionality |
| ----- | ----- | ----- |
| Header Hero Banner with Arrows and Interactive Carousel Footer Type 2 | **projects** (rendered in the projects carousel)  *Additional variables may be needed* | Make each section animate as in the Figma prototype |

Each **project info page** features specific content of a project. ISR fetch to gdg-fisk-content/ProjectsPageResponse/{projectId}. 

| Components | State variables | Additional animation functionality |
| ----- | ----- | ----- |
| Header Hero Banner Overview Paragraph The Problem Statement Banner Features Video Demo Relevant Links Footer | **project** (attributes are used throughout the pagel)  *Additional variables may be needed* | Creatively implement any animation to each section |

## Codelabs (/codelabs)

This scrollable page features all the codelabs with necessary key information in a nuanced way. Each codelab should be linked to associated /codelabs/${codelabId} page (**the codelab info page**). ISR fetch to gdg-fisk-content/CodelabsPageResponse (\*Remember gdg-fisk-content is our Firestore collection name.)

| Components | State variables | Additional animation functionality |
| ----- | ----- | ----- |
| Header Overview Paragraph Footer | **codelabs** (rendered in the entire page)  *Additional variables may be needed* | Make each section animate creatively |

Each **codelab info page** features specific content of a codelab. ISR fetch to gdg-fisk-content/CodelabsPageResponse{id}.

| Header Iframe Footer | codelab (attributes are used throughout the pagel)  *Additional variables may be needed* | Creatively implement any animation to each section |
| :---- | ----- | :---- |

## Work Culture (/workCulture)

This page features a few key graphs and roadmaps, along with other specific content. ISR fetch to gdg-fisk-content/CulturePageResponse (\*Remember gdg-fisk-content is our Firestore collection name.)

| Components | State variables | Additional animation functionality |
| ----- | ----- | ----- |
| Header Hero Banner Video Banner More Info (Stats component, Image with a shape component, Roadmap component) | **stats** (attributes are used for the stats component) **testimonials** (attributes are used for the roadmap component)  *Additional variables may be needed* | Creatively implement any animation to each section |

## Contact (/contact)

This page should help our site visitors make contact or subscribe to us. Its two forms should be able to make a post request using [useFormState](https://react-hook-form.com/docs/useformstate) Hook from react-dom to maintain [ISR consistency](#data-engineering) throughout the frontend logic.  
This can be a sample [server action](https://github.com/KarkiAdit/your-next-tech/blob/master/src/actions/create-post.ts) and this can be a sample [client component](https://github.com/KarkiAdit/your-next-tech/blob/master/src/components/posts/post-create-form.tsx) definition.

| Header Contact Form Newsletter Footer | contactInfo (used to setup contact form changes) newsletterInfo (used to setup newsletter form changes)  *Additional variables may be needed* | Creatively implement any animation to each section |
| :---- | ----- | :---- |

# Inspirational Awesome Animations

[https://www.cloudbrowser.ai/](https://www.cloudbrowser.ai/)  
[https://www.framer.com/features/animations/](https://www.framer.com/features/animations/)

# References

1. [https://www.youtube.com/watch?v=nxaRKSQMMco\&ab\_channel=Builder](https://www.youtube.com/watch?v=nxaRKSQMMco&ab_channel=Builder)  
2. [https://youtu.be/rTq\_8DxZyFY](https://youtu.be/rTq_8DxZyFY)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAQCAMAAAAhxq8pAAADAFBMVEUAAABAQEBERkZFR0ZER0ZDR0VISEhFRUVERkVER0ZDR0dDRkNESERDRkZER0VESEhESEZCR0RDR0ZER0dERkZGRkZDRkRARUVASEhERkVFSEhDR0VER0ZGRkZDR0VFSEVFRUVFR0VER0YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACxWeV0AAAAInRSTlMAEH/fz58gMO/vn1BAoL9AgHDfcIBQoDAgz2CQr19vYGBvGxXIWQAAAIJJREFUeF5jYKAIMMIYHFIMDE9/QthMUDFmqRevGKRhKqBASQhECEM4MJUM32EMIGCG0n/FvwhLMDyDcFiggp9YZBkYvkI5WAFMO6M04x9p9m9QDpiUZofKMTz5BRNUYnjG8gXE4BVl+Pwa5qTPP8BiDJ/vMfAywGznBTERAO54ZAAAT90XrfZ0HKwAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAQCAYAAAAWGF8bAAAAx0lEQVR4Xu2TYRHCMAyFKwEJSEBCjyVpXIAEHIATJCBhEpCAhEkA0tEtTVcod/zku8ufvDR7fduc+/NTmHkNge6t1QU82x0TQHRMg8i4t7rGI266QJc0b3Xt7Gq1d3jvV69zQyZUn9QAMHg5K8vnpuTBtFNzXzEawj5rKL0AmE7pFku3KXrR8jPHeaRELy00m2NhuYIstT1hPB8OqoF9dKmDbQQD3ZZcTznIJ2S1GmlZ5k4DhENa3FrbDz+Bk5eTIqhVdFbJ8wG0lJX5M/zhmwAAAABJRU5ErkJggg==>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAQAQMAAAAs1s1YAAAABlBMVEUAAABER0byc6G0AAAAAXRSTlMAQObYZgAAAB9JREFUeF5jYEAD9h8YmEA0MwOYZmSWWQjhs4H56BgAT4ECDeGaeV4AAAAASUVORK5CYII=>

[image6]: <data:image/png;base64,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>
