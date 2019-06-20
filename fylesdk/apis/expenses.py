from .api_base import ApiBase

class Expenses(ApiBase):
    """Class for Expenses APIs."""

    POST_EXPENSE = '/api/tpa/v1/expenses'
    GET_EXPENSES = '/api/tpa/v1/expenses'
    GET_EXPENSES_COUNT = '/api/tpa/v1/expenses/count'
    GET_EXPENSE_BY_ID = '/api/tpa/v1/expenses/{0}'
    GET_EXPENSE_ATTACHMENTS = '/api/tpa/v1/expenses/{0}/attachments'

    def post(self, data):
        """Create an Expense for an Employee.

        Parameters:
            data (dict): Dict in Expense schema.
        
        Returns:
            ID from the new Expense.
        """
        return self._post_request(data, Expenses.POST_EXPENSE)
        
    def get(self, updated_at=None, settled_at=None, reimbursed_at=None, approved_at=None, state=None, offset=None, verified=None, limit=None, submitted=None, fund_source=None):
        """Get a list of existing Expenses, excluding the file attachments, that match the parameters.
        
        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list. (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)
            submitted (bool): If set to true, all Expenses that are already submitted will alone be returned. (optional)
            settled_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            approved_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            reimbursed_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            state(str): A parameter to filter expenses by the state that they're in. (optional)
            verified(bool): A parameter to filter verified or unverified expenses. (optional)
            fund_source(str): A parameter to filter expenses by fund source. (optional)

        Returns:
            List with dicts in Expenses schema.
        """
        return self._get_request({
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit,
            'submitted': submitted,
            'settled_at': settled_at,
            'reimbursed_at': reimbursed_at,
            'approved_at': approved_at,
            'state': state,
            'verified': verified,
            'fund_source': fund_source
        }, Expenses.GET_EXPENSES)

    def count(self, updated_at=None, exported=None, submitted=None):
        """Get the count of existing Expenses that match the given parameters.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            exported (bool): If set to true, all Expenses that are exported alone will be returned. (optional)
            submitted (bool): If set to true, all Expenses that are already submitted will alone be returned. (optional)

        Returns:
            Count of Expenses.
        """
        return self._get_request({
            'updated_at': updated_at,
            'exported': exported,
            'submitted': submitted
        }, Expenses.GET_EXPENSES_COUNT)

    def get_by_id(self, expense_id):
        """Get an Expense by Id including the file attachments.

        Parameters:
            expense_id (str): Unique ID to find an Expense. Expense Id is our internal Id, it starts with prefix tx always. (required)

        Returns:
            Dict in Expense schema.
        """
        return self._get_request({}, Expenses.GET_EXPENSE_BY_ID.format(expense_id))
    
    def get_attachments(self, expense_id):
        """Get all the file attachments associated with an Expense.

        Parameters:
            expense_id (str): Unique ID to find an Expense. Expense Id is our internal Id, it starts with preifx tx always. (required)

        Returns:
            List with dicts in Attachments schema.
        """
        return self._get_request({}, Expenses.GET_EXPENSE_ATTACHMENTS.format(expense_id))