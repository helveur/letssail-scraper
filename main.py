import os
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "/tmp/playwright"

from flask import Flask, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route("/")
def index():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://letssail.ch/fr/balise/41452/preverenges")
        vent = page.locator("#vent_vitesse .nb").inner_text().split()[0]
        rafale = page.locator("#vent_rafale .nb").inner_text().split()[0]
        browser.close()
    return jsonify({"vent": vent, "rafale": rafale})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
