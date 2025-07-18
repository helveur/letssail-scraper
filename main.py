from flask import Flask, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route('/')
def get_wind():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://letssail.ch/fr/balise/41452/preverenges", timeout=60000)
        page.wait_for_selector("#vent_vitesse .nb", timeout=60000)
        page.wait_for_selector("#vent_rafale .nb", timeout=60000)

        vent = page.query_selector("#vent_vitesse .nb").inner_text().split()[0]
        rafale = page.query_selector("#vent_rafale .nb").inner_text().split()[0]
        browser.close()
    return jsonify({"vent": vent, "rafale": rafale})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
