import solara

from aiidalab_sssp.data import html_cite, html_license


@solara.component
def Overview():
    with solara.ColumnsResponsive(12) as main:
        with solara.VBox():
            solara.Details(
                summary="How to cite",
                children=[solara.HTML(unsafe_innerHTML=html_cite)],
                expand=False,
            )

            solara.Details(
                summary="License",
                children=[solara.HTML(unsafe_innerHTML=html_license)],
                expand=False,
            )
    return main
