from settings import db
from models import FeatureRequest


class FeatureRequestManager(object):
    def create_feature_request(
            self,
            title,
            description,
            client,
            client_priority,
            target_date,
            product_area
    ):
        """

        :param title:
        :param description:
        :param client:
        :param client_priority:
        :param target_date:
        :param product_area:
        :return:
        """

        request = FeatureRequest(title,description, client, client_priority, target_date, product_area)
        db.session.add(request)
        db.session.commit()

    def get_all_feature_request(self):
        """

        :return:
        """
        results = FeatureRequest.query.all()
        return results

    def drop_all_features(self):
        """

        :return:
        """
        return FeatureRequest.query.delete()

    def update_records(self, priority, client):
        """

        :return:
        """
        db.session.query(FeatureRequest).filter(
            FeatureRequest.client_priority >= priority, FeatureRequest.client == client).update(
            {"client_priority": (FeatureRequest.client_priority + 1)}
        )
        db.session.commit()

    def get_feature_request_by_id(self):
        """

        :return:
        """

        return FeatureRequest.query.filter_by().first()