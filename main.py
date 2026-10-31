
def define_env(env):
    """
    Hook function
    """

    @env.macro
    def new_in_v(version):
        articles = {
            6.0: "/news/articles/20261021b.md",
            6.1: "/news/articles/20261021.md",
        }
        try:
            article = articles[version]
        except KeyError:
            # raise ValueError(f"No news article configured for version {version!r}") from None
            article = "/"
        return f'[<span class="badge-new">New in v{version}</span>]({article})'
