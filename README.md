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
  <li>📡 Sends a GET request to <code>https://m.imdb.com/news/movie/</code> using a custom <code>User-Agent</code> header for compatibility.</li>
  <li>🧼 Parses the HTML response using <strong>BeautifulSoup</strong> with the <code>html.parser</code>.</li>
  <li>🔍 Extracts news cards by locating all <code>&lt;div&gt;</code> tags with class <code>ipc-list-card--border-line</code>.</li>
  <li>For each news item:
    <ul>
      <li>📝 <strong>Title</strong> is fetched from an <code>&lt;a&gt;</code> tag and cleaned using <code>.text.strip()</code>.</li>
      <li>📰 <strong>Description</strong> is extracted from a <code>&lt;div&gt;</code> with class <code>ipc-html-content-inner-div</code>.</li>
      <li>🖼️ <strong>Image</strong> URL is fetched from the <code>src</code> attribute of the <code>&lt;img&gt;</code> tag.</li>
      <li>🔗 <strong>External Link</strong> is pulled from the <code>href</code> of the anchor tag.</li>
    </ul>
  </li>
  <li>💾 The extracted data is saved in the database using <code>IMBD_News.objects.create(**news)</code>.</li>
</ul>

<pre><code>def scrape_imdb_news():
    url = 'https://m.imdb.com/news/movie/'
    headers = { 
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_items = soup.find_all('div', class_='ipc-list-card--border-line')
    
    for item in news_items:
        title = item.find('a', class_="ipc-link ipc-link--base sc-dd244256-2 gbQCSG")
        description = item.find('div', class_="ipc-html-content-inner-div")
        image = item.find('img', class_="ipc-image")
        external_link = title['href'] if title else "No external link"
        
        title = title.text.strip() if title else "No Title"
        description = description.text.strip() if title else "No Description"
        image = image['src']
        
        news = {
            'title': title,
            'description': description,
            'image': image,
            'external_link': external_link
        }
        IMBD_News.objects.create(**news)
</code></pre>

<h3>🗞️ <code>scrape_toi_news()</code> - Scraping Times of India News</h3>
<ul>
  <li>🌐 Sends a GET request to <code>https://timesofindia.indiatimes.com/news</code>.</li>
  <li>🧼 Uses BeautifulSoup to parse the HTML content.</li>
  <li>🔎 Finds all <code>&lt;li&gt;</code> items (containers for each news item).</li>
  <li>For each news item:
    <ul>
      <li>📝 <strong>Title</strong> from <code>&lt;p class="CRKrj"&gt;</code></li>
      <li>📰 <strong>Description</strong> from <code>&lt;p class="W4Hjm"&gt;</code></li>
      <li>🖼️ <strong>Image</strong> from <code>src</code> or <code>data-src</code> of <code>&lt;img&gt;</code></li>
      <li>🔗 <strong>External Link</strong> from <code>&lt;a href="..."&gt;</code></li>
    </ul>
  </li>
  <li>🔁 Converts relative image URLs to absolute using TOI's domain prefix if necessary.</li>
  <li>🚫 Skips duplicate entries by checking if the title already exists.</li>
  <li>💾 Saves data using <code>TOI_News.objects.create(**news)</code>.</li>
</ul>

<pre><code>def scrape_toi_news():
    url = "https://timesofindia.indiatimes.com/news"
    headers = { 
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_items = soup.find_all('li')
    
    for item in news_items:
        title_tag = item.find('p', class_="CRKrj")
        description_tag = item.find('p', class_="W4Hjm")
        image_tag = item.find('img')
        link_tag = item.find('a', href=True)

        if not (link_tag and title_tag and description_tag and image_tag):
            continue

        title = title_tag.text.strip() if title_tag else "No Title"
        description = description_tag.text.strip() if description_tag else "No Description"
        external_link = link_tag['href'].strip()
        image = None
        if image_tag:
            if image_tag.has_attr('data-src'):
                image = image_tag['data-src']
            elif image_tag.has_attr('src'):
                image = image_tag['src']
            if image and image.startswith("/"):
                image = "https://static.toiimg.com" + image

        if TOI_News.objects.filter(title=title).exists():
            print("Duplicate found. Skipping:", title)
            continue

        news = {
            'title': title,
            'description': description,
            'image': image,
            'external_link': external_link        
        }
        TOI_News.objects.create(**news)
</code></pre>

</div>
