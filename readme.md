# 人管理アプリ with Django
## 事前準備
---
### pipenvのインストール

```bash
# *バージョンの指定いる？
$ pip install pipenv
```

### pipenvのシェルコマンドで起動

```bash
$ pipenv shell
```

---
### Djangoのインストール

```bash
# *バージョン指定がある時はバージョンを指定する
$ pip install django
```

### バーション確認で、ちゃんとインストール出来ているかの確認

```
>>> import django
>>> django.get_version()
```
---
### プロジェクト作成

```bash
$ django-admin startproject サイト名
```

---
### アプリ作成
```
$ python manage.py startapp アプリ名
```

___

