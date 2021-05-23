from rest_framework.relations import PrimaryKeyRelatedField


class PrimaryKeyRelatedFieldID(PrimaryKeyRelatedField):
    def to_internal_value(self, data):
        return super(PrimaryKeyRelatedFieldID, self).to_internal_value(data).pk
