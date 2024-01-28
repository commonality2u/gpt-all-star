from langchain_core.prompts import PromptTemplate

create_technologies_list_template = PromptTemplate.from_template(
    """Your task is to list the exact techniques for building an application with the following specifications.
Only technologies related to source code implementation should be listed, not version control tools, technologies related to automated testing or deployment, or tools related to project management.
There is no need to provide a description for each technology.
Avoid providing personal opinions or alternatives, only provide the exact technologies.

There are the specifications to build the application:
```
{specifications}
```

Technologies Guidelines
```
Relevance: Only include technologies that are essential and will be actively used in the project. Avoid mentioning any technologies that are not required.
Compatibility: Ensure that the listed technologies are compatible with each other. Exclude any technologies that cannot be integrated or used in conjunction with others. For example, Pandas (Python library) and Node.js can't be used together. Another example is MongoDB (NoSQL database) and MySQL (SQL database) shouldn't be used together unless that is specified in project description.
Preferences: In scenarios where multiple technology options are available for a specific project component, prioritize the following preferred technologies.

- Node.js
- SQLite OR MongoDB
- Bootstrap
- HTML
- CSS3
- Docker / Docker Compose
```

**IMPORTANT**: The output should be presented in markdown format.

FILENAME.md
```
CONTENT
```

The following tokens must be replaced like so:
FILENAME is the lowercase combined path and file name including the file extension
CONTENT is the text in the file

Example representation of a file:

technologies.md
```
- Node.js
- SQLite OR MongoDB
- Bootstrap
- HTML
- CSS3
- Docker / Docker Compose
```
"""
)
