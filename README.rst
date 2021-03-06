TM1py
=======================
TM1py is an object oriented interface to the new IBM Cognos TM1 REST API, written in Python.
The module aims to make interaction with TM1 more straightforward.


Features
=======================
TM1py offers handy features to interact with TM1 from Python, such as

- Retrieve data from cubes (in concise JSON structure)

.. code-block:: python

    >>> from TM1py import TM1pyQueries as TM1
    >>> login = TM1pyLogin.native('admin', 'apple')
    >>> tm1 = TM1(ip='localhost', port=8001, login=login, ssl=False)
    >>> data = tm1.get_view_content(cube_name='Plan_BudgetPlan', 
                                    view_name='High Level Profit And Loss')
    >>> value = data[('[plan_version].[FY 2004 Budget]',
                      '[plan_business_unit].[10000]',
                      '[plan_department].[1000]',
                      '[plan_chart_of_accounts].[Revenue]',
                      '[plan_exchange_rates].[local]',
                      '[plan_source].[budget]',
                      '[plan_time].[Q2-2004]')]
    >>> print(value)
    51966012.14

- Write data into cubes

.. code-block:: python

    >>> from TM1py import TM1pyQueries as TM1
    >>> login = TM1pyLogin.native('admin', 'apple')
    >>> tm1 = TM1(ip='', port=8001, login=login, ssl=False)
    >>> cube_name = 'Plan_BudgetPlan'
    >>> coordinates_and_values = {
            ('FY 2004 Budget', 'Germany', 'IT', 'Web Site', 'local', 'input', 'Oct-2005'): 5320,
            ('FY 2004 Budget', 'Germany', 'IT', 'Web Site', 'local', 'input', 'Nov-2005'): 6190,
            ('FY 2004 Budget', 'Germany', 'IT', 'Web Site', 'local', 'input', 'Dec-2005'): 5790
        }
    >>> tm1.write_values(cube_name, coordinates_and_values)

- Migrate TM1 objects

.. code-block:: python

    >>> from TM1py import TM1pyQueries as TM1
    >>> login = TM1pyLogin.native('admin', 'apple')
    >>> tm1_source = TM1(ip='localhost', port=8001, login=login, ssl=False)
    >>> tm1_target = TM1(ip='localhost', port=56912, login=login, ssl=False)
    >>> p = tm1_source.get_process('new')
    >>> tm1_target.create_process(p)

- Execute lines of TI code

.. code-block:: python

    >>> from TM1py import TM1pyQueries as TM1
    >>> login = TM1pyLogin.native('admin', 'apple')
    >>> tm1 = TM1(ip='localhost', port=8081, login=login, ssl=False)
    >>> lines_prolog = [
    >>>     "AddClient ( 'Chewbacca' );"
    >>> ]
    >>> lines_epilog = [
    >>>     "AssignClientPassword ( 'Chewbacca', 'apple' );",
    >>>     "AssignClientToGroup ( 'Chewbacca', 'ADMIN' );",
    >>>     "SecurityRefresh;"
    >>> ]
    >>> tm1.execute_TI_code(lines_prolog=lines_prolog, lines_epilog=lines_epilog)

- CRUD features for CellAnnotations
- CRUD features for Processes
- CRUD features for Chores
- CRUD features for NativeViews
- CRUD features for MDXViews
- CRUD features for Subsets
- CRUD features for Cubes
- CRUD features for Dimensions, Elements, ElementAttributes
- CRUD features for Users
- Generate MDX from NativeViews
- Execute Processes and Chores
- Query Threads
- Query MessageLog and TransactionLog


Requirements
=======================
http://docs.python-requests.org/en/master/

Installation
=======================
Download TM1py.py file and copy it into your project folder.

Contribution
=======================
TM1py is still at an early stage. Contribution is very welcome. 

