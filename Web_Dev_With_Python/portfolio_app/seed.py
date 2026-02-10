from app import app, db, Project

# Updated Data with richer technical details
projects_data = [
    {
        "title": "AI-Powered Adaptive Learning Platform",
        "description": "A comprehensive Learning Management System (LMS) engineered with Python and Django. Features a robust backend using Django ORM for complex data modeling of users, quizzes, and results. Implements secure user authentication, dynamic MVT templating, and adaptive algorithms that analyze user performance to recommend personalized study modules.",
        "image": "learning_plat.jpg", 
        "link": "#"
    },
    {
        "title": "Real-Time Weather Forecast API",
        "description": "A full-stack weather application powered by a custom REST API built with Flask. Integrates the OpenWeatherMap API to fetch real-time meteorological data. Features efficient JSON data parsing, environment variable management for API key security, and robust error handling for invalid city queries. optimized for scalability and modular frontend integration.",
        "image": "weather.jpg", 
        "link": "#"
    },
    {
        "title": "Dynamic Content Blog Engine",
        "description": "A lightweight Content Management System (CMS) developed with Flask and Jinja2. Utilizes dynamic routing to generate individual post pages efficiently without code duplication. Features include a modular template inheritance structure, custom 404 error handling, and a scalable dictionary-based data structure that simulates a NoSQL database approach.",
        "image": "blog.jpg", 
        "link": "#"
    }
]

def seed_database():
    """Populates the database with initial project data."""
    with app.app_context():
        print("Connecting to database...")
        
        # We need to update existing records, not just skip them
        # This loop finds the project and updates the description
        for p_data in projects_data:
            project = Project.query.filter_by(title=p_data["title"]).first()
            
            if project:
                print(f" - Updating description for: {p_data['title']}")
                project.description = p_data["description"]
                project.image = p_data["image"] # Ensures images are updated too
            else:
                print(f" - Creating new project: {p_data['title']}")
                new_project = Project(
                    title=p_data["title"],
                    description=p_data["description"],
                    image=p_data["image"],
                    link=p_data["link"]
                )
                db.session.add(new_project)

        db.session.commit()
        print("Success! Project details have been updated.")

if __name__ == "__main__":
    seed_database()