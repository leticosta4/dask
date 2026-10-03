from __future__ import annotations

from dask.dataframe.dask_expr.diagnostics._analyze import analyze
from dask.dataframe.dask_expr.diagnostics._explain import explain

__all__ = ["analyze", "explain"]

# track-flaky: commit trivial para disparar CI (2026-09-28)
