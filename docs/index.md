# DeepGroundwater

## Promoting research through blog posts and open-source code 

DeepGroundwater was inspired from the idea that not all research belongs on academic journals. There is great work done by students, postdocs, and research leads that may not advance the science, but deserves to be shared with the community. Furthermore, the peer-review process often can take weeks, if not months, for a paper to make it from draft to published. There is a need for a site to share developing reserach, and code, with others to spurn discovery and novelty; and we at Deep Groundwater hope we can provide that here. 

## Editorial Board

DeepGroundwater is managed by the following maintainers:

- [Tadd Bindas](https://github.com/taddyb)
- [Jonathan M. Frame](https://github.com/jmframe)
- [Ryoko Araki](https://github.com/RY4GIT)
- Jeremy Rapp
- Soelem Aafnan Bhuiyan

## Contributions

We welcome contributions from students, professors and industry professionals in the broad range of research related to hydrology and water resources. Contributions should be made by a GitHub pull request. An editorial review is required from at least two members of the board. 

*Note that our editorial review is intended to ensure that the contribution is on brand for DeepGroundWater and the markdown formatting works with MkDocs, and is not intended to ensure scientific rigor.*

### How to contribute

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