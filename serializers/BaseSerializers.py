from rest_framework import serializers


class BaseSerializers(serializers.ModelSerializer):
    modified_by = serializers.SerializerMethodField()

    @staticmethod
    def get_modified_by(obj):
        return "{}".format(obj.modified_by)
