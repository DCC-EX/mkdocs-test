
def define_env(env):
    """
    Hook function
    """

    @env.macro
    def new_in_v6():
        return '[<span class="badge-new">New in v6.0</span>](/news/articles/20261021b.md)'
