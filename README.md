# aws-sam-tutorial

## mangum
- lambdaでAPIを実行するためのライブラリ

## aws sam
- サーバレスアプリをビルド&デプロイするためのツール

## ビルド ~ ローカル実行の手順

### requirements.txtをapi/配下に作成
`poetry export --without-hashes > api/requirements.txt`
<br/>テンプレートのCodeUriに指定したディレクトリのrequirements.txtからしか、必要なパッケージを読み取れない(?)ため

### lambda向けdockerのコンテナイメージをビルドする
`sam build --use-container`

### ローカルでAPIを立ち上げ
`sam local start-api`

## その他

### cognito client-idの記載場所
「ユーザープール」> 「アプリケーションの統合」>「アプリケーションクライアントのリスト」