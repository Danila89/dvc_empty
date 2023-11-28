from dvclive import Live
import random

if __name__ == "__main__":
    with Live() as live:
        live.log_param("result", random.random())
