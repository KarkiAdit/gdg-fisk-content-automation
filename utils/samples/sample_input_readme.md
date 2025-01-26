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

| git pull origin dev
                     git add .
                              git commit \-m "Added feature X to improve functionality Y"
                                                                                         git checkout dev
                                                                                                         git push origin dev |
| :---- |

Code Review

| git pull origin dev && git pull origin master
                                               git checkout master
                                                                  git merge dev
                                                                               git push origin master |
| :---- |

3. Deployment will begin once the homepage is complete, using Netlify to auto-deploy changes from **google-devs-fisk/master**. As other pages may still be in progress, **dev \-\> master** merges must be handled carefully, especially after a month. Pushes to dev should now be production-ready, replacing any earlier experimental or test code.   
   Developers can try prod deployment by Netlify (\*don’t forget the prod flag).

| netlify login
               netlify deploy \--prod |
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

| git clone https://github.com/google-devs-fisk/google-devs-fisk-website.git 
                                                                             cd google-devs-fisk-website |
| :---- |

2. Install all the dependencies

| npm install |
| :---- |

   

3. Refactor anytime for any dependency-related errors:

| rm \-rf node\_modules package-lock.json .next
                                               npm cache clean \--force
                                                                       npm install |
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

[image1]: https://storage.googleapis.com/gdg-fisk-assets/images/34154097240e48bfaad9aa07f7e10db2.png

[image2]: https://storage.googleapis.com/gdg-fisk-assets/images/402d3a0357bd45de9c2e290c0ebb42d1.png

[image3]: https://storage.googleapis.com/gdg-fisk-assets/images/6ee935f362d643af85ff92c59ed3b49d.png

[image6]: https://storage.googleapis.com/gdg-fisk-assets/images/af0691ddb0ec461585e631a125f6249d.png