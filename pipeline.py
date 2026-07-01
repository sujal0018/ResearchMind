from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain


def extract_text(content) -> str:
    """Normalize LangChain message content into plain text.

    Some models (e.g. Gemini via langchain_google_genai) return `.content` as a
    list of content blocks like [{'type': 'text', 'text': '...', 'extras': {...}}]
    instead of a plain string. This flattens either shape into clean text.
    """
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text", ""))
            elif isinstance(block, str):
                parts.append(block)
        return "\n".join(parts).strip()
    return str(content)


def run_research_pipeline(topic: str) -> dict:

    state = {}

    # step 1 - search agent working
    print("\n" + " ="*50)
    print("step 1 - search agent is working ...")
    print("="*50)

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })
    state["search_results"] = extract_text(search_result['messages'][-1].content)

    print("\n search result ", state['search_results'])

    # step 2 - reader agent
    print("\n" + " ="*50)
    print("step 2 - Reader agent is scraping top resources ...")
    print("="*50)

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results']}"
        )]
    })

    state['scraped_content'] = extract_text(reader_result['messages'][-1].content)

    print("\nscraped content: \n", state['scraped_content'])

    # step 3 - writer chain

    print("\n" + " ="*50)
    print("step 3 - Writer is drafting the report ...")
    print("="*50)

    research_combined = (
        f"SEARCH RESULTS : \n {state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\n Final Report\n", state['report'])

    # step 4 - critic report

    print("\n" + " ="*50)
    print("step 4 - critic is reviewing the report ")
    print("="*50)

    state["feedback"] = critic_chain.invoke({
        "report": state['report']
    })

    print("\n critic report \n", state['feedback'])

    return state


if __name__ == "__main__":
    topic = input("\n Enter a research topic : ")
    run_research_pipeline(topic)