from dotenv import load_dotenv

load_dotenv()

import os

REGION_NAME: str = os.getenv("REGION_NAME", "ap-northeast-1")

COGNITO_CLIENT_ID: str = os.getenv("COGNITO_CLIENT_ID")
