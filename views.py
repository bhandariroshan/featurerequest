from flask.views import MethodView, View
from flask import render_template, redirect
from flask import send_from_directory
from flask import jsonify
from manager import FeatureRequestManager
from flask import request
import json


class CSSHandler(MethodView):
    def get(self, path):
        return send_from_directory('static/css', path)


class JSHandler(MethodView):
    def get(self, path):
        return send_from_directory('static/js', path)


class MainHandler(MethodView):
    def __init__(self):
        self.template_name = "feature.html"

    def get(self):
        return render_template(self.template_name)

    def post(self):
        post_data = json.loads(str(request.data).replace('b\'','').replace('\'',''))
        manager = FeatureRequestManager()
        manager.update_records(post_data['priority'], post_data['client'])
        manager.create_feature_request(
            title=post_data['title'],
            description=post_data['description'],
            client=post_data['client'],
            client_priority=post_data['priority'],
            target_date=post_data['targetDate'],
            product_area=post_data['productArea']
        )
        return jsonify({'status': 'Successfully saved a request.'})


class FeatureHandler(MethodView):
    def __init__(self):
        self.template_name = "featurelist.html"

    def get(self):
        return render_template(self.template_name)

    def post(self):
        manager = FeatureRequestManager()
        data = manager.get_all_feature_request()
        return_data = []
        for each_data in data:
            return_data.append({
                'id': each_data.id,
                'title': each_data.title,
                'description': each_data.description,
                'client': each_data.client,
                'priority': each_data.client_priority,
                'targetDate': each_data.target_date,
                'productArea': each_data.product_area
            })
        return jsonify({'data': return_data})
