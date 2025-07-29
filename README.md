markdown
# Edamam Nutrition Analysis MCP Server

Welcome to the `edamam-nutrition-analysis` MCP server. This server provides powerful tools for analyzing nutritional data using natural language processing and semantically structured data. Whether you're a developer, a startup, or a non-profit, this service offers a comprehensive solution for recipe nutrition analysis and text analysis.

## Overview

The `edamam-nutrition-analysis` server offers various functionalities to help you extract and compute nutritional information from food recipes and text inputs. It provides detailed analysis in real-time, including ingredient extraction, quantity adjustment for cooking processes, and classification of recipes for cuisine, meal, and dish types.

### Key Features

- **Real-Time Recipe Analysis**: Analyze food recipes with entity extraction, measure and quantity computation, and nutrition calculation. The server adjusts quantities for specific cooking processes like oil absorption in fried recipes, and marinate absorption.

- **Text Entity Extraction**: Extract food entities with measures and quantities from unstructured text, making it ideal for chatbots transcribing natural speech to text.

- **Detailed Nutrition Data**: Get comprehensive nutrition data output for each ingredient or text string, including calories, fats, carbohydrates, protein, cholesterol, and sodium, covering a total of 28 macro and micronutrients.

- **Diet and Health Labeling**: Automatically generate diet, allergy, and health labels like Vegan, Paleo, Gluten-Free, Low-Sodium, and Dairy-Free based on the ingredients.

- **Cost-Effective**: Free access for developers, startups, and non-profits with a basic plan. Enterprise customers can opt for low-cost licensing based on usage.

## Tools

The server provides two main tools to analyze nutritional data:

1. **Individual Text Line Analysis**
   - **Function**: `/api/nutrition-data`
   - **Description**: This tool extracts nutritional information from a short unstructured food text, such as an ingredient line. It returns structured data, including quantity, measure, and food, along with diet, health, and allergen labels if available. The built-in food logging feature allows context-sensitive analysis, matching terms like "rice" to cooked or raw forms based on context.

2. **Full Recipe Analysis**
   - **Function**: `/api/nutrition-details`
   - **Description**: This tool provides nutritional information based on a submitted recipe content through a POST request. It analyzes the recipe title and ingredient list to return comprehensive nutritional data.

Both tools are designed to deliver fast, accurate, and detailed nutritional analysis, making the `edamam-nutrition-analysis` server an invaluable resource for anyone looking to understand the nutritional content of food recipes and ingredients.

## Parameters

### Individual Text Line Analysis
- **nutrition_type**: *(optional)* String - Select between the cooking and food logging processor.
- **ingr**: *Required* String - The ingredient.

### Full Recipe Analysis
- **force**: *(optional)* Boolean - Forces the re-evaluation of the recipe.
- **beta**: *(optional)* Boolean - Allow beta features in the request and response.

Explore these tools to enhance your applications with precise nutritional insights and make informed decisions based on comprehensive dietary data.