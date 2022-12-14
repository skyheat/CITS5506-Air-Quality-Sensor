from datetime import datetime
from app.api import bp
from flask import jsonify, request, url_for
from app.models import AirQuality
from app import db
from app.api.errors import bad_request
from sqlalchemy import func
import time

# change to timestamp
@bp.route("/airquality/<string:timestamp>", methods=["GET"])
def get_airquality(timestamp):
    return jsonify(AirQuality.query.get_or_404(timestamp).to_dict())


@bp.route("/airquality", methods=["GET"])
def get_airqualitys():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20, type=int), 100)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return jsonify(data)


@bp.route("/airqualitys", methods=["POST"])
def create_airquality():
    data = request.get_json() or {}
    if (
        "temp" not in data
        or "humidity" not in data
        or "particles" not in data
        or "eco2" not in data
        or "tvoc" not in data
    ):
        return bad_request("Must include all fields")
    if "timestamp" not in data:
        data["timestamp"] = str(datetime.now()).replace(" ", "-")
    if "js_timestamp" not in data:
        data["js_timestamp"] = time.mktime(datetime.now().timetuple()) * 1000

    print(
        db.session.query(AirQuality.timestamp)
        .filter_by(timestamp=data["timestamp"])
        .scalar()
    )
    if AirQuality.query.filter_by(timestamp=data["timestamp"]).scalar():
        return bad_request("Data exists for that timestamp")

    airquality = AirQuality()
    airquality.from_dict(data)
    db.session.add(airquality)
    db.session.commit()

    response = jsonify(airquality.to_dict())
    response.status_code = 201
    response.headers["Location"] = url_for(
        "api.get_airquality", timestamp=airquality.timestamp
    )

    return response


@bp.route("/airqualitys/<string:timestamp>", methods=["PUT"])
def update_airquality(timestamp):
    airquality = AirQuality.query.get_or_404(timestamp)
    data = request.get_json() or {}
    airquality.from_dict(data)
    db.session.commit()

    return jsonify(airquality.to_dict())
