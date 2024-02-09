from typing import Annotated

from auth import CognitoAuthClient, LoginFailException
from fastapi import FastAPI, Path
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from mangum import Mangum
from model import Account, AuthenticationResult, LoginInfo

app = FastAPI()


@app.exception_handler(LoginFailException)
def exception_handler(_: Request, exception: LoginFailException) -> JSONResponse:
    return JSONResponse(content={"message": str(exception)}, status_code=401)


@app.post("/login")
def login(body: LoginInfo) -> AuthenticationResult:
    return CognitoAuthClient.login(email=body.email, password=body.password)


@app.get("/account/{accountId}")
def get_account(account_id: Annotated[int, Path(alias="accountId")]) -> Account:
    return Account(accountId=account_id)


lambda_handler = Mangum(app)


# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, port=8000)
