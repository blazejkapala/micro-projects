import os
from datetime import datetime
import markdown  # You might need to install this: pip install markdown

def read_readme(project_dir):
    """Read entire README.md file and convert to HTML"""
    readme_path = os.path.join(project_dir, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Convert Markdown to HTML
            html_content = markdown.markdown(content)
            return html_content
    return "<p>No description available</p>"

def generate_website():
    # Configuration
    excluded_files = {'index.html'}
    root_dir = os.getcwd()
    projects_dir = 'projects'
    
    if not os.path.exists(projects_dir):
        os.makedirs(projects_dir)

    projects = []
    
    for root, dirs, files in os.walk(projects_dir):
        for file in files:
            if file.endswith('.html'):
                relative_path = os.path.join(root, file).replace('\\', '/')
                modified_time = os.path.getmtime(relative_path)
                modified_date = datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d')
                
                project_dir = os.path.dirname(os.path.join(root, file))
                project_name = os.path.basename(project_dir).replace('-', ' ').title()
                project_description = read_readme(project_dir)
                
                projects.append({
                    'name': project_name,
                    'path': relative_path,
                    'date': modified_date,
                    'description': project_description
                })

    # Prepare the project cards HTML
    if projects:
        projects_html = ''.join(f"""
        <article class="project-card">
            <h3>{project['name']}</h3>
            <div class="project-content">
                {project['description']}
            </div>
            <div class="project-date">Last updated: {project['date']}</div>
            <a href="{project['path']}" class="project-link">View Project</a>
        </article>
        """ for project in projects)
    else:
        projects_html = '''
        <div class="project-card">
            <h3>No Projects Found</h3>
            <div class="project-content">
                <p>Add projects to get started</p>
            </div>
            <div class="project-date">Create your first project</div>
            <a href="#" class="project-link" style="background-color: #71717a">Create Project</a>
        </div>
        '''

    # Generate the complete HTML
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Playground - Project Collection</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f5;
        }}

        .projects-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(90%, 1fr));
            gap: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }}

        .project-card {{
            background: white;
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            display: flex;
            flex-direction: column;
        }}

        .project-card h3 {{
            margin: 0;
            font-size: 20px;
            color: #18181b;
            font-weight: 600;
        }}

        .project-content {{
            margin: 16px 0;
            color: #4b5563;
            flex-grow: 1;
        }}

        .project-content h1 {{
            font-size: 1.5em;
            margin-top: 0;
        }}

        .project-content h2 {{
            font-size: 1.25em;
        }}

        .project-content h3 {{
            font-size: 1.1em;
        }}

        .project-content p {{
            margin: 8px 0;
        }}

        .project-content ul, .project-content ol {{
            margin: 8px 0;
            padding-left: 20px;
        }}

        .project-date {{
            color: #71717a;
            font-size: 14px;
            font-style: italic;
            margin: 8px 0;
        }}

        .project-link {{
            display: block;
            background-color: #3b82f6;
            color: white;
            text-decoration: none;
            padding: 8px 0;
            border-radius: 6px;
            text-align: center;
            font-weight: 500;
            transition: background-color 0.2s;
            margin-top: auto;
        }}

        .project-link:hover {{
            background-color: #2563eb;
        }}

        code {{
            background-color: #f1f5f9;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: monospace;
        }}

        pre {{
            background-color: #f1f5f9;
            padding: 12px;
            border-radius: 6px;
            overflow-x: auto;
        }}

        pre code {{
            background-color: transparent;
            padding: 0;
        }}
    </style>
</head>
<body>
    <div class="projects-grid">
        {projects_html}
    </div>
</body>
</html>'''

    # Write the generated HTML to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    generate_website()