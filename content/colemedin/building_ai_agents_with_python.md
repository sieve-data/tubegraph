---
title: Building AI agents with Python
videoId: e7qvd2bOITc
---

From: [[colemedin]] <br/> 

OpenAI has released its brand new Agent SDK, an open-source AI agent framework built on top of the previously experimental Swarm [00:00:25]. While Swarm was primarily for educational purposes, the Agent SDK is claimed to be production-ready and designed to help users [[Building fullscale AI agents | build full agentic AI apps]] with minimal abstractions [00:00:17, 00:00:32, 00:00:36, 00:00:39]. This article explores the capabilities of the Agent SDK, demonstrating how to [[Building AI Agents | build powerful agents]] and evaluating its effectiveness compared to other frameworks like LangChain, CrewAI, and Pydantic AI [00:00:43, 00:00:50].

## Core Concepts of the Agent SDK

The Agent SDK is structured around four core concepts that simplify [[Developing AI Agents using Python | developing AI agents]]:
*   **Agents** These are your Large Language Models (LLMs) equipped with instructions and tools [01:52, 01:57].
*   **Handoffs** This mechanism allows different specialized agents to collaborate and tackle various parts of a problem, a common practice in effective agent architecture [01:59, 02:02, 02:06, 02:08].
*   **Guard Rails** A crucial feature that allows the creation of custom safety checks, which can validate LLM input/output, and even stop responses if issues like hallucinations are detected [02:13, 02:15, 02:18, 02:20, 02:23, 02:25, 02:26].
*   **Tracing** Provides visibility into LLM and agent operations, helping with debugging and monitoring agents in production by showing prompts and outputs [02:30, 02:32, 02:34, 02:36, 02:37, 02:39, 02:40, 02:43].

## Getting Started

[[Setting up AI Agents with Python and LangChain | Setting up AI agents with Python and LangChain]] or other frameworks can sometimes be complex, but the Agent SDK aims for simplicity [02:45]. Installation is a single `pip` command [02:54].

```bash
pip install openai-agent
```
<a class="yt-timestamp" data-t="02:55">[02:55]</a>

The documentation provides comprehensive guides for getting started and understanding all features [01:36, 01:38, 01:40].

## [[Step by step process for building AI agents | Step-by-step process for building AI agents]]: Travel Planner Assistant

To demonstrate the Agent SDK's capabilities, a travel planner assistant is built iteratively [03:19, 03:46]. This assistant can take user preferences, plan trips, and leverage specialized agents for hotel reservations and activity suggestions [03:49, 03:51, 03:55, 03:57, 03:59, 04:02].

### Version 1: Basic Agent

The first version focuses on a minimal setup to define and run an agent [03:01, 03:02, 03:27, 03:28].
*   **Define Agent**: An agent is defined by a name, instructions (system prompt), and an LLM model (e.g., GPT-4o mini) [06:10, 06:12, 06:14, 06:16, 06:19, 06:23].
*   **Run Agent**: A simple `runner.run` call executes the agent with a user prompt [06:30, 06:33, 06:36, 06:37].

```python
from openai_agent import Agent, runner
import os

# Load environment variables
# load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Define the agent
travel_agent = Agent(
    name="TravelAgent",
    instructions="You are a helpful travel planning assistant.",
    model="gpt-4o-mini", # Hardcoded for V1 simplicity
)

def main():
    # Run the agent with a user prompt
    output = runner.run(travel_agent, "Write me a haiku about recursion in programming.")
    print(output)

if __name__ == "__main__":
    main()
```
<a class="yt-timestamp" data-t="06:03">[06:03]</a> <a class="yt-timestamp" data-t="06:05">[06:05]</a> <a class="yt-timestamp" data-t="06:07">[06:07]</a> <a class="yt-timestamp" data-t="06:10">[06:10]</a> <a class="yt-timestamp" data-t="06:12">[06:12]</a> <a class="yt-timestamp" data-t="06:14">[06:14]</a> <a class="yt-timestamp" data-t="06:16">[06:16]</a> <a class="yt-timestamp" data-t="06:19">[06:19]</a> <a class="yt-timestamp" data-t="06:21">[06:21]</a> <a class="yt-timestamp" data-t="06:23">[06:23]</a> <a class="yt-timestamp" data-t="06:25">[06:25]</a> <a class="yt-timestamp" data-t="06:26">[06:26]</a> <a class="yt-timestamp" data-t="06:28">[06:28]</a> <a class="yt-timestamp" data-t="06:30">[06:30]</a> <a class="yt-timestamp" data-t="06:33">[06:33]</a> <a class="yt-timestamp" data-t="06:34">[06:34]</a> <a class="yt-timestamp" data-t="06:36">[06:36]</a> <a class="yt-timestamp" data-t="06:39">[06:39]</a> <a class="yt-timestamp" data-t="06:40">[06:40]</a> <a class="yt-timestamp" data-t="06:42">[06:42]</a>

### Version 2: Structured Outputs

[[Advancing AI agents with Python and custom coding | Advancing AI agents with Python and custom coding]] often involves standardizing LLM responses [07:11]. This version introduces structured outputs, forcing the LLM to return JSON in a predefined schema [07:15, 07:17, 07:21]. This helps reduce hallucinations by ensuring consistent data [08:29, 08:31].

*   **Define Pydantic Model**: A Pydantic class (`TravelPlan`) specifies the expected output fields (destination, duration, budget, activities, notes) [07:43, 07:46, 07:49, 07:51, 07:53, 07:56].
*   **Assign Output Type**: The `output_type` parameter in the `Agent` definition is set to this Pydantic class, instructing the LLM on the required output format [08:14, 08:17, 08:19, 08:22].

```python
from pydantic import BaseModel, Field
# ... (imports and load_dotenv from V1)

class TravelPlan(BaseModel):
    destination: str = Field(description="The travel destination.")
    duration_days: int = Field(description="The duration of the trip in days.")
    recommended_budget: float = Field(description="The recommended budget for the trip.")
    recommended_activities: list[str] = Field(description="A list of recommended activities.")
    notes: str = Field(description="Any additional notes or advice for the trip.")

travel_agent = Agent(
    name="TravelAgent",
    instructions="You are a helpful travel planning assistant. Always output a structured travel plan.",
    model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
    output_type=TravelPlan, # New: structured output
)

def main():
    queries = [
        "Plan a trip to Miami for 5 days with a budget of $2000.",
        "I'm planning a trip to Tokyo for 10 days with a budget of $5000.",
    ]
    for query in queries:
        print(f"\n--- Query: {query} ---")
        response: TravelPlan = runner.run(travel_agent, query)
        print(f"Destination: {response.destination}")
        print(f"Duration: {response.duration_days} days")
        print(f"Budget: ${response.recommended_budget}")
        print(f"Activities: {', '.join(response.recommended_activities)}")
        print(f"Notes: {response.notes}")

if __name__ == "__main__":
    main()
```
<a class="yt-timestamp" data-t="07:39">[07:39]</a> <a class="yt-timestamp" data-t="07:41">[07:41]</a> <a class="yt-timestamp" data-t="07:43">[07:43]</a> <a class="yt-timestamp" data-t="07:46">[07:46]</a> <a class="yt-timestamp" data-t="07:49">[07:49]</a> <a class="yt-timestamp" data-t="07:51">[07:51]</a> <a class="yt-timestamp" data-t="07:53">[07:53]</a> <a class="yt-timestamp" data-t="07:56">[07:56]</a> <a class="yt-timestamp" data-t="07:57">[07:57]</a> <a class="yt-timestamp" data-t="07:59">[07:59]</a> <a class="yt-timestamp" data-t="08:01">[08:01]</a> <a class="yt-timestamp" data-t="08:03">[08:03]</a> <a class="yt-timestamp" data-t="08:05">[08:05]</a> <a class="yt-timestamp" data-t="08:06">[08:06]</a> <a class="yt-timestamp" data-t="08:09">[08:09]</a> <a class="yt-timestamp" data-t="08:10">[08:10]</a> <a class="yt-timestamp" data-t="08:12">[08:12]</a> <a class="yt-timestamp" data-t="08:14">[08:14]</a> <a class="yt-timestamp" data-t="08:17">[08:17]</a> <a class="yt-timestamp" data-t="08:19">[08:19]</a> <a class="yt-timestamp" data-t="08:22">[08:22]</a> <a class="yt-timestamp" data-t="08:25">[08:25]</a> <a class="yt-timestamp" data-t="08:27">[08:27]</a> <a class="yt-timestamp" data-t="08:29">[08:29]</a> <a class="yt-timestamp" data-t="08:31">[08:31]</a> <a class="yt-timestamp" data-t="08:32">[08:32]</a> <a class="yt-timestamp" data-t="08:34">[08:34]</a> <a class="yt-timestamp" data-t="08:35">[08:35]</a> <a class="yt-timestamp" data-t="08:37">[08:37]</a> <a class="yt-timestamp" data-t="08:38">[08:38]</a> <a class="yt-timestamp" data-t="08:40">[08:40]</a> <a class="yt-timestamp" data-t="08:42">[08:42]</a> <a class="yt-timestamp" data-t="08:44">[08:44]</a> <a class="yt-timestamp" data-t="08:46">[08:46]</a> <a class="yt-timestamp" data-t="08:49">[08:49]</a> <a class="yt-timestamp" data-t="08:50">[08:50]</a>

### Version 3: Adding Tools

Tools give AI agents the ability to interact with the external world, such as searching for flights or getting weather information [11:38, 11:41, 11:42, 11:44, 11:47]. A weather tool is added to help the travel agent recommend activities based on climate [11:49, 11:50, 11:51, 11:54, 11:56].

*   **Define Tool Function**: A standard Python function is decorated with `@function_tool` to mark it as an agent tool [12:03, 12:05, 12:07, 12:10, 12:12, 12:14, 12:16].
    *   Parameters for the tool are determined by the LLM based on the conversation [12:20, 12:23, 12:25, 12:27, 12:30].
    *   A docstring within the function describes its purpose and when the LLM should use it [12:34, 12:36, 12:38, 12:40, 12:42].
    *   The return value of the function is given back to the LLM for it to reason about the result [12:26, 12:28, 12:31, 12:33].
*   **Add Tool to Agent**: The tool is added to the agent's `tools` list during its definition [13:43, 13:46, 13:48, 13:50, 13:52].

```python
from openai_agent import Agent, runner, function_tool
# ... (imports from V2)

WEATHER_DATA = {
    "Miami": {"temperature": "25-35°C", "conditions": "Sunny"},
    "Paris": {"temperature": "12-22°C", "conditions": "Partly Cloudy"},
    "Tokyo": {"temperature": "20-30°C", "conditions": "Humid"},
}

@function_tool
def get_weather_forecast(city: str, date: str) -> str:
    """
    Get the weather forecast for a specified city and date.
    The LLM will determine the city and date from the conversation.
    """
    if city in WEATHER_DATA:
        weather = WEATHER_DATA[city]
        return f"Weather in {city} on {date}: {weather['conditions']}, temperatures around {weather['temperature']}."
    return f"Weather forecast for {city} is not available."

travel_agent = Agent(
    name="TravelAgent",
    instructions="You are a helpful travel planning assistant. Always output a structured travel plan and consider weather conditions if available.",
    model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
    output_type=TravelPlan,
    tools=[get_weather_forecast], # New: add the weather tool
)

def main():
    queries = [
        "Plan a trip to Miami for 5 days with a budget of $2000, considering the weather for June 15th.",
        "I'm planning a trip to Paris for 7 days in August, what's the weather like?",
    ]
    for query in queries:
        print(f"\n--- Query: {query} ---")
        response: TravelPlan = runner.run(travel_agent, query)
        print(f"Destination: {response.destination}")
        print(f"Duration: {response.duration_days} days")
        print(f"Budget: ${response.recommended_budget}")
        print(f"Activities: {', '.join(response.recommended_activities)}")
        print(f"Notes: {response.notes}")

if __name__ == "__main__":
    main()
```
<a class="yt-timestamp" data-t="11:59">[11:59]</a> <a class="yt-timestamp" data-t="12:03">[12:03]</a> <a class="yt-timestamp" data-t="12:05">[12:05]</a> <a class="yt-timestamp" data-t="12:07">[12:07]</a> <a class="yt-timestamp" data-t="12:10">[12:10]</a> <a class="yt-timestamp" data-t="12:12">[12:12]</a> <a class="yt-timestamp" data-t="12:14">[12:14]</a> <a class="yt-timestamp" data-t="12:16">[12:16]</a> <a class="yt-timestamp" data-t="12:18">[12:18]</a> <a class="yt-timestamp" data-t="12:20">[12:20]</a> <a class="yt-timestamp" data-t="12:23">[12:23]</a> <a class="yt-timestamp" data-t="12:25">[12:25]</a> <a class="yt-timestamp" data-t="12:27">[12:27]</a> <a class="yt-timestamp" data-t="12:30">[12:30]</a> <a class="yt-timestamp" data-t="12:32">[12:32]</a> <a class="yt-timestamp" data-t="12:34">[12:34]</a> <a class="yt-timestamp" data-t="12:36">[12:36]</a> <a class="yt-timestamp" data-t="12:38">[12:38]</a> <a class="yt-timestamp" data-t="12:40">[12:40]</a> <a class="yt-timestamp" data-t="12:42">[12:42]</a> <a class="yt-timestamp" data-t="12:44">[12:44]</a> <a class="yt-timestamp" data-t="12:46">[12:46]</a> <a class="yt-timestamp" data-t="12:47">[12:47]</a> <a class="yt-timestamp" data-t="12:50">[12:50]</a> <a class="yt-timestamp" data-t="12:52">[12:52]</a> <a class="yt-timestamp" data-t="12:54">[12:54]</a> <a class="yt-timestamp" data-t="12:55">[12:55]</a> <a class="yt-timestamp" data-t="12:57">[12:57]</a> <a class="yt-timestamp" data-t="13:00">[13:00]</a> <a class="yt-timestamp" data-t="13:01">[13:01]</a> <a class="yt-timestamp" data-t="13:04">[13:04]</a> <a class="yt-timestamp" data-t="13:05">[13:05]</a> <a class="yt-timestamp" data-t="13:07">[13:07]</a> <a class="yt-timestamp" data-t="13:09">[13:09]</a> <a class="yt-timestamp" data-t="13:11">[13:11]</a> <a class="yt-timestamp" data-t="13:13">[13:13]</a> <a class="yt-timestamp" data-t="13:16">[13:16]</a> <a class="yt-timestamp" data-t="13:18">[13:18]</a> <a class="yt-timestamp" data-t="13:20">[13:20]</a> <a class="yt-timestamp" data-t="13:22">[13:22]</a> <a class="yt-timestamp" data-t="13:23">[13:23]</a> <a class="yt-timestamp" data-t="13:26">[13:26]</a> <a class="yt-timestamp" data-t="13:28">[13:28]</a> <a class="yt-timestamp" data-t="13:31">[13:31]</a> <a class="yt-timestamp" data-t="13:33">[13:33]</a> <a class="yt-timestamp" data-t="13:34">[13:34]</a> <a class="yt-timestamp" data-t="13:37">[13:37]</a> <a class="yt-timestamp" data-t="13:39">[13:39]</a> <a class="yt-timestamp" data-t="13:41">[13:41]</a> <a class="yt-timestamp" data-t="13:43">[13:43]</a> <a class="yt-timestamp" data-t="13:46">[13:46]</a> <a class="yt-timestamp" data-t="13:48">[13:48]</a> <a class="yt-timestamp" data-t="13:50">[13:50]</a> <a class="yt-timestamp" data-t="13:52">[13:52]</a> <a class="yt-timestamp" data-t="13:54">[13:54]</a>

### Version 4: Agent Handoffs and Mixture of Experts

To prevent hallucinations when an agent handles too many tools, a "mixture of experts" approach is beneficial, where multiple specialized agents collaborate [14:40, 14:43, 14:45, 14:48, 14:50, 14:53, 14:55, 14:57, 15:00, 15:02]. This version adds flight and hotel agents [15:05, 15:07, 15:09, 15:11]. The primary travel agent can then hand off the conversation to these specialists as needed [15:13, 15:16, 15:18].

*   **Define Specialized Agents and Tools**:
    *   A `FlightRecommendation` Pydantic model and `search_flights` tool are created for the flight agent [15:29, 15:30, 15:32, 15:34, 15:36, 15:37, 15:40, 15:41, 15:44, 15:46, 15:48].
    *   Similarly, a `HotelRecommendation` Pydantic model and `search_hotels` tool are created for the hotel agent [17:03, 17:05, 17:08, 17:11, 17:13, 17:15, 17:17, 17:19, 17:20, 17:23, 17:25, 17:28].
*   **Define `handoff_description`**: Each specialized agent includes a `handoff_description` attribute, which tells the primary agent when to transfer control [16:29, 16:31, 16:34, 16:36, 16:39, 17:46, 17:49, 17:52].
*   **Add Handoffs to Primary Agent**: The primary agent's `handoffs` parameter lists the specialized agents it can call upon [18:10, 18:12, 18:15, 18:18, 18:21, 18:22, 18:24, 18:27, 18:29].

```python
from openai_agent import Agent, runner, function_tool
from pydantic import BaseModel, Field
import os

# ... (TravelPlan, get_weather_forecast, WEATHER_DATA from V3)

# New: Flight Agent Models and Tools
class FlightRecommendation(BaseModel):
    airline: str
    departure_time: str
    arrival_time: str
    price: float
    notes: str

MOCK_FLIGHTS = {
    ("New York", "Chicago"): [
        {"airline": "Ocean Air", "departure_time": "08:00 AM", "arrival_time": "10:00 AM", "price": 150.00},
        {"airline": "SkyJet", "departure_time": "09:00 AM", "arrival_time": "11:00 AM", "price": 180.00},
    ],
}

@function_tool
def search_flights(origin: str, destination: str, date: str) -> list[dict]:
    """
    Search for flights from an origin city to a destination city on a specific date.
    The LLM will determine the origin, destination, and date from the conversation.
    """
    key = (origin, destination)
    if key in MOCK_FLIGHTS:
        return MOCK_FLIGHTS[key]
    return []

flight_agent = Agent(
    name="FlightSpecialist",
    handoff_description="This agent specializes in finding and recommending flights.",
    instructions="You are a flight booking specialist. Use the search_flights tool to find flight options.",
    model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
    tools=[search_flights],
    output_type=FlightRecommendation,
)

# New: Hotel Agent Models and Tools
class HotelRecommendation(BaseModel):
    hotel_name: str
    location: str
    price_per_night: float
    amenities: list[str]
    justification: str

MOCK_HOTELS = {
    "Paris": [
        {"hotel_name": "Grand Hotel Paris", "location": "City Center", "price_per_night": 250.00, "amenities": ["Pool", "Wi-Fi"]},
        {"hotel_name": "Eiffel View Inn", "location": "Near Eiffel Tower", "price_per_night": 350.00, "amenities": ["Wi-Fi", "Restaurant"]},
    ],
}

@function_tool
def search_hotels(city: str, date: str, max_price: float = None, amenities: list[str] = None) -> list[dict]:
    """
    Search for hotels in a specific city for a given date, with optional max price and amenities.
    """
    if city in MOCK_HOTELS:
        filtered_hotels = []
        for hotel in MOCK_HOTELS[city]:
            if max_price is None or hotel["price_per_night"] <= max_price:
                if amenities is None or all(a in hotel["amenities"] for a in amenities):
                    filtered_hotels.append(hotel)
        return filtered_hotels
    return []

hotel_agent = Agent(
    name="HotelSpecialist",
    handoff_description="This agent specializes in finding and recommending hotels.",
    instructions="You are a hotel booking specialist. Use the search_hotels tool to find hotel options.",
    model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
    tools=[search_hotels],
    output_type=HotelRecommendation,
)

travel_agent = Agent(
    name="TravelAgent",
    instructions="You are a helpful travel planning assistant. Use tools and handoff to specialized agents when appropriate.",
    model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
    output_type=TravelPlan,
    tools=[get_weather_forecast],
    handoffs=[flight_agent, hotel_agent], # New: define handoffs
)

def main():
    queries = [
        "I need a flight from New York to Chicago for next month.",
        "Find me a hotel in Paris with a pool for under $300 per night for my trip in August.",
    ]
    for query in queries:
        print(f"\n--- Query: {query} ---")
        response = runner.run(travel_agent, query)
        # Dynamic printing based on response type (simplified for example)
        if isinstance(response, FlightRecommendation):
            print(f"Airline: {response.airline}, Departure: {response.departure_time}, Price: ${response.price}")
        elif isinstance(response, HotelRecommendation):
            print(f"Hotel: {response.hotel_name}, Price: ${response.price_per_night}, Amenities: {', '.join(response.amenities)}")
        else:
            print(f"Destination: {response.destination}, Budget: ${response.recommended_budget}")


if __name__ == "__main__":
    main()
```
<a class="yt-timestamp" data-t="15:20">[15:20]</a> <a class="yt-timestamp" data-t="15:22">[15:22]</a> <a class="yt-timestamp" data-t="15:24">[15:24]</a> <a class="yt-timestamp" data-t="15:26">[15:26]</a> <a class="yt-timestamp" data-t="15:29">[15:29]</a> <a class="yt-timestamp" data-t="15:30">[15:30]</a> <a class="yt-timestamp" data-t="15:32">[15:32]</a> <a class="yt-timestamp" data-t="15:34">[15:34]</a> <a class="yt-timestamp" data-t="15:36">[15:36]</a> <a class="yt-timestamp" data-t="15:37">[15:37]</a> <a class="yt-timestamp" data-t="15:40">[15:40]</a> <a class="yt-timestamp" data-t="15:41">[15:41]</a> <a class="yt-timestamp" data-t="15:44">[15:44]</a> <a class="yt-timestamp" data-t="15:46">[15:46]</a> <a class="yt-timestamp" data-t="15:48">[15:48]</a> <a class="yt-timestamp" data-t="15:50">[15:50]</a> <a class="yt-timestamp" data-t="15:53">[15:53]</a> <a class="yt-timestamp" data-t="15:55">[15:55]</a> <a class="yt-timestamp" data-t="15:58">[15:58]</a> <a class="yt-timestamp" data-t="16:01">[16:01]</a> <a class="yt-timestamp" data-t="16:03">[16:03]</a> <a class="yt-timestamp" data-t="16:05">[16:05]</a> <a class="yt-timestamp" data-t="16:08">[16:08]</a> <a class="yt-timestamp" data-t="16:11">[16:11]</a> <a class="yt-timestamp" data-t="16:12">[16:12]</a> <a class="yt-timestamp" data-t="16:14">[16:14]</a> <a class="yt-timestamp" data-t="16:16">[16:16]</a> <a class="yt-timestamp" data-t="16:18">[16:18]</a> <a class="yt-timestamp" data-t="16:20">[16:20]</a> <a class="yt-timestamp" data-t="16:22">[16:22]</a> <a class="yt-timestamp" data-t="16:25">[16:25]</a> <a class="yt-timestamp" data-t="16:27">[16:27]</a> <a class="yt-timestamp" data-t="16:29">[16:29]</a> <a class="yt-timestamp" data-t="16:31">[16:31]</a> <a class="yt-timestamp" data-t="16:34">[16:34]</a> <a class="yt-timestamp" data-t="16:36">[16:36]</a> <a class="yt-timestamp" data-t="16:39">[16:39]</a> <a class="yt-timestamp" data-t="16:41">[16:41]</a> <a class="yt-timestamp" data-t="16:43">[16:43]</a> <a class="yt-timestamp" data-t="16:45">[16:45]</a> <a class="yt-timestamp" data-t="16:48">[16:48]</a> <a class="yt-timestamp" data-t="16:50">[16:50]</a> <a class="yt-timestamp" data-t="16:52">[16:52]</a> <a class="yt-timestamp" data-t="16:54">[16:54]</a> <a class="yt-timestamp" data-t="16:56">[16:56]</a> <a class="yt-timestamp" data-t="16:57">[16:57]</a> <a class="yt-timestamp" data-t="16:59">[16:59]</a> <a class="yt-timestamp" data-t="17:01">[17:01]</a> <a class="yt-timestamp" data-t="17:03">[17:03]</a> <a class="yt-timestamp" data-t="17:05">[17:05]</a> <a class="yt-timestamp" data-t="17:08">[17:08]</a> <a class="yt-timestamp" data-t="17:11">[17:11]</a> <a class="yt-timestamp" data-t="17:13">[17:13]</a> <a class="yt-timestamp" data-t="17:15">[17:15]</a> <a class="yt-timestamp" data-t="17:17">[17:17]</a> <a class="yt-timestamp" data-t="17:19">[17:19]</a> <a class="yt-timestamp" data-t="17:20">[17:20]</a> <a class="yt-timestamp" data-t="17:23">[17:23]</a> <a class="yt-timestamp" data-t="17:25">[17:25]</a> <a class="yt-timestamp" data-t="17:28">[17:28]</a> <a class="yt-timestamp" data-t="17:30">[17:30]</a> <a class="yt-timestamp" data-t="17:33">[17:33]</a> <a class="yt-timestamp" data-t="17:35">[17:35]</a> <a class="yt-timestamp" data-t="17:38">[17:38]</a> <a class="yt-timestamp" data-t="17:40">[17:40]</a> <a class="yt-timestamp" data-t="17:43">[17:43]</a> <a class="yt-timestamp" data-t="17:44">[17:44]</a> <a class="yt-timestamp" data-t="17:46">[17:46]</a> <a class="yt-timestamp" data-t="17:49">[17:49]</a> <a class="yt-timestamp" data-t="17:52">[17:52]</a> <a class="yt-timestamp" data-t="17:54">[17:54]</a> <a class="yt-timestamp" data-t="17:57">[17:57]</a> <a class="yt-timestamp" data-t="17:59">[17:59]</a> <a class="yt-timestamp" data-t="18:01">[18:01]</a> <a class="yt-timestamp" data-t="18:03">[18:03]</a> <a class="yt-timestamp" data-t="18:05">[18:05]</a> <a class="yt-timestamp" data-t="18:06">[18:06]</a> <a class="yt-timestamp" data-t="18:08">[18:08]</a> <a class="yt-timestamp" data-t="18:10">[18:10]</a> <a class="yt-timestamp" data-t="18:12">[18:12]</a> <a class="yt-timestamp" data-t="18:15">[18:15]</a> <a class="yt-timestamp" data-t="18:18">[18:18]</a> <a class="yt-timestamp" data-t="18:21">[18:21]</a> <a class="yt-timestamp" data-t="18:22">[18:22]</a> <a class="yt-timestamp" data-t="18:24">[18:24]</a> <a class="yt-timestamp" data-t="18:27">[18:27]</a> <a class="yt-timestamp" data-t="18:29">[18:29]</a>

### Version 5: Guard Rails, Context, and Tracing

This final version integrates advanced features to improve agent robustness and personalization:

#### Guard Rails
A budget guardrail is implemented to check if a user's trip request is realistic before the agent attempts to plan it [19:37, 19:39, 19:41, 19:43, 19:45, 19:48, 19:50, 19:51, 19:53, 19:56, 19:58, 20:00]. This prevents the agent from attempting to process impossible scenarios [21:10, 21:12, 21:20, 21:22].

*   **Define Guardrail Agent**: A `BudgetAnalysis` model and corresponding agent are created to determine if a budget is realistic [20:02, 20:04, 20:05, 20:07, 20:09, 20:11, 20:12].
*   **Implement Guardrail Function**: A function (`budget_guard_rail`) prompts the `BudgetAnalysis` agent and sets a `trip_wire_triggered` flag if the budget is unrealistic [20:29, 20:31, 20:33, 20:35, 20:37, 20:39, 20:40, 20:42, 20:44, 20:46, 20:47, 20:49, 20:52, 20:54, 20:57, 20:59, 21:01, 21:03, 21:05, 21:09, 21:10, 21:12, 21:15, 21:18, 21:20, 21:22, 21:24, 21:26, 21:28, 21:30].
*   **Add to Agent**: The `input_guard_rails` parameter of the primary agent is assigned this guardrail function [21:34, 21:36, 21:38, 21:40].

#### User Context Management
The Agent SDK allows passing metadata (like user ID or preferences) to tools without explicitly including it in the LLM's prompt [22:53, 22:55, 22:58, 23:00, 23:04, 23:06, 23:09, 23:10, 23:13, 23:15, 23:17, 23:20, 23:22]. This enables tools to alter their behavior based on user context, enhancing personalization [23:24, 23:26, 23:28, 23:31, 23:33, 23:34, 23:36, 23:39, 23:40, 23:42, 23:45, 23:48, 23:50, 23:52, 23:54, 23:56, 23:58, 24:00, 24:02, 24:05, 24:07, 24:09, 24:11, 24:14, 24:17, 24:18, 24:20, 24:23, 24:26, 24:28, 24:29, 24:31, 24:33, 24:35, 24:37, 24:40, 24:43, 24:45, 24:47, 24:50, 24:52, 24:53, 24:55, 24:57, 24:59, 25:00, 25:02].

*   **Define User Context Class**: A `UserContext` data class stores user preferences (e.g., `preferred_airlines`, `hotel_amenities`) [23:00, 23:04].
*   **Pass Context to Runner**: The `runner.run` function accepts a `user_context` parameter, which is then made available to tools via a `wrapper` argument in their function signatures [23:48, 23:50, 23:52, 23:54, 23:56, 23:58, 24:00, 24:02, 24:05, 24:07, 24:09, 24:11, 24:14].

#### Tracing
Tracing allows monitoring agent execution to understand workflows, debug issues, and ensure proper functionality [25:04, 25:05, 25:08, 25:10, 25:12]. While OpenAI's platform provides default tracing, custom integrations like Pydantic Logfire are recommended for broader compatibility (e.g., with OpenRouter or Ollama) and powerful features [25:14, 25:17, 25:20, 25:21, 25:23, 25:25, 25:27, 25:30, 25:32, 25:35, 25:37, 25:39, 25:42, 25:44].

*   **Integration with Logfire**: Logfire can be integrated with just two lines of code, providing detailed traces of agent execution, including calls to agents, guardrails, and LLMs [25:50, 25:52, 25:54, 25:56, 25:58, 26:00, 26:02, 26:04, 26:07, 26:08, 26:10, 26:11, 26:13, 26:15, 26:17, 26:20, 26:22, 26:24, 26:28, 26:31, 26:33, 26:35, 26:37, 26:40, 26:42, 26:44, 26:45, 26:47, 26:49, 26:51, 26:53, 26:56, 26:58, 26:59, 27:02, 27:04].

## Evaluation of the OpenAI Agent SDK

The OpenAI Agent SDK is easy to use and powerful for [[Building AI Agents | building agentic systems]] [28:29, 28:32, 30:42, 30:43, 30:45]. It offers features like guard rails, which are often missing in other frameworks [22:43, 22:44, 22:47, 22:49].

However, compared to more mature frameworks like [[Building AI agents with Pydantic AI | Pydantic AI]] and LlamaGraph, it has some limitations:
*   **Abstraction vs. Control**: The SDK leans towards a higher level of abstraction, similar to LangChain and CrewAI, which can lead to an "abstraction distraction" [28:02, 28:05, 28:06, 28:09]. While simple to use, this reduces low-level control and customizability, making it harder to adapt agents to unique needs [27:52, 27:55, 27:57, 27:58, 28:11, 28:13, 28:15, 28:16, 28:19, 28:21, 30:04, 30:06, 30:08, 30:10, 30:12, 30:47, 30:49, 30:52]. For instance, complex handoff scenarios (e.g., multiple agents, custom pre/post-handoff rules) are not straightforward [28:36, 28:38, 28:40, 28:42, 28:45, 28:47, 28:49, 28:51, 28:53].
*   **Missing Human-in-the-Loop**: The SDK lacks built-in support for human approval or intervention before tool calls or agent execution, a feature well-supported by LlamaGraph [29:04, 29:07, 29:09, 29:11, 29:13, 29:16, 29:17, 29:21].
*   **Testing and Evaluation**: Unlike [[Understanding AI agents | Pydantic AI]], which offers detailed documentation and features for testing agents with mock LLMs and tools, the Agent SDK currently provides no direct guidance on testing or evaluating agent performance [29:29, 29:32, 29:35, 29:37, 29:39, 29:41, 29:43, 29:45, 29:47, 29:50, 29:52, 29:55, 29:58].

Despite these points, as a brand new framework, the OpenAI Agent SDK is expected to evolve and add more features over time [30:01, 30:54, 30:56, 30:58, 31:00]. It provides a good [[Building AI agents from scratch with Python | starting point for building AI agents from scratch with Python]] due to its simplicity [27:06, 27:09, 27:12, 27:14, 27:16].