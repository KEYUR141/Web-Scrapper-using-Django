# Web-Scrapper-using-Django

<div class="Intro">
  <h2>1.Introduction</h2>
  <p>
  This project is a 💻 <strong>Django-powered web application</strong> built for practicing and demonstrating 
  <strong>web scraping</strong> skills. It scrapes data from two major sources — 🎬 <strong>IMDb</strong> 
  for top movie listings and 📰 <strong>Times of India (TOI)</strong> for the latest news articles. Using libraries 
  like <code>requests</code> and <code>BeautifulSoup</code>, the data is fetched, processed, and displayed on a 
  responsive Bootstrap-powered frontend. The project features simple navigation, live search functionality, and 
  dynamic rendering of images, titles, and external links — all managed through Django views and models.
</p>
<h2>🚀 Features</h2>
<ul>
  <li>Scrapes <strong>top movies</strong> from IMDb 🎥</li>
  <li>Scrapes <strong>latest news articles</strong> from Times of India 🗞️</li>
  <li>Displays data dynamically using Django models and templates</li>
  <li>Search functionality for quickly finding movies or news</li>
  <li>Responsive Bootstrap-based UI</li>
</ul>
</div>

<div class="Second Step">
  <h2>🧠 Step 2: Code Explanation - Web Scraping Functions</h2>

<h3>🎬 <code>scrape_imdb_news()</code> - Scraping IMDb News</h3>
<ul>
  <li>📡 Sends a GET request to <code>https://m.imdb.com/news/movie/</code> with a custom User-Agent header for reliability.</li>
  <li>🧹 Parses the response using <strong>BeautifulSoup</strong> with the <code>html.parser</code>.</li>
  <li>🔍 Finds all news article containers using <code>div</code> with class <code>ipc-list-card--border-line</code>.</li>
  <li>📌 Extracts:
    <ul>
      <li><strong>Title</strong> from anchor tag</li>
      <li><strong>Description</strong> from a <code>div</code> tag</li>
      <li><strong>Image URL</strong> from <code>&lt;img&gt;</code> tag's <code>src</code></li>
      <li><strong>External Link</strong> from the anchor tag’s <code>href</code></li>
    </ul>
  </li>
  <li>💾 Each article is saved into the <code>IMBD_News</code> model using Django ORM.</li>
</ul>

<h3>🗞️ <code>scrape_toi_news()</code> - Scraping Times of India News</h3>
<ul>
  <li>🌐 Sends a GET request to <code>https://timesofindia.indiatimes.com/news</code>.</li>
  <li>📑 Uses BeautifulSoup to parse the HTML content.</li>
  <li>🔍 Searches for <code>&lt;li&gt;</code> elements that contain:
    <ul>
      <li><strong>Title</strong> from <code>&lt;p class="CRKrj"&gt;</code></li>
      <li><strong>Description</strong> from <code>&lt;p class="W4Hjm"&gt;</code></li>
      <li><strong>Image</strong> using <code>src</code> or <code>data-src</code> attributes from <code>&lt;img&gt;</code></li>
      <li><strong>External Link</strong> from <code>&lt;a href="..."&gt;</code></li>
    </ul>
  </li>
  <li>🧠 Smart check: If the image URL starts with <code>/</code>, it prepends <code>https://static.toiimg.com</code> to make it a valid link.</li>
  <li>🚫 Skips duplicate articles based on the <code>title</code> using <code>TOI_News.objects.filter(title=title).exists()</code>.</li>
  <li>📥 Finally, saves the data into the <code>TOI_News</code> model using Django ORM.</li>
</ul>

</div>
