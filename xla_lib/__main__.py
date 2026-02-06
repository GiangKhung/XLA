"""Module entrypoint to run the XLA demo via `python -m xla_lib`.

This will delegate to the `main()` function in the top-level `run_demo.py`.
"""
import sys

def _run():
    try:
        # Import top-level run_demo module and call its main()
        from run_demo import main
    except Exception as e:
        print(f"Không thể import 'run_demo': {e}")
        sys.exit(1)

    try:
        main()
    except SystemExit:
        raise
    except Exception as e:
        print(f"Lỗi khi chạy main(): {e}")
        sys.exit(1)

if __name__ == "__main__":
    _run()
