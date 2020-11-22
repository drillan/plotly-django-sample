# plotly-django-sample

Plotlyを使ったDjangoのサンプル

```bash
pip install plotly django
```

```bash
django-admin startproject mysite
cd mysite
python manage.py startapp app
```

```bash
tree
```
```bash
.
├── app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── mysite
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-38.pyc
    │   └── settings.cpython-38.pyc
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

`mysite/settings.py`

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # 追記
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 追記
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

`mysite/ulrs.py`

```python
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include(('app.urls', 'app'), namespace='app', )),
]
```

`app/urls.py`

```python
from django.urls import path

from . import views

urlpatterns = [path("", views.LineChartsView.as_view(), name="plot")]
```

`app/views.py`

```python
from django.views.generic import TemplateView
import plotly.graph_objects as go


def line_charts():
    fig = go.Figure(
        go.Scatter(x=[1, 2, 3], y=[3, 5, 2]), layout=go.Layout(width=400, height=400)
    )
    return fig.to_html(include_plotlyjs=False)


class LineChartsView(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        context = super(LineChartsView, self).get_context_data(**kwargs)
        context["plot"] = line_charts()
        return context
```

`templates/plot.html`

```html
{% block head %}
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
{% endblock %}

{% block content %}
<div class="title"><h1>Plotlyのグラフを描画</h1></div>
<div class="graph">{{plot|safe}}</div>
{% endblock %}
```

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```