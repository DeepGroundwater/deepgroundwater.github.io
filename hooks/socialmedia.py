from textwrap import dedent
import urllib.parse

x_intent = "https://x.com/intent/tweet"

def on_page_markdown(markdown, **kwargs):
    page = kwargs['page']
    config = kwargs['config']
    if page.meta.get('template') != 'blog-post.html': # Only apply the social media tags to blog posts
        return markdown

    page_url = config.site_url+page.url
    page_title = urllib.parse.quote(page.title+'\n')

    return markdown + dedent(f"""
    <div style="text-align: center;" markdown="1">
    </h2>
    [Share on :simple-x:]({x_intent}?text={page_title}&url={page_url}){{ .md-button }}
    </div>
    """)
