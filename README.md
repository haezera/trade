# _pytrading_ (0.2.0)

![example workflow](https://github.com/haezera/pytrading/actions/workflows/python-app.yml/badge.svg)\
**warning: anything within pytrading shall not be miscontrued as financial advice.**\ 
**note: development has currently been paused as of 10/11/2023, as I work on some other projects. API should be semi-functional, and the TUI app should be also functional. Please keep a lookout for the web-app release!**
## _about_
trade is an algorithmic trading helper.

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
