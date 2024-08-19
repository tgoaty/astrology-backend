from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import NatalData, CompatibilityData
from services.natal_service import get_natal_description
from services.compatibility_service import get_compatibility_info

app = FastAPI()

# origins = [
#     "http://localhost:8080",
#     "https://astrol.netlify.app",
#     "http://localhost:5173",
#     "http://localhost:5172",
#     "http://localhost:5171"
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Access-Control-Allow-Origin"]
)


@app.post('/api/natal/description')
async def get_description(data: NatalData):
    result = get_natal_description(data)
    return result


@app.post('/api/compatibility')
async def get_compatibility(data: CompatibilityData):
    result = get_compatibility_info(data)
    return result


@app.get('/')
async def home():
    return 'server is working'
