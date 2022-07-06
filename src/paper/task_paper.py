import shutil

import pytask
from pytask_latex import compilation_steps as cs

from src.config import BLD
from src.config import ROOT
from src.config import SRC


documents = ["research_paper", "research_pres_30min"]

for document in documents:

    @pytask.mark.task
    @pytask.mark.latex(
        script=SRC / "paper" / f"{document}.tex",
        document=BLD / "paper" / f"{document}.pdf",
        compilation_steps=cs.latexmk(
            (
                "--pdf",
                "--interaction=nonstopmode",
                "--synctex=1",
                "--cd",
                "--quiet",
                "--shell-escape",
            )
        ),
    )
    def task_compile_documents():
        pass


@pytask.mark.parametrize(
    "depends_on, produces",
    [
        (BLD / "paper" / f"{document}.pdf", ROOT / f"{document}.pdf")
        for document in documents
    ],
)
def task_copy_to_root(depends_on, produces):
    shutil.copy(depends_on, produces)
