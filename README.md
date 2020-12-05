# crypto-asset-easy-management

Python と Excel を用いて取引所上の暗号資産の管理を簡易的に行えるツールを作ってみました。

毎日定時、毎週決まった曜日、毎月決まった日付での定期的な買い・売りを自動的に行い、その記録をエクセルに残していくことができるツールです。

およそ 1 週間程度で、ささっとつくったので、細かい箇所にはバグがあったりするかもしれません。もしご利用頂く場合は、自己責任の元で、お願いします。

ソースコードは GitHub を参照ください。

[https://github.com/YasunoriMATSUOKA/crypto-asset-easy-management](https://github.com/YasunoriMATSUOKA/crypto-asset-easy-management)

まずは簡単に使用方法を説明します。

## 環境構築

### git clone

レポジトリをクローンしてください。

公開鍵認証の方

```sh
git clone git@github.com:YasunoriMATSUOKA/crypto-asset-easy-management.git
```

GitHub CLI の方

```sh
gh repo clone YasunoriMATSUOKA/crypto-asset-easy-management
```

それ以外の方

```sh
git clone https://github.com/YasunoriMATSUOKA/crypto-asset-easy-management.git
```

### ディレクトリへ移動

クローンしたディレクトリに移動してください。

```sh
cd crypto-asset-easy-management
```

### 設定ファイルとデータファイルを git の追跡対象から除く

最終的に認証情報を書き込むことになる config.xlsx や履歴を蓄積していく data.xlsx については、初回のレポジトリクローンでひな型ファイルを手元に入手した後、以下コマンドを実行して git の追跡対象から明示的に除いてローカルにコミットしておいたほうが良いでしょう。

```sh
git rm --cached config.xlsx
```

```sh
git rm --cached data.xlsx
```

### Python のインストール

各自の環境に合わせて 3.x 系列のバージョンをインストールしてください。ここの手順の詳細説明は省略します。

### pip の最新化

以下のようなコマンドを実行して頂けばよいのですが、python3 の箇所は各自の環境によって異なると思うので適宜読み替えて対応してください。

```sh
python3 -m pip install --upgrade pip
```

ポイントとしては、Python の実行ファイルのパスを指定できる方法なら何でも OK です。
パスやランチャーが設定済で、python や python3 や py や py3.7 や py3.8 等で実行できるのであれば、そちらを使っていただいて OK と思いますし、直接実行ファイルのパスを指定して頂いても OK と思います。
ただし、以降のライブラリのインストール先と揃っていないと、ライブラリインストールしたのに、ライブラリが見つからないエラーが発生したりすると思うので、そのあたりは揃える必要があることにご注意ください。

### ライブラリのインストール

必要なライブラリをインストールしていきます。エクセル操作に Pandas、取引所連携用のライブラリとして ccxt、スケジュール実行支援ライブラリとして schedule、その他、Pandas、エクセル周りで必要なライブラリをインストールします。
具体的には以下コマンドを全て実行してください。

#### NumPy

```sh
pip install numpy
```

#### pandas

```sh
pip install pandas
```

#### xlrd

```sh
pip install xlrd
```

#### ccxt

```sh
pip install ccxt
```

#### schedule

```sh
pip install schedule
```

#### xlwt

```sh
pip install xlwt
```

#### openpyxl

```sh
pip install openpyxl
```

## 設定ファイル、取引記録ファイルのテンプレートファイルをコピーしてリネーム

実際に使用する設定ファイルは、Git の追跡対象から除外するために、`config_template.xlsx`をコピーして`config.xlsx`にリネームして、`config.xlsx`ファイルの方を使用してください。
また、実際に使用する取引記録ファイルについても、同様に Git の追跡対象から除外するために、`data_template.xlsx`をコピーして`data.xlsx`にリネームして、`data.xlsx`ファイルの方を使用してください。

## 設定ファイルへ定期自動買い付けの設定を記入

設定ファイルは、エクセルファイルの`config.xlsx`です。
各シートでの設定項目について、簡単に説明します。
起動前に、こちらの設定ファイルへ、API Key, API Secret や、自動買い付けの設定等を記入してください。

### シート：api

- exchange_name: 取引所名は小文字で正確に記入頂く必要があります。デフォルトでは`zaif`が指定されています。(本記事のほとんど唯一の NEM 的な要素かもしれません(汗))
- api_key: 取引所連携のために必要な API Key をこちらに記入してください。
- api_secret: 取引所連携のために必要な API Secret をこちらに記入してください。
- api_key, api_secret は取引所にログインして、各自取得する必要があります。その手順は省略します。

なお、API Key, API Secret は取引所の資産に直接アクセスできる、極めて繊細な認証情報なので、取引所の ID やパスワードと同等かそれ以上に注意して扱い、秘密を保つよう心掛け、漏洩のリスクが疑われる状況が生じた場合、即座に取引所から無効化できるよう、意識しておくことが大切です。

デフォルトは以下の状態ですが、このままでは動作しないので、各自で取引所の API Key, API Secret を取得して、記入してください。

| exchange_name | api_key          | api_secret          |
| ------------- | ---------------- | ------------------- |
| zaif          | put_your_api_key | put_your_secret_key |

### シート: auto_periodic_trade

- exchange_name: 取引所名 ... api シートで指定していない取引所をここに指定するとエラーになります。デフォルトでは`zaif`が指定してあります。(本記事のほとんど唯一の...以下略)
- pair: 取引したい資産ペアを半角英数大文字、`/`区切りで指定してください。例えば NEM ならば、`XEM/JPY`のようになります。(本記事のほとんど唯一の...以下略)
- type: 指値注文、成行注文をこちらで指定できます。成行注文は zaif では対応していないため、指値注文の`limit`がデフォルトで指定してあります。他の取引所で成行注文を使う場合は、`market`を指定してください。
- side: 買い、売りのどちらかをここで指定します。買いの場合は`buy`、売りの場合は`sell`を指定してください。デフォルトは`buy`にしてあります。
- amount: 買い、売りしたい数量を、次の項目の`unit`とともに指定してください。
- unit: 買い、売りしたい数量の単位を前の項目の`amount`とともに指定してください。
- period: 毎日指定時刻に取引を行うか、毎週決まった曜日に取引を行うか、毎月決まった日付に取引を行うかをここで指定できます。毎日指定時刻に取引を行う場合は`daily`、毎週決まった曜日に取引を行う場合は`weekly`、毎月決まった日付に取引を行う場合は`monthly`を指定してください。

デフォルトでは、以下のようになっていると思います。皆様のお好みに合わせて適宜修正してください。

| exchange_name | pair    | type  | side | amount | unit | period  |
| ------------- | ------- | ----- | ---- | ------ | ---- | ------- |
| zaif          | XEM/JPY | limit | buy  | 100    | JPY  | daily   |
| zaif          | XEM/JPY | limit | buy  | 100    | JPY  | weekly  |
| zaif          | XEM/JPY | limit | buy  | 100    | JPY  | monthly |

### シート: ticker

- exchange_name: 取引所名
- pair: 取引したい資産ペアを半角英数大文字、`/`区切りで指定
- min_order_amount: 各資産毎に 1 回の取引で注文できる最小数量が設定されています。例えば`zaif`の`XEM/JPY`の場合、`1XEM`以上である必要があります。
- min_order_unit: 各資産毎に取引の際に指定できる数量の最小単位が設定されています。例えば`zaif`の`XEM/JPY`の場合、`0.1XEM`単位の精度までしか、取引したい数量を設定できません。
- min_price_unit: 各資産の取引所の価格についても、取引の際に指定できる最小単位が設定されています。例えば`zaif`の`XEM/JPY`の場合、`0.0001JPY`単位の精度までしか価格を指定できません。

デフォルトでは以下のようになっています。

| exchange_name | pair    | min_order_amount | min_order_unit | min_price_unit |
| ------------- | ------- | ---------------- | -------------- | -------------- |
| zaif          | XEM/JPY | 1                | 0.1            | 0.0001         |

### シート: time

- period: 自動取引のタイミング, `daily`, `weekly`, `monthly`の 3 種類
- time: 文字列として`HH:MM`の形式で指定頂く必要があります。例えば`'08:30`のような形でエクセルに入力して頂くと良いかと思います。
- day_of_every_weeks: period が`weekly`の場合、必要です。

デフォルトでは以下のようになっています。

| period  | time   | day_of_every_weeks | day_of_every_months |
| ------- | ------ | ------------------ | ------------------- |
| daily   | '07:30 |                    |                     |
| weekly  | '07:30 | Thursday           |                     |
| monthly | '07:30 |                    | 3                   |

## 起動

以下コマンドで実行すると、設定ファイルを読み込んで、指定されたタイミングで、指定された資産を指定された数量で、自動的に繰り返し注文が行われます。

```sh
python3 main.py
```

注文の記録は、エクセルファイル`data.xlsx`に記録されていくので、過去にどのような注文を出したか特に意識せずに記録を手元に残すことができます。

なお、`data.xlsx`が開いていた場合、記録を書き込むことができなくなってしまうため、動作中は`data.xlsx`をなるべく開かないようにしたほうが良いと思います。

なお、この処理は放置していると、半永久的に動作し続けます。
停止させる際には、`Ctrl` + `C`を入力してください。

## 解説

### 特徴

#### ログ出力の設定

コンソールへの出力、ログファイルへの出力、それぞれでログレベルを独立に設定したり、ログファイルのローテーションを設定したり、ログレベルを意識してかなり細かくログを入れる等の実装を行いました。エントリーポイント以降は、エントリーポイントの logger の子を引き継いでそのまま使用することで、設定が引き継がれ、ログレベルやログファイル出力先やログローテーション等の設定も引き継がれるのは、とても便利でした。

ログレベルは、デフォルトでは、コンソールには`INFO`、ログファイルには`DEBUG`でログ出力されるように設定してあります。コンソールに`CRITICAL`、`ERROR`、`WARNING`等が出力されていた場合は、何らかの設定ミスや、通信がうまく行かなかった等の場合が考えられるので、必要に応じてログファイル`log/log.log`の詳細なデバッグログを確認頂くと、問題解決の助けになるかもしれません。過去のログは、毎日ローテーションされていき、31 日分のファイルが保持される設定としています。

エントリーポイントのファイルとエントリーポイントから読んでいる子プロセスのファイルの内容をこちらに記載しておくので、もし良ければ参考にして頂けると幸いです。

エントリーポイント

```python:main.py
import traceback
from logging import getLogger, handlers, StreamHandler, Formatter, DEBUG, INFO, WARNING, ERROR, CRITICAL, basicConfig
from src.start import start


def main():
    logger.info("start")
    start()


if __name__ == "__main__":
    streamHandler = StreamHandler()
    streamHandler.setLevel(INFO)

    fileHandler = handlers.TimedRotatingFileHandler(
        filename="log/log.log",
        when="MIDNIGHT",
        backupCount=31,
        encoding="utf-8"
    )
    fileHandler.setLevel(DEBUG)

    formatter = "%(asctime)s : %(levelname)s : %(module)s : %(message)s"
    fileHandler.setFormatter(Formatter(formatter))
    streamHandler.setFormatter(Formatter(formatter))

    basicConfig(
        handlers=[streamHandler, fileHandler]
    )

    logger = getLogger(__name__)
    logger.setLevel(DEBUG)

    try:
        main()
    except Exception as error:
        logger.critical(error)
        logger.debug(traceback.format_exc())

```

子プロセス

```python:src/start.py
import time
import traceback
from logging import getLogger
import schedule
from src.utils.config.get_auto_periodic_trade_dict import get_auto_periodic_trade_dict
from .set_schedule import set_schedule

logger = getLogger("__main__").getChild(__name__)


def start():
    logger.debug("start")
    auto_periodic_trade_dict = get_auto_periodic_trade_dict()
    for trade_config in auto_periodic_trade_dict:
        try:
            logger.debug("try get auto periodic trade config")
            exchange_name = trade_config["exchange_name"]
            logger.debug(exchange_name)
            pair = trade_config["pair"]
            logger.debug(pair)
            type = trade_config["type"]
            logger.debug(type)
            side = trade_config["side"]
            logger.debug(side)
            amount = trade_config["amount"]
            logger.debug(amount)
            unit = trade_config["unit"]
            logger.debug(unit)
            period = trade_config["period"]
            logger.debug(period)
            try:
                logger.debug("try set schedule")
                set_schedule(
                    period,
                    exchange_name,
                    pair,
                    type,
                    side,
                    amount,
                    unit,
                    schedule
                )
                logger.info("success")
            except Exception as error:
                logger.error("failure")
                logger.error(error)
                logger.debug(traceback.format_exc())
        except Exception as error:
            logger.error("failure")
            logger.error(error)
            logger.debug(traceback.format_exc())
    while True:
        schedule.run_pending()
        time.sleep(1)

```

なお、本記事においては、これ以降お見せするコード上では、敢えて`logger`や例外処理の`try/catch`を除いて見やすくしたコードを参考に置いておくので、その旨ご承知おきください。

#### 定時実行処理で schedule を使用

毎日決まった時間や、毎週決まった曜日や、毎月決まった日付に処理を行うために、schedule というライブラリを使用しています。

サンプルとなりうるコードをこちらに残しておきます。

```python:src/start.py
import time
import schedule
from src.utils.config.get_auto_periodic_trade_dict import get_auto_periodic_trade_dict
from .set_schedule import set_schedule


def start():
    auto_periodic_trade_dict = get_auto_periodic_trade_dict()
    for trade_config in auto_periodic_trade_dict:
        exchange_name = trade_config["exchange_name"]
        pair = trade_config["pair"]
        type = trade_config["type"]
        side = trade_config["side"]
        amount = trade_config["amount"]
        unit = trade_config["unit"]
        period = trade_config["period"]
        set_schedule(
            period,
            exchange_name,
            pair,
            type,
            side,
            amount,
            unit,
            schedule
        )
    while True:
        schedule.run_pending()
        time.sleep(1)
```

```python:src/set_schedule.py
import datetime
from src.utils.config.get_time import get_time
from src.utils.config.get_day_of_every_weeks import get_day_of_every_weeks
from src.utils.config.get_day_of_every_months import get_day_of_every_months
from src.execute_order import execute_order


def set_schedule(period, exchange_name, pair, type, side, amount, unit, schedule):
    trade_time = get_time(period)
    if period == "daily":
        schedule.every().day.at(trade_time).do(
            execute_order, exchange_name, pair, type, side, amount, unit
        )
    elif period == "weekly":
        day_of_every_weeks = get_day_of_every_weeks(period)
        function_string = "schedule.every()." + day_of_every_weeks.lower() + \
            ".at(trade_time).do(execute_order, exchange_name, pair, type, side, amount, unit)"
        logger.debug(function_string)
        eval(function_string)
            logger.info("success")
    elif period == "monthly":
        day_of_every_months = get_day_of_every_months(period)
        if datetime.datetime.now().day == day_of_every_months:
            schedule.every().day.at(trade_time).do(
                execute_order, exchange_name, pair, type, side, amount, unit
            )
```

#### エクセルファイルの読書やデータ処理で pandas を使用

pandas では DataFrame という型で、データを扱うのが一般的なようです。
エクセルから pandas の DataFrame として直接読み込んだり、逆にエクセルへ pandas の DataFrame を書き込んだりといった形で使用しました。
実際に使用してみて、改めて pandas が非常に便利であることに気づきました。
Query のような感触で、pandas の表データの中からしかるべきデータを抜き出す操作が、とても直感的で分かりやすかったです。

```python:src/utils/excel/read_excel_as_df.py
import pandas as pd


def read_excel_as_df(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df
```

pandas の DataFrame からエクセルファイルに書き込み

```python:src/utils/excel/write_excel_from.py
def write_excel_from_df(df, file_path, sheet_name):
    df.to_excel(file_path, sheet_name=sheet_name, index=False)

```

pandas の DataFrame から条件に合致する行を抽出し、さらにそこから列名を指定して値を取得

```python:src/utils/config/get_min_order_amount.py
from .read_config_as_df import read_config_as_df


def get_min_order_amount(exchange_name, pair):
    config_ticker_df = read_config_as_df("ticker")
    config_ticker_exchange_df = config_ticker_df[
        config_ticker_df["exchange_name"] == exchange_name
    ]
    config_ticker_exchange_pair_df = config_ticker_exchange_df[
        config_ticker_exchange_df["pair"] == pair
    ]
    min_order_amount = config_ticker_exchange_pair_df.iloc[0]["min_order_amount"]
    return min_order_amount
```

#### 取引所連携ライブラリとして ccxt を使用

比較的有名＆自分自身も何度か記事にしたことがあるライブラリですが、全世界の様々な取引所に対応している点が魅力です。認証周り等の細かい実装を全てライブラリにお任せできるので、とても簡単に取引所連携ツールを作成することができます。JavaScript/TypeScript, PHP, Python で使用可能なライブラリです。
[https://github.com/ccxt/ccxt](https://github.com/ccxt/ccxt)

サンプルコードを以下にいくつか乗せておくので、もしよければ参考にしてみてください。

取引所のパブリックな API にアクセスするための設定

```python:src/utils/ccxt/get_public_exchange.py
import ccxt


def get_public_exchange(exchange_name):
    exchange = eval("ccxt." + exchange_name + "()")
    return exchange
```

板情報取得

```python:src/utils/ccxt/fetch_order_book.py
from .get_public_exchange import get_public_exchange


def fetch_order_book(exchange_name, pair):
    exchange = get_public_exchange(exchange_name)
    order_book = exchange.fetch_order_book(pair)
    return order_book
```

取引所のプライベートな API にアクセスするための設定

```python:src/utils/ccxt/get_private_exchange.py
import ccxt
from ..config.get_api_key import get_api_key
from ..config.get_api_secret import get_api_secret


def get_private_exchange(exchange_name):
    exchange = eval("ccxt." + exchange_name +
                    "({'apiKey': '" + get_api_key(exchange_name) + "', '" + "secret': '" + get_api_secret(exchange_name) + "'})")
    return exchange
```

指値注文、成行注文

```python:src/utils/
from .get_private_exchange import get_private_exchange

# type = "limit" 指値注文
# type = "market" 成行注文
# side = "buy" 買い
# side = "sell" 売り
# amount, price is number
# if type is "market", price is not necessary


def create_order(exchange_name, pair, type, side, amount, price=None):
    exchange = get_private_exchange(exchange_name)
    if type == "limit":
        result = exchange.create_order(
            pair,
            type=type,
            side=side,
            amount=str(amount),
            price=str(price)
        )
    elif type == "market":
        result = exchange.create_order(
            pair,
            type=type,
            side=side,
            amount=str(amount)
        )
    return result
```

## 所感

Python を書いていて思うことは、基本的に全ての処理が同期的に実行され、ライブラリが充実しているので、非常にストレスフリーで、書いていて本当に楽という印象が強かったです。

本格的な開発を行うつもりは無い方でも、日々の業務の中のちょっとしたルーチンワークの自動化や効率化にとても役立つスキルだと思うので、もし興味をお持ちいただいた方は、ソースコードを見て頂いて、「ああ、こんなことやってるんだな...」とか「俺だったらこうするぜ！」とか、何かあれば、お気軽にコメント等頂けるととても嬉しいです。

## まとめ

今年は DeFi が大きく流行し、中央集権的な取引所サービスについては、あまり目新しい出来事はなかったと思います。
しかし、それでも、法定通貨と暗号資産の交換という観点では、今後も中央集権的な取引所サービスは一定の存在感を保ち続けると思います。
そのような取引所との付き合い方として、日々の値動きにとらわれすぎず、淡々と自動的にちょっとずつ買い続ける or 保有している資産を淡々と売却して取り崩していく。
そんな形の付き合い方をこのツールやこの記事で提案できていたら幸いです。

また、暗号資産に興味がさほどない方にとっても、DX が叫ばれる現代において、本記事が、自分自身の身の回りのちょっとしたタスクやルーチンワークを合理化したり自動化したりするヒントになれば幸いです。

最後に、来年にはいよいよ NEM の次期バージョンの Symbol もローンチが予定され、今後も NEM/Symbol ブロックチェーンからは良い意味で目を離せない展開が続きそうです。今後の展開も楽しみにしています。
