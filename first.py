from fastapi import FastAPI

app = FastAPI()

items = []


@app.get("/")
def root():
    return {"hello", "word"}


@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items
