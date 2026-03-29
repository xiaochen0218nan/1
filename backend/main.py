from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="生活助理后端API",
    description="基于大模型的个人智能生活助理后端服务",
    version="0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"msg": "Hello, this is your Life Assistant API!"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get('message')
    # TODO: 调用AI模型接口获得回复，现为回显
    reply = f"你输入了：{user_input} （此处将在下一步接入大模型API）"
    return {"response": reply}
