"""`xla_lib` package wrapper for the XLA demo scripts.

This package provides a module entry point so the demo can be run via
`python -m xla_lib` and still use the top-level `run_demo.py` script.
"""

__all__ = ["main"]

try:
    from run_demo import main  # re-export main if available at top-level
except Exception:
    # Lazy fallback; importing `main` may fail until runtime when sys.path is set.
    main = None
