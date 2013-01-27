{% load markup %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="description" content="Glancy Design Description">
    <title>Glancy Design - {{ page.title }}</title>
    <link rel="stylesheet" href="/static/css/style.css" />
  </head>
  <body id="{{ page.title|lower }}-page">
    <div id="header">
      <a href="/"><img src="static/img/logo.png" alt=""></a>
    </div>
    <div id="nav">
      <ul>
        <li id="home-link"><a href="/">Home</a></li>
        <li id="about-link"><a href="/about">About</a></li>
        <li id="portfolio-link"><a href="/portfolio">Portfolio</a></li>
        <li id="pricing-link"><a href="/pricing">Pricing</a></li>
        <li id="suppliers-link"><a href="/suppliers">Suppliers</a></li>
        <li id="contact-link"><a href="/contact">Contact</a></li>
      </ul>
    </div>
    <div id="content" class="clearfix">
      {% block content %}
          <h2>{{ page.title }}</h2>
          {{ page.content|markdown }}
      {% endblock %}
    </div>
    <div id="footer">© Glancy Design</div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
    {% block script %}{% endblock %}
  </body>
</html>
