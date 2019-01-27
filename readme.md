# 人管理アプリ with Django
## 事前準備
---
#### pipenvのインストール

`$pip install pipenv`
*バージョンの指定いる？

pipenvのシェルコマンドで起動

`$pipenv shell`

---
Djangoのインストール

`$pip install django`*バージョン指定がある時はバージョンを指定する

バーション確認で、ちゃんとインストール出来ているかの確認

```
>>> import django
>>> django.get_version()
```
---
プロジェクト作成

`$ django-admin startproject サイト名`

---
アプリ作成
`$ python manage.py startapp アプリ名`

___

