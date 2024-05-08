import os

from flask import Flask, jsonify, redirect, request, send_file
from flask_cors import CORS
from pymongo import MongoClient

import checkurl as checkurl
import qrgen as qrgen

app = Flask(__name__)
CORS(app)
# Set up MongoDB client

mongodb_url = os.environ.get("MONGODB_URL")

client = MongoClient(mongodb_url)
db = {"links":{}}
links = db["links"]


@app.route("/")
def home():
    return "QR code API "


@app.route("/qr")
def qrcode():
    # Get track, data and key parameters from query string
    track = request.args.get("track", False)
    data = request.args.get("data")
    key = request.args.get("key", None)

    # Check if tracking is enabled and link is valid
    if track:
        code = checkurl.check(data)
        if code == "200":
            # Check if link already exists in MongoDB
            if links.get(data):
                print(data)
                # If link already exists, construct URL for tracking link
                #data = request.host_url + "track?link=" + data
            else:
                # If link does not exist, insert link into MongoDB with open count of 0 and key (if provided)
                link_data = {"url": data, "open_count": 0}
                if key:
                    link_data["key"] = key
                else: link_data["key"] = None
                links[data] = link_data
                print(link_data)
                print(links)
                # Construct URL for tracking link
                #data = request.host_url + "track?link=" + data
        else:
            return "Not valid link"

    # Generate QR code for link
    return send_file(qrgen.qr(data), mimetype="image/png")


@app.route("/track")
def track_link():
    # Find link in MongoDB
    link = request.args.get("link", False)
    # found_link = links.get(link) # links.find_one({"url": link})

    if link:
        # If link exists, increment open count and redirect to link
        open_count = links[link]["open_count"] + 1
        links[link]["open_count"] = open_count
        return redirect(link)
    else:
        return "Link not found"


@app.route("/links")
def show_links():
    # Retrieve all links in MongoDB
    key = request.args.get("key", None)
    link_list = []
    print(links.values())
    if key:
        # Retrieve links with the given key from the database
        for link in links.values():
            if link["key"] == key:
                link_list.append(
                    (
                        link["url"],
                        link["open_count"],
                        request.host_url + "track?link=" + link["url"],
                    )
                )
    else:
        # Retrieve all links from the database
        for link in links.values():
            link_list.append(
                (
                    link["url"],
                    link["open_count"],
                    request.host_url + "track?link=" + link["url"],
                )
            )

    return jsonify(link_list)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, use_reloader=True)