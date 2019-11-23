# news-statistics

This script generates the evolution by day for multiple topics chosen by the user.

Make sure that: <b>your_current_day * number_of_topics < 500</b>

<h1>APIs used:</h1>
<ul>
  <li>
    <a href="https://newsapi.org/">News API</a>
    <p>This script is written using the developer version of the API. I'd recommend to generate a new api key if you want to test the app, as it's restricted to only 500 requests per day.</p>
  </li>  
</ul>

<h1>Libraries used:</h1>
<ul>
  <li><b>matplotlib</b> for data visualization</li>  
  <li><b>datetime</b> for retrieving the current calendar day</li>
  <li><b>calendar</b> for retrieving the last day of a specific month</li>
</ul>
