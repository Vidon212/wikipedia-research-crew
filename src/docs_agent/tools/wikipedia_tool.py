from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import wikipedia

class WikipediaSearchInput(BaseModel):
    """Input schema for WikipediaSearchTool."""
    query: str = Field(..., description="The query to search for on Wikipedia.")

class WikipediaSearchTool(BaseTool):
    name: str = "wikipedia_search"
    description: str = (
        "A tool that searches Wikipedia for a given query and returns a summary of the most relevant article."
    )
    args_schema: Type[BaseModel] = WikipediaSearchInput

    def _run(self, query: str) -> str:
        try:
            # Search for the query
            search_results = wikipedia.search(query)
            if not search_results:
                return f"No Wikipedia articles found for '{query}'."
            
            # Get the page of the first result
            page_title = search_results[0]
            page = wikipedia.page(page_title)
            
            # Extract content. We take a large chunk (4000 chars) to ensure the agent finds what it needs
            content = page.content[:4000]
            return f"Source: {page.url}\n\nTitle: {page_title}\n\nContent Snippet:\n{content}..."

        except wikipedia.exceptions.DisambiguationError as e:
            return f"Disambiguation error: The query '{query}' relates to multiple topics. Please be more specific. Possible options: {', '.join(e.options[:5])}"
        except wikipedia.exceptions.PageError:
            return f"Page error: Could not find a Wikipedia page for '{query}'."
        except Exception as e:
            return f"An error occurred: {str(e)}"
