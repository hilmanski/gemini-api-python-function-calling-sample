# About
Connecting Google Gemini API to the internet using SerpApi: Google Answer Box API

Step-by-step tutorial: [Read the blog post here.](https://serpapi.com/blog/access-real-time-data-with-gemini-api-using-function-calling)

## How to run the basic sample

Python env setup (one time only)
```
python -m venv env 
```

Activate source
```
source env/bin/activate
```

Install Gemini Python SDK
```
pip install google-generativeai
```

Gemini Setup
- Get your API Key
- Export it with
```
export GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Run
```
python main.py
```

## How to run the realtime sample
Install SerpApi package
```
pip install google-search-results
export SERPAPI_API_KEY='GET_YOUR_API_KEY_FROM_SERPAPI_DOT_COM'
```

Run 
```
python realtime.py
```


## Reference
- [Gemini API Function Calling Docs](https://ai.google.dev/gemini-api/docs/function-calling)
- [SerpApi answer box](https://serpapi.com/direct-answer-box-api)
- https://github.com/google-gemini/cookbook/blob/main/quickstarts/Function_calling_config.ipynb
- https://codelabs.developers.google.com/codelabs/gemini-function-calling#6 (common way - using function declaration)