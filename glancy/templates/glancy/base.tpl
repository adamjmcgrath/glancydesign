{% load markup %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="description" content="Curtains and Soft Furnishings South West London">
    <title>Glancy Design - {{ page.title }}</title>
    <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Cinzel:400,700">
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
          <div id="main">{{ page.content|markdown }}</div>
          <div id="side">
          {% if page.photo %}<img src="{{ page.photo_url }}" alt="">{% endif %}
          </div>
      {% endblock %}
    </div>
    <div id="footer">© Glancy Design <span>{% now "Y" %}</span></div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
    {% block script %}{% endblock %}
    <script type="text/javascript">
        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', 'UA-1505389-9']);
        _gaq.push(['_trackPageview']);
        (function() {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
        })();
    </script>
  </body>
</html>
