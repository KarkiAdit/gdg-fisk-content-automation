from models import ProjectsPageResponse, Project, Section, TextContent, VideoContent

sample_projects = [
    Project(
        id="project1",
        projectHeroImg="https://example.com/images/project1-hero.png",
        projectTitle="Innovative AI for Education",
        readTimeInMins=8,
        overview=Section(
            textContents=[
                TextContent(
                    content="This project explores AI-driven solutions for personalized education.",
                    imgUrl="https://example.com/images/overview1.png"
                ),
                TextContent(
                    content="Our goal is to make learning more engaging and efficient."
                ),
            ]
        ),
        problemStatement="Traditional educational systems lack personalized learning tools.",
        features=Section(
            textContents=[
                TextContent(
                    content="Adaptive learning models based on student behavior.",
                    imgUrl="https://example.com/images/feature1.png"
                ),
                TextContent(
                    content="Real-time progress tracking and insights."
                ),
            ]
        ),
        demo=VideoContent(
            title="AI Education Demo",
            imgUrl="https://example.com/images/demo1-thumbnail.png",
            videoUrl="https://example.com/videos/ai-education-demo.mp4",
            genres=["education", "technology", "demo"]
        ),
        relevantLinks=[
            "https://github.com/example/ai-education",
            "https://example.com/projects/ai-education"
        ],
        author="John Doe"
    ),
    Project(
        id="project2",
        projectHeroImg="https://example.com/images/project2-hero.png",
        projectTitle="Green Energy Optimization",
        readTimeInMins=6,
        overview=Section(
            textContents=[
                TextContent(
                    content="This project aims to optimize green energy usage through advanced analytics."
                ),
            ]
        ),
        problemStatement="Inefficient use of renewable energy sources leads to significant waste.",
        features=Section(
            textContents=[
                TextContent(
                    content="AI-powered energy distribution optimization.",
                    imgUrl="https://example.com/images/feature2.png"
                ),
            ]
        ),
        demo=VideoContent(
            title="Green Energy Demo",
            imgUrl="https://example.com/images/demo2-thumbnail.png",
            videoUrl="https://example.com/videos/green-energy-demo.mp4",
            genres=["energy", "sustainability", "analytics"]
        ),
        relevantLinks=[
            "https://github.com/example/green-energy",
            "https://example.com/projects/green-energy"
        ],
        author="Jane Smith"
    ),
]

# Sample projects object
sample_project_page_response = ProjectsPageResponse(projects=sample_projects)