# How to contribute

Below are the steps needed to create a blog post for DeepGroundwater:

1. Fork the [DeepGroundwater github website](https://github.com/DeepGroundwater/DeepGroundwater.github.io)
2. Run the following commands to install mkdocs to your env

    ```sh
    pip install uv
    uv venv
    source .venv/bin/activate
    uv pip install -e .
    ```

3. Create a .md file in the `docs/blog/posts` folder 
4. Follow the following format for your post to ensure it builds on MkDocs
    ```markdown
    ---
    date:
    created: YYYY-MM-DD
    authors:
    - your_author_username
    ---

    # Title

    Here is where your header (abstract) will be. This is what will appear on the blog post site

    <!-- more --> # This is here to mark where the header ends and the content begins

    Blog post content!

    ```
5. Add your name to the `docs/blog/.authors.yml` file, following the format of the page
6. Run `mkdocs serve` in your terminal using the new env to test your blog post renders. Check for formatting
7. Push your code to your fork, and create a pull request!
  - In your pull request, select any of the editorial board to create your review. Two are required for the post to go live
  - Once the post is reviewed, we'll merge your PR!
