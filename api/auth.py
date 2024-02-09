import boto3
from constants import COGNITO_CLIENT_ID, REGION_NAME

from api.model import AuthenticationResult

client = boto3.client("cognito-idp", region_name=REGION_NAME)


class LoginFailException(Exception):
    def __str__(self) -> str:
        return (
            "ログインに失敗しました。メールアドレスもしくはパスワードが間違っています。"
        )


class CognitoAuthClient:
    @classmethod
    def login(cls, email: str, password: str) -> str | None:
        try:
            response = client.initiate_auth(
                # ユーザー名(メールアドレス)とパスワードを使った認証方式
                # 利用可能な認証フローは、コンソールのアプリケーションクライアント設定で確認
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={"USERNAME": email, "PASSWORD": password},
                ClientId=COGNITO_CLIENT_ID,
            )

            # パスワード未登録のユーザーは、トークン取得不可
            # レスポンスに含まれるSessionの値を使って、パスワードを再設定する

            if challenge_name := response.get("ChallengeName"):
                if challenge_name == "NEW_PASSWORD_REQUIRED":
                    print("トークンを取得できません")
                    return None

            # OauthにおけるIDトークンとアクセストークン
            # IDトークン → ユーザーが認証されたことを証明するトークン
            # アクセストークン → 認証後にユーザーが同意すると発行され、認可(ユーザーがリソースにアクセスすることを許可する)に使用されるトークン

            return AuthenticationResult(
                accessToken=response["AuthenticationResult"]["AccessToken"],
                idToken=response["AuthenticationResult"]["IdToken"],
            )

        except client.exceptions.NotAuthorizedException:
            raise LoginFailException()
