"""
app.py - Flask REST API para ytmusicapi
Executado dentro do container Docker na porta 3001
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Instância pública (sem autenticação) para buscas e exploração
from ytmusicapi import YTMusic

yt = YTMusic()


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "service": "ytmusicapi",
        "version": "1.0",
        "endpoints": [
            "GET  /search?q=<query>&limit=<n>",
            "GET  /search/songs?q=<query>&limit=<n>",
            "GET  /search/albums?q=<query>&limit=<n>",
            "GET  /search/artists?q=<query>&limit=<n>",
            "GET  /search/playlists?q=<query>&limit=<n>",
            "GET  /artist/<channelId>",
            "GET  /album/<browseId>",
            "GET  /song/<videoId>",
            "GET  /playlist/<playlistId>",
            "GET  /charts",
            "GET  /home",
        ]
    })


@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "")
    limit = int(request.args.get("limit", 10))
    filter_type = request.args.get("filter", None)  # songs, videos, albums, artists, playlists

    if not query:
        return jsonify({"error": "Parâmetro 'q' é obrigatório"}), 400

    try:
        results = yt.search(query, filter=filter_type, limit=limit)
        return jsonify({"query": query, "results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/search/songs", methods=["GET"])
def search_songs():
    query = request.args.get("q", "")
    limit = int(request.args.get("limit", 10))
    if not query:
        return jsonify({"error": "Parâmetro 'q' é obrigatório"}), 400
    try:
        results = yt.search(query, filter="songs", limit=limit)
        return jsonify({"query": query, "filter": "songs", "results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/search/albums", methods=["GET"])
def search_albums():
    query = request.args.get("q", "")
    limit = int(request.args.get("limit", 10))
    if not query:
        return jsonify({"error": "Parâmetro 'q' é obrigatório"}), 400
    try:
        results = yt.search(query, filter="albums", limit=limit)
        return jsonify({"query": query, "filter": "albums", "results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/search/artists", methods=["GET"])
def search_artists():
    query = request.args.get("q", "")
    limit = int(request.args.get("limit", 10))
    if not query:
        return jsonify({"error": "Parâmetro 'q' é obrigatório"}), 400
    try:
        results = yt.search(query, filter="artists", limit=limit)
        return jsonify({"query": query, "filter": "artists", "results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/search/playlists", methods=["GET"])
def search_playlists():
    query = request.args.get("q", "")
    limit = int(request.args.get("limit", 10))
    if not query:
        return jsonify({"error": "Parâmetro 'q' é obrigatório"}), 400
    try:
        results = yt.search(query, filter="playlists", limit=limit)
        return jsonify({"query": query, "filter": "playlists", "results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/artist/<channel_id>", methods=["GET"])
def get_artist(channel_id):
    try:
        result = yt.get_artist(channel_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/album/<browse_id>", methods=["GET"])
def get_album(browse_id):
    try:
        result = yt.get_album(browse_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/song/<video_id>", methods=["GET"])
def get_song(video_id):
    try:
        result = yt.get_song(video_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/playlist/<playlist_id>", methods=["GET"])
def get_playlist(playlist_id):
    limit = int(request.args.get("limit", 100))
    try:
        result = yt.get_playlist(playlist_id, limit=limit)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/charts", methods=["GET"])
def get_charts():
    country = request.args.get("country", "ZZ")
    try:
        result = yt.get_charts(country=country)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/home", methods=["GET"])
def get_home():
    limit = int(request.args.get("limit", 3))
    try:
        result = yt.get_home(limit=limit)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=False)
