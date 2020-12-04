from ..api_base import ApiBase


class Reimbursements(ApiBase):
    """Class for Reimbursements APIs."""

    GET_REIMBURSEMENTS = '/api/tpa/v1/reimbursements'
    GET_REIMBURSEMENT_BY_ID = '/api/tpa/v1/reimbursements/{0}'
    GET_REIMBURSEMENTS_COUNT = '/api/tpa/v1/reimbursements/count'
    POST_REIMBURSEMENTS = '/api/tpa/v1/reimbursements/complete'

    def post(self, data):
        """Complete Reimbursements in bulk.

        Parameters:
            data (list): List of Reimbursement IDs.

        Returns:
            List of updated Reimbursement IDs.
        """
        return self._post_request(data, Reimbursements.POST_REIMBURSEMENTS)

    def get(self, updated_at=None, offset=None, limit=None, exported=None):
        """Get Reimbursements that satisfy the parameters.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list. (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)
            exported (bool): If set to true, all Reimbursements that are exported alone will be returned. (optional)

        Returns:
            List with dicts in Reimbursements schema.
        """
        return self._get_request({
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit,
            'exported': exported
        }, Reimbursements.GET_REIMBURSEMENTS)

    def get_by_id(self, reimbursement_id):
        """Get an Reimbursement by Id.

        Parameters:
            reimbursement_id (str): Unique ID to find an Reimbursement. Reimbursement Id is our internal Id, it starts with prefix re always. (required)

        Returns:
            Dict in Reimbursement schema.
        """
        return self._get_request({}, Reimbursements.GET_REIMBURSEMENT_BY_ID.format(reimbursement_id))

    def count(self, updated_at=None, exported=None):
        """Get the number of Reimbursements that satisfy the parameters.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            exported (bool): If set to true, all Reimbursements that are exported alone will be returned. (optional)

        Returns:
            Count of Reimbursements.
        """
        return self._get_request({
            'updated_at': updated_at,
            'exported': exported
        }, Reimbursements.GET_REIMBURSEMENTS_COUNT)

    def get_all(self, updated_at=None, exported=None):
        """
        Get all the reimbursements based on paginated call
        """

        count = self.count(updated_at, exported)['count']
        reimbursements = []
        page_size = 200
        for i in range(0, count, page_size):
            segment = self.get(offset=i, limit=page_size, updated_at=updated_at, exported=exported)
            reimbursements = reimbursements + segment['data']
        return reimbursements
