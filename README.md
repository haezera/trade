# _pytrading_ (0.1.2)

![example workflow](https://github.com/haezera/pytrading/actions/workflows/python-app.yml/badge.svg)\
**warning: anything within pytrading shall not be miscontrued as financial advice.**
## _about_
pytrading began as a learning experience into the quantitative and algorithmic trading game. It aims to provide investors statistically driven information and actions on assets within the US (and hopefully, eventually, global) stock market. 

## _documentation_
<a href="https://haezera.github.io/pytrading/index.html" target="_blank">Link to documentation</a>

### Versions/Updates
<details closed>
<summary> Versions </summary>
<details closed>
<summary>0.1.2</summary>
  <ul>
    <li> Major user routes completed </li>
    <li> Beginning of stock analysis API routes </li>
    <li> Basic unit testing</li>
  </ul>
</details>
  
<details closed>
<summary>0.1.1</summary>
  <ul>
    <li> Establishment of API</li>
    <li> Project goal change - full stack project </li>
    <li> xlsx exporting included</li>
  </ul>
</details>

<details closed>
<summary>0.1.0</summary>
  <ul>
    <li> TUI experience</li>
    <li> Stock analysis, beta backtester implemented </li>
    <li> No API, no front end</li>
  </ul>
</details>
</details>


## _features_
TUI App:
<ul>
  <li>A fairly rigid TUI experience</li>
  <li>Retrieval of income statements for any US stock</li>
  <li>Retrieval of balance sheets for any US stock</li>
  <li>Retrieval of cash flow statements for any US stock</li>
  <li>SMA strategy (Simple moving strategy)</li>
  <li>AO strategy (Awesome oscillator strategy)</li>
  <li>VWAP strategy (Volume weighted average price)</li>
  <li>Backtesting application</li>
  <li>Backtester exporting to xlsx files</li>
</ul>
Full Stack React/Flask Application:
<ul>
  <li>Routes currently being completed</li>
  <li>mySQL server initialisation and helper queries created</li>
</ul>

## _planned features_
By version 1.0.0, the following features will be integrated:
<ul>
  <li>Live trading feature, where traders can get more information minute by minute.</li>
  <li>The implementation of my own trading algorithm (check out the research paper!)</li>
  <li>Be a REST API that interacts with a frontend (probably a JavaScript one)</li>
  <li>Stock graphing; graphing of strategies (akin to yahoo finance)</li>
</ul>

Some longer term goals are:
<ul>
  <li>Web-scraping sentiment-analysis</li>
  <li>Pairs trading using faster live analysis of two correlated assets</li>
  <li>Execution system using some sort of trading platform (to be decided)</li>
</ul>
