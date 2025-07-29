import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/edamam/api/edamam-nutrition-analysis'

mcp = FastMCP('edamam-nutrition-analysis')

@mcp.tool()
def api_nutrition_data(ingr: Annotated[str, Field(description='The ingredient.')],
                       nutrition_type: Annotated[Union[str, None], Field(description='Select between the cooking and food logging processor.')] = None) -> dict: 
    '''This returns the nutritional analysis for the specified food text by extracting information from a short unstructured food text (usually an ingredient line and returns the following structured data for the text: quantity, measure and food,) and if available: diet, health and allergen labels for the text. With the built in food logging feature, this allows for change of context. For example, “rice” will normally be matched to raw rice while, with the food logging feature on, it will match to ready to eat ‘cooked rice.’ <b>Access Point:</b> https://api.edamam.com/api/nutrition-data'''
    url = 'https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-data'
    headers = {'x-rapidapi-host': 'edamam-edamam-nutrition-analysis.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ingr': ingr,
        'nutrition-type': nutrition_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def api_nutrition_details(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''This returns the nutritional information based on a POST request of the recipe content. The POST request submits the recipe content, specifically the recipe title and ingredient list. The response the API returns, will contain the nutritional analysis for the recipe based on the information provided. <b>Access Point:</b> https://api.edamam.com/api/nutrition-details'''
    url = 'https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-details'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'edamam-edamam-nutrition-analysis.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
