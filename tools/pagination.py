from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class Pagination(PageNumberPagination):
    max_page_size = 200
    page_query_param = "page_size"

    def _get_left_count(self) -> int:
        count = self.page.paginator.count
        page_size = self.get_page_size(self.request)
        page = self.page.number
        return max(count - (page * page_size), 0)

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('left', self._get_left_count()),
            ('results', data)
        ]))
