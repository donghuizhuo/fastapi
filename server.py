import asyncio
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "World"}   

@app.get("/slow-data")
async def get_slow_data():
    await asyncio.sleep(2)
    return {"message": "Slow data loaded"}

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)


