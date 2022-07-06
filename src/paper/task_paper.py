import shutil

import pytask
from pytask_latex import compilation_steps as cs

from src.config import BLD
from src.config import ROOT
from src.config import SRC


documents = ["research_paper", "research_pres_30min"]


# @pytask.mark.latex(
#     [
#         "--pdf",
#         "--interaction=nonstopmode",
#         "--synctex=1",
#         "--cd",
#         "--quiet",
#         "--shell-escape",
#     ]
# )
# @pytask.mark.parametrize(
#     "depends_on, produces",
#     [
#         (SRC / "paper" / f"{document}.tex", BLD / "paper" / f"{document}.pdf")
#         for document in documents
#     ],
# )
# def task_compile_documents():
#     pass

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


# for document in documents:

#     @pytask.mark.task
#     @pytask.mark.latex(
#         script=BLD / "paper" / f"{document}.pdf",
#         document= ROOT / f"{document}.pdf",
#         # compilation_steps=cs.latexmk(
#         #     (f"--{document}", "--interaction=nonstopmode", "--pdf", "--quiet", "--shell-escape","--synctex=1", "--cd")
#         # ),
#     )
#     def task_copy_to_root(depends_on, produces):
#         shutil.copy(depends_on, produces)
