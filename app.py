import json
import unittest
import uuid
from dataclasses import dataclass

from flask import render_template, request, jsonify

from config import db, app


def generate_uuid():
    return str(uuid.uuid4())


@dataclass
class NameAndPicture(db.Model):
    id: str
    title: str
    img: str

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid, unique=True)
    title = db.Column(db.String(255), nullable=False)
    img = db.Column(db.String(255), nullable=False)


@app.route("/")
def main():
    all_name_and_pictures = NameAndPicture.query.all()
    return render_template("index.html", objects=all_name_and_pictures)


@app.route("/v1/api/find-all", methods=["GET"])
def find_all():
    all_name_and_pictures = NameAndPicture.query.all()
    if len(all_name_and_pictures) > 0:
        return jsonify(all_name_and_pictures), 200
    else:
        return jsonify({"message": "Any name and pictures found"}), 404


@app.route("/v1/api/find-by-id/<string:id>", methods=["GET"])
def find_by_id(id):
    name_and_picture = NameAndPicture.query.get(id)
    if name_and_picture:
        return jsonify(name_and_picture), 200
    else:
        return (
            jsonify({"message": "Name and picture with given id " + id + " not found"}),
            404,
        )


@app.route("/v1/api/create", methods=["POST"])
def create():
    try:
        if request.method == "POST":
            data = request.json
            id = data.get("id")
            title = data.get("title")
            img = data.get("img")
            if title is None or img is None:
                return jsonify({"error": "Title and img are required"}), 400
            obj = NameAndPicture(id=id, title=title, img=img)
            db.session.add(obj)
            db.session.commit()
        return (
            jsonify({"message": "Name and picture created successfully", "obj": obj}),
            201,
        )
    except Exception as e:
        return jsonify({"message": "App failed: " + str(e)}), 500


@app.route("/v1/api/update", methods=["PUT"])
def update():
    try:
        if request.method == "PUT":
            data = request.json
            if (
                data.get("id") is None
                or data.get("title") is None
                or data.get("img") is None
            ):
                return jsonify({"error": "Id, title and img are required"}), 400
            name_and_picture = NameAndPicture.query.get(data.get("id"))
            name_and_picture.title = data.get("title")
            name_and_picture.img = data.get("img")
            db.session.commit()
        return jsonify({"message": "Name and picture updated successfully"}), 201
    except Exception as e:
        return jsonify({"message": "App failed: " + str(e)}), 500


@app.route("/v1/api/delete-by-id/<string:id>", methods=["DELETE"])
def delete_by_id(id):
    name_and_picture = NameAndPicture.query.get(id)
    if name_and_picture:
        db.session.delete(name_and_picture)
        db.session.commit()
        return jsonify(name_and_picture), 200
    else:
        return (
            jsonify({"message": "Name and picture with given id " + id + " not found"}),
            404,
        )


class NetquestAssignmentTestCase(unittest.TestCase):
    test_name_and_picture_id = ""

    def setUp(self) -> None:
        app.config["TESTING"] = True
        app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = "postgresql://postgres:admin123@localhost:5432/netquest_assignment"
        self.app = app.test_client()

    def test01_create(self):
        # given, when
        response = self.app.post(
            "/v1/api/create",
            json={
                "title": "Test 1 - test case object",
                "img": "Test 1 - test case object",
            },
            content_type="application/json",
        )
        data = json.loads(response.data.decode())
        # then
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", data)
        self.assertEqual(data["message"], "Name and picture created successfully")
        self.__class__.test_name_and_picture_id = data["obj"]["id"]

    def test02_update(self):
        # given, when
        response = self.app.put(
            "/v1/api/update",
            json={
                "id": self.__class__.test_name_and_picture_id,
                "title": "Test 1 - test case object - updated",
                "img": "Test 1 - test case object - updated",
            },
            content_type="application/json",
        )
        data = json.loads(response.data.decode())
        # then
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", data)
        self.assertEqual(data["message"], "Name and picture updated successfully")

    def test03_find_all(self):
        # given, when
        response = self.app.get("/v1/api/find-all")
        data = json.loads(response.data.decode())
        # then
        self.assertEqual(response.status_code, 200)
        self.assertEqual(True, len(data) > 0)

    def test04_find_by_id(self):
        # given, when
        response = self.app.get(
            "/v1/api/find-by-id/" + self.__class__.test_name_and_picture_id
        )
        data = json.loads(response.data.decode())
        # then
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.__class__.test_name_and_picture_id, data["id"])

    def test05_delete_by_id(self):
        # given, when
        response = self.app.delete(
            "/v1/api/delete-by-id/" + self.__class__.test_name_and_picture_id
        )
        data = json.loads(response.data.decode())
        # then
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.__class__.test_name_and_picture_id, data["id"])


if __name__ == "__main__":
    app.run(debug=True)
