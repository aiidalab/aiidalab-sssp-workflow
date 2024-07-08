import solara
from solara.alias import rv

from aiidalab_sssp.pages import explore, verify
from aiidalab_sssp.data import articles, names
from aiidalab_sssp.components import banner


@solara.component
def PeopleCard(name):
    with solara.Card(f"Employee of the Month: {name}") as main:
        with rv.CardText():
            solara.Markdown(
                """
                * Department: foo
                * Skills: bar, baz
                """
            )
            with solara.Link(f"/people/{name}"):
                solara.Button("View employee", text=True, icon_name="mdi-profile")
    return main


@solara.component
def Layout(children=[]):
    router = solara.use_context(solara.routing.router_context)
    with solara.VBox() as navigation:
        with rv.List(dense=True):
            with rv.ListItemGroup(v_model=router.path):
                with solara.Link(solara.resolve_path("/")):
                    with solara.ListItem("Home", icon_name="mdi-home", value="/"):
                        pass
                with solara.ListItem("tabular data", icon_name="mdi-database"):
                    for name in names:
                        pathname = f"/tabular/{name}"
                        with solara.Link(solara.resolve_path(pathname)):
                            solara.ListItem(name, value=pathname)
                with solara.ListItem("Articles", icon_name="mdi-book-open"):
                    for name, article_ in articles.items():
                        pathname = f"/article/{name}"
                        with solara.Link(solara.resolve_path(pathname)):
                            solara.ListItem(article_.title, value=pathname)

    with solara.AppLayout(navigation=navigation, title="Solara demo", children=children) as main:
        pass
    return main


@solara.component
def Page():
    with solara.VBox() as main:
        solara.Title("Standard Solid-State Pseudopotential (SSSP) » Home")
        with solara.ColumnsResponsive(12):
            banner.Overview()
        with solara.ColumnsResponsive([6, 6], small=[12]):
            explore.Overview()
            verify.Overview()

    return main

